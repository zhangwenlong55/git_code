"""
使用字典统计输出单次字母出现的频次
"""
word = input()
dit = {}

for i in word:
    dit[i] = word.count(i)

print(dit)