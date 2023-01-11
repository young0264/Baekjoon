from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    s = deque(input().split())
    ns = s.popleft()
    for i in range(n-1):
        q = s.popleft()
        if ord(q) <= ord(ns[0]):
            ns = q+ns
        else:
            ns = ns+q

    print(ns)
