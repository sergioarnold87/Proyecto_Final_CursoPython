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

    # funcioanlidades sobre la extracción aleatoria
    def takeRandomPawn(self):
      """
      Toma una ficha de la bolsa de forma aleatoria y la elimina de la bolsa
      """
      from numpy import random
        idx = random.randint(0, len(self.letters) - 1)
        letter = self.letters[idx]
        self.letters.remove(letter)
     return letter

class Word:

    def __init__(self):
        self.word = []

    def __str__(self):
        """
        Imprimimos la palabra en formato string
        """
        string = ""
        for i in range(len(self.word)):
            string += self.word[i]
        return string

    def areEqual(self, w):
        """
        Comprueba si dos palabras son iguales
        """
    return self.word == w.word

    def isEmpty(self):
        """
        Comprueba si una palabra es vacías
        """
    return len(self.word) == 0

    @classmethod
    def readWord(cls):
        """
        Lee una palabra por teclado y la devuelve como un objeto de la clase word
        """

        input_word = input().strip()
        w = Word()
        for c in input_word.upper():
            w.word.append(c)
        return w

    def readWordFromFile(f):
    """
    Lee una palabra del fichero f y la devuelve como un objeto de la clase word
    """
    word = Word()
    file_word = f.readline()
    # Consideramos toda la línea salvo el salto de línea
    for c in file_word[:-1]:
        w.word.append(c)
    return word


# Clase Dictionary

class Dictionary:

    filepath = "/content/drive/MyDrive/Proyecto_Final_CursoPython/dictionary.txt"

    @staticmethod
    def validateWord(word):
        """
        Comprueba si la palabra word se encuentra en el diccionario
        """
        with open(Dictionary.filepath, "r") as f:
            w = Word.readWordFromFile(f)
            while (not w.isEmpty() and not word.areEqual(w)):
                w = Word.readWordFromFile(f)

        if w.isEmpty(): and not word.areEqual(w):
            print("La palabra no se encuentra en el diccionario")
            return False
        else:
            return True
