while True:
    s = input()
    if s == '*':
        exit(0)
    length = len(s)
    flag = 0
    for i in range(1, length):
        se = set()
        for j in range(length - i):
            se.add(s[j] + s[j + i])
        if len(se) != length - i:
            flag = 1
            print(s + " is NOT surprising.")
            break
    if not flag :
        print(s + " is surprising.")

