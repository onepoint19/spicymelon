class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None or grid == []:
            return 0
        def flip (i, j):
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            if i-1>-1:
                flip(i-1,j)
            if i+1 < len(grid):
                flip(i+1,j)
            if j-1 > -1:
                flip(i, j-1)
            if j+1 < len(grid[0]):
                flip(i,j+1)
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # print(i,j)
                    num += 1
                    flip(i,j)
        return num
        
