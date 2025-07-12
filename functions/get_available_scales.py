import csv
from pathlib import Path
from typing import Set
from .types import RootNote


BASE_DIR = Path(__file__).parent.parent
DATA_PATH = BASE_DIR / "data" / "DATABASE.csv"


def get_available_scales_for_root(root: RootNote) -> Set[str]:
    """
    Returns all unique scales available for a given root note from the CSV database

    Args:
        root: Musical root note to search for

    Returns:
        Set of available scale names (e.g., {'menor', 'frigia', 'armonica'})
    """
    scales = set()

    try:
        with open(DATA_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["root"] == root:
                    scales.add(row["scale"])
    except FileNotFoundError:
        print(f"Error: Database not found at {DATA_PATH}")
    except Exception as e:
        print(f"Error reading CSV: {e}")

    return scales
