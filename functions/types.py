from typing import TypedDict, List, Literal, Tuple

RootNote = Literal["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

ScaleType = str


class ChordData(TypedDict):
    scale_note: str
    chord: str
    chord_note: str
    scale_note_order: int


class CSVRow(TypedDict):
    root: RootNote
    scale: ScaleType
    scale_note_order: str
    scale_note: str
    chord: str
    chord_note: str


ScaleSearchParams = Tuple[RootNote, ScaleType]
ScaleChordsResult = List[ChordData]
