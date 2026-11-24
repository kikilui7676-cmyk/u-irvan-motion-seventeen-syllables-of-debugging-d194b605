import os
from pathlib import Path

TEXT = """The tests all pass now
I changed nothing since they failed
No one dares touch it"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
