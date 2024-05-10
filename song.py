
# Importar los módulos necesarios para la ejecución del programa.
from genre import GENRE
from datetime import *
class Song():
    """Constructor of the class.

        The constructor of the class Song is used to create a new song.

        Syntax
        ------
          song = Song(id, name, artist, duration, release_date, genres)

        Parameters
        ----------
          id : int
            The unique identifier of the song.
          name : str
            The name of the song.
          artist : str
            The artist of the song.
          duration : int
            The duration of the song in seconds.
          release_date : date
            The release date of the song.
          genres : list
            The genres of the song.

        Returns
        -------
          The new song.

        Example
        -------
          song = Song(1, "calorro", "estopa", 189, date.today(), [GENRE.POP])
        """
    #Realizar la implementación de la clase Song.
    def __init__(self,ID,nombre,artista,duracion,fecha_salida,genre):
      self.ID=ID
      self.nombre=nombre
      self.artista=artista
      self.duracion=duracion
      self.fecha_salida=fecha_salida
      self.genre=genre
      #getters
    def get_ID(self):
      if isinstance(self.ID,int):
        return self.ID
      else:
        raise TypeError('No es del entero')
    def get_Genre(self):
      if isinstance(self.genre,GENRE):
          return self.genre
      else:
          raise TypeError('No es del tipo GENRE')
    def get_nombre(self):
      if isinstance(self.nombre,str):
        return self.nombre
      else:
        raise TypeError('No es un nombre')
    def get_artista(self):
      if isinstance(self.artista,str):
        return self.artista
      else:
        raise TypeError('No es un nombre')
    def get_duracion(self):
      if isinstance(self.duracion,datetime):
          return self.duracion
      else:
          raise TypeError('No tiene una duracion')
    def get_fecha_salida(self):
      if isinstance(self.fecha_salida,time):
          return self.fecha_salida
      else:
          raise TypeError('No tiene un dia especifico')
      #setters
    def set_duracion(self,duracion):
      self.duracion=duracion
    def set_nombre(self,nombre):
      self.nombre=nombre
    def add_genre(self,genre):
        if not self.genre:
            return self.genre
        else:
            return f'ya tenemos un {self.genre}'
    def __eq__(self, other):#si es misma song
        if isinstance(other,Song):
          return self.ID == other.ID
        else:
          return f'no tiene mismo id no es la misma cancion'
    def __str__(self):
       return f'El nombre:{self.nombre}\nEl artista:{self.artista}\nLa id:{self.ID}\nLa duracion:{self.duracion}\nfecha de salida:{self.fecha_salida}'



def main():
    """Function main of the module.

    The function main of this module is used to test the Class Song.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a Song.")
    print("=================================================================.")
    song = Song(1, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if song.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_name() == "calorro":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_artist() == "estopa":
        print("Test PASS. The parameter artist has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_duration() == 189:
        print("Test PASS. The parameter duration has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_release_date() == date.today():
        print("Test PASS. The parameter release_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_genres() == [GENRE.POP]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    song2 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if str(song2) == "estopa tocando calorro durante 189 segundos.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(song2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(song2))


    print("=================================================================.")
    print("Test Case 3: song add_genre")
    print("=================================================================.")
    song2.add_genre(GENRE.ROCK)
    genres = song2.get_genres()
    if genres == [GENRE.POP, GENRE.ROCK]:
        print("Test PASS. The method add_genre(genre) has been implemented correctly.")
    else:
        print("Test FAIL. Check the method add_genre(genre), "+ " RESULT: " + str(genres))
    
    print("=================================================================.")
    print("Test Case 4: Test the method __eq__")
    print("=================================================================.")
    song3 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])
    if song2 == song3:
        print("Test PASS. The method __eq__ has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __eq__().")
    


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()