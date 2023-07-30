def romanToInt(s):
    roman = {"I":1,"V":5,"X":10,"L":50,"C":10,"D":500,"M":1000}
    result = 0
    for i in range(len(s)):
        if (i+1 < len(s) and roman[s[i]] < roman[s[i+1]]):
            result -= roman[s[i]]
        else:
            result += roman[s[i]]
    return result
s = "LVIII"
romanToInt(s)