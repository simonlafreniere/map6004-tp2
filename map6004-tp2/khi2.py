from matrice import Matrice


class Khi2:
    def __init__(self):
        pass


def expected_matrice(originale):
    n = Matrice.get_n(originale)
    expected = []
    for row in range(len(originale)):
        originale_row = originale[row]
        expected_row = []
        for col in range(len(originale_row)):
            expected_value = Matrice.get_total_row(originale, row) * Matrice.get_total_col(originale, col) / n
            expected_row.append(expected_value)
        expected.append(expected_row)
    return expected
