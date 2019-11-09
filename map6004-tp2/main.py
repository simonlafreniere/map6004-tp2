from excell_file_extration import ExcellExtractor
from khi2 import Khi2


def find_distance(matrice, row):
    dists = []
    for j in range(len(matrice)):
        dists.append(Khi2.distance(matrice[row], matrice[j]))
    return dists


if __name__ == "__main__":
    loc = "data.xlsx"
    extractor = ExcellExtractor(loc)
    matrice = extractor.extract_matrix()
    distances = []
    for i in range(len(matrice)):
        distances.append(find_distance(matrice, i))

    test = ""
