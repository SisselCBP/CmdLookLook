#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2019-04-07 13:16:39
# 这只竹鼠很漂亮呀

import re, time, sys

class file_1005():

    def __init__(self):

        self.f_id = 1005

        self.core = "/proc/self/comm"
        self.system = ["linux"]
        self.description = "/proc下comm"
        
    def analysis(self, content):
        if content != '':
            return '/proc下comm: {}'.format(content)
        return False
        
