#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard
"""

import sys


def is_safe(board, row, col):
    # Loop through each row and column
    for r in range(n):
        for c in range(n):
            # Check if the current position is safe for placing a queen
            safe = all(
                col != c and
                col + (r - board[0]) != c and
                col - (r - board[0]) != c
                for board in placed_queens
            )
            if safe:
                # Place the queen at the current position
                placed_queens.append([r, c])

                # If the last row is reached, a solution is found
                if r == n - 1:
                    solutions.append(placed_queens[:])
                    placed_queens = []
                break
        else:
            # Backtrack to the previous row if no safe
            # position is found in the row
            while r >= 0:
                c = placed_queens[r][1] + 1
                del placed_queens[r]
                if c < n:
                    break
                r -= 1
            if r < 0:
                break


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Get the value of N from the command-line argument
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = []
    placed_queens = []

    # Print the solutions
    for solution in solutions:
        print(solution)
