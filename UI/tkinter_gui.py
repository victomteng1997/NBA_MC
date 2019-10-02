# -*- coding: utf-8 -*-

##################################
# 说明
# 偶然间在某网站看到大家对nba经理模式的讨论，突发奇想觉得自己可以做一个简单的游戏。话不多说，现在搞起
# 本游戏将暂时以英语为主要语言，因为网上的资料/数据库大多为英语。当然，我会在闲暇时间进行中文翻译工作。
##################################

import copy
import threading

import tkinter as tk

class tkinter_GUI():
    tkinter_log = None
    tkinter_input_history = None

    def __init__(self):
        self.root = tk.Tk()
        self.root.title = "My Game"
