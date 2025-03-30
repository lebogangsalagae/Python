#Programme for a column
#14 March 2024
#Lebogang Salagae

num= int(input("Enter a number between -6 and 2:\n"))
if num>-6 and num<93:
    for i in range(num,num+41,7):
        if i>=0 and i<10:
            print((""),i)
        else:
            print(i)
else:
    print("Invalid input! The value of 'n' should be between -6 and 2.")