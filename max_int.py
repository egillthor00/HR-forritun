max_int = 0

while True: #loop that keeps running until input is a negativenumber
    num_int = int(input("Input a number: "))
    if num_int >= 0:
        if num_int > max_int:
            max_int = num_int #if the new input is higher than the old number then change it
    elif num_int < 0:
        break #if number is negative break loop

print("The maximum is", max_int)  # print current max_int
