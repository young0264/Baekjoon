n = int(input())
arr = []
answer = 0
cnt = 0
for _ in range(n):
    arr.append(int(input()))
r_arr = sorted(arr,reverse=True)
# print(arr)
# print(r_arr)

#
# for i in range(n):
#     idx = i+1
#     if arr[i] < r_arr[i]:
#         res = r_arr[i] - arr[i]
#         answer += res
# print(answer)

for i in range(-1,-n-1,-1):
    if arr[i] == n:
        cnt += 1
        n -= 1
print(n)