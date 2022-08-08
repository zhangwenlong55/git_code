"""
牛客网--格式化清单
"""

lis = ['apple', 'ice cream', 'watermelon', 'chips', 'hotdogs', 'hotpot']

start = True
while start:
    lis.pop()
    print(lis)
    if lis == []:
        break
