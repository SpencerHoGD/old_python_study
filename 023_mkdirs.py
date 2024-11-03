# !/usr/bin/python

import os

# scr_dir = r'd:\read_write_test'
# dst_dir = r'd:\read_write_test_copy'
SRC_DIR = "$HOME/Pictures"
DST_DIR = "$HOME/Pictures/test_copy"


def get_pathlist_and_filelist(dirpath):
    path_list = []
    file_list = []
    for path, dirs, files in os.walk(dirpath):
        path_list.append(path)
        for file in files:
            file_path = os.path.join(path, file)
            file_list.append(file_path)

    return path_list, file_list
    # print(pathList)
    print(file_list)


def mkdirs(dirpath):
    """逐级创建多层目录
    Args:
        dirpath (str): 多层目录列表
    """
    for path in dirpath:
        if not os.path.exists(path):
            os.mkdir(path)


if __name__ == "__main__":
    # scr_dir = r'd:\read_write_test'
    # dst_dir = r'd:\read_write_test_copy'
    SRC_DIR = "$HOME/Pictures"
    DST_DIR = "$HOME/Pictures/test_copy"
    path_list, file_list = get_pathlist_and_filelist(SRC_DIR)
    for path in path_list:
        dst_path = path.replace(SRC_DIR, DST_DIR)
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
