def fibo():
    length_sequence = int(input("Input the length of the sequence: "))
    sum=0
    num1=0
    num2=1

    print("Fibonacci Sequence:")
    print("-------------------")
    print(0)
    for i in range(0, length_sequence - 1):
# fibonacci is the last two sums = to the new sum
        num1=num2
        num2=sum
        sum=num1+num2
        print(sum)

def abuntant():
    max_number = int(input("Input the max number to check: "))
    sum1 = 0

    print("Abundant numbers:")
    print("-----------------")
    for i in range(1, max_number + 1):
        for p in range(1, i):
            if i % p == 0: # if the number that we are checking(i) is divisible p
                sum1 = sum1 + p
        if sum1 > i:
            print(i)
        sum1 = 0 #set the sum1 variable back to 0 for the next number


choice = input("Input f|a|b (fibonacci, abundant or both): ")

if choice == "f":
    fibo()
elif choice == "a":
    abuntant()
elif choice == "b":
    fibo()

    abuntant()