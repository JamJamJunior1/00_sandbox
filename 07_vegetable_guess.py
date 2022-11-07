
print("Pick either Carrot, Broccoli, Peas or Sweetcorn")
print("I will attempt to guess your choice")

answer = input("Is the vegetable green? Y/N").lower()

if answer == "n":
    answer = input("Is the vegetable orange? Y/N").lower()
    if answer == "y":
        print("It must be Carrot!")
    else:
        print("It must be a Sweetcorn!")

else:
    answer = input("Does the vegetable look like a tree? Y/N").lower()
    if answer == "y":
        print("It must be a Broccoli!")
    else:
        print("It must be Peas")
