class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            match s[i]:
                case 'I':
                    result += 1
                case 'V':
                    if s[i - 1] == 'I' and i > 0:
                        result += 3
                    else:
                        result += 5
                case 'X':
                    if s[i - 1] == 'I' and i > 0:
                        result += 8
                    else:
                        result += 10
                case 'L':
                    if s[i - 1] == 'X' and i > 0:
                        result += 30
                    else:
                        result += 50
                case 'C':
                    if s[i - 1] == 'X' and i > 0:
                        result += 80
                    else:
                        result += 100 
                case 'D':
                    if s[i - 1] == 'C' and i > 0:
                        result += 300
                    else:
                        result += 500
                case 'M':
                    if s[i - 1] == 'C' and i > 0:
                        result += 800
                    else:
                        result += 1000
        return result


if __name__ == '__main__':
    sol = Solution()
    # assert sol.romanToInt('IV') == 4
    # assert sol.romanToInt('IX') == 9
    # assert sol.romanToInt('XV') == 15
    # assert sol.romanToInt('XL') == 40
    # assert sol.romanToInt('XC') == 90
    # assert sol.romanToInt('CD') == 400
    # assert sol.romanToInt('CM') == 900
    assert sol.romanToInt("MMMCDXC") == 3490
