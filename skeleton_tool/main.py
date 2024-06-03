from pathlib import Path
from typing import Optional
import toml

import typer
from rich import print
from rich.console import Console
from rich.table import Table
from typing_extensions import Annotated, Doc, deprecated

APP_NAME = "skeleton-tool"
DEFAULT_KEY = 'default'

app = typer.Typer(no_args_is_help=True)
app_dir = typer.get_app_dir(APP_NAME)
console = Console()

@app.command()
def login(
    username: Annotated[str, typer.Option()] = '',
    password: Annotated[str, typer.Option()] = '',
    organization: Annotated[str, typer.Option()] = 'default'
    ):
    """
    Login to skeleton tool
    """
    # check if config exists
    config_path: Path = Path(app_dir) / "cosilico.config"
    if not config_path.is_file():
        print("Config file doesn't exist, in the future create one with [bold red]skeleton-tool config[/bold red] for faster login.")
        config: dict = {}
    else:
        with config_path.open() as f:
            config: dict = toml.load(f)
    
    if organization in config and not username:
        username = config[organization]['username']
    if organization in config and not password:
        password = config[organization]['password']

    if not username:
        username = typer.prompt('Enter username')
    if not password:
        username = typer.prompt('Enter password', hide_input=True)
    if not organization:
        organization = typer.prompt('Enter organization')

    # perform login
    print(f"Logged [bold green]{username}[/bold green] \
into [bold green]{organization}[/bold green] :test_tube:")

@app.command()
def config(
    organization: Annotated[str, typer.Option(
        prompt='Enter organization',
        help="this is a help message"
    )],
    username: Annotated[str, typer.Option(prompt='Enter username')],
    password: Annotated[str, typer.Option(prompt='Enter password', hide_input=True)],
    make_default: Annotated[bool, typer.Option(prompt='Make default')]
    ):
    """
    Configure the skeleton tool
    """
    Path(app_dir).mkdir(parents=True, exist_ok=True)
    config_path: Path = Path(app_dir) / "cosilico.config"
    if not config_path.is_file():
        config: dict = {}
    else:
        with config_path.open() as f:
            config: dict = toml.load(f)
    
    entry = {
        'username': username,
        'password': password,
        'organization': organization,
    }
    config[organization] = entry

    if make_default:
        config[DEFAULT_KEY] = entry
    
    with config_path.open('w') as f:
        toml.dump(config, f)



    table = Table("organization", "username")
    table.add_row(organization, username)

    print(f"Added [bold green]{organization}[/bold green] to config :fire:")
    console.print(table)

@app.command()
def shoot(name: str):
    """
    Shoot the portal gun
    """
    print(f"Shooting portal gun at {name}")


@app.command()
def load(
    name: Annotated[str, typer.Argument(help="name of blah")],
    foo: Annotated[Optional[int], typer.Argument(help="blah blah")] = None,
    bar: Annotated[int, typer.Option(help="foo foo bar")] = 1,
    formal: bool = False
):
    """
    Load the portal gun
    """
    print("Loading portal gun")