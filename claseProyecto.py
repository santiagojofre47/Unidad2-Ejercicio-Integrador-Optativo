class Proyecto:
    __idProyecto = None
    __titulo = None
    __palabrasClave = None
    __puntaje = None

    def __init__(self, idproyecto = None, titulo = None, palabras = None):
        self.__idProyecto = idproyecto
        self.__titulo = titulo
        self.__palabrasClave = palabras
        self.__puntaje = 0

    def __str__(self):
        return 'ID de Proyecto: {} Titulo: {} Palabras clave: {} Puntaje: {}\n' .format(self.__idProyecto, self.__titulo, self.__palabrasClave, self.__puntaje)

    def getID(self):
        return self.__idProyecto      

    def SumarPuntos(self, puntos):
        if type(puntos) == int:
            self.__puntaje+= puntos

    def restarPuntos(self, puntos):
        if type(puntos) == int:
            self.__puntaje-=puntos    

   # def getPuntaje(self):
       # return self.__puntaje

    def __gt__(self, otroProyecto):
        if type(otroProyecto) == Proyecto:
            if self.__puntaje < otroProyecto.__puntaje:
                return True
            else:
                return False

                

      



    