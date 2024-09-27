import typer

app = typer.Typer()


@app.command()
def print_term(text: str = "default text") -> None:
    print(text)


@app.command()
def print_hello_world() -> None:
    print("Hello, World!")


@app.command()
def test_resource_loading() -> None:
    import importlib.resources as pkg_resources
    import manta.resources
    content = pkg_resources.read_text(manta.resources, 'example_text.txt')
    print(content)


if __name__ == "__main__":
    app()
