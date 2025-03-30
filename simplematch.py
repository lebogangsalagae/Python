# Program to check wildcards
# Lebogang Salagae
# 27 April 2024

#checking if a pattern matches the word
def match(pattern, word):
    # Base case
    if len(pattern)==0 and len(word)==0:
        return True
    
    if len(pattern)==0 or len(word)==0:
        return False
    
    if pattern[0] == '?' or pattern[0] == word[0]:
        return match(pattern[1:], word[1:])
    
   
    return False