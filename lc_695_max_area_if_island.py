class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxarea = 0
        if grid == None or grid == []:
            return maxarea
        area = 0
        def countIsland (i,j, area):
            if grid[i][j] == 0:
                return area
            area += 1
            grid[i][j] = 0
            if i-1 > -1:
                area = countIsland(i-1,j, area)
            if i+1 < len(grid):
                area = countIsland(i+1,j, area)
            if j-1 > -1:
                area = countIsland(i, j-1, area)
            if j+1 < len(grid[0]):
                area = countIsland(i, j+1, area)
            return area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # print(i,j)
                    area = 0
                    a =  countIsland(i,j, area)
                    maxarea = max(maxarea, a)
        return maxarea
