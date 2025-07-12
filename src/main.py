import csv
import random
from typing import List, Dict, TypedDict, Literal
from pathlib import Path

from utils import print_chords_table

BASE_DIR = Path(__file__).parent.parent  # Asume que main.py está en src/
DATA_PATH = BASE_DIR / "data" / "DATABASE.csv"

# Definición de tipos
RootNote = Literal[
    'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
]

ScaleType = Literal['menor', 'frigia', 'armonica']

class ChordData(TypedDict):
    scale_note: str
    chord: str
    chord_note: str
    scale_note_order: int  # Cambiado a scale_note_order

class CSVRow(TypedDict):
    root: str
    scale: str
    scale_note_order: str  # Nombre de columna actualizado
    scale_note: str
    chord: str
    chord_note: str

def get_scale_chords(
    root: RootNote,
    scale: ScaleType
) -> List[ChordData]:
    """
    Returns the notes, chords, and chord notes for a given root and scale.
    If multiple chords exist for a scale note, selects one randomly.
    
    Args:
        root: Musical root note (e.g., 'C', 'C#', 'D')
        scale: Scale type (e.g., 'menor', 'frigia', 'armonica')
    
    Returns:
        List of dictionaries with chord data containing:
        - scale_note: str
        - chord: str
        - chord_note: str
        - scale_note_order: int
    """
    chords_data: List[ChordData] = []
    note_chords: Dict[str, List[ChordData]] = {}
    
    with open(DATA_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_row: CSVRow = row  # type: ignore
            if csv_row['root'] == root and csv_row['scale'] == scale:
                try:
                    chord_data: ChordData = {
                        'scale_note': csv_row['scale_note'],
                        'chord': csv_row['chord'],
                        'chord_note': csv_row['chord_note'],
                        'scale_note_order': int(csv_row['scale_note_order'])  # Conversión a int
                    }
                    
                    # Agrupar acordes por nota
                    if chord_data['scale_note'] not in note_chords:
                        note_chords[chord_data['scale_note']] = []
                    note_chords[chord_data['scale_note']].append(chord_data)
                except (ValueError, KeyError) as e:
                    print(f"Warning: Error processing row - {e}. scale_note_order null")
                    continue
    
    # Seleccionar un acorde aleatorio para cada nota y ordenar
    chords_data = [random.choice(chords) for chords in note_chords.values()]
    chords_data.sort(key=lambda x: x['scale_note_order'])
    
    return chords_data

if __name__ == "__main__":
    # Ejemplo de uso
    e_minor_chords = get_scale_chords('E', 'menor')
    print_chords_table(e_minor_chords)