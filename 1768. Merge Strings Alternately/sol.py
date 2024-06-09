class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        Merged_str = ''
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            Merged_str += word1[i] + word2[j]
            i += 1
            j += 1
        Merged_str += word1[i:] + word2[j:]
        return Merged_str
