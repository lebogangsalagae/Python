
num=int(input("Enter a number:\n"))

for i in range(1, num):
    if num%i ==0:
        print(i)
        print("The proper divisors of",num, "are:\n")
    
