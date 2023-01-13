'''
뒤에 들어올 수 arr[i]가 arr[stack[-1]]보다 크면 stack[-1]=idx에 해당하는 위치의 answer[idx]에 현재값 arr[i]를 저장

앞서 입력된 수보다는 작은수들이 들어오기 때문에 현재의 arr[i]값을 기준으로 while stack을 통한 answer 값을 보장할 수 있다.
'''

n = int(input())
arr = list(map(int,input().split()))
stack = [0]
answer = [-1]*n

for i in range(1,n):
    while stack:
        if arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            answer[idx] = arr[i]
        else:
            break
    stack.append(i)

print(*answer)




