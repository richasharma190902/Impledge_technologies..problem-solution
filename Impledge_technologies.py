
import time

# Function to check if a word can be compounded from smaller words in the list
def is_compounded(word, word_set):
    if not word:
        return False
    for i in range(1, len(word)):
        prefix, suffix = word[:i], word[i:]
        if prefix in word_set and (suffix in word_set or is_compounded(suffix, word_set)):
            return True
    return False

def find_longest_compounded_words(input_file):
    with open(input_file, 'r') as file:
        words = file.read().split()

    word_set = set(words)  # Convert the list of words to a set for faster lookup

    start_time = time.time()

    # Sort the words by length in descending order
    words.sort(key=lambda x: (-len(x), x))

    longest_compound = ''
    second_longest_compound = ''

    for word in words:
        if is_compounded(word, word_set):
            if not longest_compound:
                longest_compound = word
            elif not second_longest_compound:
                second_longest_compound = word
            else:
                break

    end_time = time.time()
    time_taken = end_time - start_time

    return longest_compound, second_longest_compound, time_taken

# Input file paths
input_file_01 = 'C:\\Users\RICHA\Downloads\Input_01.txt'
input_file_02 = 'C:\\Users\RICHA\Downloads\Input_02.txt'

# Find the longest and second longest compounded words and measure time for Input 01
longest_compound_01, second_longest_compound_01, time_taken_01 = find_longest_compounded_words(input_file_01)

# Find the longest and second longest compounded words and measure time for Input 02
longest_compound_02, second_longest_compound_02, time_taken_02 = find_longest_compounded_words(input_file_02)

# Display the results
print("Input 01 Results:")
print("Longest Compound Word:", longest_compound_01)
print("Second Longest Compound Word:", second_longest_compound_01)
print("Time taken:", time_taken_01, "seconds")

print("\nInput 02 Results:")
print("Longest Compound Word:", longest_compound_02)
print("Second Longest Compound Word:", second_longest_compound_02)
print("Time taken:", time_taken_02, "seconds")
