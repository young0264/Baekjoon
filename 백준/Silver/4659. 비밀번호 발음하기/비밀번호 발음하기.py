arr = ['a', 'e', 'i', 'o', 'u']
brr = ['a', 'e', 'i', 'o', 'u', 'w','y']
crr = ['ee', 'oo']



def v1(s):
    for i in arr:
        if i in s:
            return True
    return False

def v2(ss):
    con_a, con_b = 0,0
    for s in ss:
        if s in brr: #모음
            con_a += 1
            con_b = 0
        else:
            con_b += 1
            con_a = 0
        if con_a == 3 or con_b == 3:
            return False
    return True

def v3(s):
    length = len(s)
    for i in range(length-1):
        res = s[i:i+2]
        # print("res : ", res)
        if res[0]==res[1] :
            if (res[0]=='e' or res[0]=='o' ):
                # print(res)
                continue
            else:
                return False
    return True




while True:
    s = input()
    if s == 'end':
        break
    if (v1(s) == True )and( v2(s) == True) and (v3(s) == True):
        print("<"+s+"> "+ "is acceptable.")
    else:
        print("<"+s+"> "+ "is not acceptable.")

