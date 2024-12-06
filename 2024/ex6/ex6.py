import os

print("Day 6: Guard Gallivant")


def read_grid(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def find_guard_position(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '^':   # Haut
                return (x, y), 0
            elif cell == '>':  # Droite
                return (x, y), 1
            elif cell == 'v':  # Bas
                return (x, y), 2
            elif cell == '<':  # Gauche
                return (x, y), 3
    raise ValueError("Position du garde introuvable dans la grille.")


def turn_right(direction):
    return (direction + 1) % 4


def move(position, direction):
    x, y = position
    # Directions : Haut (0), Droite (1), Bas (2), Gauche (3)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dx, dy = directions[direction]
    return (x + dx, y + dy)


def is_obstacle(grid, position):
    x, y = position
    return not (0 <= y < len(grid) and 0 <= x < len(grid[y])) or grid[y][x] == '#'


def mark_visited_positions(grid, visited):
    marked_grid = [list(row) for row in grid]
    for x, y in visited:
        marked_grid[y][x] = 'X'
    return [''.join(row) for row in marked_grid]


def print_grid(grid):
    for row in grid:
        print(row)


def part_one(file_path):
    grid = read_grid(file_path)
    position, direction = find_guard_position(grid)

    visited = set()
    visited.add(position)

    while True:
        next_position = move(position, direction)

        if is_obstacle(grid, next_position):
            direction = turn_right(direction)
            if is_obstacle(grid, move(position, direction)):
                break
        else:
            position = next_position
            visited.add(position)

        if is_obstacle(grid, position):
            break

    # Affichage final de la grille avec toutes les positions visitées marquées
    # marked_grid = mark_visited_positions(grid, visited)
    # print("Grille finale avec positions visitées (X) :")
    # print_grid(marked_grid)

    return len(visited)


def part_two(file_path):
    return 0


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input6.txt')

partOne = part_one(file_path)
print(f"Part One: {partOne}")

partTwo = part_two(file_path)
print(f"Part Two: {partTwo}")
