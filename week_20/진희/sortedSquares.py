class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        ans = [None for i in nums]

        # len(nums)-1 부터 0까지 인덱싱
        for i in range(len(nums)-1, -1, -1):
            # 왼쪽이 큰 경우
            if abs(nums[l]) > abs(nums[r]):
                # ans에 넣기
                ans[i] = nums[l]**2
                l += 1
            # 오른쪽이 큰 경우
            else:
                ans[i] = nums[r]**2
                r -= 1
        return ans
