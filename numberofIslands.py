def checkIslands(row, col, grid, visited):
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    for direction in directions:
        newRow = row+direction[0]
        newCol = col+direction[1]
        if newRow in range(0,len(grid)) and newCol in range(0,len(grid[0])):
            if grid[newRow][newCol]=="1" and visited[newRow][newCol]==False:
                visited[newRow][newCol]=True
                checkIslands(newRow, newCol, grid, visited)

class Solution(object):
    def numIslands(self, grid):
        islands = 0
        rows = len(grid)
        if rows==0:
            return islands
        cols = len(grid[0])
        visited = [[False for j in range(cols)]for i in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1" and visited[row][col]==False:
                    print("island!")
                    visited[row][col]=True
                    islands+=1
                    checkIslands(row, col, grid, visited)

        return islands
    
    


        
