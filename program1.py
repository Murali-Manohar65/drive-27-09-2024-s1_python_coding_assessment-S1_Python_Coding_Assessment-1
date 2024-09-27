class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
                   def numIslands(grid):
    if not grid:
        return 0
    
    # Get the number of rows and columns
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    def dfs(r, c):
        # Check for boundary conditions and whether the cell is land and not visited
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W' or visited[r][c]:
            return
        
        # Mark the current cell as visited
        visited[r][c] = True
        
        # Explore all adjacent cells (up, down, left, right)
        dfs(r-1, c)  # up
        dfs(r+1, c)  # down
        dfs(r, c-1)  # left
        dfs(r, c+1)  # right
    
    # Count the number of islands
    island_count = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'L' and not visited[r][c]:
                # Start DFS and mark all the land cells of the current island
                dfs(r, c)
                island_count += 1
    
    return island_count

# Test cases
dispatch_1 = [["L","L","L","L","W"], 
              ["L","L","W","L","W"], 
              ["L","L","W","W","W"], 
              ["W","W","W","W","W"]]

dispatch_2 = [["L","L","W","W","W"], 
              ["L","L","W","W","W"], 
              ["W","W","L","W","W"], 
              ["W","W","W","L","L"]]

print("Output for Dispatch 1:", numIslands(dispatch_1))  # Output should be 1
print("Output for Dispatch 2:", numIslands(dispatch_2))  # Output should be 3
 
        return 0
