#Lebogang Salagae
#Programme to convert
#20 March 2023

n=input("Enter the date and time (yyyy-mm-dd hh:mm) :\n")

a= int(n[11:13])
if a == 0:
    hour= 12
    time= 'am'
elif a < 12:
    hour = a
    time = 'am'
elif a == 12:
    hour = 12
    time= 'pm'
else:
    hour = a - 12
    time= 'pm'
    
if n[5] == '0' and n[6] == '1':
    d = 'January'
elif n[5] == '0' and n[6] == '2':
    d = 'February'
elif n[5] == '0' and n[6] == '3':
    d = 'March'
elif n[5] == '0' and n[6] == '4':
    d = 'April'
elif n[5] == '0' and n[6] == '5':
    d = 'May'
elif n[5] == '0' and n[6] == '6':
    d = 'June'
elif n[5] == '0' and n[6] == '7':
    d = 'July'
elif n[5] == '0' and n[6] == '8':
    d = 'August'
elif n[5] == '0' and n[6] == '9':
    d = 'September'
elif n[5] == '1' and n[6] == '0':
    d = 'October'
elif n[5] == '1' and n[6] == '1':
    d = 'November'
elif n[5] == '1' and n[6] == '2':
    d = 'December'

e= int(n[8:10].lstrip('0'))    
if e =='1' or e==21 or e==31:
    e_sf='st'
elif e ==2 or e==22:
    e_sf='nd'
elif e ==3 or e==23:
    e_sf='rd'
else:
    e_sf='th'

print(str(hour) + ':' + n[14:] + ' '+ time + ' on the ' + str(e) + e_sf + ' of '+ d + ' \'' + n[2:4])