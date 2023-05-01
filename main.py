import pygame
import math
from module import vecteur, have_indice
import time
from classe import Skieur

#############################################
# Classe
pygame.init()
clock = pygame.time.Clock()
#############################################

#############################################
# Variable globale
BACKGROUND = '#EEEDDA'
LARGEUR = 1000
HAUTEUR = 600
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR), )
ecran.fill(BACKGROUND)
FONT = 'font/Daydream.ttf'
numero_ecran = 0
continuer = True
#############################################

#############################################
# Entité
carte = pygame.image.load('sprite/courchevel.png').convert_alpha()
graphe = pygame.image.load('sprite/all.png').convert_alpha()

debutant = Skieur.Skieur('Débutant', 'sprite/debutant.png', 50, ecran, 1, 'Merlet', 'Tania')
intermediaire = Skieur.Skieur('Intermédiaire', 'sprite/intermediaire.png', 50, ecran, 2, 'Merlet', 'Tania')
professionnel = Skieur.Skieur('Professionnel', 'sprite/pro.png', 50, ecran, 3, 'Merlet', 'Tania')

all_skieur = [debutant, intermediaire, professionnel]
#############################################

for skieur in all_skieur:

    if len(skieur.cheminement) == 0:
        skieur.cheminement.append(skieur.lieu)

    skieur.reinitialisation()

#############################################
# Boucle principale
while continuer:

    clock.tick(30)

    if numero_ecran >= 1:

        if numero_ecran == 1:

            pave = []

            font_tex = pygame.font.SysFont(FONT, 30)

            texte1 = font_tex.render('Une course entre informaticiens a lieu :', False, 'black')
            pave.append(texte1)

            texte2 = font_tex.render('- Ils sont tous diplômés d\'un Master en algorithme et ont'
                                     ' écouté leurs cours de L2', False, '#EC0000')
            pave.append(texte2)

            texte3 = font_tex.render('- Ils connaissent par coeur'
                                     ' les algorithmes de plus court chemin', False, 'black')
            pave.append(texte3)

            texte4 = font_tex.render('- Après avoir minutieusement étudié le terrain, ils se mirent'
                                     ' à construire un graphe valué', False, 'black')
            pave.append(texte4)

            texte5 = font_tex.render('Se rappelant de leurs incroyables années de licence ainsi'
                                     ' que de leurs éminents professeurs', False, 'black')
            pave.append(texte5)

            texte6 = font_tex.render('Ils ne pouvaient pas se tromper !', False, 'black')
            pave.append(texte6)

            texte7 = font_tex.render('Cependant ils avaient tous un niveau de ski différent ...', False, '#1AA474')
            pave.append(texte7)

            texte8 = font_tex.render('L\'un était encore débutant, l\'autre était intermédiaire'
                                     ' et le dernier professionnel', False, '#1AA474')
            pave.append(texte8)

            texte9 = font_tex.render('Qui des trois va gagner ? ', False, 'black')
            pave.append(texte9)

            correction = 0
            for ligne in pave:
                ecran.blit(ligne, (50, 70 + correction))
                correction += 50
                del ligne

        elif numero_ecran == 2:

            ecran.fill(BACKGROUND)
            ecran.blit(carte, (0, -80))
            ecran.blit(graphe, (0, -80))

            for skieur in all_skieur:

                if skieur.course < skieur.vitesse:

                    skieur.course += 1

                    if skieur.course == skieur.vitesse:

                        skieur.changer_coord(
                            skieur.position[skieur.cheminement[skieur.progression]][0] - 15,
                            skieur.position[skieur.cheminement[skieur.progression]][1] - 20)

                        skieur.lieu = skieur.cheminement[skieur.progression]
                        skieur.progression += 1

                        if skieur.progression < len(skieur.cheminement):

                            skieur.course = 0

                            skieur.changer_coord(skieur.position[skieur.lieu][0] - 15,
                                                 skieur.position[skieur.lieu][1] - 20)

                            skieur.vitesse = math.ceil(skieur.matrice_distance[have_indice.name_to_indice(
                                skieur.lieu), have_indice.name_to_indice(
                                skieur.cheminement[skieur.progression])] * 5)

                            skieur.mouvement_x, skieur.mouvement_y = vecteur.mouvement(
                                skieur.position[skieur.lieu],
                                skieur.position[skieur.cheminement[skieur.progression]],
                                skieur.vitesse)

                        else:
                            skieur.mouvement_x = 0
                            skieur.mouvement_y = 0
                            skieur.termine = True

                skieur.mouvement(skieur.mouvement_x, skieur.mouvement_y)

            if all_skieur[0].progression < len(all_skieur[0].cheminement):
                font = pygame.font.SysFont(FONT, 25)
                trajet = f"{all_skieur[0].prenom} prenez " \
                         f"{all_skieur[0].matrice_structure[have_indice.name_to_indice(all_skieur[0].lieu), have_indice.name_to_indice(all_skieur[0].cheminement[all_skieur[0].progression])]}" \
                         f" vers " \
                         f"{all_skieur[0].cheminement[all_skieur[0].progression]}" \
                         f" pendant " \
                         f"{all_skieur[0].matrice_distance[have_indice.name_to_indice(all_skieur[0].lieu), have_indice.name_to_indice(all_skieur[0].cheminement[all_skieur[0].progression])]}" \
                         f" minutes"
                trajet = font.render(trajet, True, 'black')

                ecran.blit(trajet, (40, 550))

            termine = 0

            for skieur in all_skieur:

                if skieur.termine:
                    termine += 1

            if termine == len(all_skieur):
                time.sleep(1)
                ecran.fill(BACKGROUND)
                numero_ecran += 1

        elif numero_ecran == 3:

            font = pygame.font.SysFont(FONT, 25)
            correction = 5

            for elem in debutant.trajet_total:

                ss_trajet = font.render(elem, False, '#AB9203')
                ecran.blit(ss_trajet, (50, 50 + correction))

                correction += 30

            correction = 5

            for elem in intermediaire.trajet_total:

                ss_trajet = font.render(elem, False, '#019C3A')
                ecran.blit(ss_trajet, (500, 50 + correction))

                correction += 30

            texte = font.render('Appuyez sur ESPACE pour voir le parcours du gagnant !', False, '#ED800C')

            ecran.blit(texte, (300, 500))

        elif numero_ecran == 4:

            font = pygame.font.SysFont(FONT, 30)
            correction = 5

            for elem in professionnel.trajet_total:

                ss_trajet = font.render(elem, False, '#ED800C')
                ecran.blit(ss_trajet, (270, 80 + correction))

                correction += 30

    else:

        my_font = pygame.font.SysFont(FONT, 80)
        name_surface = my_font.render('Une course à Courch ?', True, (0, 0, 0))

        font = pygame.font.SysFont(FONT, 30)
        texte = font.render('Suivant avec ESPACE et Précédent avec ECHAP', True, (0, 0, 0))

        ecran.blit(name_surface, (200, HAUTEUR // 2 - 100))
        ecran.blit(texte, (250, 500))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            continuer = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                numero_ecran += 1
                ecran.fill(BACKGROUND)

                if numero_ecran == 2:

                    for skieur in all_skieur:
                        skieur.reinitialisation()

                elif numero_ecran == 5:
                    continuer = False

            elif event.key == pygame.K_ESCAPE:
                numero_ecran -= 1
                ecran.fill(BACKGROUND)

                if numero_ecran == -1:
                    continuer = False

                elif numero_ecran == 2:

                    for skieur in all_skieur:
                        skieur.reinitialisation()

    pygame.display.flip()

pygame.quit()
