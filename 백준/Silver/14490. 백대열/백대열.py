def gcd(a,b):
    i = min(a,b)
    while True:
        if a%i==0 and b%i==0:
            return i
        i -= 1
a,b = input().split(':')
a,b = int(a),int(b)
mod = gcd(a,b)
a,b = a//mod,b//mod
print(str(a)+":"+str(b))
