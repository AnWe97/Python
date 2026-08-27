import tkinter as tk

"""FUNCTIONS"""

def push_button(clicked_button: tk.Button) -> None:
    """PUSH BUTTON"""
    global PLAYER

    if clicked_button["text"] == "":
        clicked_button["text"] = PLAYER

        if PLAYER == "X":
            clicked_button.config(fg="red")
        else:
            clicked_button.config(fg="blue")

        # Change player
        if PLAYER == "O":
            PLAYER = "X"
        else:
            PLAYER = "O"


"""CONSTANTS"""
PLAYER = "X"

WINDOW_SIZE = "800x600"

FRAME_CONFIG = {

    "bg": "darkgray"

}

LABEL_CONFIG = {

    "bg": "darkgray",
    "font": ("Arial", 25, "bold")

          }

BUTTON_CONFIG = {

    "bg": "black",
    "width": 5,
    "font": ("Arial", 25, "bold")

}


"""TKINTER SETUP"""
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry(WINDOW_SIZE)
root.configure(background="darkgray")

"""VARIABLES"""
button_text = tk.StringVar(value="")

"""MAINLOOP"""
header_frame = tk.Frame(root, **FRAME_CONFIG)
header_frame.pack(side="top", fill="both", expand=False, pady=75)

header = tk.Label(header_frame, text="Tic Tac Toe", **LABEL_CONFIG)
header.pack()

field_frame = tk.Frame(root, **FRAME_CONFIG)
field_frame.pack(side="top", fill="y", expand=True)

#buttons
for i in range(3):

    for j in range(3):

        button = tk.Button(field_frame, text="", **BUTTON_CONFIG)
        button.config(command=lambda b=button: push_button(b))
        button.grid(row=i, column=j, padx=15, pady=10)


root.mainloop()