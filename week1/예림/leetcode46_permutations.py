# 46. permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프노드일때
            if len(elements) == 0:
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                # print("perv", prev_elements)
                # print("next재귀돌러가즈아", next_elements)
                dfs(next_elements)
                prev_elements.pop()
                # print("**백트래킹", prev_elements)

        dfs(nums)
        # print("=========")
        return results