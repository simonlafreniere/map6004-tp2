class Vecteur:
    @staticmethod
    def get_n(vecteur):
        n = 0
        for i in range(len(vecteur)):
            n += vecteur[i]
        return n

    @staticmethod
    # normalisation (total = 1)
    def normalize(vector):
        result = []
        n = Vecteur.get_n(vector)
        for i in range(len(vector)):
            result.append(vector[i] / n)
        return result

    # @staticmethod
    # def get_total_row(vector):
    #     total = 0
    #     for col in range(len(vector)):
    #         total += vector[col]
    #     return total
