import logging


# 带参数的装饰器
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warning":
                logging.warning("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@use_logging(level="info")
def foo(name="foo"):
    print("i am %s" % name)


def decUpper(func):
    pass


if __name__ == "__main__":
    foo()

