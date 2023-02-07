t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    answer = 0
    dic = dict()
    for i in range(n):
        dic[arr[i]] = 1
    arr.sort()
    for left in range(n-2):
        for right in range(n-1,left+1,-1):
            if (arr[left]+arr[right])%2 == 0:
                res = (arr[left]+arr[right])//2
                if res in dic:
                    answer += 1
    print(answer)

