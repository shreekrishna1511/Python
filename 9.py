a=int(input("Write first number"))
b=int(input("Write second number"))


def add(a,b):
    return a + b

result=add(a,b)
print("Addition:"+str(result))


def sub(a,b):
    return a - b
result=sub(a,b)
print("Subtraction:" + str(result))

def divison(a,b):
    return a / b

result=divison(a,b)
print("Division:"+str(result))


def multiply(a,b):
    return a * b

result=multiply(a,b)
print("Multiplication:"+str(result))