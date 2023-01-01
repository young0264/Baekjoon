from collections import deque
n = int(input())
arr = deque()
cnt = 0
while True:
    m = int(input())
    if m == -1:
        break
    if m == 0 :
        arr.popleft()
        cnt -= 1
    elif cnt < n:
        cnt += 1
        arr.append(m)
if not arr:
    print('empty')
else:
    for i in arr:
        print(i,end=' ')