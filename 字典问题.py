# -*- coding:utf-8 -*-
'''
将[{1:”a”},{2:”b”}]转换为[{‘value’:’a’, ‘key’:1},{‘value’:’b’, ‘key’:2}]

Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。

'''
dict={1:'a',2:'b'}
# print(dict.items())dict_items([(1, 'a'), (2, 'b')])
l=[{'key':key,'value':value} for key,value in dict.items()]
print(l)
# '遍历字典的key'
d={1:'ss',2:'dd'}
for i in d.keys():
    print(i)
    print('==============')
for i in d:
    print(i,end='')
#遍历字典的value
for v in  d.values():
    print(v)
#k v 一起迭代
for k,v in d.items():
    print(k,v)
