import os

print("Day 6: ")


def read_grid(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def part_one(file_path):
    return 0


def part_two(file_path):
    return 0


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input6.txt')

partOne = part_one(file_path)
print(f"Part One: {partOne}")

partTwo = part_two(file_path)
print(f"Part Two: {partTwo}")
