#! /usr/bin/env python
'''
Created on 2019-10-14
hexiaoming
'''

import os
from os import path
import shutil
from shutil import copyfile


# def getFnlist(dirs):
#     """获取多层目录的文件夹和文件列表
#     get dirPaths list and filePaths
#     Args:
#         folder (str): 根目录的文件夹名称(os.path)
#     Returns:
#         (dirPathsList, filePathsList) (list, list): 文件夹路径列表和文件路径列表
#     """
i = 0
j = 0
# k = 0
scr_dir = r'd:\read_write_test'
dst_dir = r'd:\read_write_test_copy'
filePathsList = []
dirPathsList = []
for dirPaths, floderNames, fileNames in os.walk(dirs):
    # for fileName in fileNames:
    #     filePathsList.append(os.path.join(dirPaths, fileName))
    #     print(filePathsList)
    #     i += 1
    for floderName in floderNames:
        # print(os.path.join(dirPaths, floderName))
        dirPathsList.append(os.path.join(dirPaths, floderName))
        # print(dirPathsList)
        j += 1
        for old in dirPathsList:
            new = old.replace(scr_dir, dst_dir)
            print(new)
        
print(f'{i} dirPath has been listed')
print(f'{j} fileNames has been listed')
    # print(floderNames)
    # print(fileNames)
    # for file_name in fileNames:
    #     src_file_path = os.path.join(dirPaths, file_name)
    #     dst_file_path = src_file_path.replace(scr_dir, dst_dir)
    #     print(dst_file_path)
    #     j += 1
# print(f'{j} src_file_paths has been listed')
# print(f'{j} dst_file_paths has been listed')
#     for dir_name in floderNames:
#         src_dir_path = os.path.join(dirPaths, dir_name)
#         dst_dir_path = src_file_path.replace(scr_dir, dst_dir)
#         print(dst_file_path)
#         k += 1
# print(f'{k} directorys has been listed')
