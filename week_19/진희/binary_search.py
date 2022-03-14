
class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums)-1
        mid = (end+start)//2

        while start <= end:
            # mid 인덱스에 있는 값이 target 보다 작으면
            if nums[mid] < target:
                start = mid+1
                mid = (end+start)//2
            # 크면
            elif nums[mid] > target:
                end = mid-1
                mid = (end+start)//2
            # 같으면
            else:
                return mid
        return -1


a = Solution()
print(a.search([-1, 0, 3, 5, 9, 12], 12))
