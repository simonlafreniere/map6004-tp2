from matrice import Matrice
from vecteur import Vecteur


class Khi2:
    # @staticmethod
    # def expected_matrice(originale):
    #     n = Matrice.get_n(originale)
    #     expected = []
    #     for row in range(len(originale)):
    #         expected_row = []
    #         for col in range(len(originale[row])):
    #             expected_value = Matrice.get_total_row(originale, row) * Matrice.get_total_col(originale, col) / n
    #             expected_row.append(expected_value)
    #         expected.append(expected_row)
    #     return expected

    # @staticmethod
    # def degres_liberte(matrice):
    #     return (len(matrice) - 1) * (len(matrice[0]) - 1)

    # @staticmethod
    # def chi2(originale, expected):
    #     rows = len(originale)
    #     cols = len(originale[0])
    #     x2 = 0
    #     for row in range(rows):
    #         for col in range(cols):
    #             x2 += (originale[row][col] - expected[row][col]) ** 2 / expected[row][col]
    #     return x2

    @staticmethod
    # distance entre 2 lignes
    # les vecteurs doivent etre normaliser premierement (total = 1)
    def distance(vecteur1, vecteur2):
        vect1 = Vecteur.normalize(vecteur1)
        vect2 = Vecteur.normalize(vecteur2)
        dist = 0
        for i in range(len(vecteur1)):
            # pas de division par zero..
            if vect1[i] == 0.0 and vect2[i] == 0.0:
                continue
            dist += (((vect1[i] - vect2[i]) ** 2) / (vect1[i] + vect2[i])) / 2
        return dist
