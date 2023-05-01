import pygame
import numpy as np
from module import have_pos, fill_mat, pcc_matrice, pcc, vecteur

class Skieur:

    position = have_pos.pos('data/positions.txt')
    termine = False

    def __init__(self, prenom, path, vitesse, ecran, niveau, lieu, destination):

        self.prenom = prenom
        self.font = pygame.font.SysFont("font/test.ttf", 20)
        self.affichage_prenom = self.font.render(prenom, False, 'black')

        self.lieu = lieu
        self.debut = lieu
        self.destination = destination

        self.niveau = niveau

        self.vitesse = vitesse
        self.course = 0
        self.progression = 0

        self.matrice_distance = np.full((67, 67), 10000)
        self.matrice_successeurs = np.empty((67, 67), dtype=object)
        self.matrice_structure = np.empty((67, 67), dtype=object)

        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))

        self.position_x = Skieur.position[self.lieu][0] - 15
        self.position_y = Skieur.position[self.lieu][1] - 20
        self.mouvement_x = 0
        self.mouvement_y = 0

        self.prenom_position_x = self.position_x
        self.prenom_position_y = self.position_y - 10

        self.ecran = ecran

        fill_mat.fill_mat(self.matrice_distance, self.matrice_successeurs, self.matrice_structure, 'data/vert.txt', 'data/rouge.txt',
                          'data/noir.txt', 'data/mecanique.txt', self.niveau)

        pcc_matrice.floyd_warshall(self.matrice_distance, self.matrice_successeurs)

        self.trajet_total, self.cheminement = pcc.plus_court_chemin(self.lieu, self.destination, self.matrice_distance, self.matrice_successeurs,
                                                          self.matrice_structure, self.prenom)
        self.trajet_total = self.trajet_total.split('/')


    def mouvement(self, decalage_x, decalage_y):

        self.position_x += decalage_x
        self.position_y += decalage_y
        self.prenom_position_x += decalage_x
        self.prenom_position_y += decalage_y

        self.ecran.blit(self.image, (self.position_x, self.position_y))
        self.ecran.blit(self.affichage_prenom, (self.prenom_position_x, self.prenom_position_y))


    def affichage(self):

        self.ecran.blit(self.affichage_prenom, (self.prenom_position_x, self.prenom_position_y))

        self.ecran.blit(self.image, (self.position_x, self.position_y))


    def changer_coord(self, coord_x, coord_y):

        self.position_x = coord_x
        self.position_y = coord_y

        self.affichage()

    def reinitialisation(self):

        self.lieu = self.debut

        self.termine = False

        self.course, self.progression = 0, 0
        self.vitesse = 50
        self.position_x = self.position[self.lieu][0] - 15
        self.position_y = self.position[self.lieu][1] - 20
        self.prenom_position_x = self.position_x
        self.prenom_position_y = self.position_y - 10

        self.mouvement_x, self.mouvement_y = vecteur.mouvement(self.position[self.lieu], self.position[
            self.cheminement[self.progression]], self.vitesse)

        self.prenom_position_x = self.position_x
        self.prenom_position_y = self.position_y - 10