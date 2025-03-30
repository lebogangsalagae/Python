#Programme testing validity of time
#29 February 2024
#Lebigang Salagae

h= int(input("Enter the hours:\n"))
m= int(input("Enter the minutes:\n"))
s= int(input("Enter the seconds:\n"))

if(h>= 0 and h<=23):
   if(m>=0 and m<=59):
      if(s>=0 and s<=59):
         print("Your time is valid.")
      else:
         print("Your time is invalid.")
   else:
      print("Your time is invalid.")
else:print("Your time is invalid.")