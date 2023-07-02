# https://leetcode.com/problems/valid-sudoku/
from collections import defaultdict


def isValidSudoku(board):
    rowHmap = defaultdict(set)  # <i, set(values)>
    columnHmap = defaultdict(set)  # <j, set(values)>
    gridHmap = defaultdict(set)  # <(i%3, j%3), set(values)>

    for i in range(len(board)):
        for j in range(len(board[i])):
            value = board[i][j]
            if value == ".":
                continue

            if (value in rowHmap[i] or
                value in columnHmap[j] or
                    value in gridHmap[(i // 3, j // 3)]):
                return False
            else:
                rowHmap[i].add(value)
                columnHmap[j].add(value)
                gridHmap[(i // 3, j // 3)].add(value)

    return True


if __name__ == "__main__":
    # board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
    #   ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                          ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(isValidSudoku(board))
