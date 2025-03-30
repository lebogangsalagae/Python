#Programme for anagram sets
#Lebogang Salagae
#5 May 2024


def read_file(file_path):
    #read all words from the file starting after 'START'
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

def anagram_find(words, length):
    anagram_dict = {}
    for word in words:
        if len(word) == length:
            key = "".join(sorted(word))  
            if key in anagram_dict:
                if word not in anagram_dict[key]:
                    anagram_dict[key].append(word)
            else:
                anagram_dict[key] = [word]

    # collect only sets with more than one word
    anagram_sets = [sorted(set) for set in anagram_dict.values() if len(set) > 1]
    
    anagram_sets.sort(key=lambda x: x[0])
    return anagram_sets

def anagram_write(anagram_sets, output_file):
    with open(output_file, 'w') as file:
        for anagram_set in anagram_sets:
            file.write(str(anagram_set) + "\n")

def main():
    print("***** Anagram Set Search *****")
    
    # ask for word length
    word_length = int(input("Enter word length:\n"))
    print("Searching...")
    
    words_file_path = 'EnglishWords.txt'
    try:
        words = read_file(words_file_path)
    except FileNotFoundError:
        print(f"Error: Could not find '{words_file_path}'.")
        return
    
    anagram_sets = anagram_find(words, word_length)

    # get output file name
    output_file = input("Enter file name:\n")
    print("Writing results...")
    
    anagram_write(anagram_sets, output_file)
    
    print("Done")

if __name__ == "__main__":
    main()
