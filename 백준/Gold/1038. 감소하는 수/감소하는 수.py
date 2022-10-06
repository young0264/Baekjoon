# n번째 감소하는 수를 출력

n = int(input())
cnt = 0
arr = []
def isRightNum(strNum):    #문자형
    pos = 10
    for i in strNum:
        if int(i) < pos:
            pos = int(i)
        else:
            return False
    return True

def dfs(strNum,lastNum):
    global cnt
    if isRightNum(strNum):
        arr.append(int(strNum))
    for i in range(0,lastNum):
        dfs(strNum+str(i),i)

for i in range(10):
    dfs(str(i),i)
arr.sort()
# print(arr)
if n < len(arr) :
    print(arr[n])
else:
    print(-1)


