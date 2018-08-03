
import sympy

oo=float('inf')

num= sympy.symbols('num')
#store all the functions in the variable
a=0.1*num**2
b=1000*num
c=sympy.log(num)
d=sympy.sqrt(num)
e= 2**num
fact= sympy.factorial(num)
f=[a, b, c,d,e,fact]
def bubbl_sort(f):
    n = len(f)
    for n in range(n, 1, -1):
        for i in range(n - 1):
            if sympy.limit(f[i] / f[i+1], num, oo) == 0: #calculate the limit function to check which order is greater
                f[i + 1], f[i] = f[i], f[i + 1] #swapping of functions stored in variable
    return f

output = bubbl_sort(f)
print(output)
