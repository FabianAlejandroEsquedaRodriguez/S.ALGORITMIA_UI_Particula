import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):

    distancia = math.sqrt(pow( (x_2 - x_1), 2) + pow((y_2 - y_1), 2) )
    return distancia
    