N = int(input())
A = list(map(int, input().split()))

i = 1
while i:
    for a in A:
        if (a%(1<<i))!=0:
            exit(print(i-1))
    i+=1
