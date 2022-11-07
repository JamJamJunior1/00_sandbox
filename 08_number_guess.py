number = 4
num_guess = 3

while num_guess > 0:
    guess = int(input("Guess a number between 1 and 10"))

    if guess != number:
        num_guess -= 1
        print("Incorrect, you have {} guesses left".format(num_guess))
    else:
        print("Correct, you got it {} guesses".format(num_guess))
        break

if num_guess == 0:
    print("your a failure")
