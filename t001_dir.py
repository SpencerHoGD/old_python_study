import platform


def p():
    x = platform.system()
    print(x)


def d():
    x = dir(platform)
    print(x)


def f():
    # Use "e" to convert a number into scientific number format (with a lower-case e):

    txt = f"We have {5000000000:e} chickens."

    print(txt)


if __name__ == "__main__":
    # p()
    # d()
    f()
