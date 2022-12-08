priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_priority(character):
    index = priority.find(character)
    return index + 1


def part1(rucksacks):
    result = 0
    for rucksack in rucksacks:
        left, right = (
            rucksack[0 : len(rucksack) // 2],
            rucksack[len(rucksack) // 2 :],
        )

        right_map = {}
        for c in right:
            right_map[c] = True

        for c in left:
            if c in right_map:
                result += get_priority(c)
                break

    return result


def part2(rucksacks):
    result = 0
    group = []
    for rucksack in rucksacks:
        group.append(rucksack)

        if len(group) < 3:
            continue

        common = list(set(group[0]) & set(group[1]) & set(group[2]))
        result += get_priority(common[0])
        group = []

    return result


def main():
    rucksacks = []
    with open("day3_input.txt", "r+") as file:
        for line in file:
            rucksacks.append(line.strip())

    print("Answers:")
    print(f"Part1: {part1(rucksacks)}")
    print(f"Part2: {part2(rucksacks)}")


if __name__ == "__main__":
    main()
