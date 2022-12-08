scores = {
    "AA": 3,
    "AB": 6,
    "AC": 0,
    "BA": 0,
    "BB": 3,
    "BC": 6,
    "CA": 6,
    "CB": 0,
    "CC": 3,
}

shape_scores = {"A": 1, "B": 2, "C": 3}


def normalize_shape(shape):
    if shape == "X":
        return "A"
    if shape == "Y":
        return "B"

    return "C"


def get_shape_score(my_choice):
    if my_choice == "X":
        return 1
    elif my_choice == "Y":
        return 2

    return 3


def get_appropriate_action(opponent, outcome):
    if outcome == "Z":
        if opponent == "A":
            return "B"
        if opponent == "B":
            return "C"
        if opponent == "C":
            return "A"

    if outcome == "X":
        if opponent == "A":
            return "C"
        if opponent == "B":
            return "A"
        if opponent == "C":
            return "B"

    return opponent


def part1(actions):
    result = 0
    for action in actions:
        normalized_shape = normalize_shape(action[1])
        outcome_score = scores[action[0] + normalized_shape]
        result += outcome_score + shape_scores[normalized_shape]

    return result


def part2(actions):
    result = 0
    for action in actions:
        me = get_appropriate_action(action[0], action[1])
        outcome_score = scores[action[0] + me]
        result +=  outcome_score + shape_scores[me]

    return result


def main():
    actions = []
    with open("day2_input.txt", "r+") as file:
        for line in file:
            actions.append((line[0], line[2]))

    total_score_part1 = part1(actions)
    total_score_part2 = part2(actions)

    print("Answer:")
    print(f"Part1: {total_score_part1}")
    print(f"Part2: {total_score_part2}")


if __name__ == "__main__":
    main()
