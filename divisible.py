#Programme for divisibility of 3
#Lebogang Salagae
#10 April 2024

num= input("Enter an integer or \'DONE\' to quit:\n")

string =''
while num != "DONE":
    string = string + num + ' ' #adds space between numbers for iteration
    num = input("Enter an integer or \'DONE\' to quit:\n")
    
sliced= string[0:-1]

first_number= ''
count= 0
sum=0

while ' ' in sliced :
    space= sliced.find(' ') #finding the first space
    first_number= sliced[:space] #locating the first number
    sliced= sliced[space+1:] #string without the first number
    space= sliced.find(' ')#locating the second space
    
    if ' ' in sliced:
        next_number= sliced[:space] #locating the next number
    else:
        next_number= sliced #locatingg the last number
        
    #converting string to integers
    first_number = int(first_number)
    next_number = int(next_number)
    
    if first_number%3==0 and next_number%3 == 0:
        count= count + 1
        sum= sum+ first_number + next_number
print(sum)
print(count)