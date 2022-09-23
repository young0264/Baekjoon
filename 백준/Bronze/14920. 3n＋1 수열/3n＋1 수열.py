n = int(input())
s = set()
s.add(n)
answer = 1
while n != 1:
    if n%2 == 0:
        n = n//2
        if n not in s:
            s.add(n)
        else:
            break
    else:
        n = 3*n+1
        if n not in s:
            s.add(n)
        else:
            break
    answer += 1

print(answer)