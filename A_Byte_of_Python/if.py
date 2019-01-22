number = 23
guess = int(input('Enter an integer: '))

if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    print('No it is a little higher than that')
else:
    print('No it is a little lower than that')

print('Done')
