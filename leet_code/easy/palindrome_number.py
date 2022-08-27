class Solution:

    def num_to_list(self, num):
        num_list = []
        while num > 0:
            num_list.append(num % 10)
            num = num // 10
        return num_list

    def isPalindrome(self, num: int) -> bool:
        if num < 0:
            return False
        num_list = self.num_to_list(num)
        for i in range(len(num_list) // 2):
           if num_list[i] != num_list[(i+1) * -1]:
               return False
        return True


if __name__ == '__main__':
    test1 = Solution()
    assert test1.isPalindrome(121)