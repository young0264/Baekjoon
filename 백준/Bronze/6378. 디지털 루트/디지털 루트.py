while True:
    n = input()
    if n=='0':
        break
    res =0
    while True:
        for i in n:
            res += int(i)
        if len(str(res)) == 1:
            break
        else:
            n = str(res)
            res = 0
    print(res)
