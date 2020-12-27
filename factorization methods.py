import math
import timeit

#Trial Division
def trial_fact(n):
    x = 2
    while x <= math.sqrt(n):
        if n % x == 0:
            print("n = " + str(x) + " * " + str(n/x))
            break
        x += 1



#Fermat's factorization algorithm
def Fermats_fact(n):
    x = math.ceil(math.sqrt(n))
    y = 1
    while x < n:
        if x**2 - y**2 > n:
            y = y+1
        elif x**2 - y**2 < n:
            x = x+1
            y = 1
        elif x**2 - y**2 == n:
            a = x-y
            b = x+y
            print("n = " + str(a) + " * " + str(b))
            break
                
