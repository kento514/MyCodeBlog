A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for i in range(A+1):
    if X - i*500 < 0:
        break
    for j in range(B+1):
        if X - (i*500+j*100) < 0:
            break
        if (X - (i*500+j*100))//50<=C:
            ans += 1
            
print(ans)

