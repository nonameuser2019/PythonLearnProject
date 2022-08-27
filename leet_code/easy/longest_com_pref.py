class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            part_word = ''
            try:
                for word in strs:
                    part_word += word[i]
                if len(set(part_word)) == 1:
                    res += strs[0][i]
                else:
                    break
            except IndexError:
                break
        return res



if __name__ == '__main__':
    test1 = Solution()
    assert test1.longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'