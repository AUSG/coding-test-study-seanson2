# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = nums[:1]
        for i in nums[1:]:
            runningSum.append(i+runningSum[-1])
        return runningSum

# 새로운 변수 안 만들고 풀기
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         for i in range(1, len(nums)):
#             nums[i] = nums[i]+nums[i-1]
#         return nums
