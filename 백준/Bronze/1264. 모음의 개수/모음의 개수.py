

arr = [97, 101, 105, 111, 117, 65, 69, 73, 79, 85]
while True:
    answer = 0
    s = input()
    if s == '#':
        break
    for i in s:
        if ord(i) in arr:
            answer +=1
    print(answer)
