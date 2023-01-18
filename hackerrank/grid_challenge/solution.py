def sort_rows(grid):
    for i in range(len(grid)):
        row_list = list(grid[i])
        row_list.sort()
        grid[i] = row_list


def grid_challenge(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    sort_rows(grid)
    for i in range(num_cols):
        for j in range(num_rows - 1):
            if grid[j][i] > grid[j + 1][i]:
                return "NO"
    return "YES"
