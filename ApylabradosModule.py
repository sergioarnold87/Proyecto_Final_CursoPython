class Pawns:

  def __init__(self):
    self.letters = []


  def addPawn(self, c):
    """
    Añade una ficha c al array de caracteres letters
    """
    self.letters.append(c)


  def addPawns(self, c, n):
    """
    Añade n veces una ficha c al array de caracteres letters
    """
    for i in range(n):
        self.addPawn(c)


  def createBag(self):
    """
    Crea la bolsa con las 100 fichas del juego
    """
    import pandas as pd
    filepath = 'bag_of_pawns.csv'
    bag = pd.read_csv(filepath)
    for item in bag.itertuples():
      self.addPawns(item[1], item[2])


  def showPawns(self):
    """
    Muestra las fichas que contiene la bolsa y el número de veces que está repetida cada ficha
    """
    counted = []
    for c in self.letters:
      if c not in counted:
        counted.append(c)
        print("{}: {}".format(c, self.letters.count(c)))


  def takeRandomPawn(self):

  """
  Toma una ficha de la bolsa de forma aleatoria y la elimina de la bolsa
  """
  from numpy import random
  idx = random.randint(0, len(self.letters) - 1)
  letter = self.letters[idx]
  self.letters.remove(letter)
  return letter
