n = int(input())
circ = input()
arr = []
dic = dict()
for i in range(n):
    num = int(input())
    dic[chr(65+i)] = num
res = 0
for i in range(len(circ)):
    if 65 <= ord(circ[i]) <= 90:
        arr.append(dic[circ[i]])
    else:
        if circ[i] =='*':
            a = arr.pop()
            b = arr.pop()
            arr.append(a*b)
        elif circ[i] == '+':
            a = arr.pop()
            b = arr.pop()
            arr.append(a+b)
        elif circ[i] == '-':
            a = arr.pop()
            b = arr.pop()
            arr.append(b-a)
        else:
            a = arr.pop()
            b = arr.pop()
            result = float(format(b/a,".2f"))
            arr.append(result)

print(format(*arr,".2f"))
