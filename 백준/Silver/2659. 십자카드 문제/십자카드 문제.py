import sys

#arr의 값을 순서대로 문자열로 바꾸는 함수
def change(arr):
    res = ""
    for i in arr:
        res += str(i)
    return res

def findClockNum(ar):
    minNum = sys.maxsize
    for i in range(4):
        pr = ar.pop()
        ar = [pr] + ar
        res = int(change(ar))
        minNum = min(minNum,res)
    return minNum
dic = dict()
arr = list(map(int,input().split()))
min_res = sys.maxsize
length = len(arr)

min_res = findClockNum(arr)
#시계수 구하기
#시계수
answer = 0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            for t in range(1,10):
                pre = str(i)+str(j)+str(k)+str(t)
                res = findClockNum([i,j,k,t])
                if int(pre) == res:
                    answer += 1
                    if min_res == res:
                        print(answer)
                        exit(0)

