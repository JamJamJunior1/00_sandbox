#welcome these annoying customers in
print("---Welcome to Split My Bill---")

#ask them for their total bill_total for everything to work from beginning
valid = False
while not valid:
    try:
        bill_total = float(input("What is the total bill?"))
        valid = True
    except ValueError:
        print("Error please enter a whole number")

#Ask how many people are sharing
valid = False
while not valid:
    try:
        people = int(input("How many people are sharing?"))
        valid = True
    except ValueError:
        print("Error please enter a whole number")

#Ask what percentage of a tip they want to leave
valid = False
while not valid:
    try:
        tip_percentage = int(input("What percentage tip would you like to leave"))
        valid = True
    except ValueError:
        print("Error please enter a whole number")

#math
percentage_decimal = tip_percentage/100
tip_total = bill_total*percentage_decimal
bill_total = bill_total + tip_total

cost_per_person = bill_total/people
#bill and cost answers
print("Total bill including tip is ${}".format(bill_total))
print("Total cost per person is ${}".format(cost_per_person))
