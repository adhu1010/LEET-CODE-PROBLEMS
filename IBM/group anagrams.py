from collections import defaultdict

class Solution (object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))  # sort the word to get the anagram key
            anagram_map[key].append(word)

        return list(anagram_map.values())

#Time Complexity: O(n * k log k) where n is the number of strings and k is the maximum length of a string (due to sorting each string)
#Space Complexity: O(n * k) for storing the anagrams in the dictionary
# This code defines a class `Solution` with a method `groupAnagrams` that groups anagrams from a list of strings.
# The method uses a dictionary to map sorted strings (as keys) to lists of their corresponding anagrams.
# The sorted string serves as a unique identifier for each group of anagrams.   
# The method iterates through each string, sorts it, and appends the original string to the corresponding list in the dictionary.
# Finally, it returns a list of the grouped anagrams.