class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = {} # (r, c) -> LIP

        def dfs(r, c, prev):
            if (r < 0 or r == R or
                c < 0 or c == C or
                matrix[r][c] <= prev):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res
        
        for r in range(R):
            for c in range(C):
                dfs(r, c, -1)
        return max(dp.values())