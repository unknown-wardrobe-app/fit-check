# Makefile for fitcheck-dbal 

GIT_ROOT := $(shell git rev-parse --show-toplevel)

help:
	@echo "Makefile for fitcheck-dbal. Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'	

venv: ## Setup a virtual environment
	[ -d .venv ] || python3 -m venv .venv --prompt=fitcheck_dbal

clean-venv: ## Destroy the virtual environment if it exists
	[ ! -d .venv ] || rm -rf .venv

clean-test: ## Remove testing artifacts
	[ ! -d .pytest_cache ] || rm -rf .pytest_cache

clean-pyc: ## Remove package artifacts and cached byte code
	find . -name __pycache__ -exec rm -rf {} +
	find . -name *.egg-info -exec rm -rf {} +

clean-cov: ## Remove code coverage artifacts
	[ ! -e .coverage ] || rm -f .coverage

clean: clean-venv clean-test clean-pyc clean-cov ## Clean up develepment environment

activate: ## Activate the virtual environment for bootstrapping (does NOT activate for you).
	@echo 
	@echo
	@echo "Virtual environment created!"
	@echo "Activate it by running the following:"
	@echo
	@echo "    source .venv/bin/activate"
	@echo 

.PHONY: test
test: bootstrap ## Run unittests on the source directory
	@( \
		source .venv/bin/activate; \
		pytest --cov=fitcheck_dbal; \
		coverage report -m; \
	)

.PHONY: lint
lint: bootstrap ## Run lint checks on the source directory
	@( \
		source .venv/bin/activate; \
		pylint src/fitcheck_dbal; \
	)

bootstrap: venv ## Bootstrap the virtual environment
	@( \
		source .venv/bin/activate; \
		pip install --upgrade pip; \
		pip3 install --require-virtualenv -r requirements.txt; \
		pip3 install --require-virtualenv -r dev_requirements.txt; \
		pip3 install --editable . ; \
	)
	@$(MAKE) activate

grpc: bootstrap ## Create gRPC tooling for this package
	[ -d src/fitcheck_dbal/messages ] || mkdir src/fitcheck_dbal/messages
	[ -d src/fitcheck-dbal/services ] || mkdir src/fitcheck_dbal/services
	( \
		source .venv/bin/activate; \
		python -m grpc_tools.protoc \
			-I$(GIT_ROOT)/protobufs/dbal \
			--python_out=$(GIT_ROOT)/backend/fitcheck-dbal/src/fitcheck_dbal/messages \
			--pyi_out=$(GIT_ROOT)/backend/fitcheck-dbal/src/fitcheck_dbal/messages \
			--grpc_python_out=$(GIT_ROOT)/backend/fitcheck-dbal/src/fitcheck_dbal/services \
			$(GIT_ROOT)/protobufs/dbal/*.proto; \
	)

