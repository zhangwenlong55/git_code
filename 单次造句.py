"""
输入单词造句,输入0结束输入
"""
st = []
start = True
while start:
    s = input()
    if s != "0":
        st.append(s)
    elif s == "0":
        start = False
print(" ".join(st))