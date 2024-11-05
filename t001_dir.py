import platform


def p():
    x = platform.system()
    print(x)


def d():
    x = dir(platform)
    print(x)


if __name__ == "__main__":
    p()
    d()
