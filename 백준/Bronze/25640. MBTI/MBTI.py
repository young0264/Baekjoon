s = input()
n = int(input())
answer = 0
for i in range(n):
    ns = input()
    if s == ns:
        answer += 1
print(answer)