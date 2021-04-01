import sys


def my_precious_logger(text: str):
    if "error" in text:
        sys.stderr.write(text)
    else:
        sys.stdout.write(text)


my_precious_logger("error: file not found")
