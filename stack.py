# -*- coding:utf-8 -*-
'''
自定义一个栈结构：后进先出
栈的抽象数据类型：1 入栈 2出栈 3返回栈顶元素 4 判断是否为空 5 返回栈大小
'''
class Stack(object):
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


