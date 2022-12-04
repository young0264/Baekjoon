n, s = map(int, input().split())
arr = list(map(int, input().split()))+[0]
answer = 1000000
sum_value = 0
left, right = 0, 0
sum_value += arr[right]
length = 1
flag = 0
while right < n :
    if sum_value >= s:
        answer = min(answer, length)
        flag = 1
        # print("length,left,right,sum_value",length,left,right,sum_value)
    if left == right:
        sum_value = arr[right]
        length = 1
        if sum_value < s:
            right += 1
            sum_value += arr[right]
            length += 1
        else:
            left += 1
            right += 1
            sum_value = arr[right]
    else:
        if sum_value < s:
            right += 1
            sum_value += arr[right]
            length += 1

        elif sum_value >= s:
            sum_value -= arr[left]
            left += 1
            length -= 1

if not flag:
    print(0)
else:
    print(answer)
