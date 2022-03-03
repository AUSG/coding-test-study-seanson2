class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # 큰 수(n)와 작은 수(m) 구하기
        nums.sort()
        n = nums[0]
        m = nums[-1]

        # 최대 공약수 구하기
        # m~1 loop
        i = m
        while True:
            # n과 m이 모두 나누어 떨어지는 수
            if n % i == 0 and m % i == 0:
                return i
            i -= 1
