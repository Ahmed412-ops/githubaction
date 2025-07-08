def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.

    Args:
        name (str): The name to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

greeted_name = "Ahmed2"
if __name__ == "__main__":
    print(greet(greeted_name))