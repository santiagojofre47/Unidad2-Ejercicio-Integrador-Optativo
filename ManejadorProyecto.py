import csv
from claseProyecto import Proyecto
from manejadorIntegrantes import manejadorIntegrantes

class manejadorProyecto:
    __lista = []

    def __init__(self):
        self.__lista = []

    def agregarProyecto(self, unProyecto):
        if type(unProyecto) == Proyecto:
            self.__lista.append(unProyecto)

    def leerArchivo(self):
        archivo = open('proyectos.csv')
        reader = csv.reader(archivo,delimiter = ';')
        band = False
        for fila in reader:
            if not band:
                band = True
            else:
                unProyecto = Proyecto(fila[0],fila[1],fila[2])
                self.agregarProyecto(unProyecto)
        archivo.close()

    def __str__(self):
        s = ''
        for proyecto in self.__lista:
            s+=str(proyecto) + '\n'
        return s
    

    def calcularPuntaje(self, unManjadorIntegrantes):
        if type(unManjadorIntegrantes) == manejadorIntegrantes:
            for i in range(len(self.__lista)):
                if unManjadorIntegrantes.getCantidadIntegrantes(self.__lista[i].getID()) >= 3:
                    self.__lista[i].SumarPuntos(10)
                else:
                    self.__lista[i].restarPuntos(20)
                    print('El Proyecto debe tener como mínimo 3 integrantes.')

                if unManjadorIntegrantes.getCategoriaDirector(self.__lista[i].getID()):
                    self.__lista[i].SumarPuntos(10)
                else:
                    self.__lista[i].restarPuntos(5)
                    print('El Director del Proyecto debe tener categoría I o II.')

                if unManjadorIntegrantes.getCategoriaCoDirector(self.__lista[i].getID()):
                    self.__lista[i].SumarPuntos(10)
                else:
                    self.__lista[i].restarPuntos(5)
                    print('El Codirector del Proyecto debe tener como mínimo categoría III.')

                if not unManjadorIntegrantes.HayCoDirector(self.__lista[i].getID()):
                    self.__lista[i].restarPuntos(10)
                    print('El Proyecto debe tener un Director')

                if not unManjadorIntegrantes.HayDirector(self.__lista[i].getID()):    
                    self.__lista[i].restarPuntos(10)
                    print('El Proyecto debe tener un Codirector')
    
    def mostrarRanking(self):
       self.__lista.sort()
       for proyecto in self.__lista:
           print(proyecto)


if __name__ == '__main__':
    unManejador = manejadorProyecto()
    unManejador.leerArchivo()  
    unmanejador2 = manejadorIntegrantes(5)
    unmanejador2.leerArchivo()
    unManejador.calcularPuntaje(unmanejador2)
    unManejador.mostrarRanking()
    
    
    

