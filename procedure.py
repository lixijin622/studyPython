x = int(input("Please enter an integer: "))
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

for w in str(x):
    print(w, end=" ")

tList = ['hi', 'hello', 'world']
for w in tList[:]:
    if len(w) < 5:
        tList.insert(x, w)  # 超出了list边界就会接在后边，负数就是前边
print(tList)
