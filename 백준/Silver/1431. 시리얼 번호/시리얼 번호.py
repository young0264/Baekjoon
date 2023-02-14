n = int(input())
arr = []

for _ in range(n):
    s = input()
    num = 0
    for i in s:
        if 48 <= ord(i)<= 57:
            num += int(i)
    arr.append((len(s), num, s))

new_arr = sorted(arr, key=lambda x:(x[0],x[1],x[2]))
for a in new_arr:
    print(a[2])