import math
a = float(input("Write a number"))
b = float(input("Write its power"))


def pow(a, b):
    return math.pow(a, b)


result=pow(a, b)

print(float(result))

def ceil(a):
    return math.ceil(a)



result=ceil(a)

print(float(result))

def floor(a):
    return math.floor(a)



result=floor(a)

print(float(result))




def fact(a):
    return math.factorial(a)
a=int(input("Write number to find factorial"))


result=fact(a)

print(result)