a,b = map(int,input().split())
b = str(b)
b_list = list(b)
m = len(b_list)
for i in range(m):
    if i == 0:
        print(b_list[i]+'*'+str(a)+'^'+str(m-i-1),end='')
    else:
        if int(b_list[i]) == 0:
            continue
        else:
            print('+'+b_list[i]+'*'+str(a)+'^'+str(m-i-1),end='')



