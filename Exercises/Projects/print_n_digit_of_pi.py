import math

def nthDigOfPi(n):
    pi = math.pi;
    print(str(pi).replace(".", "")[n-1])

nthDigOfPi(2);