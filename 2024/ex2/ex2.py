import os

print("Day 2: Red-Nosed Reports")


def is_safe_report(levels):
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    is_increasing = all(0 < diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff < 0 for diff in differences)

    return is_increasing or is_decreasing


def is_safe_with_removal(levels):
    if is_safe_report(levels):
        return True

    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe_report(modified_levels):
            return True

    return False


def check_reports_from_file(file_path, check_with_removal=False):
    safe_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            levels = list(map(int, line.split()))

            if check_with_removal:
                if is_safe_with_removal(levels):
                    safe_count += 1
            else:
                if is_safe_report(levels):
                    safe_count += 1

    return safe_count


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input2.txt')

safe_reports = check_reports_from_file(file_path)
print(f"Part One: {safe_reports}")

safe_reports_with_removal = check_reports_from_file(
    file_path, check_with_removal=True)
print(f"Part Two: {safe_reports_with_removal}")
