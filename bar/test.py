import os


def env():
    bar = os.environ.get("BAR")
    return bar or "fizz"


if __name__ == "__main__":
    print(env())
