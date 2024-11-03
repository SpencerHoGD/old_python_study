from dectimeit import get_time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor


@get_time
def t1():
    with ThreadPoolExecutor() as executor:
        future = executor.submit(pow, 323, 1235)
        print(future.result())

t1()

