#Programme for coordinates
#8 March 2024
#Lebogang Salagae

lat= eval(input("Enter first number:\n"))
min1= eval(input("Enter second number:\n"))
sec1= eval(input("Enter third number:\n"))
long= eval(input("Enter fourth number:\n"))
min2= eval(input("Enter fifth number:\n"))
sec2= eval(input("Enter sixth number:\n"))

if lat >= -90 and lat <=90 and min1 >= 0 and min1<= 59 and sec1 >= 0 and sec1<=59 and long >= -180 and long <= 180 and min2 >=0 and min2 <=59 and sec2 >=0 and sec2 <=59:
    print("WOW! Looks like geographic coordinates!")
else:
    print("Hmmm ... looks like 6 random numbers.")