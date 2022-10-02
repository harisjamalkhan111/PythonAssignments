#Factorail of a number

def factorial(n):
    if n<0:
        return 0
    else:
        fact =1
        for i in range(1,n+1):
            fact=fact*i
        return fact

fact=int(input('enter the number to take factorial : '))
print('factorial : ',factorial(fact))

