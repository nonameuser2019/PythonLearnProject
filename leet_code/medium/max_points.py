class Solution:
    # https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
    # have not complited
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        result = 0
        if k == len(cardPoints):
            return sum(cardPoints)
        while k:
            if cardPoints[0] > cardPoints[-1]:
                result += cardPoints.pop(0)
            else:
                result += cardPoints.pop(-1)
            k -= 1
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxScore([1,2,3,4,5,6,1], 3) == 12
    assert sol.maxScore([11,49,100,20,86,29,72], 4) == 232
        