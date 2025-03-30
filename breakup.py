#Programme to comma-separate a sentence
#Lebogang Salagae
#29 March 2024

n= input("Enter a sentence:\n")

a= n.lower()
b=a.split

first=a[0:a.find(' ')]
second=a[a.find(' ')+1: a.find(' ',a.find(' ')+1)]

while len(second) >0:
    b_pos= second.find(' ')
    if b_pos >-1:
        word = second[b_pos+1]
    else:
        word = second
        second= ''


print("The word list: " + b + ', ' + c + ', ')