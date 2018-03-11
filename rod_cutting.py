##def cut(a,n,price,s):
##    if s>8:
##        return price-a[n+1]
##    elif s==8 or n<0:
##        return price
##    else:
##        b = max(cut(a,n-1,price+a[n],s+n+1),cut(a,n-1,price,s))
##        return b
a = [3,5,8,9,10,17,17,20]
##print(cut(a,7,0,0))

dp = [[0 for i in range(9)] for j in range(9)]


for i in range(1,9):
    dp[i][1] = 1
for j in range(9):
    dp[1][j] = a[0]*j
for i in range(2,9):
    for j in range(i,9):
        dp[i][j] = max(dp[i-1][j],dp[i][j-i]+a[i-1])
    for j in range(i+1,9):
        dp[j][i] = dp[i][i]

for i in range(9):
    print(dp[i])
