n = input()
answer = 0 #정답 축척공간
now = '' #문자형 숫자를 담을 공간
dir = 0 #짝수 -> 양수, 홀수 -> 음수

for i in n :
    if i == '+':
        if dir%2 == 0:
            answer += int(now)
            now = ''
        else:
            answer -= int(now)
            now = ''
    elif i =='-':
        if dir%2 == 0:
            answer += int(now)
            now = ''
            dir += 1
        else:
            answer -= int(now)
            now = ''
    else:
        now += i
    #print(answer)
if dir%2 == 0:
    answer += int(now)
    now = ''
else:
    answer -= int(now)
    now = ''
print(answer)
