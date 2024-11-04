import os


def decMakeDir(func):

    def handleFunc(*args, **kwargs):
        dirname = func(*args, **kwargs)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        elif not os.path.isdir(dirname):
            pass

        return dirname

    return handleFunc


def getWorkDir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@decMakeDir
def getTmpDir():
    return os.path.join(getWorkDir(), "tmp")


@decMakeDir
def getLogDir():
    return os.path.join(getTmpDir(), "log")


@decMakeDir
def getCacheDir():
    return os.path.join(getTmpDir(), "cache")


@decMakeDir
def getVCodeDir():
    return os.path.join(getTmpDir(), "vcode")


if __name__ == "__main__":
    # d = getWorkDir()
    # print(d)
    getTmpDir()
    # getCacheDir()
