def init_base():

    base_lieux = {
        'Merlet': 0,
        'Chanrossa': 1,
        'Signal': 2,
        'Praline': 3,
        'Mugnier': 4,
        'Bel-air': 5,
        'Stade': 6,
        'Bosse': 7,
        'Prameruel': 8,
        'Creux': 9,
        'Courchevel-1650': 10,
        'Creux-noirs': 11,
        'Vizelle': 12,
        'Pralong': 13,
        'Saulire': 14,
        'Verdons': 15,
        'Lac': 16,
        'Jardin': 17,
        'Courchevel-1550': 18,
        'Chenus': 19,
        'Loze-1': 20,
        'Loze-2': 21,
        'St-bon': 22,
        'Le-praz': 23,
        'Praz-juguet': 24,
        'Folyeres': 25,
        'Tania': 26
    }

    for i in range(1, 41):
        base_lieux[str(i)] = base_lieux['Tania'] + i


    return base_lieux