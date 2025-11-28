from osw import console

def hello_world() -> None:
    """Print greeting message."""
    console.print("Hello World!", style="bold green")


if __name__ == "__main__":
    hello_world()