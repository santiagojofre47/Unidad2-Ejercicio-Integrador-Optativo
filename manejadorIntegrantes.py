import numpy as np
import csv
from claseIntegrante import Integrante


class manejadorIntegrantes:
    __cantidad = None
    __dimension = None
    __incremento = None

    def __init__(self, dimension, incremento = 5):
        self.__integrantes = np.empty(dimension, dtype = Integrante)
        self.__dimension = dimension
        self.__cantidad = 0
        self.__incremento = incremento

    def agregarIntegrante(self,unIntegrante):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__integrantes.resize(self.__dimension)
        self.__integrantes[self.__cantidad] = unIntegrante
        self.__cantidad += 1

    def leerArchivo(self):
        archivo = open('integrantesProyecto.csv')
        reader = csv.reader(archivo,delimiter=';') 
        band = False
        for fila in reader:
            if not band:
                band = True
            else:
                unIntegrante = Integrante(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregarIntegrante(unIntegrante)
        archivo.close()

    def __str__(self):
        s = ''
        for i in range(self.__cantidad):
            s+= str(self.__integrantes[i])+'\n'
        return s

    def HayDirector(self, idproyecto):
        i = 0
        encontro = False
        while i < self.__cantidad and not encontro:
            if self.__integrantes[i].getID() == idproyecto:
                if self.__integrantes[i].getRol() == 'director':
                    encontro = True
                    return True
                else:
                    i+=1
            else:
                i+=1
        if not encontro:
            return False 

    def HayCoDirector(self, idproyecto):
        i = 0
        encontro = False
        while i < self.__cantidad and not encontro:
            if self.__integrantes[i].getID() == idproyecto:
                if self.__integrantes[i].getRol() == 'codirector':
                    encontro = True
                    return True
                else:
                    i+=1
            else:
                i+=1
        if not encontro:
            return False                                 


    def getCantidadIntegrantes(self, idproyecto):
        i = 0
        cantidad = 0
        while i < self.__cantidad:
            if self.__integrantes[i].getID() == idproyecto:
                cantidad+=1
                i+=1
            else:
                i+=1 
        return cantidad              

    def getCategoriaDirector(self, idproyecto):
        encontro = False
        i = 0
        while i < (self.__cantidad) and not encontro:
            if self.__integrantes[i].getID() == idproyecto:
                if (self.__integrantes[i].getCategoria() == 'I' or self.__integrantes[i].getCategoria() == 'II') and self.__integrantes[i].getRol() == 'director':
                    encontro = True
                    return True    
                else:
                    i+=1
            else:
                i+=1        

        if  not encontro:
            return False

    def getCategoriaCoDirector(self, idproyecto):
        i = 0
        encontro = False
        while i < self.__cantidad and not encontro:
            if self.__integrantes[i].getID() == idproyecto:
                if (self.__integrantes[i].getCategoria() == 'I' or self.__integrantes[i].getCategoria() == 'II' or self.__integrantes[i].getCategoria() == 'III') and self.__integrantes[i].getRol() == 'codirector':
                    encontro = True
                    return True
                else:
                    i+=1
            else:
                i+=1       
                    
        if not encontro:
            return False        
