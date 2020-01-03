import os
import subprocess
import click
from config import config
def init():
    for key in config:
        os.environ[key] = config[key]

def __runserver():
    subprocess.run(r'python -m flask run')    


@click.group()
def cli():
    pass
    
@cli.command('runserver',help='Runs the flask server')
def runserver():
    init()
    __runserver()



if __name__ == '__main__':
    cli()   