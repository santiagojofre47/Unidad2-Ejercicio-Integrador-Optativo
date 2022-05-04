from manejadorIntegrantes import manejadorIntegrantes
from ManejadorProyecto import manejadorProyecto

if __name__ == '__main__':
    unManejadorProyecto = manejadorProyecto()
    unManejadorIntegrante = manejadorIntegrantes(5)
    unManejadorProyecto.leerArchivo()
    unManejadorIntegrante.leerArchivo()
    unManejadorProyecto.calcularPuntaje(unManejadorIntegrante)
    unManejadorProyecto.mostrarRanking()
