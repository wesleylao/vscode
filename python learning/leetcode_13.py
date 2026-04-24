class Solution:
    def __init__(self, *arr: list[str]):
        self.arr = arr
        self.romanToInt_result = self.__romanToInt() 
    def __romanToInt(self):
        result = []
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
        for group in self.arr:
            group_res = []
            for s in group:
                total = 0
                tmp = 0
                for ch in reversed(s):
                    c = roman_map[ch]
                    if c >= tmp:
                        total += c
                    else:
                        total -= c
                    tmp = c
                group_res.append(total)
            result.append(group_res)
        return result
    
A = ["III"]
B = ['XI'] 
C = ['CIII'] 
a = Solution(A, B, C)
print(a.romanToInt_result)