import math

sqrt_five = math.sqrt(5)
Phi = (1 + sqrt_five)/2

def fib(num):
    num= num-1
    return int((Phi**num-(-Phi)**-num)/sqrt_five)

print(fib(5))