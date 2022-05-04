class Integrante:
    __idProyecto = None
    __apellidoNombre =  None
    __dni = None
    __categoriaInvestigacion = None
    __rol = None

    def __init__(self, idproyecto = None, nombre = None, dni = None, categoria = None, rol = None):
        self.__idProyecto = idproyecto
        self.__apellidoNombre = nombre
        self.__dni = dni
        self.__categoriaInvestigacion = categoria
        self.__rol = rol
    
    def getID(self):
        return self.__idProyecto

    def getRol(self):
        return self.__rol

    def getCategoria(self):
        return self.__categoriaInvestigacion


    def __str__(self):
        return 'ID de Proyecto: {}\nApellido y Nombre: {}\nDNI:{}\nCategoria de Investigacion: {}\nROL:{}\n' .format(self.__idProyecto,self.__apellidoNombre,self.__dni,self.__categoriaInvestigacion,self.__rol)
            

