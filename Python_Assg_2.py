#modified the code to include cube roots between 0 and 1, and less than 0 as well

#cube = 27
#cube = 0.5
cube =-0.5

num_guesses = 0
epsilon = 0.0001

low = min(cube, -1)
high = max(cube, 1)

guess = (high + low) / 2.0

while abs(guess ** 3 - cube) >= epsilon:
    if guess ** 3 < cube:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2.0
    num_guesses += 1

print('num_guesses = {}'.format(num_guesses))
print('The cube root of',cube,'is',guess)