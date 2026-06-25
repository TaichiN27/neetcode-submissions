class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # rows cols countを変数で用意

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        # dfs関数スタート
        def dfs(r,c):
            # 範囲外であればreturn
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # 0であればreturn
            if grid[r][c] == "0":
                return

            # 1であれば0に変える
            if grid[r][c] == "1":
               grid[r][c] = "0" 



            #左右上下に対してdfsを進める
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        # loopで開始のrowとcolを回す

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c) 
        
        return count



        