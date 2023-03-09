N = int(input())
a = list(map(int, input().split()))

a = sorted(a, reverse=True)
ans = 0
for i in range(len(a)):
    if i%2==0:
        ans += a[i]
    else:
        ans -= a[i]
        
print(ans)