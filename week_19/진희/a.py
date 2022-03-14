class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ans = []
        l = len(nums)
        for i in range(l):
            count = 0
            for j in range(l):
                if i > j:
                    count += 1
            ans.append(count)
        return ans


a = Solution()
a.smallerNumbersThanCurrent([8, 1, 2, 2, 3])
