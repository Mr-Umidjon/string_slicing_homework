def main(s):
    """
    The s string variable is given. return the characters in the odd position.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    return s[1::2]


print(main("abcdef"))
