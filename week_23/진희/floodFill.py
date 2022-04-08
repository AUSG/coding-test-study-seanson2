class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        color = image[sr][sc]

        def dfs(r, c):
            if r <= -1 or r >= n or c <= -1 or c >= m or image[r][c] is not color:
                return
            image[r][c] = newColor
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        if color is not newColor:
            dfs(sr, sc)
        return image
