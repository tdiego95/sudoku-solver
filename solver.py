#											#
# SUDOKU SOLVER WITH BACKTRACKING ALGORITHM #
#											#

# Starting sudoku board 9x9
board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

box_len = 3


# Solve the sudoku
def solve():

	found_pos = find_empty()
	if not found_pos:
		return True
	else:
		row, col = found_pos

	for num in range(1, 10):
		if valid(num, found_pos):
			board[row][col] = num
			
			if solve():
				return True
			
			board[row][col] = 0


# Check if the specified number could be valid for the specified position
def valid(num, pos):

	y, x = pos

	# Check row
	for j in range(len(board[0])):
		if board[y][j] == num and j != x:
			return False

	# Check column
	for k in range(len(board)):
		if board[k][x] == num and k != y:
			return False

	# Check box
	box_x = x // box_len
	box_y = y // box_len

	for r in range(box_y*box_len, box_y*box_len + box_len):
		for c in range(box_x*box_len, box_x*box_len + box_len):
			if board[r][c] == num and (r, c) != pos:
				return False

	return True


# Print sudoku board on console
def print_board():

	for j in range(len(board)):
		if j % box_len == 0 and j != 0:
			print('- - - - - - - - - - - - - - - ')

		for k in range(len(board[0])):
			if k % box_len == 0 and k != 0:
				print('| ', end='')

			if k == len(board[0]) - 1:
				print(board[j][k], ' ')
			else:
				print(board[j][k], ' ', end='')


# Find the first empty spot to fill
def find_empty():

	for j in range(len(board)):
		for k in range(len(board[j])):
			if board[j][k] == 0:
				return(j, k) # row, col

	return None


print('Starting board:\n')
print_board()
print('\n')
solve()
print('Solved board:\n')
print_board()