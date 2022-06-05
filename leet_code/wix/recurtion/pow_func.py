class Solution(object):
    def myPow(self, x, n):
        if n == 1:
            return x
        return self.myPow(x*x, n - 1)

s = Solution()

print(s.myPow(2, 4))
assert s.myPow(2, 3) == 8