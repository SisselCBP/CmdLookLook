#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2018-12-20 14:46:40
# 这只竹鼠很漂亮呀

"""
本文件负责导入文件和命令。
"""

import re, os, sys
import importlib

class LoadFile(object):
    def __init__(self):
        self.cmd_path = './Cmd'
        if not os.path.exists(self.cmd_path):
            pass
            #os.mkdir(self.rules_path) # 创建规则目录
        self.file_list = self.list_parse()

        self.result = []
        # import function from rule
        for file_ in self.file_list:
            file_name = file_.split('.')[0]
            file_file = 'Cmd.'+ file_name

            my_module = importlib.import_module(file_file)
            my_class = getattr(my_module, file_name)
            self.result.append(my_class)


    def list_parse(self):
        files = os.listdir(self.cmd_path)
        result = []

        for f in files:
            if f.startswith('file_') and (not f.endswith('pyc')):
                result.append(f)
        return result

def load():
    load_ = LoadFile()
    return load_.result

if __name__ == '__main__':
    pass
