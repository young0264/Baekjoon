import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input().rstrip())
    arr = [input().rstrip() for _ in range(n)]
    arr.sort()
    flag = 0
    for i in range(n-1):
        length = len(arr[i])
        if arr[i] == arr[i+1][:length]:
            print("NO")
            flag = 1
            break
    if not flag:
        print("YES")

    # for i in range(n-1):
        # if not flag:
        #     for j in range(i+1,n):
        #         if arr[i] in arr[j]:
        #             print("NO")
        #             flag = 1
        #             break
    # if not flag :
    #     print("YES")
