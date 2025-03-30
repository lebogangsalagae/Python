#Programme to identify errors
#Lebogang Salagae
#10 April 2024

# testchecker.py
"""
>>> import triangle
>>> triangle.classify_by_angle(9, 7, 8)
'acute'
>>> triangle.classify_by_angle(7, 8, 9)
'acute'
>>> triangle.classify_by_angle(8, 7, 9)
'acute'
>>> triangle.classify_by_angle(5, 7, 10)
'obtuse'
>>> triangle.classify_by_angle(10, 5, 7)
'obtuse'
>>> triangle.classify_by_angle(7, 5, 10)
'obtuse'
>>> triangle.classify_by_angle(4, 3, 5)
'right'
>>> triangle.classify_by_angle(5, 3, 4)
'right'
>>> triangle.classify_by_angle(3, 4, 5)
'right'

"""
import doctest
doctest.testmod(verbose=True)