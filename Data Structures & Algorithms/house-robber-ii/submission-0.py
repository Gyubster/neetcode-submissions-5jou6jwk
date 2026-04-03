class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums) ==2:
            return max(nums[0], nums[1])

        def rob_linear(numbers):
            dp = [0] * len(numbers)
            dp[0] = numbers[0]
            dp[1] = max(numbers[0], numbers[1])
            
            for i in range(2, len(numbers)):
                dp[i] = max(dp[i-1], dp[i-2]+numbers[i])

            return dp[-1]

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))