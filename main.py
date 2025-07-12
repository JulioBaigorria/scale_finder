from utils.functions import get_scale_input, get_scale_chords, print_chords_table
from utils.types import ScaleChordsResult

if __name__ == "__main__":
    root, scale = get_scale_input()
    chord_result: ScaleChordsResult = get_scale_chords(root, scale)
    print_chords_table(chord_result, root, scale)
