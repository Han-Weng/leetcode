class Solution:
    def canJump(self, nums):
        max_reach, n = 0, len(nums)
        for i, x in enumerate(nums):
            if max_reach < i: return False
            if max_reach >= n - 1: return True
            print(i,x)
            max_reach = max(max_reach, i + x)
