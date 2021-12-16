import pygame # importation de la librairie pygame
import Classes
import random
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
fond=pygame.image.load("Projet Pac-man\Images\-Amogus.png")
maze= Classes.Maze()

# creation du joueur et des ennemis
player = Classes.Joueur()
listeEnnemis = []
for indice in range(Classes.Ennemi.NbEnnemis):
    mechant = Classes.Ennemi()
    listeEnnemis.append(mechant)

### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))
    # joueur en action
    player.health_bar(screen)
    player.update(screen)
    maze.block_surf = pygame.image.load("Projet Pac-man\Images\-MazeBlock.png").convert_alpha()


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
        # musique
            if event.key == pygame.K_m:
                pygame.mixer.music.load("Projet Pac-man\Sons\Giorno_JJBA.mp3")
                pygame.mixer.music.play()

    ### Actualisation de la scene ###
    # joueur
    player.deplacer()
    screen.blit(player.image,player.rect) # appel de la fonction qui dessine le joueur
    # duo de vilain
    for ennemi in listeEnnemis:
        ennemi.deplacer()
        screen.blit(ennemi.image,ennemi.rect) # appel de la fonction qui dessine les ennemis
    # labyrinthe
    maze.draw(screen, maze.block_surf) # on dessine le labyrinthe

    ### Collisions ###
    # joueur VS murs
    rectBlock = maze.block_surf.get_rect()
    if player.rect.colliderect(rectBlock):
        player.vitesse=0
    # vilains VS murs & joueur
    for vilain in listeEnnemis:    
        if vilain.rect.colliderect(rectBlock):
            vilain.sens=random.randint(1,4)
        elif vilain.rect.colliderect(player.rect):
            player.health-=50
            player.rect.x=45
            player.rect.y=514
            player.sens="O"

    ### Fin de jeu ###
    if player.health==0:
           running = False # running est sur False
           sys.exit() 

    pygame.display.update() # pour ajouter tout changement à l'écran
    clock.tick(FPS)