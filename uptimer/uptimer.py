import requests
import click


def check_url(url):
    try:
        response = requests.head(url)
    except requests.exceptions.ConnectionError:
        click.echo(f"ConnectionError: Can't reach {url}")
        return None
    return response.status_code


def colorize_status(url, status):
    if status // 100 == 2:
        click.secho(f"{url} -> {status}", fg="green")
    elif status // 100 == 3:
        click.secho(f"{url} -> {status}", fg="yellow")
    elif status // 100 == 4:
        click.secho(f"{url} -> {status}", fg="bright_red")
    elif status // 100 == 5:
        click.secho(f"{url} -> {status}", fg="red")
    else:
        click.secho(f"{url} -> {status}", fg="magenta")

@click.command()
@click.argument("url")
def check(url):
    status_code = check_url(url)
    if status_code:
        colorize_status(url, status_code)


if __name__ == "__main__":
    check()
