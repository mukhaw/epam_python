def read_magic_number(path: str) -> bool:
    try:
        with open(path) as f:
            file = f.readline().rstrip("\n")
        return file.isdigit() and int(file) >= 1 and int(file) < 3
    except ValueError as err:
        return err
