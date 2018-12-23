# -*- coding:utf-8 -*-
'''
1 利用set set() 函数创建一个无序不重复元素集{}
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
2利用append
3 利用index 与append

'''


l=[1,3,1,5,6]
l=list(set(l))
print(l)
l=[1,5,5,6]
l1=[]
for i in l:
    try:
        l1.index(i)
    except ValueError:
        l1.append(i)
print(l1)
l=[2,3,4,4,5]
l2=[]
for i in l:
    if not i in l2:
        l2.append(i)
print(l2)


