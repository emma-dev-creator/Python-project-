colours_by_day = {
"MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
"TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
"WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
"THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
"FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE",
}

all_colours = []
for day_colours in colours_by_day.values():
    all_colours.extend(c.strip() for c in day_colours.split(","))

total = len(all_colours)
red_count = all_colours.count("RED")
probability_red = red_count / total

print(f"Total colours recorded: {total}")
print(f"RED appears: {red_count} times")
print(f"Probability of picking RED at random: {probability_red:.4f} ({probability_red*100:.2f}%)")