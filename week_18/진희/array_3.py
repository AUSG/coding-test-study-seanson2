class Solution:
    def canBeIncreasing(self, nums) -> bool:
        # nums 중에 하나씩 빼기
        for i in range(0, len(nums)):
            temp_nums = nums[:]
            temp_nums.pop(i)
            temp_sort = sorted(temp_nums)
            # 그 결과 정렬이 잘 됐음 True
            if temp_nums == temp_sort and len(temp_nums) == len(set(temp_nums)):
                return True

        # 끝까지 빼봐도 정렬 안되면 False
        return False


s = Solution()
print(s.canBeIncreasing([1, 1, 1]))
