#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2019-04-17 13:16:39
# 这只竹鼠很漂亮呀

import re, time, sys

class file_1004():

    def __init__(self):

        self.f_id = 1004

        self.core = "~/.bash_history"
        self.system = ["linux"]
        self.description = "bash_history"
        
    def analysis(self, content):
        if content != '':
            return 'bash_history: {}'.format(content)
        return False
        
