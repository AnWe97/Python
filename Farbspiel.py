import tkinter as tk
import random

"""FUNCTIONS"""
def push_button(clicked_button: tk.Button) -> None:
    """Button push configuration"""

    current_button_color = current_color.get()

    color_amount_dict[clicked_button.cget("bg")] -= 1
    clicked_button.config(bg=COLOR_TRANSLATION[current_button_color])
    color_amount_dict[clicked_button.cget("bg")] += 1

    label_pack()

def label_pack() -> None:
    """Destroys all current labels and packs new labels on the right side"""

    for widget in label_frame.winfo_children():
        widget.destroy()

    for index, opt in enumerate(COLOR_OPTIONS_GER):
        row_frame = tk.Frame(label_frame, bg="lightgray")
        row_frame.pack(fill="x", pady=2)

        text_lb = tk.Label(row_frame, text=f"Anzahl {opt}:", fg="orange", **TEXT_CONFIG)
        text_lb.pack(side="left", anchor="w")

        farbe_eng = COLOR_OPTIONS_ENG[index]
        zahl_lb = tk.Label(row_frame, text=str(color_amount_dict[farbe_eng]), fg="green", **TEXT_CONFIG)
        zahl_lb.pack(side="right", anchor="e")

"""CONSTANTS"""
ROOT = tk.Tk()
COLOR_OPTIONS_GER = ["Rot", "Grün", "Blau", "Gelb"]
COLOR_OPTIONS_ENG = ["red", "green", "blue", "yellow"]

COLOR_TRANSLATION = {

    "Rot": "red",
    "Grün": "green",
    "Blau": "blue",
    "Gelb": "yellow"

}

HEADER_TEXT_CONFIG = {
    "bg":"lightgray",
    "font": ("Arial", 24, "bold")
}

BUTTON_CONFIG = {
    "width": 8,
    "height": 4,
    "borderwidth": 2,
    "relief": "solid"
}

TEXT_CONFIG = {
    "bg": "lightgray",
    "font": ("Arial", 16, "bold")
}

"""TKINTER SETUP"""
ROOT.geometry("800x500")
ROOT.title("Farbspiel")
ROOT.config(bg="lightgray")

"""VARIABLES"""
current_color = tk.StringVar(value="Rot")

color_amount_dict = {

    "red": 0,
    "green": 0,
    "blue": 0,
    "yellow": 0

}

"""WIDGETS"""
header_frame = tk.Frame(ROOT, bg="lightgray")
header_frame.pack(side="top")

content_frame = tk.Frame(ROOT, bg="lightgray")
content_frame.pack(side="top", fill="both", expand=True)

radio_frame = tk.Frame(content_frame, bg="lightgray")
radio_frame.pack(side="left", padx=20, expand=True, anchor="center")

gamefield_frame = tk.Frame(content_frame, bg="lightgray")
gamefield_frame.pack(side="left", expand=True, anchor="center", pady=10)

label_frame = tk.Frame(content_frame, bg="lightgray")
label_frame.pack(side="left", expand=True, padx=20, anchor="center")

# radiobuttons
for opt in COLOR_OPTIONS_GER:
    rb = tk.Radiobutton(
        radio_frame,
        text=opt,
        variable=current_color,
        value=opt,
        **TEXT_CONFIG
    )
    rb.pack(anchor="w")

# header
header_label = tk.Label(header_frame, text="Farbspiel", fg="Green", **HEADER_TEXT_CONFIG)
header_label.pack(anchor="center")

# game field buttons
for i in range(4):
    for j in range(4):

        button_color = random.choice(COLOR_OPTIONS_ENG)

        color_amount_dict[button_color] += 1

        button = tk.Button(gamefield_frame, bg=button_color, **BUTTON_CONFIG)
        button.config(command=lambda b=button: push_button(b))
        button.grid(row=i, column=j)

label_pack()

"""MAINLOOP"""
ROOT.mainloop()