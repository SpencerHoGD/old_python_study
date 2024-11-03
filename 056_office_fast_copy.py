#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2019-10-14
"""快速的复制或者移动大量的小文件
"""

import os
import shutil
from concurrent import futures


# def getFnlist(folder):
#     """获取多层目录的文件夹和文件列表
#     Args:
#         folder (str): 根目录的文件夹名称(os.path)
#     Returns:
#         (folderList, file_name_list) (list, list): 文件夹和文件的列表
#     """
#     file_name_list = []
#     folderList = []
#     for root, dirs, files in os.walk(folder):
#         folderList.append(root)
#         file_name_list.extend([os.path.join(root, fn) for fn in files])

#     return folderList, file_name_list


def getFnlist(folder):
    """获取多层目录的文件夹和文件列表
    Args:
        folder (str): 根目录的文件夹名称(os.path)
    Returns:
        (folderList, file_name_list) (list, list): 文件夹和文件的列表
    """
    j = 0    #文件数量
    file_name_list = []
    k = 0    #文件夹数量
    folderList = []
    for root, dirs, files in os.walk(folder):
        folderList.append(root)
        k += 1
        # file_name_list.extend([os.path.join(root, fn) for fn in files])
        for fn in files:
            file_name_list.extend([os.path.join(root, fn)])
            j += 1

    return file_name_list, folderList
    # print(f'{j} file have been listed')
    # print(f'{k} folder have been listed')


def mkDirs(folderList):
    """逐级创建多层目录
    Args:
        folderList (str): 多层目录列表
    """
    for folder in folderList:
        if not os.path.exists(folder):
            os.mkdir(folder)


def moveFile(src_dist):
    source, dist = src_dist
    shutil.move(source, dist)


def copyFile(src_dist):
    source, dist = src_dist
    shutil.copy(source, dist)


def start():
    # 复制或者移动的目标文件夹
    distFolder = r"D:\read_write_test_copy"
    # 需要复制的文件夹
    sourceFolder = r"D:\read_write_test"

    if not os.path.exists(distFolder):
        os.mkdir(distFolder)
    distFolder = os.path.abspath(distFolder)
    sourceFolder = os.path.abspath(sourceFolder)

    folderList, file_name_list = getFnlist(sourceFolder)
    folderList = [folder.replace(os.path.dirname(sourceFolder), distFolder) for folder in folderList]

    mkDirs(folderList)
    for folder in folderList:
        print(folder)
    srcDisFiles = [(fn, fn.replace(os.path.dirname(sourceFolder), distFolder)) for fn in file_name_list]

    threads = 10
    threads = max(threads, len(srcDisFiles))

    with futures.ThreadPoolExecutor(threads) as excutor:
        excutor.map(copyFile, srcDisFiles)


if __name__ == '__main__':
    start()

