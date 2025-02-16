# Solution for `151. Reverse Words in a String`
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # remove leading, trailing whitespaces.
        words = s.split() # splits a string into a list
        words.reverse()
        return " ".join(words)