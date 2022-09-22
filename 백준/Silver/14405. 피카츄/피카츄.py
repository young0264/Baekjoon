arr = ["pi", "ka", "chu"]
s = list(input())
while len(s)>0:
    # print(s)
    if ''.join(s[:2]) == arr[0]:
        s = s[2:]
    elif ''.join(s[:2]) == arr[1]:
        s = s[2:]
    elif ''.join(s[:3]) == arr[2]:
        s = s[3:]
    else:
        print("NO")
        exit(0)
print("YES")