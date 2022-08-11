"""
求得兔子数量和月数
"""

def rabbit(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    return rabbit(n-1) + rabbit(n-2)

s = int(input())
print(rabbit(s))