"""
    :module_name: cli
    :module_summary: a CLI for fitcheck_dbal
    :module_author: Nathan Mendoza
"""

import click
import grpc
from .grpc.services_pb2_grpc import (
    add_UserDocumentServiceServicer_to_server,
    UserDocumentServiceStub
)
from .grpc.requests_pb2 import NewUser, QueryForUser

import futures

from . import UserDocumentController


@click.command()
def fitcheck_dbal():
    """Entry point to fitcheck-dbal"""
    click.echo('Hello World!')


@click.command()
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_UserDocumentServiceServicer_to_server(UserDocumentController(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


@click.command()
def request():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = UserDocumentServiceStub(channel)
        response = stub.CreateUserDocument(
            NewUser(username="johndoe", password="supersecretstring"))
        print("Client received: " + response.result)
        response = stub.GetUserDocument(
            QueryForUser(userid=response.result.userid))
        print("Client received: " + response.result)
