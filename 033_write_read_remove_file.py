# encoding:utf-8
"""
Created on 2019-09-09
hexiaoming
"""
import os

# file = '/Users/hexiaoming/Documents'


def write_file(f):
    """yes"""
    with open(f, "w", encoding="utf-8") as f:
        f.write("first line\nsecond line\nthird line\n")


def read_file(f):
    """yes"""
    with open(f, "r", encoding="utf-8") as f:
        for line in f.readlines():
            print(line)


def remove_file(f):
    """yes"""
    if os.path.exists(f):
        os.remove(f)
        print(f"{f} had just been deleted.")
    else:
        print(f"{f} does not exists.")


def main():
    file = "./tmp/test_file.txt"
    write_file(file)
    read_file(file)
    # remove_file(file)


if __name__ == "__main__":
    main()
