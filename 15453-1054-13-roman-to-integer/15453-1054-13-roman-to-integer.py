class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        c = len(s) - 1

        while c >= 0:
            if s[c] == "I":
                res += 1
            elif s[c] == "V":
                if s[c - 1] == "I" and c > 0:
                    res += 4
                    c -= 1
                else:
                    res += 5
                print(res)
            elif s[c] == "X":
                if s[c - 1] == "I" and c > 0:
                    res += 9
                    c -= 1
                else:
                    res += 10
            elif s[c] == "L":
                if s[c - 1] == "X"  and c > 0:
                    res += 40
                    c -= 1
                else:
                    res += 50
            elif s[c] == "C":
                if s[c - 1] == "X" and c > 0:
                    res += 90
                    c -= 1
                else:
                    res += 100
                print(res)
            elif s[c] == "D":
                if s[c - 1] == "C"  and c > 0:
                    res += 400
                    c -= 1
                else:
                    res += 500
            elif s[c] == "M":
                if s[c - 1] == "C" and c > 0:
                    res += 900
                    c -= 1
                else:
                    res += 1000
            c -= 1
        return res