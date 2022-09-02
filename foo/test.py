import os


def env():
    foo = os.environ.get("FOO")
    return foo or "bar"


if __name__ == "__main__":
    print(env())
