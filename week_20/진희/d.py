class Solution:
    def twoSum(numbers, target):
        r = 1
        ans = []
        r_find = True
        for l in range(0, len(numbers)):
            sum_temp = numbers[l]+numbers[r]
            l_max = numbers[l]
            while sum_temp < target and r < len(numbers)-1 and r_find:
                if l_max < numbers[r]:
                    l_max = numbers[r]
                r += 1
                sum_temp = numbers[r]+l_max
            r_find = False
            sum = numbers[r]+numbers[l]
            if sum == target:
                ans.append(l+1)
                ans.append(r+1)
                return ans


a = Solution
# print(a.twoSum([3, 24, 50, 79, 88, 150, 345], 200))
# print(a.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8))
# print(a.twoSum([2, 3, 4], 6))
print(a.twoSum([12, 13, 23, 28, 43, 44, 59, 60, 61, 68, 70, 86, 88, 92, 124, 125, 136, 168, 173, 173, 180, 199, 212, 221, 227, 230, 277, 282, 306, 314, 316, 321, 325, 328, 336, 337, 363, 365, 368, 370, 370, 371, 375, 384, 387, 394, 400, 404, 414, 422, 422,
      427, 430, 435, 457, 493, 506, 527, 531, 538, 541, 546, 568, 583, 585, 587, 650, 652, 677, 691, 730, 737, 740, 751, 755, 764, 778, 783, 785, 789, 794, 803, 809, 815, 847, 858, 863, 863, 874, 887, 896, 916, 920, 926, 927, 930, 933, 957, 981, 997], 542))
