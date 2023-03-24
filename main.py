lower_limit = int(input("Enter lower range limit: "))
upper_limit = int(input("Enter upper range limit: "))
divisor = int(input("Enter the number to be divided by: "))

for i in range(lower_limit, upper_limit + 1):
    if i % divisor == 0:
        print(i)