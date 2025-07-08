def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.

    Args:
        name (str): The name to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

greeted_name = "Ahmed"
if __name__ == "__main__":
    print(greet(greeted_name))
# The above code defines a function `greet` that takes a name as input and returns a greeting message.