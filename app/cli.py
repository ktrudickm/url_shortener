import typer
import requests
import webbrowser
from typing import Optional
from typing_extensions import Annotated
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://localhost:80")
app = typer.Typer()

@app.command()
def shorten(original: str, short: Annotated[Optional[str], typer.Argument()] = None):
    """Shorten a URL via the API."""
    if short is None:
        response = requests.post(f"{BASE_URL}/shorten_url", json={"long_url": original})
    else:
        response = requests.post(f"{BASE_URL}/shorten_url", json={"long_url": original, "short_url": short})
    print(f"Response status code: {response.status_code}")
    print(f"Response text: {response.text}")
    if response.status_code == 200:
        typer.echo(f"Success! The shortened URL: {response.json()['short_url']}")
    else:
        typer.echo(response.json()['detail'])

@app.command()
def lookup(short_url: str):
    """Lookup a short url via the API."""
    response = requests.get(f"{BASE_URL}/redirect/{short_url}", allow_redirects=False)
    if response.status_code == 302:
        webbrowser.open(response.headers['Location'])
    else:
        typer.echo(response.json()['detail'])

@app.command()
def list_all():
    """List all short urls via the API."""
    response = requests.get(f"{BASE_URL}/list_urls")
    if response.status_code == 200:
        typer.echo(response.json())
    else:
        typer.echo("Error: Could not retrieve list of short urls.")

@app.command()
def delete(short_url: str):
    """Delete a short url via the API."""
    response = requests.delete(f"{BASE_URL}/delete/{short_url}")
    if response.status_code == 200:
        typer.echo(f"Successfully deleted `{response.json()['short_url']}`")
    else:
        typer.echo(response.json()['detail'])


if __name__ == "__main__":
    app()

# TODO:
# - Work on responses, especially or shorten route
# - [ ] Add tests for CLI
