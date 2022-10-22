n = int(input())
for i in range(n):
    m = int(input())
    answer = []
    dic = dict()
    arr1 = list(map(str, input().split()))
    arr2 = list(map(str, input().split()))
    arr3 = list(map(str, input().split()))
    for j in range(m):
        dic[arr2[j]] = arr3[j]
    for j in range(m):
        answer.append(dic[arr1[j]])
    print(*answer)