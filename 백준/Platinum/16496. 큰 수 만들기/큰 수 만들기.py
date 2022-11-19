n = int(input())
arr = list(map(int,input().split()))
# length = len(str(max(arr)))
# print(length)
arr.sort(key=lambda x:str(x)*10, reverse=True)
answer = ''.join(map(str,arr))

print(int(answer))
