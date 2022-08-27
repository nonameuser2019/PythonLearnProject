class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        open_ph = '([{'
        open_list = []
        close_list = []
        for ph in s:
            if ph in open_ph:
                open_list.append(ph)
            else:
                close_list.append(ph)
        close_list.reverse()
        for i in range(len(open_list)):
            if open_list[i] == '(' and close_list[i] != ')':
                return False
            elif open_list[i] == '[' and close_list[i] != ']':
                return False
            elif open_list[i] == '{' and close_list[i] != '}':
                return False
        return True


if __name__ == '__main__':
    test1 = Solution()
    assert test1.isValid('()')
    assert test1.isValid('(){}'), test1.isValid('(){}')
