#Lebogang Salagae
#8 May 2024
#Programme to count substrings

def generate_substrings(string):
    """
    Generate all substrings of lengths 6 to 12 from the given string.

    Args:
    string (str): The input string.

    Returns:
    list: A list containing all generated substrings.
    """
    # Your code here
    count=0
    list=[]
    i=[string[:6:], string[1:7:], string[2:8:], string[3:9:],string[4:10:]]
    while i in string:
        count+=1
        string=string[string.find(i)+1:]
        return str(count)
    list.i[s
    
def count_substrings(string):
    """
    Count the number of substrings of lengths 6 to 12 in the given string.

    Args:
    string (str): The input string.

    Returns:
    int: The total count of substrings.
    """
    # Your code here
    int=0
    i=string[::5]
    while i in string
    count+=1
    string=string[string.find(i)+1:]
    return str(count)    

def main():
    """
    Main function to generate and count substrings of lengths 6 to 12 from a given string.
    """
    input_string = input("Enter a string:\n")
    input_string = input_string.lower()
    
    substring_count = count_substrings(input_string)
    print("Total substrings of length 6 to 12:", substring_count)    

    substrings = generate_substrings(input_string) 
    if len(substrings) == 0:
        print("Substrings of length 6 to 12:")
        print("[]")
    else:
        print("Substrings of length 6 to 12:")
        print(", ".join(substrings))


if __name__ == "__main__":
    main()
