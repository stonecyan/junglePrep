def orangesRotting(grid):
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        minutes = 0
        ylength = len(grid)
        xlength = len(grid[0])
        fresh = 0
        rotten = []
        for i in range(ylength):
            for j in range(xlength):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    rotten.append([i,j])
        
        if fresh==0:
            return minutes
        if len(rotten)==0:
            return -1
        
        rottenCount=0
        while True:
            newRotten = []
            for coordinate in rotten:
                xcoordinate = coordinate[1]
                ycoordinate = coordinate[0]
                for d in direction:
                    newX = xcoordinate+d[1]
                    newY = ycoordinate+d[0]
                    if newX in range(0,xlength) and newY in range(0,ylength):
                        if grid[newY][newX]==1:
                            grid[newY][newX]=2
                            newRotten.append([newY,newX])
                            rottenCount+=1
            rotten = newRotten
            if len(newRotten)==0:
                if rottenCount==fresh:
                    break
                return -1
            minutes+=1
        return minutes
