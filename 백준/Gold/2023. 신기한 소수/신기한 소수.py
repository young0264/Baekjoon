import math,sys
n = int(input())
arr = []
# box = ''
def isPrimeNum(x):

    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def dfs(cnt,box):
    res = ''.join(box)
    if cnt == n:
        if isPrimeNum(int(res)):
            arr.append(int(res))
        return
    if isPrimeNum(int(res)):
        for i in range(10):
           dfs(cnt+1,box+[str(i)])
for i in range(2,10):
    dfs(1,[str(i)])
arr.sort()
for i in arr:
    print(i)

