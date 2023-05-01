
def niveau(level):

    coeff_vert = 1
    coeff_rouge = 1
    coeff_noir = 1


    if level == 1:
        coeff_vert += 0.75
        coeff_rouge += 1.5
        coeff_noir += 3

        return coeff_vert, coeff_rouge, coeff_noir

    elif level == 2:
        coeff_vert += 0.45
        coeff_rouge += 0.9
        coeff_noir += 2
        return coeff_vert, coeff_rouge, coeff_noir

    else:
        return coeff_vert, coeff_rouge, coeff_noir