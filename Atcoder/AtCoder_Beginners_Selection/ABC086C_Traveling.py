N = int(input())

txy = [list(map(int, input().split())) for _ in range(N)]

x = 0
y = 0
t0 = 0
for i in range(N):
    Lnum = abs(txy[i][1]-x)+abs(txy[i][2]-y)
    Tnum = txy[i][0] - t0
    if Lnum - Tnum > 0 or (Tnum-Lnum)%2==1:
        exit(print('No'))
    t0, x, y = txy[i]
    
print('Yes')