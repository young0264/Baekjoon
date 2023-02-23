n = int(input())
s = input()
answer = 0

arr = ['a', 'e', 'i', 'o', 'u']
for i in s:
    if i in arr:
        answer += 1

print(answer)