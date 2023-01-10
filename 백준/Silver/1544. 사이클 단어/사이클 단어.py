from collections import deque
n = int(input())
dic = dict()

for _ in range(n):
    s = deque(input())
    ns = ''.join(s)
    flag = 0
    length = len(s)
    if not dic:
        dic[ns] = 1
    else:
        for i in range(length-1):
            s = deque(s)
            x = s.popleft()
            s = ''.join(s)+x
            if s in dic:
                dic[s] += 1
                flag = 1
                break
    if not flag:
        dic[ns] = 1
print(len(dic))

