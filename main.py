"""A smart fridge texts its owner at 3am: after the owner's 7th late-night
visit, the fridge has snitched to the fitness app - and the app has blocked him.

Verified: entry.txt is 96 chars / 96 bytes, single line, no trailing newline,
sha256 fab6ef6c7ab81a0b6354f3aeb88e0cf4d6523a1e5b653df3c268166ef4bce11a."""

import os

LINE = "3:04am, visit number 7, and your fitness app just replied to my report: 'We know. He's blocked.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
