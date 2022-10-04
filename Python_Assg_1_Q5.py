#check string operations
print('WELCOME TO PYTHON CALCULATOR\n')
num1=int(input('enter the first number: '))
num2=int(input('enter the second number: '))

op=int(input('enter the operation to perform:\n 1. ADD \n 2. SUBTRACT \n 3. MULTIPLY \n 4. DIVIDE \n'))

if op == 1:
    print("sum is: ",num2+num1)
 
elif op == 2:
    print("difference is: ",num1-num2)
 
elif op == 3:
    print("product is: ",num1*num2)

elif op == 4:
    print("division is: ",num1/num2)
 
else:
    print("invalid operation")
