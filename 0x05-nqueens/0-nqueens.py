#!/usr/bin/python3
""" N Queens Algorithm with Backtracking (Recursion inside Loop) """
import sys


def is_safe(board, row, col):
    """Check if it is safe to place a queen at a given
    position on the hessboard.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_n_queens(n):
    """olves the N-Queens problem by finding
       all possible solutions for placing N queens on an NxN chessboard
    """
    def solve(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * n
    solve(0)
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)
