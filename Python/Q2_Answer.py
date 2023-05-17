# Question 2: -
# Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
# he can remove just one character at the index in the string, and the remaining characters will occur the same
# number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .

# Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
# an explanation for the same.
# Example input 1 - s = “abc”. This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }
# Example output 1- YES
# Example input 2 - s “abcc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves
# character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }
# Example output 2 - NO

def validString(string):
    
    # Count the frequency of each character
    char_freq = {}
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Count the frequency of frequencies
    freq_freq = {}
    for freq in char_freq.values():
        freq_freq[freq] = freq_freq.get(freq, 0) + 1

    # If there is only one frequency, the string is valid
    if len(freq_freq) == 1:
        return "YES"
    
    # If there are more than two frequencies, the string is not valid
    if len(freq_freq) > 2:
        return "NO"
    
    # If there are exactly two occurence only once, the string is valid
    min_freq, max_freq = min(freq_freq), max(freq_freq)
    min_freq_count, max_freq_count = freq_freq[min_freq], freq_freq[max_freq]
    
    # If the minimum frequency occurs only one, the string is valid
    if min_freq_count == 1 and min_freq == 1:
        return "Yes"
    
    # If the maximum frequency occurs only once and its count is 1 greater than minimum frequecny
    # the string is valid

    if max_freq_count == 1 and max_freq - min_freq == 1:
        return "YES"
    
    return "NO"

            

string1 = 'abc'
print(validString(string1))

string2 = 'abcc'
print(validString(string2))
