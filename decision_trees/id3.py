import math
from collections import Counter

values = {
  "outlook" : ["Sunny", "Overcast", "Rain"],
  "temperature" : ["Hot", "Mild", "Cool"],
  "humidity" : ["High", "Normal"],
  "wind" : ["Weak", "Strong"],
  "play_tennis" : [ 0, 1]
}


training_X = [
  [ 1, "Sunny", "Hot" , "High" ,"Weak",0],
  [ 2, "Sunny", "Hot" , "High" ,"Strong", 0],
  [ 3, "Overcast", "Hot" , "High" ,"Weak",1],
  [ 4, "Rain", "Mild" , "High" ,"Weak",1],
  [ 5, "Rain", "Cool" , "Normal" ,"Weak",1],
  [ 6, "Rain", "Cool" , "Normal" ,"Strong",0],
  [ 7, "Overcast", "Cool" , "Normal" ,"Strong",1],
  [ 8, "Sunny", "Mild" , "High" ,"Weak",0],
  [ 9, "Sunny", "Cool" , "Normal" ,"Weak",1],
  [ 10, "Rain", "Mild" , "Normal" ,"Weak",1],
  [ 11, "Sunny", "Mild" , "Normal" ,"Strong",1],
  [ 12, "Overcast", "Mild" , "High" ,"Strong",1],
  [ 13, "Overcast", "Hot" , "Normal" ,"Weak",1],
  [ 14, "Rain", "Mild" , "High" ,"Strong",0]
]

training_Y = [[0,0,1,1,1,0,1,0,1,1,1,1,1,0]]


def entropy(possible_values, data, col=5):
  cuentas = Counter(data[col])
  entropia = 0
  for value in possible_values:
    entropia = entropia - (cuentas[value]/len(data[col])) * math.log(cuentas[value]/len(data[col]), 2)

  return entropia

def gain(X, values, attribute):
    suma_entropias = 0
    for value in values[attribute]:
        

def obtenemos_best_attribute(X, values):
    entropia = entropy(values["play_tennis"], X)
    max_gain = 0
    for attr in values.iteritems():
        new_gain = gain(X, values, attr)
        if new_gain > max_gain:
            max_gain = new_gain

def id3(X, values, nivel):
    best_attribute, pos_best_attribute, gain = obtenemos_best_attribute(values) # Con el calculo del inf. gain
    print("{} {} ({})".format('-'*(nivel+1), best_attribute, gain))
    for possible_value in values[best_attribute]:
        X_filtrado = X.filter(lambda x: x[pos_best_attribute] == possible_value)
        entropia = entropy(values["play_tennis"], X_filtrado)
        if entropia != 0:
            values.pop(best_attribute)
            id3(X_filtrado, values, nivel+1)
        elif len(values) == 2:
            print("{} ?".format(possible_value))
        else:
            print("{} {} ({})".format("*"*(nivel+1), X_filtrado[5], entropia))




def main():
  #print(entropy(values["play_tennis"], training_Y))
  id3(training_X, values, 0)

if __name__ == '__main__':
    main()
