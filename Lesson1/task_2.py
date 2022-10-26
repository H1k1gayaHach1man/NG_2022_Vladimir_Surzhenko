
num1 = int(input("num1:"))
num2 = int(input("num2:"))
ask_operation = input("What operation do you want to perform: +, -, /, *?")
if ask_operation == '+':
    result = (num1+num2)
    print(result)
elif ask_operation == '-':
    result = (num1-num2)
    print(result)
elif ask_operation == '/':
    result = (num1/num2)
    print(result)
elif ask_operation == '*':
    result = (num1*num2)
    print(result)
else: print('unknown operation')    


