class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s)-1
        for i in range(0, len(s)//2):
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        return s
