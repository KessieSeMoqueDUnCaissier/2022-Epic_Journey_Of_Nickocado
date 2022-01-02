import pygame # importation de la librairie pygame
from pygame.locals import *
from pygame import mixer
import Classes
from Classes import*
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init() 
# définir une clock
clock=pygame.time.Clock()
FPS=400

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("The journey of Nikocado") 

# chargement de l'image de fond et du laby
fond=pygame.image.load("Projet Pac-man\Images\-Amogus.png").convert_alpha()
rip_bozo=pygame.image.load("Projet Pac-man\Images\-Nick-Avocado.png").convert_alpha()

# musique
mixer.init()
mixer.music.load("Projet Pac-man\Sons\Retro.mp3")
mixer.music.play(10)

# creation du joueur et des ennemis
player = Classes.Joueur()
listeEnnemis = []
for indice in range(Classes.Ennemi.NbEnnemis):
    mechant = Classes.Ennemi()
    old_x2, old_y2 = mechant.rect.x, mechant.rect.y
    vi_Y=mechant.vitesseY
    vi_X=mechant.vitesseX
    listeEnnemis.append(mechant)

# creation des burgers et des cocas
burger=Classes.Burger()
coca=Classes.Coca()

# Record
record=open("Projet Pac-man\Record.txt","r")
high_score=record.read()

### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte
while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))
    # joueur en action
    player.health_bar(screen)
    player.update(screen)
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
        # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
                player.image=pygame.image.load("Projet Pac-man\Images\-NickGauche.png").convert_alpha()
            if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la droite
                player.image=pygame.image.load("Projet Pac-man\Images\-NickDroite.png").convert_alpha()
            if event.key == pygame.K_DOWN: # on déplace le vaisseau de 1 pixel vers le bas
                player.sens = "bas"
                player.image=pygame.image.load("Projet Pac-man\Images\-NickBas.png").convert_alpha()
            if event.key == pygame.K_UP: # on déplace le vaisseau de 1 pixel vers le haut
                player.sens = "haut"
                player.image=pygame.image.load("Projet Pac-man\Images\-NickHaut.png").convert_alpha()

    # R.I.P
            if event.key == pygame.K_ESCAPE:
                running = False # running est sur False 
                sys.exit()
                
    # DEDICACE A LEO ROI SOLEIL
            if event.key == pygame.K_j:
                mixer.music.load("Projet Pac-man\Sons\Giorno_JJBA.mp3")
                mixer.music.play()
        
    ### Actualisation de la scene ###
    # joueur
    old_x, old_y = player.rect.x, player.rect.y
    vx=player.vitesseX
    vy=player.vitesseY
    player.deplacer()
    screen.blit(player.image,player.rect) # appel de la fonction qui dessine le joueur
    # duo de vilain
    for ennemi in listeEnnemis:
        screen.blit(ennemi.image,ennemi.rect) # appel de la fonction qui dessine les ennemis
    # labyrinthe
    mur = pygame.image.load("Projet Pac-man\Images\-MazeBlock.png").convert_alpha() 
    dessiner_niveau(screen, niveau, mur)
    # burgers
    dessiner_burger(screen, niveau, burger.image)
    # cocas
    dessiner_coca(screen, niveau, coca.image)

    ### Collisions ###
    player.rect.x, player.rect.y, vx, vy = bloque_sur_collision1(niveau, (old_x, old_y), (player.rect.x, player.rect.y), vx, vy)
    # vilains VS murs & joueur
    sus=pygame.mixer.Sound("Projet Pac-man\Sons\Vine_Boom.mp3")
    for vilain in listeEnnemis:   
        vilain.rect.x,vilain.rect.y, vi_X, vi_Y = bloque_sur_collision1(niveau,(old_x2, old_y2), (vilain.rect.x, vilain.rect.y), vi_X, vi_Y)    
        if vilain.rect.x <= player.rect.x:
            vilain.rect.x +=  vilain.vitesseX
        if vilain.rect.x >= player.rect.x:
            vilain.rect.x -= vilain.vitesseX
        if vilain.rect.y <= player.rect.y:
            vilain.rect.y += vilain.vitesseY
        if vilain.rect.y >= player.rect.y:
            vilain.rect.y -= vilain.vitesseY
        
        # Coca = Tueur de TheRock
        if collision2(niveau,(player.rect.x,player.rect.y)):
            player.etat="charge"

        if player.etat=="charge":
            vilain.image=pygame.image.load("Projet Pac-man\Images\-Rock2.png").convert_alpha()
            if player.rect.colliderect(vilain.rect):
                vilain.disparaitre()
                player.score+=200
                player.compteur+=1
                
        if player.compteur>=2:   
            player.etat="normal"
            player.compteur=0  

        if player.etat=="normal":
            vilain.image=pygame.image.load("Projet Pac-man\Images\-Rock.png").convert_alpha()
            if vilain.rect.colliderect(player.rect):
                sus.play()
                player.mourir()
                vilain.disparaitre()
    # manger       
    if collision(niveau,(player.rect.x,player.rect.y)):
        player.marquer()

    ### Fin de jeu ###
    if player.health<=0:
        player.vitesseX=0
        player.vitesseY=0
        final_score=player.score

        if len(high_score)==0:
            with open("Projet Pac-man\Record.txt","w") as file:
                file.write(str(final_score)) 
        else:
            if int(high_score) < player.score:
                with open("Projet Pac-man\Record.txt","w") as file:
                    file.write(str(final_score))
                final_score=int(high_score)

        top_score=player.font.render(f"Record:{int(high_score)}",1,(255,195,0))
        score_fin=player.font.render(f"Score actuel:{player.score}",1,(234,31,31))
        fin_text=player.font.render(f"R.I.P Bozo, Appuie sur Echap pour en finir...",1,(255,255,255))

        screen.blit(rip_bozo,(0,0))
        rip_bozo.blit(fin_text,(222,550))
        rip_bozo.blit(score_fin,(0,150))
        rip_bozo.blit(top_score,(0,120))
    pygame.display.update() # pour ajouter tout changement à l'écran
    clock.tick(FPS)