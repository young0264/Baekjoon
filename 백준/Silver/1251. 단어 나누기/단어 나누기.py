s = input()
length = len(s)
arr = []
# print(length)
for i in range(length-2):
    for j in range(i+1,length-1):
        for k in range(j+1,length):
            a = s[:i+1]
            b = s[i+1:j+1]
            c = s[k:]
            na = a[::-1]
            nb = b[::-1]
            nc = c[::-1]
            res = (na+nb+nc)
            if len(res)==length:
                arr.append(res)
arr.sort()
print(arr[0])