def parse_grid():
    with open("project_euler/_11_largest_product_in_a_grid/grid.txt", "r") as fd:
        lines = fd.readlines()
    grid = []
    for line in lines:
        row = list(map(int, line.strip().split()))
        grid.append(row)
    return grid


def product(arr):
    result = 1
    for item in arr:
        result *= item
    return result


def get_horizontal(grid, size, row, col):
    if col <= size - 3:
        return product(grid[row][col : col + 4])
    return -1


def get_vertical(grid, size, row, col):
    if row <= size - 4:
        return product(grid[row + offset][col] for offset in range(4))
    return -1


def get_diagonal_up(grid, size, row, col):
    if row >= 3 and col <= size - 4:
        return product(grid[row - offset][col + offset] for offset in range(4))
    return -1


def get_diagonal_down(grid, size, row, col):
    if row <= size - 4 and col <= size - 4:
        return product(grid[row + offset][col + offset] for offset in range(4))
    return -1


def main():
    grid = parse_grid()
    size = len(grid)
    products = set()
    for row in range(size):
        for col in range(size):
            products.add(get_horizontal(grid, size, row, col))
            products.add(get_vertical(grid, size, row, col))
            products.add(get_diagonal_up(grid, size, row, col))
            products.add(get_diagonal_down(grid, size, row, col))
    return max(products)
