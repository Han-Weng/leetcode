class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        minn = 999999999999999
        for i in range(len(prices)):
            if prices[i] < minn:
                minn = prices[i]
            elif prices[i] - minn>maxx:
                maxx = prices[i] - minn
        
        return maxx