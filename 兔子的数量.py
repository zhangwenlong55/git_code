"""
求得兔子数量和月数
"""

def month(n):
    if n == 1:
        rabbit = 2
    elif n == 2:
        rabbit = 2
    return rabbit == month(n-1)+month(n-2)
    print(rabbit)