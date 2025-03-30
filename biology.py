#Programme for type of animal
#7 March 2024
#Lebogang Salagae

print("Welcome to the Biology Expert\n-----------------------------")
print("Answer the following questions by selecting from among the options.")
animal= input("The skeleton is (internal/external)?\n")

if animal== 'external':
    print("Type of animal: Arthropod\n")
else:
    fert = input("The fertilisation of eggs occurs (within the body/outside the body)?\n")
    if fert == 'within the body':
        prod= input("Young are produced by (waterproof eggs/live birth)?\n")
        if prod == 'waterproof eggs':
            skin= input("The skin is covered by (scales/feathers)?\n")
            if skin == 'scales':
                print("Type of animal: Reptile")
            else:
                print("Type of animal: Bird")
        else:
            print("Type of animal: Mammal")
    else:
        lives= input("It lives (in water/near water)?\n")
        if lives== 'in water':
            print("Type of animal: Fish")
        else:
            print("Type of animal: Amphibian")
    
        
    

