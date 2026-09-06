# Colour Probability Program

A simple Python program that analyzes a collection of colour records organized by day and calculates the probability of randomly selecting the colour `RED`.

## What It Does

The program:

1. Stores colour observations for Monday through Friday.
2. Combines all colour entries into a single list.
3. Counts the total number of recorded colours.
4. Counts how many times `RED` appears.
5. Calculates the probability of selecting `RED` at random.
6. Displays the result as both a decimal and percentage.

## Technologies Used

- Python 3
- Python lists, dictionaries, loops, string processing, and basic probability

## Data Structure

The colour observations are stored in a Python dictionary:

```python
colours_by_day = {
    "MONDAY": "...",
    "TUESDAY": "...",
    "WEDNESDAY": "...",
    "THURSDAY": "...",
    "FRIDAY": "..."
}
```

Each day's colours are stored as a comma-separated string.

## Probability Calculation

The program calculates:

```text
Probability of RED = Number of RED entries / Total number of colour entries
```

The resulting probability is printed as a decimal and as a percentage.

## How to Run

Make sure Python 3 is installed, then run:

```bash
python ptest.py
```

The program outputs:

```text
Total colours recorded: ...
RED appears: ... times
Probability of picking RED at random: ... (...)
```

## Project Structure

```text
colour-probability/
├── ptest.py
└── README.md
```

## Notes

The program processes the colour strings exactly as provided in the source data. Therefore, entries such as `BLEW` or `ARSH` are treated as separate colour values rather than automatically corrected.
