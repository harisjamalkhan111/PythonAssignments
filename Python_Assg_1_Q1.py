#swap 2 numbers
#There are multiple solutions for it like using a third variable or not using a separate variable 
#using a third variable 

c=0
a=int(input('enter the 1st number : '))
b=int(input('enter the 2nd number : '))
c=a
a=b
b=c
print('numbers after swapping 1st , 2nd: ',a,',',b)

#swap 2 numbers without using a 3rd variable

a=int(input('enter the 1st number : '))
b=int(input('enter the 2nd number : '))
a,b=b,a
print('numbers after swapping 1st , 2nd: ',a,',',b)



