class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        # encoded 한바퀴 돌기
        for i in range(0, len(encoded)):
            # encoded[i] XOR arr[-1]
            arr.append(encoded[i] ^ arr[i])
        return arr


s = Solution()
print(s.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
