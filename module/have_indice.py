from module import base_lieux

def name_to_indice(string):
    base = base_lieux.init_base()
    return base[string.capitalize()]

def indice_to_name(entier):
    base = base_lieux.init_base()
    key_val = list(base.items())
    return key_val[entier][0]
