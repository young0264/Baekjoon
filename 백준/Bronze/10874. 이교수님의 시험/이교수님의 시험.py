n = int(input())

answer = []
for i in range(10):
    answer.append(i%5+1)
# print(answer)


for i in range(n):
    arr = list(map(int,input().split()))
    if arr == answer:
        print(i+1)
        

