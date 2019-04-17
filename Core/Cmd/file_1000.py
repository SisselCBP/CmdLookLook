#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2019-04-17 13:16:39
# 这只竹鼠很漂亮呀

import re, time, sys

class file_1000():

    def __init__(self):

        self.f_id = 1000

        self.core = "/etc/passwd"
        self.system = ["linux"]
        self.description = "文件包含测试"
        
    def analysis(self, content):
        if 'root:x:0:0:root' in content:
            return '存在文件包含'
        
        return False
        
