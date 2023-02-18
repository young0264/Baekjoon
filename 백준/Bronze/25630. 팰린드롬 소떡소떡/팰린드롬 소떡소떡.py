n = int(input())
s = input()


answer = 0
time = n//2
for i in range(time):
    if s[i]==s[-i-1]:
        continue
    else:
        answer +=1

print(answer)