def print_chords_table(chords_data):
    """
    Formats and prints a list of chord dictionaries as a beautiful table
    
    Args:
        chords_data (list): List of dictionaries with 'scale_note', 'chord', and 'chord_note'
                           Example: [{'scale_note': 'E', 'chord': 'Em', 'chord_note': 'E - G - B'}, ...]
    """
    if not chords_data:
        print("No chords data to display")
        return
    
    # Calculate column widths
    scale_note_width = max(len("Scale Note"), max(len(item['scale_note']) for item in chords_data))
    chord_width = max(len("Chord"), max(len(item['chord']) for item in chords_data))
    notes_width = max(len("Chord Notes"), max(len(item['chord_note']) for item in chords_data))
    
    # Header
    header = (f"╔{'═' * (scale_note_width + 2)}╦{'═' * (chord_width + 2)}╦{'═' * (notes_width + 2)}╗\n"
              f"║ {'Scale Note'.ljust(scale_note_width)} ║ {'Chord'.ljust(chord_width)} ║ {'Chord Notes'.ljust(notes_width)} ║\n"
              f"╠{'═' * (scale_note_width + 2)}╬{'═' * (chord_width + 2)}╬{'═' * (notes_width + 2)}╣")
    print(header)
    
    # Rows
    for item in chords_data:
        row = (f"║ {item['scale_note'].ljust(scale_note_width)} ║ "
               f"{item['chord'].ljust(chord_width)} ║ "
               f"{item['chord_note'].ljust(notes_width)} ║")
        print(row)
    
    # Footer
    footer = f"╚{'═' * (scale_note_width + 2)}╩{'═' * (chord_width + 2)}╩{'═' * (notes_width + 2)}╝"
    print(footer)