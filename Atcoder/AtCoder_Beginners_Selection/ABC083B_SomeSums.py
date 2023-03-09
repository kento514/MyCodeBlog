N, A, B = map(int, input().split())

ans = 0
for i in range(1, N+1):
    Sumi = sum(list(map(int, str(i))))
    if Sumi>=A and Sumi<=B:
        ans+=i
        
print(ans)
        