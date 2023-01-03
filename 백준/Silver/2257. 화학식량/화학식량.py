se = input()
answer = 0
length = len(se)
stack = []

# 40,41,65,90

for i in se:
    if i == ')':
        res = 0
        while True:
            s = stack.pop()
            if s == '(':
                break
            res += s
        stack.append(res)

    elif i=='H':
        stack.append(1)
    elif i=='C':
        stack.append(12)
    elif i=='O':
        stack.append(16)
    elif i== '(':
        stack.append(i)
    else: # 숫자일때
        k =stack.pop()*int(i)
        stack.append(k)
print(sum(stack))



    # stack.append(i)


