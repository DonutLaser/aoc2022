def part1(ranges):
    result = 0
    for pair in ranges:
        left, right = pair[0], pair[1]

        if (
            left[0] >= right[0]
            and left[1] <= right[1]
            or right[0] >= left[0]
            and right[1] <= left[1]
        ):
            result += 1

    return result


def part2(ranges):
    result = 0
    for pair in ranges:
        left, right = pair[0], pair[1]

        if (
            right[0] <= left[0] <= right[1]
            or right[0] <= left[1] <= right[1]
            or left[0] <= right[0] <= left[1]
            or left[0] <= right[1] <= left[1]
        ):
            result += 1

    return result


def main():
    ranges = []
    with open("day4_input.txt", "r+") as file:
        for line in file:
            pair = line.strip()
            left, right = pair.split(",")

            range1_min, range1_max = left.split("-")
            range2_min, range2_max = right.split("-")
            ranges.append(
                ((int(range1_min), int(range1_max)), (int(range2_min), int(range2_max)))
            )

    print("Answers:")
    print(f"Part1: {part1(ranges)}")
    print(f"Part2: {part2(ranges)}")


if __name__ == "__main__":
    main()
