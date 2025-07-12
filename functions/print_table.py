from typing import List
from .types import ChordData, RootNote, ScaleType


def print_chords_table(
    chords_data: List[ChordData], root: RootNote, scale: ScaleType
) -> None:
    """
    Formats and prints a list of chord dictionaries as a beautiful table with header

    Args:
        chords_data: List of dictionaries with 'scale_note', 'chord', and 'chord_note'
                    Example: [{'scale_note': 'E', 'chord': 'Em', 'chord_note': 'E - G - B'}, ...]
        root: Root note (e.g. 'C', 'F#')
        scale: Scale name (e.g. 'menor', 'frigia')
    """
    if not chords_data:
        print("No chords data to display")
        return

    # Title with root and scale
    title = f"🎼 Chords for {root.upper()} {scale.title()}"
    print(f"\n{title}")
    print("=" * len(title))

    # Calculate column widths
    scale_note_width = max(
        len("Scale Note"), max(len(item["scale_note"]) for item in chords_data)
    )
    chord_width = max(len("Chord"), max(len(item["chord"]) for item in chords_data))
    notes_width = max(
        len("Chord Notes"), max(len(item["chord_note"]) for item in chords_data)
    )

    # Table header
    header = (
        f"╔{'═' * (scale_note_width + 2)}╦{'═' * (chord_width + 2)}╦{'═' * (notes_width + 2)}╗\n"
        f"║ {'Scale Note'.ljust(scale_note_width)} ║ {'Chord'.ljust(chord_width)} ║ {'Chord Notes'.ljust(notes_width)} ║\n"
        f"╠{'═' * (scale_note_width + 2)}╬{'═' * (chord_width + 2)}╬{'═' * (notes_width + 2)}╣"
    )
    print(header)

    # Table rows
    for item in chords_data:
        row = (
            f"║ {item['scale_note'].ljust(scale_note_width)} ║ "
            f"{item['chord'].ljust(chord_width)} ║ "
            f"{item['chord_note'].ljust(notes_width)} ║"
        )
        print(row)

    # Table footer
    footer = f"╚{'═' * (scale_note_width + 2)}╩{'═' * (chord_width + 2)}╩{'═' * (notes_width + 2)}╝"
    print(footer)
