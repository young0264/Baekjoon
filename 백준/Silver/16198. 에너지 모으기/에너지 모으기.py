import sys
n = int(input())
arr = list(map(int,input().split()))
answer = -sys.maxsize
# for i in range(n-2):
#     energy = arr[i-1]*arr[i+1]
#     new_arr = arr[:i] + arr[i+1:]

def dfs(array,sum_value):
    global answer
    if len(array) == 3:
        sum_value += (array[0]*array[-1])
        answer = max(answer,sum_value)
        # print(sum_value , array)
        return sum_value
    for i in range(1,len(array)-1):
        # array = array[:i]+array[i+1:]
        dfs(array[:i]+array[i+1:],sum_value+(array[i-1]*array[i+1]))
        # print(array[:i]+array[i+1:])
        # dfs(array,sum_value)
dfs(arr,0)
print(answer)

