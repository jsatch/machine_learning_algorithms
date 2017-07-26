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
  [ 1, "Sunny", "Hot" , "High" ,"Weak"],
  [ 2, "Sunny", "Hot" , "High" ,"Strong"],
  [ 3, "Overcast", "Hot" , "High" ,"Weak"],
  [ 4, "Rain", "Mild" , "High" ,"Weak"],
  [ 5, "Rain", "Cool" , "Normal" ,"Weak"],
  [ 6, "Rain", "Cool" , "Normal" ,"Strong"],
  [ 7, "Overcast", "Cool" , "Normal" ,"Strong"],
  [ 8, "Sunny", "Mild" , "High" ,"Weak"],
  [ 9, "Sunny", "Cool" , "Normal" ,"Weak"],
  [ 10, "Rain", "Mild" , "Normal" ,"Weak"],
  [ 11, "Sunny", "Mild" , "Normal" ,"Strong"],
  [ 12, "Overcast", "Mild" , "High" ,"Strong"],
  [ 13, "Overcast", "Hot" , "Normal" ,"Weak"],
  [ 14, "Rain", "Mild" , "High" ,"Strong"]
]

training_Y = [[0,0,1,1,1,0,1,0,1,1,1,1,1,0]]




def entropy(possible_values, data, col=0):
  cuentas = Counter(data[col])
  entropia = 0
  for value in possible_values:
    entropia = entropia - (cuentas[value]/len(data[col])) * math.log(cuentas[value]/len(data[col]), 2)

  return entropia


def main():
  print(entropy(values["play_tennis"], training_Y))

main()
