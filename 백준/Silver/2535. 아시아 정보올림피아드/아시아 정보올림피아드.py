n = int(input())
arr = []
dic = dict()
for _ in range(n):
    # nation,student,grade = map(int,input().split())
    nums = list(map(int,input().split()))
    dic[nums[0]] = 0
    arr.append(nums)
arr = sorted(arr,key=lambda x:x[2])
answer = []
for i in range(n-1,-1,-1):
    if dic[arr[i][0]] >= 2:
        continue
    else:
        dic[arr[i][0]] += 1
        answer.append((arr[i][0],arr[i][1]))
for i in range(3):
    print(answer[i][0],answer[i][1])