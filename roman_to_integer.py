def check(a):
    if(a == 'I'):
        return 1
    elif(a == 'V'):
        return 5
    elif(a == 'X'):
        return 10
    elif(a == 'L'):
        return 50
    elif(a == 'C'):
        return 100
    elif(a == 'D'):
        return 500
    elif(a == 'M'):
        return 1000
    else:
        return -1
        
        
class Solution:
    def romanToInt(self, s: str) -> int:
        s = str(s)
        i = 0
        res = 0
        if(len(s) == 1):
            return check(s[0])
        else:
            while i < len(s)-1:
                a = check(s[i])
                b = check(s[i+1])
                if(a < b):
                    res = res + (b - a)
                    i = i + 2
                else:
                    res = res + a
                    i = i + 1
                if(i == len(s) - 1):
                    res = res + check(s[-1])
        return res


a = input()
sol = Solution()
print(sol.romanToInt(a))