#Program to match in wildcards
#Lebogang Salagae
#27 April 2024

# checking if pattern with wildcards matches the word
def match(pattern, word):
    # Base case
    if len(pattern)==0 and len(word)==0:
        return True
    
    if pattern == '*' and len(word)==0:
        return True
    
    if len(pattern)==0:
        return False
    
    if pattern[0] == '*':
        return match(pattern[1:], word) or (word and match(pattern, word[1:]))
    
   
    if pattern[0] == '?' or (word and pattern[0] == word[0]):
        return match(pattern[1:], word[1:])
    
    return False