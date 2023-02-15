n = int(input())
answer = 0
for _ in range(n):
    s = input()
    if int(s[2:])<=90:
        answer += 1


print(answer)