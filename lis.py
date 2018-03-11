t = int(input())
for k in range(t):
    n = int(input())
    a = input()
    a = a.strip().split(' ')
    b = [1]*n
    max = 1
    for i in range(1,n):
        for j in range(i):
            if int(a[i])>int(a[j]):
                if b[i]<=b[j]:
                    b[i]+=1
                    max = b[i]
    if n==0:
        max = 0
        print(max)
