#Programme to find palindromic primes
#Lebogang
#27 April 2024

import sys
sys.setrecursionlimit(30000)

#checkin if a given number is a palindrome
def is_palindromic(num_str):
    
    if len(num_str) <= 1:
        return True
    
    if num_str[0] != num_str[-1]:
        return False 
    
    return is_palindromic(num_str[1:-1])

# Recursive function
def is_a_prime(number, current_divisor=None):
    if current_divisor is None:
        current_divisor = number - 1
    
    if current_divisor == 1:
        return True  
    
    if number % current_divisor == 0:
        return False
    
    return is_a_prime(number, current_divisor - 1)

# making a function to find palindromic prime
def find_palindromic_prime_numbers(start, end):
    # Base case
    if start > end:
        return []
    
    
    num_str = str(start) 
    if is_palindromic(num_str) and is_a_prime(start):
        return [start] + find_palindromic_prime_numbers(start + 1, end)
    return find_palindromic_prime_numbers(start + 1, end)

def recursive_primes(result_list, index=0):
    if index >= len(result_list):
        return
    print(result_list[index])
    recursive_primes(result_list, index + 1)

# making a function to get palindromic primes
def main():
    start_point = int(input("Enter the starting point N:\n"))
    
    end_point = int(input("Enter the ending point M:\n"))
    
    print("The palindromic primes are:")
    result_list = find_palindromic_prime_numbers(start_point, end_point)
    
    recursive_primes(result_list)
    
if __name__ == "__main__":
    main()