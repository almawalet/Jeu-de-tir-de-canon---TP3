import random


class Cible:
    """Classe permettant de représenter une cible.

    Attributs:
        canvas (tk.Canvas): La toile où la cible est dessinée.
        x (int): La position x de la cible.
        y (int): La position y de la cible.
        identifiant (int): L'identifiant de la cible dans la toile.
    """

    def __init__(self, canvas):
        """Initialise un objet Cible avec une toile donnée.

        Args:
            canvas (tk.Canvas): La toile où la cible sera dessinée.
        """
        self.canvas = canvas
        self.x = 0
        self.y = 0
        self.identifiant = 0

    def creer_nouvelle_cible(self):
        """Crée une nouvelle cible à une position aléatoire sur la toile."""
        self.x = random.randint(400, 750)
        self.x = random.randint(50, 550)
        self.identifiant = self.canvas.create_oval(self.x + 35, self.y + 35, self.x + 20, self.y + 20, fill="red")

        # Aide:
        # - x (une valeur entière aléatoire entre 400 et 750)
        # - y (une valeur entière aléatoire entre 50 et 550)
        # - Se documenter sur la méthode `create_oval` disponible pour les objets Canvas

    def est_touchee(self, projectile):
        """Vérifie si la cible est touchée par un projectile aux coordonnées données.

        Cette méthode détermine si le projectile, aux coordonnées spécifiées,
        se trouve dans une zone de 10 unités autour de la cible.

        Args:
            projectile (Projectile): L'objet Projectile dont les coordonnées
            doivent être vérifiées.

        Returns:
            bool: True si le projectile touche la cible, False sinon.
        """
        distance_x = abs(
            projectile.x - self.x)  # utilisation de la fonction abs() pour ne pas que la distance soit negative
        distance_y = abs(projectile.y - self.y)

        if distance_x <= 20 and distance_y <= 20:
            return True
        else:
            return False