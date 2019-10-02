# -*- coding: utf-8 -*-

##################################
# 说明
# 偶然间在某网站看到大家对nba经理模式的讨论，突发奇想觉得自己可以做一个简单的游戏。话不多说，现在搞起
# 本游戏将暂时以英语为主要语言，因为网上的资料/数据库大多为英语。当然，我会在闲暇时间进行中文翻译工作。
##################################

class console():
    def __init__(self):
        self.history = []
        self.input_history = []
    def console_output(self,output_text):
        print(output_text)
        self.history.append(output_text)
        return None
    def console_input(self,input_text):
        print(input_text)
        user_input = input(">> ")
        self.input_history.append(user_input)
        return user_input



############ Test for convenience

myConsole = console()
myConsole.console_output("Hi, how're you")
myConsole.console_input("Anything you want to say?")
