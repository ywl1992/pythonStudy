# -*- coding:utf-8 -*-
'''
__call__函数是在类或者对象加()触发执行

'''
import time
class Timer(object):
    def __init__(self,func):
        print('开始计时')
        self.func=func
        self.name=func.__name__

    def __call__(self, *args, **kwargs):
        a=time.time()
        res=self.func(*args,**kwargs)
        b=time.time()
        print('%s函数运行时间是%s'%(self.name,(b-a)))
        return res



@Timer #=========>>run=Timer(run)
def run(x,y):
    print('{0}{1}开始跑步'.format(x,y))
    time.sleep(3)

run('ywl','ljl')#=========>>触发__call__函数
