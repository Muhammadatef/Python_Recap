class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        int_num = 0
        rec_roman_num = 0
        reserved_s= s[::-1]
        for i in reserved_s:
            roman_int = roman_dict.get(i)
            if roman_int >= rec_roman_num:
                int_num = int_num + roman_int
            else: 
                int_num = int_num - roman_int
            rec_roman_num = roman_int
        return int_num       


        
