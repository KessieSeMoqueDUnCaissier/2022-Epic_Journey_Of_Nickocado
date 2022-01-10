# Progression du projet "The Epic Journey Of Nickocado":
![shang-bai-tik-tok](https://user-images.githubusercontent.com/90514084/147883984-15281970-8ee2-4591-aaaf-4a575d3c9c84.gif)


### 13/12/2021:

  -Début du projet "The Epic Journey of Nickocado" ✅
  
  -Création de la classe Joueur avec toutes les méthodes qui vont avec. ✅
  
  -Création de la classe Ennemi avec toutes les méthodes qui vont avec. ✅
  
  -Mise en place de la musique de jeu et des sons ✅
  
 
### 15/12/2021 

  -Mise en place de la collision joueur/ennemi, qui conduit à la perte d'une vie. ✅
  
  -Création du labyrinthe ✅
  
  -Collision des murs du labyrinthe avec le joueur ou l'ennemi ⭕
  
  
### 18/12/2021

  -Collision des murs du labyrinthe avec le joueur ou l'ennemi ⭕
  
  -Dessin des burgers et des cocas dans le labyrinthe ✅
  
  -Mise en place d'un système de Game Over ⭕
    
    
### 27/12/2021

  -Collision des murs du labyrinthe avec le joueur ou l'ennemi: ✅
  
      Solution: Prendre en compte les positions du joueur/ennemi et 
                voir si chaque élément de la liste entre en collision avec ces derniers. 
                Si collision, le joueur/ennemi bloque et se retrouve à sa position initiale.
                (FORUM)
       
  -Problèmes de hitbox à régler: le joueur se téléporte derrière les murs: ✅
  
      Solution: Affecter l'ancienne position dans la boucle de jeu afin qu'elle s'actualise en temps réel
      
  -Problèmes de hitbox à régler: l'ennemi se téléporte parfois derrière les murs ⭕
     
     
### 28/12/2021

  -Collision avec les burgers, et les cocas: ✅
  
    Solution: Fonction collision prenant en compte la position du joueur dans le niveau et crée un rectangle sur ce dernier.
              Parcourt une liste de rectangles voisins et vérifie si chaque élément de la liste 
              rentre en collision avec le rectangle du joueur.
              Renvoie alors True en cas de collision et False dans le cas contraire.
              Si True pour les burgers, le joueur marque. Si True pour le coca, le joueur devient invincible
               
  -Invincibilité du joueur si consommation de coca: ✅
  
     Problème: Si on s'inspire de Pacman, l'invincibilité est temporaire --> Solution: faire appel au module Time
               Abandon de la solution car ralentissement du programme et bien trop dure à manier.
     Solution: Octroyer la possibilité au joueur de tuer au maximum que 2 ennemis si consommation de coca.
        
  -Image de l'ennemi changeant en fonction du coca (pour savoir si le joueur est toujours invincible) ✅
  
  -Ajout des points si les ennemis meurent ✅
  
  -Problèmes de hitbox à régler: l'ennemi se téléporte parfois derrière les murs ⭕
  
  
### 01/01/2022 

  -Disparition du burger ou coca lorsque consommé ⭕
  
  -Reprise du Game Over: ⭕
  
    Affiche le score de fin
    Met une image de fin:
    
      Problème: Le joueur peut toujours se déplacer et marquer des points.
      Solution: Mettre sa vitesse à 0 si sa vie est à 0 ou moins (en cas où 2 ennemis touchent le joueur lorsqu'il a une vie)
      
    Affiche le record de jeu
 
 -Problèmes de hitbox à régler: l'ennemi se téléporte parfois derrière les murs ⭕
 
 
### 02/01/2022

  -Disparition du burger ou coca lorsque consommé ⭕
  
  -Problèmes de hitbox à régler: l'ennemi se téléporte parfois derrière les murs ⭕
  
  -Game Over: ✅
  
    Afficher le record --> création d'un fichier .txt dans lequel on place le score du joueur si le fichier est vide; 
                            sinon si le contenu du fichier str (converti en int) est inférieur au score actuel, 
                            le contenu se voit remplacer par le score actuel, et ainsi de suite...
                            
### 07/01/2022
    
  -Disparition du burger ou coca lorsque consommé ✅
  
  -Réapparition des produits consommés si le joueur est en vie et qu'il les a tous consommés (ou pas dans le cas du coca) ✅
