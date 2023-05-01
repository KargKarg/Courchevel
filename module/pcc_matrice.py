from module import have_indice

def floyd_warshall(matrice, successeurs):
    for k in range(len(matrice)):
        successeurs[k, k] = have_indice.indice_to_name(k)
        matrice[k, k] = 0
        for i in range(len(matrice)):
            for j in range(len(matrice)):
                if matrice[i, j] > matrice[i, k] + matrice[k, j]:
                    matrice[i, j] = matrice[i, k] + matrice[k, j]
                    successeurs[i, j] = successeurs[i, k]

