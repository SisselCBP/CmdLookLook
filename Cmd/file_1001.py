#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2019-04-17 13:16:39
# 这只竹鼠很漂亮呀

import re, time, sys

class file_1001():

    def __init__(self):

        self.f_id = 1001

        self.core = "/proc/self/cmdline"
        self.system = ["linux"]
        self.description = "启动指令"
        
    def analysis(self, content):
        if content != '':
            return '启动指令: {}'.format(content)
        return False
        
