# -*- coding:utf-8 -*-
'''
队列：先到先得
队列的数据抽象类型：1入队尾 2 从队首移除返回移除元素3 是否未空 4 返回对列项数 size
添加新项的一端为队尾移除项的一段为队首，当一个元素从队尾进入队列时一直向队首移动 先进先出
'''
class Queue(object):
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)