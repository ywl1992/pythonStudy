# -*- coding:utf-8 -*-
from stack import Stack

def trans(num,base):
    dg='0123456789ABCDEF'
    s=Stack()
    while num>0:
        res=num%base
        s.push(res)
        num//=base
    str=''
    while not s.isEmpty():
        str=str+dg[s.pop()]
    return str

print(trans(3000,2))


