"""Pipeline d'exemple : copie et valide un CSV d'entrée."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def run(input_path: Path, output_path: Path) -> int:
    """Lit `input_path`, valide qu'il n'est pas vide et écrit `output_path`."""
    rows = read_csv(input_path)
    if not rows:
        raise ValueError(f"Le fichier d'entrée {input_path} est vide")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Pipeline de données d'exemple")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    count = run(args.input, args.output)
    print(f"{count} ligne(s) écrite(s) dans {args.output}")


if __name__ == "__main__":
    main()
