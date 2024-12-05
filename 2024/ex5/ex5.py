import os

print("Day 5: Print Queue")


def read_grid(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def parse_input(file_path):
    data = read_grid(file_path)
    rules = []
    updates = []

    for line in data:
        if "|" in line:  # Les règles contiennent le caractère '|'
            rules.append(tuple(map(int, line.split("|"))))
        else:
            updates.append(list(map(int, line.split(","))))

    return rules, updates


def is_valid_update(update, rules):
    page_positions = {page: i for i, page in enumerate(update)}

    for a, b in rules:
        if a in page_positions and b in page_positions:
            if page_positions[a] > page_positions[b]:
                return False
    return True


def part_one(file_path):
    rules, updates = parse_input(file_path)
    valid_updates = []

    for update in updates:
        if is_valid_update(update, rules):
            valid_updates.append(update)

    middle_pages = [update[len(update) // 2] for update in valid_updates]
    return sum(middle_pages)


def topological_sort(update, rules):
    from collections import defaultdict, deque

    filtered_rules = [(a, b) for a, b in rules if a in update and b in update]

    graph = defaultdict(list)
    in_degree = {page: 0 for page in update}

    for a, b in filtered_rules:
        graph[a].append(b)
        in_degree[b] += 1

    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_pages = []

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages


def part_two(file_path):
    rules, updates = parse_input(file_path)
    invalid_updates = []

    for update in updates:
        if not is_valid_update(update, rules):
            invalid_updates.append(update)

    sorted_updates = [topological_sort(update, rules)
                      for update in invalid_updates]

    middle_pages = [update[len(update) // 2] for update in sorted_updates]
    return sum(middle_pages)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'input5.txt')

    part_one_result = part_one(file_path)
    print(f"Part One: {part_one_result}")

    part_two_result = part_two(file_path)
    print(f"Part Two: {part_two_result}")
