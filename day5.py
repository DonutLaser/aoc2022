def copy_stacks(stacks):
    result = []

    for stack in stacks:
        result.append([])

        for item in stack:
            result[-1].append(item)

    return result

def parse_stack_level(level, stack_count):
    stacks = []

    index = 0
    for _ in range(stack_count):
        item = ""
        for _ in range(3):
            item += level[index]
            index += 1

        if item.strip():
            stacks.append(item[1])
        else:
            stacks.append("")

        index += 1

    return stacks


def parse_input(lines):
    stacks = []
    moves = []

    stack_count = len(lines[0]) // 4
    for _ in range(stack_count):
        stacks.append([])

    for line in lines:
        if line.startswith(" 1") or not line.strip():
            continue

        if line.startswith("move"):
            split = line.strip().split(" ")
            moves.append((int(split[1]), int(split[3]), int(split[5])))
        else:
            level_stacks = parse_stack_level(line, stack_count)

            for i in range(stack_count):
                if level_stacks[i]:
                    stacks[i].append(level_stacks[i])

    for i in range(stack_count):
        stacks[i].reverse()

    return (stacks, moves, stack_count)


def part1(stacks, moves, stack_count):
    result = ""

    for move in moves:
        from_index = move[1] - 1
        to_index = move[2] - 1
        for _ in range(move[0]):
            last_item = stacks[from_index].pop()
            stacks[to_index].append(last_item)

    for i in range(stack_count):
        result += stacks[i][-1]

    return result


def part2(stacks, moves, stack_count):
    result = ""

    for move in moves:
        from_index = move[1] - 1
        to_index = move[2] - 1

        items_to_move = []
        for _ in range(move[0]):
            items_to_move.append(stacks[from_index].pop())

        for _ in range(len(items_to_move)):
            stacks[to_index].append(items_to_move.pop())

    for i in range(stack_count):
        result += stacks[i][-1]

    return result


def main():
    lines = []

    with open("day5_input.txt") as file:
        for line in file:
            lines.append(line)

    stacks, moves, stack_count = parse_input(lines)

    print("Answers:")
    print(f"Part1: {part1(copy_stacks(stacks), moves, stack_count)}")
    print(f"Part2: {part2(copy_stacks(stacks), moves, stack_count)}")


if __name__ == "__main__":
    main()
