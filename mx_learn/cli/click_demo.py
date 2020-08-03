import click

"""
    python click_demo.py second --name geshuai
        > hello world
        > this is second: geshuai
"""


@click.group()
def first():
    print("hello world")


@click.command()
@click.option("--name", help="the name")
def second(name):
    print("this is second: {}".format(name))


@click.command()
def third():
    print("this is third")


if __name__ == '__main__':
    first.add_command(second)
    first.add_command(third)
    first()
