def is_safe(board, row, col, n):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 'Q':
            return False
            
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False
            
    return True

def solve_n_queens_util(board, row, n):
    if row >= n:
        return [list(map(list, board))]  # Return a copy of the board when solution is found
    
    solutions = []
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'  # Place queen
            
            # Recur to place rest of the queens
            solutions.extend(solve_n_queens_util(board, row + 1, n))
            
            # Backtrack
            board[row][col] = '.'  # Remove queen
            
    return solutions

def solve_n_queens(n, first_queen_position):
    board = [['.' for _ in range(n)] for _ in range(n)]
    board[first_queen_position[0]][first_queen_position[1]] = 'Q'
    
    # Start solving from the next row after placing the first queen
    solutions = solve_n_queens_util(board, first_queen_position[0] + 1, n)
    
    # If no solutions are found, check if the initial position itself blocks all solutions
    if not solutions:
        board[first_queen_position[0]][first_queen_position[1]] = '.'  # Remove initial queen
        solutions = solve_n_queens_util(board, 0, n)  # Try from scratch
    
    return solutions

# Example usage
n = 4
first_queen_position = (0, 0)  # Placing first queen at (0,0)
solutions = solve_n_queens(n, first_queen_position)

if not solutions:
    print("No solutions found.")
else:
    for solution in solutions:
        for row in solution:
            print(" ".join(row))
        print("\n")
