n = int(input())
answer = 0
ans_arr = []

for num in range(1,n+1):
    arr = [n]
    arr.append(num)
    while True:
        if arr[-2]>=arr[-1]:
            arr.append(arr[-2] - arr[-1])
        else:
            if answer < len(arr):
                answer = len(arr)
                ans_arr = arr[:]
            break
print(answer)
print(*ans_arr)


