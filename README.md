# Impledge_technologies..problem-solution

Here's a stepwise description of the code:

1.Import the time module to measure the execution time.
2.Define a function is_compounded(word, word_set) that checks if a given word can be compounded from smaller words in the provided word set. It recursively divides 
  the word into a prefix and a suffix and checks if the prefix exists in the word set, and either the suffix exists in the word set or can be compounded itself.
3.Define a function find_longest_compounded_words(input_file) that takes an input file as a parameter:
  a. Open and read the input file, splitting its contents into a list of words.
  b. Convert the list of words into a set to allow for faster lookups.
4.Measure the starting time using time.time().
5.Sort the list of words in descending order of length and alphabetically to resolve any ties. This ensures that the longest words come first, and if two words are 
  of equal length, they are sorted alphabetically.
6.Initialize variables longest_compound and second_longest_compound to store the longest and second-longest compounded words.
7.Loop through the sorted list of words:
  a. Check if each word can be compounded using the is_compounded function.
  b. If the word can be compounded, assign it to longest_compound if it's the first compounded word found. If the first compounded word is found, assign the word 
     to second_longest_compound if it's the second such word found. If both longest and second-longest words are found, break out of the loop.
8.Measure the ending time using time.time().
9.Calculate the time taken for the operation by subtracting the starting time from the ending time.
10.Return the longest compounded word, second-longest compounded word, and the time taken.
11.Define the file paths for two input files, input_file_01 and input_file_02.
12.Call the find_longest_compounded_words function for each input file, resulting in four variables: longest_compound_01, second_longest_compound_01, time_taken_01, 
   longest_compound_02, second_longest_compound_02, and time_taken_02.
13.Print the results for Input 01 and Input 02, including the longest compounded word, second-longest compounded word, and the time taken for each input.
