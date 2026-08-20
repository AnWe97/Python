import tkinter as tk
import time
from num2words import num2words

"""FUNCTIONS"""
def reset_all() -> None:
    """Reseted das Bild auf Standart"""
    
    for zeile in labelarray:
        for label in zeile:
            label.config(fg="white")



def update_canvas() -> None:
    """Aktualisiere den Canvas im Fenster"""

    reset_all()

    hour_position, minute_position = get_time_in_words()

    for row, col in hour_position:
        labelarray[row][col].config(fg="red")

    for zeile, spalte in minute_position:
        labelarray[zeile][spalte].config(fg="red")

    for zeile, spalte in WORD_POSITIONS["ES"] + WORD_POSITIONS["IST"] + WORD_POSITIONS["UHR"]:
        labelarray[zeile][spalte].config(fg="red")

    root.after(5000, update_canvas)



def get_time_in_words() -> tuple:
    """Gib die aktuelle Uhrzeit in Worten an."""

    current_time = time.localtime()

    """Umstellung von zb. 13 Uhr -> 1 Uhr"""
    if current_time.tm_hour <= 12:
        hour = num2words(current_time.tm_hour, lang='de')

    elif current_time.tm_hour == 0:
        hour = num2words(12, lang='de')

    else:
        hour = num2words(current_time.tm_hour - 12, lang='de')

    minutes = current_time.tm_min

    """Zieh Minuten auf 0, wenn größer als 0"""
    if len(str(minutes)) < 2:
        """Einstellig"""

        minute_positions = []

        return WORD_POSITIONS[hour.upper()], minute_positions

    else:
        """Zweistellig"""

        while str(minutes)[1] != "0":
            minutes -= 1


        minutes = num2words(minutes, lang="de")

    """Korrekten ZEHN Wert auswählen"""
    if minutes.upper() == "ZEHN":
        minutes += "_MINUTE"
    elif hour.upper() == "ZEHN":
        hour += "_STUNDE"

    return WORD_POSITIONS[hour.upper()], WORD_POSITIONS[minutes.upper()]



"""CONSTANTS"""
WIDTH, HEIGHT = 650, 600


LETTERS = [
    ['E', 'S', 'Q', 'I', 'S', 'T', 'X', 'U', 'H', 'R', 'C', 'V', 'B'],  # ES, IST, UHR
    ['E', 'I', 'N', 'S', 'N', 'Z', 'W', 'E', 'I', 'M', 'K', 'P', 'J'],  # EINS, ZWEI
    ['D', 'R', 'E', 'I', 'W', 'V', 'I', 'E', 'R', 'Y', 'Q', 'X', 'C'],  # DREI, VIER
    ['F', 'Ü', 'N', 'F', 'V', 'S', 'E', 'C', 'H', 'S', 'B', 'N', 'M'],  # FÜNF, SECHS
    ['S', 'I', 'E', 'B', 'E', 'N', 'K', 'A', 'C', 'H', 'T', 'P', 'J'],  # SIEBEN, ACHT
    ['N', 'E', 'U', 'N', 'W', 'Z', 'E', 'H', 'N', 'Y', 'E', 'L', 'F'],  # NEUN, ZEHN_MINUTE, ELF
    ['Z', 'W', 'Ö', 'L', 'F', 'Q', 'Z', 'E', 'H', 'N', 'X', 'C', 'V'],  # ZWÖLF, ZEHN_STUNDE
    ['Z', 'W', 'A', 'N', 'Z', 'I', 'G', 'B', 'N', 'M', 'K', 'P', 'J'],  # ZWANZIG
    ['D', 'R', 'E', 'I', 'S', 'S', 'I', 'G', 'W', 'Y', 'Q', 'X', 'C'],  # DREISSIG
    ['V', 'I', 'E', 'R', 'Z', 'I', 'G', 'V', 'B', 'N', 'M', 'K', 'P'],  # VIERZIG
    ['F', 'Ü', 'N', 'F', 'Z', 'I', 'G', 'J', 'W', 'Y', 'Q', 'X', 'C']   # FÜNFZIG
]


WORD_POSITIONS = {
    # Basis-Wörter
    "ES": [(0, 0), (0, 1)],
    "IST": [(0, 3), (0, 4), (0, 5)],
    "UHR": [(0, 7), (0, 8), (0, 9)],

    # Stunden-Wörter
    "EINS": [(1, 0), (1, 1), (1, 2), (1, 3)],
    "ZWEI": [(1, 5), (1, 6), (1, 7), (1, 8)],
    "DREI": [(2, 0), (2, 1), (2, 2), (2, 3)],
    "VIER": [(2, 5), (2, 6), (2, 7), (2, 8)],
    "FÜNF": [(3, 0), (3, 1), (3, 2), (3, 3)],
    "SECHS": [(3, 5), (3, 6), (3, 7), (3, 8), (3, 9)],
    "SIEBEN": [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)],
    "ACHT": [(4, 7), (4, 8), (4, 9), (4, 10)],
    "NEUN": [(5, 0), (5, 1), (5, 2), (5, 3)],
    "ZEHN_STUNDE": [(6, 6), (6, 7), (6, 8), (6, 9)],
    "ELF": [(5, 10), (5, 11), (5, 12)],
    "ZWÖLF": [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4)],

    # Minuten-Wörter
    "ZEHN_MINUTE": [(5, 5), (5, 6), (5, 7), (5, 8)],
    "ZWANZIG": [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)],
    "DREISSIG": [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)],
    "VIERZIG": [(9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6)],
    "FÜNFZIG": [(10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6)]
}



"""INIT"""
root = tk.Tk()
root.title("Wortuhr")
main_frame = tk.Frame(root, width=WIDTH, height=HEIGHT, bg="black")
main_frame.pack()
font = ("Helvetica", 18, "bold")
main_frame.pack_propagate(False)



"""Create Labelarray"""
labelarray = []

for array in LETTERS:

    frame = tk.Frame(main_frame)
    frame.pack(side="top", fill="x", expand=True)
    labelarray.append([])

    for letter in array:
        label = tk.Label(frame, text=letter, fg="White", bg="Black", font=font)
        label.pack(side="left", fill="x", expand=True)
        labelarray[-1].append(label)



"""Mainloop"""
update_canvas()


root.mainloop()
