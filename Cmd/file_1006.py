#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2019-04-17 13:16:39
# 这只竹鼠很漂亮呀

import re, time, sys

class file_1006():

    def __init__(self):

        self.f_id = 1006

        self.core = "/proc/self/environ"
        self.system = ["linux"]
        self.description = "/proc下环境变量"
        
    def analysis(self, content):
        if content != '':
            return '环境变量: {}'.format(content)
        return False
        
