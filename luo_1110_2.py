Q = int(input())  # 先输入一个数字代表需要输入几行，比如Q=4，那么就需要再输入4行数据
q = []
for i in range(Q):
    q.append(input())
print(q)
for i in range(Q):
    if int(q[i])%2 <= 0.1:
        print('pb wins')
    else:
        print('zs wins')
