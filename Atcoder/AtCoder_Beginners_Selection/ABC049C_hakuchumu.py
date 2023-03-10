from collections import deque

S = list(input())
Snum = len(S)
Cam = ['dream', 'dreamer', 'erase', 'eraser']

Slist = deque()
Slist.append(['', 0])

while Slist:
    _, index = Slist.pop()
    if index==Snum:
        exit(print('YES'))
        
    for c in Cam:
        if S[index:index+len(c)] == list(c):
            Slist.append([c, index+len(c)])
    
print('NO')