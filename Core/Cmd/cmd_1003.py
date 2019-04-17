#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2019-04-17 13:16:39
# 这只竹鼠很漂亮呀

import re, time, sys

class cmd_1000():

    def __init__(self):

        self.c_id = 1000

        self.core = "echo sissel_travel_here"
        self.system = ["linux","windows"]
        self.description = "测试命令执行"
        
    def analysis(self, content):
        if 'sissel_travel_here' in content:
            return '测试命令执行成功'
        return False
        
