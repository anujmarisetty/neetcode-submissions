from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        vis=set()
        pc=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    q.append((i,j))
                    vis.add((i,j))
                elif grid[i][j]==2147483647:
                    pc+=1

        while q and pc>0:
            for i in range(len(q)):
                x,y=q.popleft()
                for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    xx=x+dx
                    yy=y+dy
                    if xx<0 or yy<0 or xx>=len(grid) or yy>=len(grid[0]):
                        continue
                    if grid[xx][yy]==-1:
                        continue
                    if (xx,yy) not in vis:
                        path_val=grid[x][y]+1
                        vis.add((xx,yy))
                        q.append((xx,yy))
                        pc-=1
                        if grid[xx][yy]>path_val:
                            grid[xx][yy]=path_val
                  
        return grid




        