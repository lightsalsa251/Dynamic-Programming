def subset(s,n):
    if s==0:
        return True
    if n<0 and s!=0:
        return False
    elif s<a[n]:
        return subset(s-a[n-1],n-1)
    else:
        return subset(s-a[n],n-1) or subset(s,n-1)

a = list(map(int,input().strip().split()))
p = len(a)
m = 0
flag1,flag = False,False
if m==0:
    if 0 in a:
        flag1 = True
else:
    print('ok')
    flag = subset(m,p-1)
print(flag)
