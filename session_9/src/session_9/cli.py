import typer
import discord
from session_9.bot import run, Bem_vindo
from dotenv import load_dotenv
import os

app = typer.Typer()
load_dotenv()

@app.command()
def start():
    """
    Start the Discord bot using the provided token.
    """
    run(os.getenv('DOCKER_TOKEN', None))

@app.command
def BEM():
    Bem_vindo()


if __name__ == "__main__":
    app()