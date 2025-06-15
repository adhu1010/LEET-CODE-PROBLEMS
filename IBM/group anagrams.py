from collections import defaultdict

class Solution (object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))  # sort the word to get the anagram key
            anagram_map[key].append(word)

        return list(anagram_map.values())
