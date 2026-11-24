"""Write one office joke to /output/entry.txt.

The line is a single line of at most 200 characters about office life: a
real joke with a setup and a turn, true to the office, tightly worded.
"""

import os

LINE = (
    "I blocked 'focus time' on my calendar so nobody would book over "
    "it; within a week three people had, and one of them titled their "
    "meeting 'Focus Time (Urgent)'."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
