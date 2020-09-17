password = " "
valid_counter = 0
invalid_counter = 0

while True:
    upper = False
    lower = False
    digit = False
    password = input("Enter a new password: ")
    if password == 'q':
        break
    if len(password) >= 6 and len(password) <= 20:
        for i in password:
            if i.isupper():
                upper = True
        for i in password:
            if i.islower():
                lower = True
        for i in password:
            if i.isdigit():
                digit = True

        if lower == False:
            print('At least one lower case letter needed')
        if upper == False:
            print('At least one upper case letter needed')
        if digit == False:
            print('At least one number needed')
        if upper == False or lower == False or digit == False:
            invalid_counter += 1
        if upper == True and lower == True and digit == True:
            print(f'Valid password of length {len(password)}')
            valid_counter += 1
    else:
        print("Invalid length")
        invalid_counter += 1

print(f'You tried {invalid_counter + valid_counter} passwords, {valid_counter} valid, {invalid_counter} invalid')