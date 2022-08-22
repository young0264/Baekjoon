h , w = map(int,input().split())
block = list(map(int,input().split()))
answer = []
for i in range(1,w-1):
    left = max(block[:i])
    right = max(block[i+1:])
    real = min(left,right)
    rain = real - block[i]
    if rain > 0:
        answer.append(rain)
print(sum(answer))