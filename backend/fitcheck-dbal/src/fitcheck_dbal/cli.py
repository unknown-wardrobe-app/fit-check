"""
    :module_name: cli
    :module_summary: a CLI for fitcheck_dbal
    :module_author: Nathan Mendoza
"""

import click
import grpc
from concurrent import futures
import fitcheckprotos.dblayer.users.account_pb2_grpc as fitcheckaccountservice
from fitcheckprotos.dblayer.users.account_pb2 import CreateAccount

from .servicers import FitcheckAccountManagementServicer


@click.group()
def fitcheck_dbal():
    """Entry point to fitcheck-dbal"""
    pass


@fitcheck_dbal.command()
@click.option('-p', '--port', default="50051")
def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fitcheckaccountservice.add_AccountManagementServicer_to_server(
        FitcheckAccountManagementServicer(),
        server
    )
    server.add_insecure_port("[::]:" + port)
    server.start()
    print(f"Server listening on port: {port}")
    server.wait_for_termination()


@fitcheck_dbal.command()
@click.option('-u', '--username', required=True)
@click.option('-p', '--password', required=True)
def makeuser(username, password):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = fitcheckaccountservice.AccountManagementStub(channel)
        response = stub.NewAccount(CreateAccount(
            username=username,
            password=password
        ))
        print(f"New user ID: {response.user.id}")
