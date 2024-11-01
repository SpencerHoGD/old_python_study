# !/usr/bin/python

import os
# scr_dir = r'd:\read_write_test'
# dst_dir = r'd:\read_write_test_copy'
scr_dir = '$HOME/Pictures'
dst_dir = '$HOME/Pictures/test_copy'




def getPathListFileList(dirpath):
    i = 0
    j = 0
    k = 0
    pathList = []
    fileList = []
    for (path, dirs, files) in os.walk(dirpath):
        pathList.append(path)
        for file in files:
            filePath = os.path.join(path, file)
            fileList.append(filePath)

    return pathList, fileList
    # print(pathList)
    print(fileList)


def mkdirs(dirpath):
    """逐级创建多层目录
    Args:
        dirpath (str): 多层目录列表
    """
    for path in dirpath:
        if not os.path.exists(path):
            os.mkdir(path)




if __name__ == '__main__':
    # scr_dir = r'd:\read_write_test'
    # dst_dir = r'd:\read_write_test_copy'
    scr_dir = '$HOME/Pictures'
    dst_dir = '$HOME/Pictures/test_copy'
    pathList, fileList = getPathListFileList(scr_dir)
    for path in pathList:
        dstPath = path.replace(scr_dir, dst_dir)
        if not os.path.exists(dstPath):
            os.mkdir(dstPath)
    
