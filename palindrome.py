#Programme for  palindrome
#Lebogang Salagae
#27 April 2024

#checkinng if string is a palindrome
def check_palindrome(p):
    p = ''.join(p.split()).lower()

    # Base cases
    if len(p) <= 1:
        return True  
    elif p[0] != p[-1]:
        return False 
    
    # Recursive case
    return check_palindrome(p[1:-1])  

# function to read input from the user and find out if it's a palindrome
def main():
    user_input = input("Enter a string:\n").strip()

    if check_palindrome(user_input):
        print("Palindrome!")
    else:
        print("Not a palindrome!")

if __name__ == "__main__":
    main()