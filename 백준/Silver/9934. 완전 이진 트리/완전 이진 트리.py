k = int(input())
arr = list(map(int,input().split()))
answer_arr = [[] for _ in range(k)]
def find(arr,depth):
    if depth == k:
        return
    mid = len(arr)//2
    answer_arr[depth].append(arr[mid])
    # print(arr[:mid], arr[mid+1:])
    find(arr[:mid],depth+1)
    find(arr[mid+1:],depth+1)
find(arr,0)
# print(answer_arr)
for ans in answer_arr:
    # print(*ans)
    # print(ans,end=' ')
    for i in ans:
        print(i,end=' ')
    print()