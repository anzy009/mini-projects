# calculator.py
def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b

print("Simple Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

result = {"+" : add(a,b), "-" : sub(a,b), "*" : mul(a,b), "/" : div(a,b)}.get(op, "Invalid")
print("Result:", result)
