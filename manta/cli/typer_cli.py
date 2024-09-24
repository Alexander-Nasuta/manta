import typer

app = typer.Typer()


@app.command()
def print_term(text: str = "default text") -> None:
    print(text)


@app.command()
def print_hello_world() -> None:
    print("Hello, World!")


if __name__ == "__main__":
    app()
