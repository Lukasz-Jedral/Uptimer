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
    # fmt: off
    colors = {
        2: "green",
        3: "yellow",
        4: "bright_red",
        5: "red",
    }
    # fmt: on
    click.secho(f"{url} -> {status}", fg=colors.get(status // 100, "magenta"))


@click.command()
@click.argument("url")
def check(url):
    status_code = check_url(url)
    if status_code:
        colorize_status(url, status_code)


if __name__ == "__main__":
    check()
