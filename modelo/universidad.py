from modelo.estudiante import Estudiante
#Clase que representa a una universidad
class Universidad:
    #Método constructor
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.estudiantes: list = []
    
    """
    Métodos consultores
    """
    def get_nombre(self)->str:
        return self.nombre

    def get_estudiantes(self)->list:
        return self.estudiantes
    
    """
    Métodos modificadores
    """
    def set_nombre(self, nombre)->str:
        self.nombre = nombre

    def set_estudiantes(self, estudiantes):
        self.estudiantes = estudiantes

    #Consultar un estudiante
    def consultar_estudiante(self, cedula: str)->Estudiante:
        lista_filtro: list = list(filter(lambda est: est.get_cedula() == cedula, self.estudiantes))
        #Retornamos el primer elemento del filtro  de busqueda
        return lista_filtro[0]

    def agregar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    #UI
    #def ui(self):

"""
1 -> Crear estudiante
    >>> Nombre materia: --
    >>> Nota materia: --
"""