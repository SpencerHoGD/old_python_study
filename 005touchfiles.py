import pathlib

PATH = '/home/liam/test/test/'
#PATH = 'images'

pathlib.Path(PATH).mkdir(exist_ok=True)

for fn in range(10**1):
    with open(f'{PATH}/{fn}.txt', 'w') as fp:
        fp.write(f"hello, pathlib {fn}")
