class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                nums[i] = ''
        nums.sort()
        return nums


if __name__ == "__main__":
    solution_1 = Solution()
    assert solution_1.removeDuplicates([1, 1, 2]) == 2, [1, 2, '']
