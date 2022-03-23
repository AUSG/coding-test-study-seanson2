class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        hint = True
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
                hint = True
            elif nums[mid] > target:
                r = mid - 1
                hint = False
            else:
                return mid
        if hint:
            return mid+1
        else:
            return mid
