class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':500}
        