class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            try:
                index = nums.index(target - nums[i], i + 1)
                if index:
                    return [i, index]
            except ValueError:
                continue



if __name__ == '__main__':
    data = [2, 7, 11, 15]
    two_sum = Solution()
    assert two_sum.two_sum(data, 9) == [0, 1]
    assert two_sum.two_sum([3, 3], 6) == [0, 1]