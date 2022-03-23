# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        last_false, last_true = 0, 0
        while l <= r:
            mid = (r+l)//2
            # True면(고장이 났으면) 아래버전 탐색
            if isBadVersion(mid):
                r = mid-1
                last_true = mid
            # False면(정상이면) 위버전 탐색
            else:
                l = mid+1
                last_false = mid

        for i in range(last_false, last_true+1):
            if isBadVersion(i):
                return i
