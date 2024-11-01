import pathlib

PATH = "/home/hxm/test"
# PATH = 'images'

pathlib.Path(PATH).mkdir(exist_ok=True)

for fn in range(10**3):
    with open(f"{PATH}/{fn}.txt", "w", encoding="utf-8") as fp:
        fp.write(f"hello, pathlib {fn}")
