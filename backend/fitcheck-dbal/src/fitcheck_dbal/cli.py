"""
    :module_name: cli
    :module_summary: a CLI for fitcheck_dbal
    :module_author: Nathan Mendoza
"""

import click


@click.command()
def fitcheck_dbal():
    """Entry point to fitcheck-dbal"""
    click.echo('Hello World!')
