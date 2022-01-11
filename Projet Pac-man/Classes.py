import pygame  # necessaire pour charger les images et les sons
import random

#Labyrinthe
niveau =           [[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [ 1,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,1],
                    [ 1,2,1,1,1,2,2,2,2,0,0,2,2,2,2,1,1,1,2,1],
                    [ 1,2,3,1,2,2,1,1,1,1,1,1,1,1,2,2,1,3,2,1],
                    [ 1,2,2,2,2,2,1,0,0,0,0,0,0,1,2,2,2,2,2,1],
                    [ 1,2,1,1,2,2,1,0,0,0,0,0,0,1,2,2,1,1,2,1],
                    [ 1,2,2,2,2,2,1,0,1,1,1,1,0,1,2,2,2,2,2,1],
                    [ 1,2,1,1,1,2,0,0,0,0,0,0,0,0,2,1,1,1,2,1],
                    [ 1,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,1],
                    [ 1,2,1,1,2,1,1,2,2,1,1,2,2,1,1,2,1,1,2,1],
                    [ 1,2,2,1,2,1,2,2,2,2,2,2,2,2,1,2,1,2,2,1],
                    [ 1,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,1],
                    [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
 
def dessiner_niveau(surface, niveau,mur):
    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                surface.blit(mur, (i*40, j*40))

def from_coord_to_grid(pos):
    x, y = pos
    i = max(0, int(x // 40))
    j = max(0, int(y // 40))
    return i, j
 
def get_neighbour_blocks(niveau, i_start, j_start):
    blocks = list()
    for j in range(j_start, j_start+2):
        for i in range(i_start, i_start+2):
            if niveau[j][i] == 1:
                topleft = i*40, j*40
                blocks.append(pygame.Rect((topleft), (40, 40)))
    return blocks
 
 
def compute_penetration(block, old_rect, new_rect):
    dx_correction = dy_correction = 0.0
    if old_rect.bottom <= block.top < new_rect.bottom:
        dy_correction = block.top  - new_rect.bottom
    elif old_rect.top >= block.bottom > new_rect.top:
        dy_correction = block.bottom - new_rect.top
    if old_rect.right <= block.left < new_rect.right:
        dx_correction = block.left - new_rect.right
    elif old_rect.left >= block.right > new_rect.left:
        dx_correction = block.right - new_rect.left
    return dx_correction, dy_correction

def bloque_sur_collision1(niveau, old_pos, new_pos, vx, vy):
    old_rect = pygame.Rect(old_pos, (40, 40))
    new_rect = pygame.Rect(new_pos, (40, 40))
    i, j = from_coord_to_grid(new_pos)
    collide_later = list()
    blocks = get_neighbour_blocks(niveau, i, j)
    for block in blocks:
        if not new_rect.colliderect(block):
            continue
 
        dx_correction, dy_correction = compute_penetration(block, old_rect, new_rect)
        if dx_correction == 0.0:
            new_rect.top += dy_correction
            vy = 0.0
        elif dy_correction == 0.0:
            new_rect.left += dx_correction
            vx = 0.0
        else:
            collide_later.append(block)
 
    for block in collide_later:
        dx_correction, dy_correction = compute_penetration(block, old_rect, new_rect)
        if dx_correction == dy_correction == 0.0:
            continue
        if abs(dx_correction) < abs(dy_correction):
            dy_correction = 0.0
        elif abs(dy_correction) < abs(dx_correction):
            dx_correction = 0.0
        if dy_correction != 0.0:
            new_rect.top += dy_correction
            vy = 0.0
        elif dx_correction != 0.0:
            new_rect.left += dx_correction
            vx = 0.0
 
    x, y = new_rect.topleft
    return x, y, vx, vy




        
                    






class Joueur() : # classe pour créer Nick Avocado
    def __init__(self) :
        self.font=font=pygame.font.Font("Oswald.ttf",25)
        self.image = pygame.image.load("Images\-NickEat.png").convert_alpha()
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
        pygame.draw.rect(surface, (60,63,60), [580,27,self.max_health,8.5])
        pygame.draw.rect(surface, (234,31,31), [580,27,self.health,8.5])

    def deplacer(self) :
        if (self.sens == "droite"):
            self.rect.x += self.vitesseX 
        elif (self.sens == "gauche"):
           self.rect.x -= self.vitesseX
        elif (self.sens == "haut"):
            self.rect.y -= self.vitesseY 
        elif (self.sens == "bas"):
            self.rect.y += self.vitesseY 

    def marquer(self):
        self.score+= 25

    def update(self,screen):
        score_text=self.font.render(f"Weight:{self.score}Kg",1,(255,255,255))
        vie_text=self.font.render(f"Cholesterol",1,(234,31,31))
        screen.blit(vie_text,(607,30))
        screen.blit(score_text,(20,20))

    def mourir(self):
            self.health-=50
            self.rect.x=374
            self.rect.y=160
            self.sens="O"
            self.image = pygame.image.load("Images\-NickEat.png").convert_alpha()


class Ennemi():
    def __init__(self):
        self.image = pygame.image.load("Images\-Rock.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([365,400])
        self.rect.y = 270
        self.vitesseX=0
        self.vitesseY=0
    NbEnnemis=1

    def disparaitre(self):
        self.image = pygame.image.load("Images\-Rock.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([365,400])
        self.rect.y = 270
        self.vitesseX=1
        self.vitesseY=1



class Burger(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images\-Burger.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
 


class Coca(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images\-Coca.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y= y

