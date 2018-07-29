'''
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the  20 X 20 grid?
'''
#!/bin/python3

grid = []

# Read the grid and add 3 trailing zeroes to every row
for grid_i in range(23):

    if grid_i < 20:
        grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
        grid_t.append(0)
        grid_t.append(0)
        grid_t.append(0)
        grid.append(grid_t)
    else:
		# Add 3 trailing zero columns to the grid
        grid_t = [0]*23
        grid.append(grid_t)

product = []
for i in range(23):
    prod = []
    
	for j in range(23):
        # pivot at [i,j] and calculate all possible products at [i,j] and store the maximum product
		if i < 20 and j < 20:
            prd = max(grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j],      # Horizontal to left
                    grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3],		# Vertical to bottom
                    grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3],	# Diagonal [i,j] to [i+3,j+3]
                    grid[i][j+3]* grid[i+1][j+2] * grid[i+2][j+1] * grid[i+3][j])	# Diagonal [i,j+3] to [i+3,j]
		# Store all the maximum products in a column, j to a list
		prod.append(prd)
	# Store all the maximum of each column products in each row, i 
	product.append(max(prod))
# Print the greatest product of four adjacent numbers
print(max(product))