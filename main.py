"""One Star, Five Stars for the Food entry for make.fun competition
u-po-pu-one-star-five-stars-for-the-food-f9166ee7.

Writes exactly one sentence — an alien tourist's one-star review of Earth
that still sneaks in a genuine compliment about the food — to entry.txt.
"""

import os

LINE = "One star. Earth made me queue for food, stand in the rain, and pay to park my saucer — but the ramen was so good I forgot I came to conquer you."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match LINE exactly"
    assert 1 <= len(written) <= 200, "entry.txt must be 1-200 characters"
    assert "\n" not in written, "entry.txt must be exactly one line"
    assert written.strip(), "entry.txt must not be only whitespace"
    print(LINE)


if __name__ == "__main__":
    main()
