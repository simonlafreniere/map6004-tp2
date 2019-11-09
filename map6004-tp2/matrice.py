class Matrice:
    def __init__(self):
        pass


# lignes ou col donnent le meme resultat
def get_n(matrice):
    n = 0
    for i in range(len(matrice)):
        n += get_total_row(i)
    return n


def get_total_col(matrice, col):
    total = 0
    for i in range(len(matrice)):
        row = matrice[i]
        total += row[col]
    return total


def get_total_row(matrice, row):
    total = 0
    vector = matrice[row]
    for i in range(len(vector)):
        total += vector[i]
    return total