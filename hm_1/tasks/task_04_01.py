def read_magic_number(path: str) -> bool:
    try:
        with open(path) as file:
            number = int(file.read().rstrip("\n"))
            return number >= 1 and number < 3
    except Exception:
        raise ValueError
