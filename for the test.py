#Testing

#def reverse(a,b):
    #while a!=0:
        #a=a[::-1]
        #break
    #b=int(a)+2
    #print(a,b)
    
#a=input("Enter a number:\n")
#b=0
#reverse(a,b)

#def square (y):
    #for i in range[1:10]:
        #return y*y
#def add(x,y):
    #return x+y

#def main():
    #y = int(input("Enter a number:\n"))
    #print(add(square(y),square(3)))
#if __name__ == "__main__":
    #main()

#def Sorty(x,y,z):
 #if x>y:
  #if y>z:
   #print(x,y,z)
  #else:
   #print(x,z,y)
 #else:
  #if y<z:
   #print(z,y,x)
  #else:
   #print(y,x,z)
#Sorty(1,2,3) 


def brigand(n):
  if n==0: print("No, said Antonio.")
  else:
    print("It was a dark and stormy night, and the head ofthe brigands said to Antonio:“Antonio, tell us a tale”. And so Antonio began:")
    n=n-1
    brigand(n)
brigand(3)

