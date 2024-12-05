import os

print("Day 4: Ceres Search")


def read_grid(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def part_one(file_path):
    def count_word_in_all_directions(grid, word):
        rows, cols = len(grid), len(grid[0])
        word_length = len(word)
        total_count = 0

        # Directions (dx, dy)
        directions = [
            (0, 1),   # Droite
            (1, 0),   # Bas
            (1, 1),   # Diagonale bas-droite
            (1, -1),  # Diagonale bas-gauche
            (0, -1),  # Gauche
            (-1, 0),  # Haut
            (-1, -1),  # Diagonale haut-gauche
            (-1, 1)   # Diagonale haut-droite
        ]

        def is_match(row, col, dr, dc):
            for i in range(word_length):
                nr, nc = row + i * dr, col + i * dc
                if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                    return False
            return True

        # Parcours de la grille
        for row in range(rows):
            for col in range(cols):
                for dr, dc in directions:
                    if is_match(row, col, dr, dc):
                        total_count += 1

        return total_count

    # Lecture de la grille et recherche
    grid = read_grid(file_path)
    word = "XMAS"
    return count_word_in_all_directions(grid, word)


def part_two(file_path):
    def count_x_mas(grid):
        rows, cols = len(grid), len(grid[0])
        total_count = 0

        def is_x_mas(row, col):
            if row - 1 < 0 or row + 1 >= rows or col - 1 < 0 or col + 1 >= cols:
                return False

            diag1 = grid[row - 1][col - 1] + \
                grid[row][col] + grid[row + 1][col + 1]
            diag2 = grid[row - 1][col + 1] + \
                grid[row][col] + grid[row + 1][col - 1]
            return diag1 in {"MAS", "SAM"} and diag2 in {"MAS", "SAM"}

        # Parcours de la grille
        for row in range(rows):
            for col in range(cols):
                if is_x_mas(row, col):
                    total_count += 1

        return total_count

    # Lecture de la grille et recherche
    grid = read_grid(file_path)
    return count_x_mas(grid)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'input4.txt')

    part_one_result = part_one(file_path)
    print(f"Part One: {part_one_result}")

    part_two_result = part_two(file_path)
    print(f"Part Two: {part_two_result}")
