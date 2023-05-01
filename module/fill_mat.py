from module import have_indice, niveau, code

def fill_mat(matrice_distance, matrice_successeurs, matrice_structure, vert, rouge, noir, mecanique, level):

    coeff_vert, coeff_rouge, coeff_noir = niveau.niveau(level)

    with open(vert, 'r') as filin:
        ligne = filin.readline().split()

        while ligne != []:
            if len(ligne) != 1:

                if matrice_distance[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] > int(ligne[2]) * coeff_vert:

                    matrice_distance[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] = int(ligne[2]) * coeff_vert

                    matrice_structure[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] = code.code_to_string(ligne[3])

                matrice_successeurs[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] = ligne[1]


            ligne = filin.readline().split()

    with open(rouge, 'r') as filin:
        ligne = filin.readline().split()

        while ligne != []:
            if len(ligne) != 1:
                if matrice_distance[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] > int(ligne[2]) * coeff_rouge:

                    matrice_distance[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] = int(ligne[2]) * coeff_rouge

                    matrice_structure[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] = code.code_to_string(ligne[3])

                matrice_successeurs[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] = ligne[1]


            ligne = filin.readline().split()

    with open(noir, 'r') as filin:
        ligne = filin.readline().split()

        while ligne != []:
            if len(ligne) != 1:
                if matrice_distance[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] > int(ligne[2]) * coeff_noir:

                    matrice_distance[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] = int(ligne[2]) * coeff_noir

                    matrice_structure[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] = code.code_to_string(ligne[3])

                matrice_successeurs[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] = ligne[1]


            ligne = filin.readline().split()

    with open(mecanique, 'r') as filin:
        ligne = filin.readline().split()

        while ligne != []:
            if len(ligne) != 1:
                if matrice_distance[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] > int(ligne[2]):

                    matrice_distance[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] = int(ligne[2])

                    matrice_structure[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] = code.code_to_string(ligne[3])

                matrice_successeurs[have_indice.name_to_indice(ligne[0]), have_indice.name_to_indice(ligne[1])] = ligne[1]


            ligne = filin.readline().split()

    for i in range(len(matrice_distance)):
        matrice_structure[i, i] = 'Rien'
