

def some_function(number: int = 0, text: str = "Hello") -> str:
    """
    This is a function that does something.

    Args:
        number (int, optional): A number. Defaults to 0.
        text (str, optional): A text. Defaults to "Hello".

    Returns:
        str: This function returns a string.

    """
    return f"{text} {number}"


class DocExample:

    def some_method(self, number: int = 0, text: str = "Hello") -> None:
        """
        This is a method that does something.

        Args:
            number (int, optional): A number. Defaults to 0.
            text (str, optional): A text. Defaults to "Hello".

        Returns:
            None: This method returns

        """
        pass