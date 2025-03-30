# Porgramme to count
#Lebogang Salagae
#24 April 2024

def count_substrings(s):
    # Your code here
    a= input_st
    if a[1] == a[-1]:
        count= count+ 1


def find_substrings(s):
    # Your code here
    input_st.strip()
    n= ''
    while n !='':
        a.append(n)
        a.append(n+1)
        count= n


def main():
    input_str = input("Enter a string:\n").strip()
    
    # Call count_substrings and print the number of substrings starting and 
    # ending with the same character.
    count = count_substrings(input_str.lower())
    print(f"The number of substrings starting and ending with the same character is: {count}.")
    
    # Call find_substrings() and print substrings
    substrings = find_substrings(input_str.lower())
    print("Substrings starting and ending with the same character:")
    if len(input_str) == 0 or count == 0:
        print("[]")
    else:
        print(", ".join(substrings))


if __name__ == "__main__":
    main()