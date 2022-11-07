number = 4
num_guess = 3

while num_guess > 0:
    guess = int(input("Guess a number between 1 and 10"))

if number in range(0, 3):
   print("Number is higher")
else: number in range(5, 10)
      print("Number is lower")

    if guess != number:
       num_guess -= 1
       print("Incorrect, you have {} guesses left".format(num_guess))

    else:
        print("Correct, you got it {} guesses".format(num_guess))
