import pygame # importation de la librairie pygame
import Classes
import math
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init() 
# définir une clock
clock=pygame.time.Clock()
FPS=400

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Nikocado au McDo") 

# chargement de l'image de fond et du laby
fond=pygame.image.load("Projet Pac-man\Images\-Amogus.png")
maze= Classes.Maze()

# creation du joueur et des ennemis
player = Classes.Joueur()


### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))
    # joueur en action
    player.health_bar(screen)
    player.update(screen)
    maze.image_surf = player.image
    maze._block_surf = pygame.image.load("Projet Pac-man\Images\-MazeBlock.png").convert()
    maze.burgers= pygame.image.load("Projet Pac-man\Images\-Burger.png")
    maze.coca= pygame.image.load("Projet Pac-man\Images\-Coca.png")

    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement

        # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
                player.image=pygame.image.load("Projet Pac-man\Images\-NickGauche.png")
            if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la droite
                player.image=pygame.image.load("Projet Pac-man\Images\-NickDroite.png")
            if event.key == pygame.K_DOWN: # on déplace le vaisseau de 1 pixel vers le bas
                player.sens = "bas"
                player.image=pygame.image.load("Projet Pac-man\Images\-NickBas.png")
            if event.key == pygame.K_UP: # on déplace le vaisseau de 1 pixel vers le haut
                player.sens = "haut"
                player.image=pygame.image.load("Projet Pac-man\Images\-NickHaut.png")
        # musique
            if event.key == pygame.K_m:
                pygame.mixer.music.load("Projet Pac-man\Sons\Giorno_JJBA.mp3")
                pygame.mixer.music.play()
    ### Actualisation de la scene ###
    # collisions
    "collision=maze.burgers.get_rect()"
    "if collision.colliderect(player.rect)==False:"
    player.deplacer()
    screen.blit(maze.image_surf,[player.rect.x,player.rect.y]) # appel de la fonction qui dessine le joueur
    maze.draw(screen, maze._block_surf) # on dessine le labyrinthe 
    maze.draw2(screen, maze.burgers)
    maze.draw3(screen, maze.coca)
    pygame.display.update() # pour ajouter tout changement à l'écran
    clock.tick(FPS)