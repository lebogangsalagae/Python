#Question
Update the program called ‘test3a.py’, attached on the Assignments page on Amathuba, by implementing the following functions:

count_substrings(s)
“””

counts the number of substrings in a given string that start and end with the same character.

returns the total number of substrings as an integer.

“””

For example, from the Python shell, you can issue the following commands:

>>> from test3a import count_substrings

>>> count_substrings(‘ENVironMent’)

    15

>>> 

find_substrings(s)
“””

finds all substrings of a given string starting and ending with the same character.

returns a list of all substrings.

“””

For example, from the Python shell, you can issue the following commands:

>>> from test3a import find_substrings

>>> find_substrings('EVEntual')

['e', 'eve', 'v', 'e', 'n', 't', 'u', 'a', 'l']

>>> 

NOTE: The automatic marker will test each of your functions individually. To enable this, you MUST NOT remove the following lines from the skeleton and/or programs given to you for this test:

if __name__=='__main__':

     main()


 When running the whole program, the expected output is as shown below.

Sample IO (The input from the user is shown in bold font – do not program this):

Enter a string:

ENVironment

The number of substrings starting and ending with the same character is: 15.

Substrings starting and ending with the same character:

e, environme, n, nviron, nvironmen, v, i, r, o, n, nmen, m, e, n, t

 

Sample IO (The input from the user is shown in bold font – do not program this):

Enter a string:

Person

The number of substrings starting and ending with the same character is: 6.

Substrings starting and ending with the same character:

p, e, r, s, o, n

 

You may consult your paper notes and textbook, but no electronic resources. You may NOT use a search engine or consult any Web resources (including Amathuba) or files on your flash disk, hard drive, etc.

Submit the test3a.py source file contained within a .ZIP file to the Automatic Marker.