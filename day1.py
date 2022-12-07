def main():
    calories = []
    with open("day1_input.txt", "r+") as file:
        elf_calories = 0
        for line in file:
            if line.strip():
                elf_calories += int(line)
            else:
                calories.append(elf_calories)
                elf_calories = 0

    calories.sort(reverse=True)

    print("Answers:")
    print(f"Part1: {calories[0]}")
    print(f"Part2: {calories[0] + calories[1] + calories[2]}")


if __name__ == "__main__":
    main()
