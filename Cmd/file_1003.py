#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2019-04-17 13:16:39
# 这只竹鼠很漂亮呀

import re, time, sys

class file_1003():

    def __init__(self):

        self.f_id = 1003

        self.core = "/proc/self/cwd"
        self.system = ["linux"]
        self.description = "/proc下路径"
        
    def analysis(self, content):
        if content != '':
            return '/proc/self/路径为: {}'.format(content)
        return False
        
