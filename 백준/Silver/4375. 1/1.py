while True:
    try:
        n = int(input())
        length = 1
        while True:
            num = int(str(1)*length)
            if num%n == 0:
                print(length)
                break
            else:
                length += 1
    except:
        break

