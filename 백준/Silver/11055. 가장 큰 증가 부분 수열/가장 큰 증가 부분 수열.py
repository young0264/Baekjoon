import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
sum_arr = [i for i in arr ]
answer = 0

for i in range(n):
    now_idx = i
    if not sum_arr[i]:
        sum_arr[i] = arr[i]
    for j in range(i + 1, n):
        if arr[now_idx] > arr[j]:  # 방문한 곳이 더 작으면
            sum_arr[j] = max(sum_arr[now_idx] + arr[j], sum_arr[j])
            now_idx = j  # 현재 pos이동
        else:
            for t in range(j-1,-1, -1):
                if arr[t] > arr[j]:
                    sum_arr[j] = max(sum_arr[j],sum_arr[t] + arr[j])

print(max(sum_arr))
