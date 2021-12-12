import pygame  # necessaire pour charger les images et les sons
import random
import math

class Maze: # creation du laby
    def __init__(self):
       self.M = 20
       self.N = 20
       self.maze = [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,1,
                     1,2,1,1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,2,1,
                     1,2,2,1,2,2,1,1,1,1,1,1,1,1,2,1,2,2,2,1,
                     1,2,2,2,2,2,1,0,0,0,0,0,0,1,2,2,2,2,2,1,
                     1,2,1,1,1,2,1,0,1,0,0,1,0,1,2,1,1,1,2,1,
                     1,2,2,3,2,2,1,0,1,1,1,1,0,1,2,2,3,2,2,1,
                     1,2,1,1,1,2,1,0,0,0,0,0,0,1,2,1,1,1,2,1,
                     1,2,2,2,2,2,2,0,1,1,1,1,0,2,2,2,2,2,2,1,
                     1,2,1,1,2,1,1,2,2,1,1,2,2,1,1,2,1,1,2,1,
                     1,2,2,1,2,1,1,2,2,2,2,2,2,1,1,2,1,2,2,1,
                     1,0,0,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def draw(self,display_surf,image_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 1:
               display_surf.blit(image_surf,( bx * 40 , by * 40))
           bx += 1
           if bx > self.M-1:
               bx = 0 
               by += 1

    def draw2(self,display_surf,image_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 2:
               display_surf.blit(image_surf,( bx * 40 , by * 41.2))
           bx += 1
           if bx > self.M-1:
               bx = 0 
               by += 1
               
    def draw3(self,display_surf,image_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 3:
               display_surf.blit(image_surf,( bx * 39.5 , by * 41))
           bx += 1
           if bx > self.M-1:
               bx = 0 
               by += 1  

class Joueur() : # classe pour créer Nick Avocado
    def __init__(self) :
        self.font=font=pygame.font.Font("Projet Pac-man\Oswald.ttf",25)
        self.image = pygame.image.load("Projet Pac-man\Images\-NickDroite.png")
        self.sens = "O"
        self.vitesse = 1
        self.score=0
        self.health=150
        self.max_health=150
        self.rect=self.image.get_rect()
        self.rect.x=45
        self.rect.y=514

    def health_bar(self,surface):
        pygame.draw.rect(surface, (60,63,60), [580,27,self.max_health,8.5])
        pygame.draw.rect(surface, (234,31,31), [580,27,self.health,8.5])

    def deplacer(self) :
        if (self.sens == "droite") and (self.rect.x < 723):
            self.rect.x += self.vitesse
        elif (self.sens == "gauche") and (self.rect.x > 45):
           self.rect.x -= self.vitesse
        elif (self.sens == "haut") and (self.rect.y > 123):
            self.rect.y -= self.vitesse
        elif (self.sens == "bas") and (self.rect.y < 514):
            self.rect.y += self.vitesse

    def marquer(self):
        self.score+= 1

    def update(self,screen):
        score_text=self.font.render(f"Weight:{self.score}Kg",1,(255,255,255))
        screen.blit(score_text,(20,20))

""""
class Ennemi():
"""

"""
class Burger():
"""
    
