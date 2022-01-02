# The Epic Journey Of Nickocado
Vous incarnez Nick Avocado dans ce jeu "Pac-Man like" dans lequel vous devez manger tous les burgers présents, en évitant un duo composé de Dwayne Johnson et The Rock! 
Le jeu est codé à l'aide du module Pygame.

-Utilisez les flèches directionnelles pour vous déplacer dans le labyrinthe. 

-En buvant du coca, vous deviendrez invincible pendant quelques secondes!

-Vous avez une barre de vie, celle-ci est drainée si l'un des membres du duo vous touche!

![nick-avocado](https://user-images.githubusercontent.com/90514084/147881522-6fbdb23b-baca-45f4-9dac-cb70177a75a4.gif)


## Découpage en fonction et en classes:

  ### Fonctions:
  
*Labyrinthe:*
  
  def dessiner_niveau(surface, niveau):
  
    Dessine le niveau sur la surface donnée.
    Utilise la surface `mur` pour dessiner les cases de valeur 1
    (Niveau est une liste de listes)
    
  def from_coord_to_grid(pos):

      Retourne la position dans le niveau en indice (i, j)
      `pos` est un tuple contenant la position (x, y) du coin supérieur gauche.
      On limite i et j à être positif.
  
  def get_neighbour_blocks(niveau, i_start, j_start):
  
    Retourne la liste des rectangles autour de la position (i_start, j_start).
    Vu que le personnage est dans le carré (i_start, j_start), il ne peut entrer en collision qu'avec des blocks dans sa case, la case en-dessous,
    la case à droite ou celle en bas et à droite. 
    On ne prend en compte que les cases du niveau avec une valeur de 1.
 
 def compute_penetration(block, old_rect, new_rect):
 
    Calcul la distance de pénétration du `new_rect` dans le `block` donné.
    `block`, `old_rect` et `new_rect` sont des pygame.Rect.
    Retourne les distances `dx_correction` et `dy_correction`.
    
 def bloque_sur_collision(niveau, old_pos, new_pos, vx, vy):
    
    Tente de déplacer old_pos vers new_pos dans le niveau.
    S'il y a collision avec les éléments du niveau, new_pos sera ajusté pour être adjacents aux éléments avec lesquels il entre en collision.
    On passe également en argument les vitesses `vx` et `vy`.
    La fonction retourne la position modifiée pour new_pos ainsi que les vitesses modifiées selon les éventuelles collisions.
    
*Burgers:* 
 
 def dessiner_burger(surface, niveau, pain): 
    
    Dessine les burgers sur la surface donnée.
    Utilise la surface `mur` pour dessiner les cases de valeur 2
    (Niveau est une liste de listes)
    
 def get_neighbour_blocks2(niveau, i_start, j_start):
     
     Fait la même chose que la fonction get_neighbour_blocks, mais prend uniquement en compte les cases de valeur 2
     
 def collision(niveau, pos)
      
      Prend en compte la position du joueur dans le niveau et crée un rectangle sur ce dernier.
      Parcourt la liste renvoyée par get_neighbour_block2 et vérifie si chaque élément de la liste rentre en collision avec le rectangle du joueur.
      Renvoie alors True en cas de collision et False dans le cas contraire.
      
*Cocas:*
  
  Même fonctions désignées pour les burgers excepté pour get_neighbour_blocks, prenant uniquement les cases de valeur 3.

### Classes:

  class Joueur() : # classe pour créer Nick Avocado
  
    def __init__(self) :
        self.font=font=pygame.font.Font("Projet Pac-man\Oswald.ttf",25)
        self.image = pygame.image.load("Projet Pac-man\Images\-NickDroite.png").convert_alpha()
        self.sens = "O"
        self.vitesseX = 1
        self.vitesseY= 1
        self.etat="normal"
        self.score=0
        self.health=150
        self.max_health=150
        self.compteur=0
        self.rect=self.image.get_rect()
        self.rect.x=374
        self.rect.y=160

    def health_bar(self,surface):

    def deplacer(self):

    def marquer(self):

    def update(self,screen):

    def mourir(self):



class Ennemi():

    def __init__(self):
        self.image = pygame.image.load("Projet Pac-man\Images\-Rock.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([365,400])
        self.rect.y = 270
        self.vitesseX=1
        self.vitesseY=1
    NbEnnemis=2

    def disparaitre(self):



class Burger():

    def __init__(self):
        self.image = pygame.image.load("Projet Pac-man\Images\-Burger.png").convert_alpha()
        self.rect = self.image.get_rect()
 
    def est_mangé(self):

class Coca():

    def __init__(self):
        self.image = pygame.image.load("Projet Pac-man\Images\-Coca.png").convert_alpha()
        self.rect = self.image.get_rect()

    def est_bu(self):
