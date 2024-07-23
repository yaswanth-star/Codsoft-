def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
number1=int(input("enter the first number: "))
number2=int(input("enter next number: "))
for symbol in operations_dict:
    print(symbol)
op_symbol=input("pick an operation: ")
number2=int(input("enter next number: "))
calculator_function=operations_dict[op_symbol]
output=calculator_function(number1,number2)
print(f"{number1} {op_symbol} {number2} = {output}")
