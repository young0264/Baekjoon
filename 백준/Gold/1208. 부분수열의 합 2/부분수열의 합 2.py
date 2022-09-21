import sys
from itertools import combinations
from bisect import bisect_left, bisect_right
def input():
    return sys.stdin.readline().rstrip()
n,s = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0

left_arr = arr[:n//2]
right_arr = arr[n//2:]

def find_sort_arr(arr):
    new_arr = []
    for i in range(1, len(arr)+1):
        for combi in combinations(arr,i):
            new_arr.append(sum(combi))
    return new_arr

def find(arr,num):
    res= bisect_right(arr,num) - bisect_left(arr,num)
    r = bisect_right(arr,num)
    l = bisect_left(arr,num)
    # print("r",res, arr, num,r,l)
    return res

left_sum_arr = find_sort_arr(left_arr)
right_sum_arr = find_sort_arr(right_arr)
left_sum_arr.sort(),right_sum_arr.sort()
res1 = find(left_sum_arr,s)
res2 = find(right_sum_arr,s)
answer += res1
answer += res2
# print("a",answer)
for i in right_sum_arr:
    # if i+leftvalue == s
    num = s-i
    answer += find(left_sum_arr,num)
print(answer)
