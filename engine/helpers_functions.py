def get_int(msg: str):
    """Return an int"""

    try:
        user_input = int(input(msg))

        return user_input
    except Exception as e:
        print("Invalid option, ", e)
        return get_int(msg)
