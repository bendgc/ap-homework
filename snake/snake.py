# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

from random import randint
import pygame as pg

pg.init()
screen_width = 600
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()

def case_pix(x, y):
    return(x*20, y*20)

snake = [
    (10, 15),
    (11, 15),
    (12, 15),
]

fruit = (randint(0,29),randint(0,29))
# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
direction = (1,0)
sens = "droite"
score = 0
while running:
    
    clock.tick(5)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            elif event.key ==pg.K_UP and sens != "bas" :
                direction = (0,-1)
                sens = "haut"
            elif event.key == pg.K_DOWN and sens != "haut" :
                direction = (0,1)
                sens = "bas"
            elif event.key == pg.K_LEFT and sens != "droite" :
                direction = (-1,0)
                sens = "gauche"
            elif event.key == pg.K_RIGHT and sens != "gauche" :
                direction = (1,0)
                sens = "droite"
            
    #condition d'échec
    if ((snake[-1][0] + direction[0])%30,(snake[-1][1] + direction[1])%30) in snake :
        snake = [(10, 15), (11, 15), (12, 15)]
        score = 0
    
    # calcul de la nouvelle position du serpent
    snake[:-1] = snake[1:]
    snake[-1] = ((snake[-1][0] + direction[0])%30,(snake[-1][1] + direction[1])%30)
    
    
    #vérification des contacts avec le fruit
    if snake[-1] == fruit :
        snake +=[fruit]
        fruit = (randint(0,29),randint(0,29))
        score +=1
    
    #dessin du damier
    for x in range(0,30):
        for y in range(0,30) :
            case = case_pix(x, y)
            rect = pg.Rect(*case, 20, 20)
            pg.draw.rect(screen,[(x+y)%2*255]*3, rect)
    

    #dessin du serpent
    for coord in snake :
        case = case_pix(coord[0],coord[1])
        rect = pg.Rect(*case,20,20)
        pg.draw.rect(screen,[250,250,0],rect)
    
    #dessin du fruit
    case = case_pix(fruit[0],fruit[1])
    rect =  pg.Rect(*case,20,20)
    pg.draw.rect(screen,[250,0,0],rect)

    #score
    pg.display.set_caption(f"Score: {score}")

    pg.display.update()

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()

