from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    rotten = frozenset(
        (x, y)
        for (y, row) in enumerate(grid)
        for (x, cell) in enumerate(row)
        if cell == 2
    )
    minutes = -bool(rotten)
    while rotten:
        rotten = frozenset(
            (x, y)
            for x, y in rotten
            for x, y in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] == 1
        )
        for x, y in rotten:
            grid[y][x] = 2
        minutes += 1
    return -1 if any(cell == 1 for row in grid for cell in row) else minutes
