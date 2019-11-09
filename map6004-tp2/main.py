from excell_file_extration import ExcellExtractor

if __name__ == "__main__":
    loc = "data.xlsx"
    file = ExcellExtractor(loc)
    matrice = file.extract_matrix()

