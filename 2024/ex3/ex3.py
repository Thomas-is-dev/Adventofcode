import re
import os

print("Day 3: Mull It Over")


def part_one(file_path):
    total_sum = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(pattern, line)
            for x, y in matches:
                total_sum += int(x) * int(y)

    return total_sum


def part_two(file_path):
    total_sum = 0
    mul_enabled = True
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    control_pattern = r"(do\(\)|don't\(\))"

    with open(file_path, 'r') as file:
        for line in file:
            position = 0
            while position < len(line):
                control_match = re.match(control_pattern, line[position:])
                if control_match:
                    control = control_match.group(1)
                    mul_enabled = control == "do()"
                    position += len(control)
                    continue

                mul_match = re.match(mul_pattern, line[position:])
                if mul_match and mul_enabled:
                    x, y = map(int, mul_match.groups())
                    total_sum += x * y
                    position += len(mul_match.group(0))
                    continue

                position += 1

    return total_sum


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input3.txt')

basic_total = part_one(file_path)
print(f"Part One: {basic_total}")

controlled_total = part_two(file_path)
print(f"Part Two: {controlled_total}")
