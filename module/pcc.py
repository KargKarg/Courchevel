from module import have_indice

def plus_court_chemin(lieu, destination, matrice_distance, matrice_successeurs, matrice_structure, prenom):
    valeur_pcc = matrice_distance[have_indice.name_to_indice(lieu), have_indice.name_to_indice(destination)]

    cheminement = []

    chemin = ""
    actuel = lieu
    successeurs = matrice_successeurs[have_indice.name_to_indice(actuel), have_indice.name_to_indice(destination)]
    cpt = 1

    while actuel != destination:
        chemin += f"{cpt}) {successeurs} pour {matrice_distance[have_indice.name_to_indice(actuel), have_indice.name_to_indice(successeurs)]} minutes avec : {matrice_structure[have_indice.name_to_indice(actuel), have_indice.name_to_indice(successeurs)]}/"
        actuel = successeurs
        successeurs = matrice_successeurs[have_indice.name_to_indice(actuel), have_indice.name_to_indice(destination)]
        cpt += 1
        cheminement.append(actuel)

    chemin += f'Le trajet prendra à {prenom} en tout : {valeur_pcc} minutes'

    return chemin, cheminement
