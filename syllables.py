#Programme for extraction
#Lebogang Salagae
#5 April 2024

def is_vowel(letter):
        vowels= ('a', 'e', 'i', 'o', 'u', 'y')
        if letter.lower() in vowels:
                return True
        else:
                return False
def next_vowel(word, index):
        for 