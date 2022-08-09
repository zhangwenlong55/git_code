word = input()
dit = {}

for i in word:
    dit[i] = word.count(i)

print(dit)