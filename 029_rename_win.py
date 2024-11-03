#coding:utf-8
#author:hexiaoming

import os
path = "D:/rename"
filelist = os.listdir(path)

count = 0

for file in filelist:   
    Olddir = os.path.join(path,file)  
    if os.path.isdir(Olddir):  
        continue
    filename = os.path.splitext(file)[0]   
    filetype = os.path.splitext(file)[1]  
    Newdir = os.path.join(path,"天昱凤凰城JPG文件列表"+str(count).zfill(4)+filetype)  
    os.rename(Olddir,Newdir)

    count+=1
