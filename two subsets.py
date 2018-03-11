t = int(input())
for k in range(t):
    n = int(input())
    a = list(map(int,input().split(' ')))
    if sum(a)%2!=0:
        print('NO')
    else:
        mid = sum(a)/2
        dp = [[True]*(int(mid)+1)]*(n+1)
        for i in range(1,int(mid)+1):
            dp[0][i] = False
        for i in range(1,n+1):
            for j in range(1,int(mid)+1):
                if j<a[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i][j-a[i]]
        if dp[i][j]:
            print("YES")
        else:
            print("NO")
