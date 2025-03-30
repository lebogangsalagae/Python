#Program to reference
#Lebogang Salagae
#19 March 2024

n= input("Enter the reference:\n")

name = n[0:n.find(')')+1]
capname= name.title()



name2=n[n.find(')')+2:n.find(',', n.find(')'))+1]
capname2= name2.capitalize()

name3= n[n.find(',', n.find(')'))+2:]
print(capname, capname2,name3, end='')

return float(block[6:block.index('_')])
