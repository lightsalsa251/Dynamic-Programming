t = int(input())
for j in range(t):
    size = input()
    size = size.strip().split(' ')
    n = int(size[0])
    m = int(size[1])
    ip = input()
    ip = ip.strip().split(' ')
    #ip has nxm elements
    list,a = [],[]
    c = -1


    for i in range(n):
        for k in range(m):
            c+=1
            a.append(int(ip[c]))
        list.append(a)
        a = []
    s = [[0]*m for i in range(n)]


    
    max = 0
    for i in range(m):
	    s[0][i] = list[0][i]
	    if s[0][i]>max:
	        max = s[0][i]


    for i in range(n):
        s[i][0] = list[i][0]
        if s[i][0]>max:
	        max = s[i][0]


    for i in range(1,n):
        for k in range(1,m):
            if list[i][k]==1:
                s[i][k] = min(s[i-1][k],s[i][k-1],s[i-1][k-1]) + 1
                
                if s[i][k]>max:
                    max = s[i][k]
                    
            else:
                s[i][k] = 0
                
    print(max)
