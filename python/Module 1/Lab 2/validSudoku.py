def isValidSudoku(board):
    # Helper function to check if a list has duplicates
    def hasDuplicates(lst):
        seen = set()
        for num in lst:
            if num != ".":
                if num in seen:
                    return True
                seen.add(num)
        return False

    # Check rows
    for row in board:
        if hasDuplicates(row):
            return "NO"

    # Check columns
    for col in zip(*board):
        if hasDuplicates(col):
            return "NO"

    # Check sub-boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if hasDuplicates(sub_box):
                return "NO"

    return "YES"


# Exercise-1
input_board_1 = [
    [5, 3, ".", ".", 7, ".", ".", ".", "."],
    [6, ".", ".", 1, 9, 5, ".", ".", "."],
    [".", 9, 8, ".", ".", ".", ".", 6, "."],
    [8, ".", ".", ".", 6, ".", ".", ".", 3],
    [4, ".", ".", 8, ".", 3, ".", ".", 1],
    [7, ".", ".", ".", 2, ".", ".", ".", 6],
    [".", 6, ".", ".", ".", ".", 2, 8, "."],
    [".", ".", ".", 4, 1, 9, ".", ".", 5],
    [".", ".", ".", ".", 8, ".", ".", 7, 9],
]
output_1 = isValidSudoku(input_board_1)
print(f"Exercise-1 Output: {output_1}")

# Exercise-2
input_board_2 = [
    [5, 3, ".", ".", 7, ".", ".", ".", "."],
    [5, ".", ".", 1, 9, 5, ".", ".", "."],
    [".", 9, 8, ".", ".", ".", ".", 6, "."],
    [8, ".", ".", ".", 6, ".", ".", ".", 3],
    [4, ".", ".", 8, ".", 3, ".", ".", 1],
    [7, ".", ".", ".", 2, ".", ".", ".", 6],
    [".", 6, ".", ".", ".", ".", 2, 8, "."],
    [".", ".", ".", 4, 1, 9, ".", ".", 5],
    [".", ".", ".", ".", 8, ".", ".", 7, 9],
]
output_2 = isValidSudoku(input_board_2)
print(f"Exercise-2 Output: {output_2}")
