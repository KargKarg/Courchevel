

def pos(path):
    position = {}
    with open(path) as filin:
        ligne = filin.readline()
        while ligne != '':
            position[ligne.split()[0]] = [int(ligne.split()[1]) - 40, int(ligne.split()[2])]
            ligne = filin.readline()
    return position