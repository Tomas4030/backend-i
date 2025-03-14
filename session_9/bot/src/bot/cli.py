import typer
import discord
from bot.main import run
from dotenv import load_dotenv
import os

app = typer.Typer()
load_dotenv()


@app.command()
def start():
    """
    Start the Discord bot using the provided token.
    """
    run(os.getenv('TOKEN', None))



if __name__ == "__main__":
    app()