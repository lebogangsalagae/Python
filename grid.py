#Programme for a grid
#14 March 2024
#Lebogang Salagae

num= int(input("Enter a number between -6 and 2:\n"))
if num>-6 and num<2:
    for i in range(1, 7):
        for c in range(1, 8):
            if num>=0 and num<10:
                print("",num, end=" ")
            else:
                print(num, end=" ")  
            num=num+1                
        print()
            
else:
    print("Invalid input! The value of 'n' should be between -6 and 2.")