# display fibonacci series

n = abs(int(input("enter the number: ")))

# first two terms
n1, n2 = 0, 1
count = 0

print("Fibonacci series:")
while count < n:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
