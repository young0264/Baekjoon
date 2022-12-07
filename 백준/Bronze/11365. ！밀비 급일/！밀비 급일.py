while True:
    s = (input())
    if s == 'END':
        break
    s = list(s)[::-1]
    print(''.join(s))