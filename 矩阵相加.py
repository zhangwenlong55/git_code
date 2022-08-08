"""
输出一个数，为该矩阵内元素的倍数
"""
lis = [[1,2,3,],[4,5,6],[7,8,9]]
lis_2 = []
s = int(input())

for i in lis:
    lis_1 = list(map(lambda x:x*s,i))
    lis_2.append(lis_1)
    
print(lis_2)
