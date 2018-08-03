
from random import randint
def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True

def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p


prime1=generate_big_prime(128)
prime2=generate_big_prime(128)


n=prime1*prime2
print("value of n is:",n)



totient=(prime1-1)*(prime2-1)


import math
while 1:
    e = randint(1,10)
    if math.gcd(e,totient)== 1:
        break

m = 141116561
print("value of m is:",m)
print("e = ",e )

#calculate c
c = pow(m,e,n)
print("c =",c)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


d = modinv(e, totient)

print("d = ",d)

#finding c^d
m = pow(c,d,n)
print("After decrypting value of m =",m)





