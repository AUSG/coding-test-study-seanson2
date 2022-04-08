class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(' ')
        for i in range(0, len(ss)):
            temp = ss[i]
            ss[i] = temp[::-1]
        return " ".join(ss)
