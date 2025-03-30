#Programme to extract
#Lebogang Salagae

def get_block(data): 
    return data[data.index('BEGIN'): data.index('END') + 3] 
def location(block): 
    location_info = block[block.index("Location: ") + 10:block.index("END") - 1] 
    return location_info[::-1].title() 

def temperature(block): 
    float(block[6:block.index(',')]) 
    
def pressure(block): 
    return 
float(block[block.index("Pressure: ") + 10:block.index("hPa")]) 
def x_coordinate(block):  
    return block[block.index(': ') + 2:block.index(',')] 
def y_coordinate(block): 
    return block[block.index(',') + 2:block.index(')')] 
def main(): data = input("Please input the raw data:\n") 
block = get_block(data) 

print('Site details:') 
print('Location:', location(block)) 
print('Coordinates:', x_coordinate(block) + ', ' + y_coordinate(block)) 
print('Temperature: {:.2f} C'.format(temperature(block))) 
print('Pressure: {:.2f} hPa'.format(pressure(block))) 

if __name__ == '__main__': 
    main()