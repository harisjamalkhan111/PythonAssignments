#check string operations

str1=input('enter the first string: ')
str2=input('enter the second string: ')

#check length of string

print('length of the first string is:',len(str1))
print('length of the second string is:',len(str2))

#cancatenate strings

cat_str=str1+' '+str2
print('result of cancatenate is: ',cat_str)

#substrings or slicing

start=int(input('location to start slicing: '))
end=int(input('location to end slicing: '))

print('string after slicing: ',cat_str[start:end+1])
