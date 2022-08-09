"""
输入一串空格分隔的单词,去重并且排序
"""
names = list(map(str,input().split()))
name_set = set(names)
print(list(sorted(name_set)))