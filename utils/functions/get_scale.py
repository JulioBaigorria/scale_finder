import sys
from typing import Tuple, cast
from utils.types import RootNote, ScaleType
from .get_available_scales import get_available_scales_for_root


def get_scale_input() -> Tuple[RootNote, ScaleType]:
    """
    Gets and validates musical input from user (only validates notes)
    Returns:
        Tuple[root_note: RootNote, scale_name: str]
    """
    valid_notes = {"C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"}

    try:
        if len(sys.argv) == 3:
            root = sys.argv[1].upper()
            if root not in valid_notes:
                raise ValueError(f"Invalid note. Use: {sorted(valid_notes)}")
            return cast(RootNote, root), sys.argv[2].lower()

        print("\n🎼 Enter musical parameters")
        while True:
            root_input = input("Root note (C, C#, D, etc.): ").strip().upper()
            if root_input in valid_notes:
                root = cast(RootNote, root_input)
                break
            print(f"Invalid note. Use: {sorted(valid_notes)}")

        available_scales = get_available_scales_for_root(root)
        print("Available Scales:", available_scales)
        scale = input("Scale name: ").strip().lower()
        return root, scale

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
