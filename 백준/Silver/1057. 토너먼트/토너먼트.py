import sys
input = sys.stdin.readline
n, left, right = map(int,input().split())
roundNum = 0
arr = [i for i in range(1,n+1)]
stack = []

# arr = [1,2,3,4,5,6]
# arr[1:3] = [7]
# print(arr)

while n>=2:
    length = (n//2)*2
    for i in range(0,length-1,2):
        # print("i : ", i, "arr : ", arr)
        a1, a2 = arr[i:i+2]
        if a1 == left and a2 == right:
            print(roundNum + 1)
            exit(0)
            break
        elif a1 == right and a2 == left:
            print(roundNum + 1)
            exit(0)
            break
        if a1 == left or a2 == left:
            # arr[i:i+2] = [left]
            stack.append(left)
        elif a1 == right or a2 == right:
            # arr[i:i+2] = [right]
            stack.append(right)
        else:
            # arr[i:i + 2] = [arr[i]]
            stack.append(arr[i])
    if len(arr)%2:
        stack.append(arr[-1])
    roundNum += 1
    arr = stack[:]
    stack = []
    n = len(arr)
    # print("arr : ", arr)
print(-1)





# import math
# n, left, right = map(int,input().split())
# answer = 0
# last = 0
#
# #홀수일때 마지막수를 last에 저장하고 n=n-1
# if n%2:
#     last = n
#
# arr = [i for i in range(1,n+1)]
# stack = []
# length = n
# flag = 1
# while flag:
#     isNotOdd=0
#     num = 0
#     if length%2: #홀수일때
#         length -=1
#         isNotOdd=1
#         num = arr[-1]
#     else:
#         isNotOdd=0
#
#     for i in range(0, length, 2):
#         if arr[i]==left and arr[i+1]==right:
#             flag = 0
#             print(answer+1)
#             exit(0)
#             break
#         elif arr[i]==right and arr[i+1]==left:
#             print(answer+1)
#             exit(0)
#             flag = 0
#             break
#         if arr[i]== left or arr[i+1]==left:
#             stack.append(left)
#         elif arr[i]==right or arr[i+1]==right:
#             stack.append(right)
#         else:
#             stack.append(arr[i])
#
#     arr = stack[:]
#     length = len(arr)
#     answer += 1
#     stack = []
#     if length%2 and isNotOdd:
#         arr.append(num)
#         length += 1
#     if len(arr)==1:
#         break
#
# if last:
#     if last==left and arr[0]==right:
#         print(answer + 1)
#     elif last==right and arr[0]==left:
#         print(answer+1)
#     else:
#         print(-1)
# else:
#     if answer:
#         print(answer)
#     else:
#         print(-1)
#
