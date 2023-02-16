n,m = map(int,input().split())
left , right = 1,m
j = int(input())
answer = 0

for _ in range(j):
    a = int(input())
    if left <= a <= right:
        continue
    elif a < left:
        res = left-a
        left -= res
        right -= res
        answer += res

    elif a > right:
        res = a - right
        left += res
        right += res
        answer += res
    # print(res)
print(answer)
