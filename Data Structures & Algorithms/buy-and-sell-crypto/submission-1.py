class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        profit = sell - buy

        for i in range(len(prices)):
            buy = prices[i]

            for j in range(i+1, len(prices)):
                sell = prices[j]
            res = max(res, profit )

        return res
        