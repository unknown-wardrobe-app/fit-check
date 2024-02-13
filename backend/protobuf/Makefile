# Makefile for fitcheck_protobuf

GIT_ROOT := $(shell git rev-parse --show-toplevel)

help:
	@echo "Makefile for fitcheck_protobuf. Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'	

venv: ## Setup a virtual environment
	[ -d .venv ] || python3 -m venv .venv --prompt=fitcheck_protobuf

clean-venv: ## Destroy the virtual environment if it exists
	[ ! -d .venv ] || rm -rf .venv

clean-pyc: ## Remove generated python modules
	rm -rf build

clean: clean-venv clean-pyc ## Clean up develepment environment

activate: ## Activate the virtual environment for bootstrapping (does NOT activate for you).
	@echo 
	@echo
	@echo "Virtual environment created!"
	@echo "Activate it by running the following:"
	@echo
	@echo "    source .venv/bin/activate"
	@echo 

bootstrap: venv ## Bootstrap the virtual environment
	( \
		source .venv/bin/activate; \
		pip install --upgrade pip; \
		pip3 install --require-virtualenv -r dev_requirements.txt; \
	)
	@$(MAKE) activate

grpc: bootstrap ## Create gRPC tooling for package
	[ -d build ] || mkdir -p build
	( \
		source .venv/bin/activate; \
		python -m grpc_tools.protoc \
			-I$(GIT_ROOT)/backend/protobuf/ \
			--python_out=$(GIT_ROOT)/backend/protobuf/build \
			--pyi_out=$(GIT_ROOT)/backend/protobuf/build \
			--grpc_python_out=$(GIT_ROOT)/backend/protobuf/build \
			$(GIT_ROOT)/backend/protobuf/fitcheck/dblayer/*.proto \
			$(GIT_ROOT)/backend/protobuf/fitcheck/dblayer/users/*.proto; \
	)


