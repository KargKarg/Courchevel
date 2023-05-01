import time

def floyd_warshall(matrice, successeurs):
    t1 = time.perf_counter()

    for k in range(len(matrice)):
        successeurs[k, k] = k
        for i in range(len(matrice)):
            for j in range(len(matrice)):
                if matrice[i, j] > matrice[i, k] + matrice[k, j]:
                    matrice[i, j] = matrice[i, k] + matrice[k, j]
                    successeurs[i, j] = successeurs[i, k]

    t2 = time.perf_counter()

    return t2 - t1

