from tkinter import N


class Solution:
    def moveZeroes(self, nums) -> None:
        i = 0
        for n in nums:
            if n == 0 and i+1 < len(nums)-1:
                nums.remove(0)
                nums.append(0)
            else:
                i += 1


a = Solution()
a.moveZeroes([0, 1, 0, 3, 12])
