class Matrice:
    def __init__(self):
        pass

    # lignes ou col donnent le meme resultat
    @staticmethod
    def get_n(matrice):
        n = 0
        for row in range(len(matrice)):
            n += Matrice.get_total_row(matrice, row)
        return n

    @staticmethod
    def get_total_col(matrice, col):
        total = 0
        for i in range(len(matrice)):
            row = matrice[i]
            total += row[col]
        return total

    @staticmethod
    def get_total_row(matrice, row):
        total = 0
        for col in range(len(matrice[row])):
            total += matrice[row][col]
        return total
