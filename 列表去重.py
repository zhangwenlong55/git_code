"""
列表去重
"""
li=[1,2,2,5,3,9,8,77,45,45,66,99,88,88,25,26,25,21,21,21,24]
for i in li:
    if li.count(i)>1:
        li.remove(i)
    li.sort()                   # 列表排序
print(li)