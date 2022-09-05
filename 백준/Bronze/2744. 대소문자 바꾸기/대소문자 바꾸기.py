s = input()
answer = ''
for i in s:
    if 65<= ord(i) <=90:
        answer += chr(ord(i)+32)
    else:
        answer += chr(ord(i)-32)
print(answer)