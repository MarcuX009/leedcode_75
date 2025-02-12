# Solution for `1768. Merge Strings lternately`
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shortest = min(len(word1), len(word2))
        output = []
        for i in range(0, shortest):
            output.append(word1[i])
            output.append(word2[i])
        if shortest < len(word2):
            output.append(word2[shortest:])
        else:
            output.append(word1[shortest:])
        result = "".join(output)
        return result