#Simple greeting
print("---Welcome to Split My Pizza---")

#Figures out the total number of slices on the pizza to figure out the math ig
valid = False
while not valid:
    try:
        pizza_slice_total = float(input("What is the total number of slices of the pizza?"))
        valid = True
    except ValueError:
        print("Error please enter a whole number")

#Figures out how many people are sharing this pizza
valid = False
while not valid:
    try:
        people = int(input("How many people are sharing?"))
        valid = True
    except ValueError:
        print("Error please enter a whole number")
#math
slices_per_person = pizza_slice_total//people
remaining_slice_total = pizza_slice_total%people
#end totals printed
print("Total slices per person is {}".format(slices_per_person))
print("Total remaining slices is {}".format(remaining_slice_total))
