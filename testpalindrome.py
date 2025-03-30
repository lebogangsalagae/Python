#Prograame to check statement coverage
#Lebogang Salagae
#11 April 2024

# testpalindrome.py
"""
>>> import palindrome
>>> palindrome.is_palindrome("989")
True
>>> palindrome.is_palindrome("")
True
>>> palindrome.is_palindrome("asantaatnasa")
True
>>> palindrome.is_palindrome("34563")
False
>>> palindrome.is_palindrome("a")
True

"""
import doctest
doctest.testmod(verbose=True)
