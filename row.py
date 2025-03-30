#Programme for a row
#14 March 2024
#Lebogang Salagae

num= int(input("Enter a number between -6 and 93:\n"))
if num>-6 and num<93:
    for i in range(num,num+7):
        if i>=0 and i<10:
            print((""),i, end=' ')
        else:
            print(i, end=' ')
else:
    print("Invalid input! The value of 'n' should be between -6 and 93.")