class Solution:
    def romanToInt(self, s: str) -> int:
        map_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = map_nums.get(s[-1])
        for i in range(len(s) - 2, -1, -1):
            if map_nums.get(s[i]) >= map_nums.get(s[i + 1]):
                result += map_nums.get(s[i])
            else:
                result -= map_nums.get(s[i])
        return result



if __name__ == '__main__':
    sol = Solution()
    assert sol.romanToInt('IV') == 4
    assert sol.romanToInt('IX') == 9
    assert sol.romanToInt('XV') == 15
    assert sol.romanToInt('XL') == 40
    assert sol.romanToInt('XC') == 90
    assert sol.romanToInt('CD') == 400
    assert sol.romanToInt('CM') == 900
    assert sol.romanToInt("MMMCDXC") == 3490
