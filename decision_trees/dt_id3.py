from numpy import genfromtxt
import math
from collections import Counter

VALORES_OUTLOOK = {
    1 : "Sunny", 2: "Overcast", 3:"Rain"
}
VALORES_TEMPERATURE={
    1: "Hot", 2: "Mild", 3:"Cold"
}
VALORES_HUMIDITY={1:"High", 2:"Normal"}
VALORES_WIND={1:"Weak", 2: "Strong"}
VALORES_Y = {1: "Yes", 2: "No"}

"""
Calculo de la entropia de un dataset. El 5to indice corresponde a Y
"""
def entropia(data, col=4):
    cuentas = Counter(data[col])
    entropia = 0
    for valor in cuentas.keys():
        entropia = entropia - (cuentas[valor]/len(data[col])) * math.log(cuentas[valor]/len(data[col]), 2)

    return entropia

"""
Calculo del information gain que es la sumatoria de la entropia de la data ya filtrada
(en relacion a Y) multiplicada por la cantidad de datos filtrados por el valor sobre el total.
"""
def gain(data, indice_campo):
    entropia_total = entropia(data)
    cuentas = Counter(data[indice_campo])

    suma_entropia_valores = 0
    for valor in cuentas.keys():
        data_filtrada = data[:, data[indice_campo] == valor] # Filtramos la data por el valor
        coef = len(data_filtrada[indice_campo]) / len(data[indice_campo])
        #print(data)
        #print(data_filtrada)
        #print(entropia(data_filtrada))
        suma_entropia_valores = suma_entropia_valores + coef * entropia(data_filtrada)
    return entropia_total - suma_entropia_valores

def obtener_best_attribute(X, campos):
    mayor = 0
    for i in campos:
        ganado = gain(X, i)
        if ganado > mayor:
            mayor = ganado

    return mayor

def id3(X, campos, nivel):
    pos_best_attr = obtener_best_attribute(X, campos)
    best_attr = campos.pop(int(pos_best_attr))
    print("{} Nodo {}".format("-"*(nivel+1), best_attr))
    cuentas = Counter(X[best_attr])
    for valor in cuentas.keys():
        data_filtrada = X[:, X[best_attr] == valor]
        entropia_valor = entropia(data_filtrada)
        if entropia_valor == 0:
            print("{} Valor {}  {} <-- hoja".format("*"*(nivel+1), valor, data_filtrada[4,0]))
        elif len(campos) == 1:
            print("{} Valor {} ???".format("*"*(nivel+1), valor))
        else:
            id3(data_filtrada, campos, nivel+1)


def main():
    training_data = genfromtxt("data.csv", delimiter=',')
    #print( entropia(training_data, 0))

    #print(gain(training_data, 0))
    #print(gain(training_data, 1))
    #print(gain(training_data, 2))
    #print(gain(training_data, 3))
    id3(training_data, [0,1,2,3], 0)



if __name__ == '__main__':
    main()
