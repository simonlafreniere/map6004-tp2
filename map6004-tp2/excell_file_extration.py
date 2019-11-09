import xlrd


class ExcellExtractor:
    def __init__(self, file):
        wb = xlrd.open_workbook(file)
        self.sheet = wb.sheet_by_index(0)

    # exclude ligne 1 et col 1 (noms)
    # ajoute totals
    def extract_matrix(self):
        matrice = []
        for i in range(1, self.sheet.nrows):
            row = []
            for j in range(1, self.sheet.ncols):
                row.append(self.sheet.cell_value(i, j))
            matrice.append(row)
        return matrice


    def get_total_row(self, row):
        total = 0
        for i in range(len(row)):
           total += row[i]
        return total


    def get_total_col(self, col):
        total = 0
        for i in range(len(col)):
            total += col[i]
        return total
