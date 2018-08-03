import fractions
n= int(input("Enter the value of n:"))

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount

p= phi(n)
print("Phi of n is:",p)
