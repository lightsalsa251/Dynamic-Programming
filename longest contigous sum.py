t = int(input())
for i in range(t):
    n = int(input())
    a = input()
    a = a.strip().split(' ')
    so_far = 0
    ending_here = 0
    for i in a:
        ending_here +=int(i)
        if ending_here<0:
            ending_here = 0
        if so_far<ending_here:
            so_far = ending_here
    if 0 not in a and so_far==0:
        so_far = min(a)
    print(so_far)
