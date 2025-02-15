def capitalize(str):
    """Capitalize the first letter of a string."""
    if not str:
        return str
    return str[0].upper() + str[1:]