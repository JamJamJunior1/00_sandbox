
times_table = int(input("What set of times tables do you want?"))
answer = 0

max_value = int(input("Enter the maximum value for your times tables:"))
print("Here is the {} times table".format(times_table))
for x in range(1, max_value):
    answer = x * times_table
    print("{} times {} is {}".format(x, times_table, answer))
