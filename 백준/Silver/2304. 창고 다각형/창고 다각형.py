#b의 최댓값인 a의 위치를 mid로 잡아서
#왼쪽에서 mid까지 & 오른쪽에서 mid까지

#새로운(더높은)높이의 bar가 나오면 이전의 x*y 넓이 더해주기
import sys
n = int(input())
arr = []
mid = [-1, -sys.maxsize] #x,y
dic = dict()
answer = 0
for _ in range(n):
    a,b = map(int,input().split())
    # arr.append([a,b])
    dic[a] = b
    if b > mid[1]:
        mid[1] = b
        mid[0] = a

now = 0
# print(dic)
x = (max(dic))

for i in range(1, mid[0]+1):
    if i in dic and now < dic[i]:
        # print("i",i)
        now = dic[i]
    answer += now
now = 0
# print("mid",mid)
# print(answer)

for i in range(x,mid[0],-1):
    # print("123",i)
    if i in dic and now < dic[i]:
        now = dic[i]
    if i == mid[0]:
        break
    answer += now

    # print(answer)
print(answer)

# 3
# 1 1
# 2 4
# 7 4

# 5
# 1 5
# 2 4
# 3 2
# 4 3
# 5 1
# arr.sort()
# now = [arr[0][0], arr[0][1]] #x,y
# # print("arr",arr)
# answer = 0
# for i in range(n):
#     # print(now)
#     if arr[i][0] == mid[0]:
#         res = (arr[i][0] - now[0])*now[1]
#         # print(res,arr[i],now)
#         answer += res
#         break
#     elif arr[i][1] > now[1]:
#         answer += (arr[i][0] - now[0])*now[1]
#         now = arr[i][0],arr[i][1]
#
# arr[-1][0] += 1
#
# now = [arr[-1][0], arr[-1][1]]
# for i in range(n-1,-1,-1):
#     if arr[i][0] == mid[0]:
#         # answer += arr[i][1]
#         if now[1] == mid[1]:
#             answer += (now[0]-1 - arr[i][0])*now[1]
#         else:
#             answer += (now[0]-1 - arr[i][0])*now[1]
#             answer += arr[i][1]
#         break
#     elif arr[i][1] > now[1]:
#         res = (now[0] - arr[i][0])*now[1]
#         answer += res
#         now = arr[i][0],arr[i][1]
#
# print(answer)
# # 5
# # 1 11
# # 2 11
# # 3 11
# # 4 11
# # 5 11
#
#
# 5
# 1 11
# 2 11
# 3 11
# 4 11
# 5 11