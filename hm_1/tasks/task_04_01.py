def read_magic_number(path: str) -> bool:
    try:
        with open(path) as file:
            line = file.read().rstrip("\n")
            if line.isdigit():
                return int(line) >= 1 and int(line) < 3
            else:
                return False
    except Exception:
        raise ValueError("This is ValueError mistake")
