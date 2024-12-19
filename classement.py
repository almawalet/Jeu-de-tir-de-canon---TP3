import tkinter as tk


class Classement:
    """Classe pour gérer la fonctionnalité de classement.

    Attributs:
        nom_fichier (str): Le nom du fichier où les scores sont sauvegardés.
        scores (list): Une liste de tuples contenant les noms et scores.
        fenetre_classement (tk.Toplevel): La fenêtre de classement.
    """

    def __init__(self, nom_fichier="classement.txt"):
        """Initialise un objet Classement avec un nom de fichier donné.

        Args:
            nom_fichier (str): Le nom du fichier où les scores sont sauvegardés. Par défaut "classement.txt".
        """
        self.nom_fichier = nom_fichier
        self.scores = self.charger_scores()
        self.fenetre_classement = None

    def charger_scores(self):
        """Charge les scores à partir du fichier de classement.

        Cette méthode lit le fichier de classement spécifié par l'attribut
        `nom_fichier`, et extrait les scores sous forme de tuples (nom, score).
        Les scores sont triés par ordre décroissant et seules les dix meilleures
        entrées sont conservées.

        Returns:
            list: Une liste triée de tuples contenant les noms et scores. Si le
            fichier de classement n'existe pas, une liste vide est retournée.

        Exemple de contenu du fichier de classement:
            Le fichier `classement.txt` doit avoir le format suivant, avec chaque ligne
            contenant un nom et un score séparés par une virgule:

            John,100
            Alice,30
            Bob,50
            Eve,0
            Charlie,10

        Exemple de sortie:
            Si le fichier `classement.txt` contient les lignes ci-dessus, la méthode
            retournera:

            [('John', 100), ('Bob', 50), ('Alice', 30), ('Charlie', 10), ('Eve', 0)]
        """
        try:
            with open(self.nom_fichier, "r") as fichier:
                    liste_tuple = []
                    if fichier is []:
                        return []
                    else:
                        for ligne in fichier:
                            ligne = ligne.strip().split(",")
                            try:
                                nom = ligne[0]
                                score = int(ligne [1])
                            except IndexError:
                                return []
                            liste_tuple.append((nom, score))
                        liste_tuple = sorted(liste_tuple, key=lambda x: x[1], reverse=True)[:10] #copier de la methode enregistrer_score
                        return liste_tuple
        except FileNotFoundError:
            with open(self.nom_fichier, "w") as fichier:
                pass
            return []

    def enregistrer_score(self, nom, score):
        """Enregistre un nouveau score dans le classement.

        Args:
            nom (str): Le nom du joueur.
           score (int): Le score du joueur.
        """
        self.scores.append((nom, score))
        # Tri des scores par ordre décroissant et on conserve que les 10 meilleurs scores
        self.scores = sorted(self.scores, key=lambda x: x[1], reverse=True)[:10]
        with open(self.nom_fichier, "a") as f:
            f.write(f"{nom},{score}\n")

    def afficher(self):
        """Affiche la fenêtre du classement avec les 10 meilleurs scores."""
        # Vérifie si la fenêtre de classement existe et est ouverte
        if (
            self.fenetre_classement is not None
            and self.fenetre_classement.winfo_exists()
        ):
            self.fenetre_classement.lift()  # Ramener la fenêtre au premier plan
            return

        self.fenetre_classement = tk.Toplevel()  # Création d'une nouvelle fenêtre
        self.fenetre_classement.geometry("300x300")
        self.fenetre_classement.title("Classement")
        label = tk.Label(                #j'ai modifié légèrement le code du label pour utiliser la methode config() sur label
            self.fenetre_classement,
            text="Les 10 meilleurs scores",
            font=("Helvetica", 16),
            )
        label.pack(anchor=tk.W, padx=10, pady=10)

        liste_de_scores = self.charger_scores()
        if liste_de_scores == []:
            label.config(text="-- Aucun score enregistré pour l'instant--")
        else:
            for element in liste_de_scores:
                index = liste_de_scores.index(element)
                label = tk.Label(self.fenetre_classement, text=f'{index + 1}. {element[0]}, {element[1]}')
                label.pack()
