flip = input()

grid = [[1, 2], [3, 4]]

for i in flip:
    if i == 'H':
        grid[0][0] , grid[1][0] = grid[1][0] , grid[0][0]
        grid[0][1] , grid[1][1] = grid[1][1] , grid[0][1]
    else:
        grid[0][0] , grid[0][1] = grid[0][1] , grid[0][0]
        grid[1][0] , grid[1][1] = grid[1][1] , grid[1][0]

print(grid[0][0], grid[0][1], '\n', grid[1][0], grid[1][1])
