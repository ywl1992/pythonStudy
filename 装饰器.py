# -*- coding:utf-8 -*-
'''
装饰器原则：不修改原函数的代码，不修改原函数的运行方式
'''
import time
def timer(func):
    print('开始装饰')
    def wrapper(*args,**kwargs):
        atime = time.time()
        res=func(*args,**kwargs)
        btime=time.time()
        print('函数运行时间是{}'.format(btime-atime))
        return res
    return wrapper
@timer#============>>run=wrapper=timer(run)
def run():
    time.sleep(2)
run()#======================>>

