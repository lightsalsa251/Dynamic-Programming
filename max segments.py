##def cut(r,count):
##    if a==r:
##        return count
##    elif a>r:
##        return 0
##    else:
##        return max(cut(r-x,count+1),cut(r-y,count+1),cut(r-z,count+1))
##t = int(input())
##for k in range(t):
##    n = int(input())
##    x,y,z = map(int,input().strip().split())
##    a = min(x,y,z)
##    print(cut(n,1))

t = int(input())
for k in range(t):
    n = int(input())
    x,y,z = map(int,input().strip().split())
    a = min(x,y,z)

    inf = -32768
    dp = [0]*(n+1)
    dp[a] = 1
    for i in range(a+1,n+1):
        if i-x<0:
            b = inf
        else:
            b = dp[i-x]
        if i-y<0:
            c = inf
        else:
            c = dp[i-y]
        if i-z<0:
            d = inf
        else:
            d = dp[i-z]
        if (b==0 or b==inf) and (c==0 or c==inf) and (d==0 or d==inf) and (i!=x and i!=y and i!=z):
            dp[i] = 0
        else:
            dp[i] = max(b,c,d)+1
    print(dp)
