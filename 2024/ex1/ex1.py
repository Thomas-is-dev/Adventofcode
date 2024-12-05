import os

print("Day 1: Historian Hysteria")


def part_one(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

    return total_distance


def part_two(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    similarity_score = 0
    right_count = {num: right_list.count(num) for num in set(right_list)}

    for num in left_list:
        similarity_score += num * right_count.get(num, 0)

    return similarity_score


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input1.txt')

total_distance = part_one(file_path)
print(f"Part One: {total_distance}")

similarity_score = part_two(file_path)
print(f"Part Two: {similarity_score}")
