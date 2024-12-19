from tkinter import messagebox


class AngleInvalideException(Exception):
    def __init__(self):
        messagebox.showinfo(
            title="Erreur d'Angle",
            message="L'angle doit être comprise entre -5 et 200."
        )

class PuissanceInvalideException(Exception):
    def __init__(self):
        messagebox.showinfo(
            title="Erreur de Puissance",
            message="La puissance doit être comprise entre 0 et 350."
        )

class ErreurDeValeur(Exception):
    def __init__(self):
        messagebox.showinfo(
            title="Erreur d'Angle ou de Puissance",
            message="L'angle et/ou la puissance doivent être des entiers."
        )