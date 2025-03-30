# Programme to test numberutil
#Lebogang Salagae
#11 April 2024

# testnumberutil.py
"""
>>> import numberutil
>>> numberutil.aswords(700)
'seven hundred'
>>> numberutil.aswords(6)
'six'
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(120)
'one hundred and twenty'
>>> numberutil.aswords(23)
'twenty three'
>>> numberutil.aswords(127)
'one hundred and twenty seven'
>>> numberutil.aswords(30)
'thirty'
>>> numberutil.aswords(130)
'one hundred and thirty'

"""
import doctest
doctest.testmod(verbose=True)