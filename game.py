import pygame as pg
from settings import * 
import sys

class Game : 

    def __init__(self):
        pg.init() # j'initialise un objet pg
        self.window = pg.display.set_mode((S_W, S_H)) # je definie la taille de la fenetre du jeu
        pg.display.set_caption("Tuto")

        self.Back_ground_image = pg.image.load('spaceèback_ground.jpg')
        self.Back_ground = pg.transform.scale(self.Back_ground_image, (S_W, S_H))

        self.FIRST_SPACSHIP_IMAGE = pg.image.load('SS1.ico')
        self.FIRST_SPACSHIP = pg.transform.rotate(pg.transform.scale(self.FIRST_SPACSHIP_IMAGE, SPACE_SHIPS_DIMENSIONS), -90)
        self.P1 = pg.Rect(100, 300, SPACE_SHIPS_DIMENSIONS[0], SPACE_SHIPS_DIMENSIONS[-1])

        self.SECOND_SPACESHIP_IMAGE = pg.image.load('SS2.ico')
        self.SECOND_SPACESHIP = pg.transform.rotate(pg.transform.scale(self.SECOND_SPACESHIP_IMAGE, SPACE_SHIPS_DIMENSIONS), 90)
        self.P2 = pg.Rect(1100,300, SPACE_SHIPS_DIMENSIONS[0], SPACE_SHIPS_DIMENSIONS[1])
    
    def ai_player(self):
        """ cette fonction rendra le joueur adversaire dynamique : c'est le deuxieme joueur qui jouera contre l'utilisateur """
        pass

    def run(self):
        clock = pg.time.Clock()
        run = True 
        while run :
            clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            self.white_font_style()
            self.add_players()
            pg.display.update()
            
            # handle mouvements
            keys_pressed = pg.key.get_pressed()
            if keys_pressed[pg.K_q] : # LEFT
                new = self.P1.x - VEL
                if new >=0:
                    self.P1.x = new
            if keys_pressed[pg.K_d] : # RIGHT 
                new = self.P1.x + VEL
                if new + SPACE_SHIPS_DIMENSIONS[-1] <= S_W:
                    self.P1.x = new 
            if keys_pressed[pg.K_z] : 
                new  = self.P1.y - VEL
                if new >= 0:
                    self.P1.y = new
            if keys_pressed[pg.K_s] : 
                new = self.P1.y + VEL
                if new + SPACE_SHIPS_DIMENSIONS[0] <= S_H:
                    self.P1.y = new
        pg.quit()
    
    def white_font_style(self):
        #self.window.fill(WHITE)
        # add something 
        self.window.blit(self.Back_ground, (0, 0))

    def add_players(self):
        self.window.blit(self.FIRST_SPACSHIP, (self.P1.x, self.P1.y))
        self.window.blit(self.SECOND_SPACESHIP, (self.P2.x, self.P2.y))

if __name__ == "__main__" : 
    new_window  = Game()
    new_window.run()

    