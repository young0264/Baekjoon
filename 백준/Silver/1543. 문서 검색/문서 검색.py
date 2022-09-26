s1 = list(map(str,input().split()))
s2 = list(map(str,input().split()))
s1 = list(''.join(s1))
s2 = list(''.join(s2))
answer = 0
# print(s1,s2)
idx = -1
length = len(s2)

while idx<len(s1):
    if s1[idx:idx+length] == s2:
        # print(idx,idx+length)
        answer += 1
        idx = idx+length
    else:
        idx += 1
        continue
print(answer)