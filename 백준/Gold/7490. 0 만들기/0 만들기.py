t = int(input())
arr = [' ', '+', '-']

import sys
def input():
    return sys.stdin.readline().rstrip()
def dfs(num,box):
    if num==n+1:
        new_box = box.replace(' ','')
        r = eval(new_box)
        if r==0:
            answer.append(box)
        return
    for a in arr:
        dfs(num+1, box+a+str(num))

answer = []
for _ in range(t):
    n = int(input())
    dfs(2,'1')
    answer.append(' ')
print(*answer,sep='\n')