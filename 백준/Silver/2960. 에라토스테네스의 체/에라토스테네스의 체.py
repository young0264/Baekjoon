import math
n,k = map(int,input().split())
count = 0
visited = [0]*(n+1)
def isPrimeNumber(n):
    if n==2 :
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

for i in range(2,n+1):
    if isPrimeNumber(i) and not visited[i]:
        num = n//i
        for j in range(1,num+1): #1,2,3
            if not visited[i*j]:
                visited[i*j] = 1
                count += 1
            if count == k:
                print(i*j)
                count+=1

