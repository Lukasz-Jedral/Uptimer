import requests
import click
from time import sleep


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
@click.argument("urls", nargs=-1)
@click.option("--daemon", "-d", default=False, is_flag=True)
def check(urls, daemon):
    while True:
        for url in urls:
            status_code = check_url(url)
            if status_code:
                colorize_status(url, status_code)
        if not daemon:
            break
        sleep(5)


if __name__ == "__main__":
    check()
