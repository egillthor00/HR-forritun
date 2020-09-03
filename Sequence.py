n = int(input("Enter the length of the sequence: ")) # Do not change this line
#alltaf +síðustu 3 tolurnar

sum=0
num1=0
num2=0
num3=1

for i in range(0, n):
    num1=num2
    num2=num3
    num3=sum
    sum=num1+num2+num3
    print(sum)