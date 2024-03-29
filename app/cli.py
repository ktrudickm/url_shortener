import typer
import requests
import webbrowser
from typing import Optional
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def shorten(original: str, short: Annotated[Optional[str], typer.Argument()] = None):
    """Shorten a URL via the API."""
    if short is None:
        response = requests.post("http://localhost:80/shorten_url", json={"long_url": original})
    else:
        response = requests.post("http://localhost:80/shorten_url", json={"long_url": original, "short_url": short})
    if response.status_code == 200:
        typer.echo(f"Success! The shortened URL: {response.json()['short_url']}")
    else:
        typer.echo(response.json()['detail'])

@app.command()
def lookup(short_url: str):
    """Lookup a short url via the API."""
    response = requests.get(f"http://localhost:80/redirect/{short_url}", allow_redirects=False)
    if response.status_code == 302:
        webbrowser.open(response.headers['Location'])
    else:
        typer.echo(response.json()['detail'])

@app.command()
def list_all():
    """List all short urls via the API."""
    response = requests.get("http://localhost:80/list_urls")
    if response.status_code == 200:
        typer.echo(response.json())
    else:
        typer.echo("Error: Could not retrieve list of short urls.")

@app.command()
def delete(short_url: str):
    """Delete a short url via the API."""
    response = requests.delete(f"http://localhost:80/delete/{short_url}")
    if response.status_code == 200:
        typer.echo(f"Successfully deleted `{response.json()['short_url']}`")
    else:
        typer.echo(response.json()['detail'])


if __name__ == "__main__":
    app()

# TODO:
# - Work on responses, especially or shorten route
# - [ ] Add tests for CLI
