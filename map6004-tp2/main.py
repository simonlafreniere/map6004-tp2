from excell_file_extration import ExcellExtractor
from matrice import Matrice
from khi2 import Khi2

if __name__ == "__main__":
    loc = "data.xlsx"
    extractor = ExcellExtractor(loc)
    matrice_originale = extractor.extract_matrix()
    matrice_expected = Khi2.expected_matrice(matrice_originale)

    test = ""
