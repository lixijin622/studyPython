print((3+5j)+2)  # 复数
print('C:\name')
print('C:\\name')
print(r'C:\name')
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to\
""")
print('she'+2*'l')
print('she''ll')
word = 'python'
print(word[0])
print(word[-1])
print(word[0:2])  # python 字符串不可改变 word[0]='J'是错的
word = 'J'+word[1:]
print(word)
print(len(word))
tList = [0, 1, 2, 3, 4, 6]
print(tList)
tList[5] = 5
print(tList)
tList.append(6)
print(tList)
tList2 = [7, 8, 9]
Lists = [tList,tList2]
print(Lists)
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
print('while end')  # 靠是否缩进判断循环体
