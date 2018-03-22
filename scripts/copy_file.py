#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
import shutil


def copyfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.copyfile(srcfile, dstfile)  # 复制文件
        print("copy %s -> %s" % (srcfile, dstfile))


if __name__ == '__main__':
    dirnames = ["doraemon", "walle"]
    for dirname in dirnames:
        filenames = os.listdir("../images/" + dirname)
        for index, filename in enumerate(filenames):
            srcfile = "../images/" + dirname + "/" + filename
            ext = filename.split('.')[1]
            dstfile = "../images/" + dirname + "_%d." % (index + 1) + ext
            copyfile(srcfile, dstfile)
