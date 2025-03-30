#Programme for statement coverage
#Lebogang Salagae
#11 April 2024

# testtimeutil.py
"""
>>> import timeutil
>>> timeutil.validate('1:15 p.m.')
True
>>> timeutil.validate('02:09 a.m.')
False
>>> timeutil.validate('1:1 a.m.')
False
>>> timeutil.validate('')
False
>>> timeutil.validate('12:61 am')
False
>>> timeutil.validate('111:01 p.m.')
False

"""
import doctest
doctest.testmod(verbose=True)