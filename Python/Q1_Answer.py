# Question 1: -
# Write a program that takes a string as input, and counts the frequency of each word in the string, there might
# be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
# highest-frequency word.

# Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
# an explanation for the same.
# Example input - string = “write write write all the number from from from 1 to 100”
# Example output - 5
# Explanation - From the given string we can note that the most frequent words are “write” and “from” and
# the maximum value of both the values is “write” and its corresponding length is 5

# Answer

def highestFrequency(string):

    # split string into words
    words = string.split()

    # Create a dictionary
    word_freq = {}

    # Count frequency for each word
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Find the maximum frequency
    max_freq = max(word_freq.values())

    # Find the length of the highest-frequency word
    high_freq_word_lenght = max(len(word) for word, freq in word_freq.items() if freq == max_freq)

    return high_freq_word_lenght

# Test case 1
string1 = "write write write all the number from from from 1 to 100"
print(highestFrequency(string1))

# Test case 2
string2 = "hello world hello world hello world"
print(highestFrequency(string2))

# Test case 3
string3 = "the quick brown fox jumps over the lazy dog"
print(highestFrequency(string3))
