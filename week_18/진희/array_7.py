class Solution:
    def nextGreaterElement(self, findNums, nums):
        st, d = [], {}
        for n in nums:
            while st and st[-1] < n:
                d[st.pop()] = n
            st.append(n)

        return [d.get(x, -1) for x in findNums]


a = Solution()
a.nextGreaterElement([4, 1, 2], [1, 0, 3, 4, 2])
