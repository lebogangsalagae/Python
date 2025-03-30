#Programme to search for an anagram
#Lebogang Salagae
#4 May 2024

def read_words(file_path):
    words = []
    start_reading = False
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if start_reading:  
                if line:  
                    words.append(line.lower())  
            elif line == "START": 
                start_reading = True

    return words 

# function to count the letters in a word
def count_letters(word):
    letter_counts = {}
    word = word.lower()  
    for letter in word:
        if letter.isalpha():  
            letter_counts[letter] = letter_counts.get(letter, 0) + 1  
    return letter_counts

# function to find anagrams from a list of words
def find_anagrams(target_word, word_list):
    anagrams = []
    target_letter_counts = count_letters(target_word)  
    for word in word_list:
        if word == target_word.lower():  
            continue
        if count_letters(word) == target_letter_counts:  
            anagrams.append(word)
    return sorted(anagrams)  

def main():
    print("***** Anagram Finder *****")
    user_input = input("Enter a word:\n").strip()  # ask the user for a word
    words_file_path = 'EnglishWords.txt' 

    words = None
    try:
        words = read_words(words_file_path)
    except IOError:
        print(f"Sorry, could not find file '{words_file_path}'.")
        return

    if not words: 
        print(f"Sorry, could not find any words in '{words_file_path}'.")
        return
    
    anagrams = find_anagrams(user_input, words)

    if anagrams: 
        print(anagrams)  
    else:  
        print(f"Sorry, anagrams of '{user_input}' could not be found.")


if __name__ == "__main__":
    main()