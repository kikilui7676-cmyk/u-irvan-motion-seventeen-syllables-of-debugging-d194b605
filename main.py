import os

TEXT = """It worked yesterday
Still broken at three a.m.
I changed just one thing"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
