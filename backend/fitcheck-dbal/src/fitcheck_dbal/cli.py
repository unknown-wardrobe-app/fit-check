"""
    :module_name: cli
    :module_summary: a CLI for fitcheck_dbal
    :module_author: Nathan Mendoza
"""

import click
import time
import grpc

from fitcheck_dbal import UserDocumentController
from fitcheck_dbal.rpc.dbal_pb2_grpc import (
    add_UserDocumentServiceServicer_to_server,
    UserDocumentServiceStub,
    NewUser,
    QueryForUser
)

from concurrent import futures


@click.command()
@click.argument('action')
def fitcheck_dbal(action):
    """Entry point to fitcheck-dbal"""
    if action == 'serve':
        serve()
    elif action == 'request':
        request()
    else:
        click.echo(f"Unknown action: {action}")
        exit(1)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_UserDocumentServiceServicer_to_server(UserDocumentController(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


def request():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = UserDocumentServiceStub(channel)
        response = stub.CreateUserDocument(
            NewUser(username="johndoe", password="supersecretstring"))
        print("Client received: ", response.new_user.userid)
        time.sleep(2)
        response = stub.GetUserDocument(
            QueryForUser(userid=str(response.new_user.userid))
        )
        print("Client received: ", response)
