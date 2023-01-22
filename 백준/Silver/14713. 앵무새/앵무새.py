from collections import deque

n = int(input())
arr = []
for _ in range(n):
    bird = deque(list(map(str,input().split())))
    arr.append(bird)

sentence = list(map(str,input().split()))
length = len(sentence)
for i in range(length):
    word = sentence[i]
    flag = 0
    while True:
        for j in range(n):
            if arr[j] and arr[j][0] == word:
                arr[j].popleft()
                flag = 1
                break
        if flag:
            break
        else:
            print('Impossible')
            exit(0)
    # print("arr : ", arr)

for i in range(n):
    if arr[i]:
        print('Impossible')
        exit(0)
print('Possible')
