# 65~90
from collections import deque

answer = ''
stack = []
que = deque()
s = input()
length = len(s)
priority = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}  # ( 설정은 stack에서 -1번째 처리를 위함
for i in range(length):
    if s[i] == '(':
        stack.append(s[i])
    elif s[i] in priority:  # 연산자
        while stack and priority[stack[-1]] >= priority[s[i]]:
            answer += stack.pop()

        stack.append(s[i])

        # if not stack:
        #     stack.append(s[i])
        # elif priority[stack[-1]] < priority[s[i]] : #우선순위가 높은건 그냥 stack에 넣어
        #     stack.append(s[i])
        # else:
        #     #우선순위가 낮거나 같은게 들어올때
        #     # priority[stack[-1]] >= priority[s[i]]
        #
        #     while stack and stack[-1] != '(':
        #         answer += stack.pop()
        #     stack.append(s[i])
    elif 65 <= ord(s[i]) <= 90:
        answer += s[i]  # 알파벳
    else:  # ) 닫히는 괄호 들어올 때
        # if stack:
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
    # print("answer : ", answer,stack)
while stack:
    if stack[-1] != '(':
        answer += stack.pop()
    else:
        stack.pop()
print(answer)
