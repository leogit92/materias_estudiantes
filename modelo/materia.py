#Clase que representa a una materia
class Materia:
    #Método constructor
    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.calificacion: float = 0
    
    def __str__(self) -> str:
        materia_str: str = "Nombre: "+self.nombre+"\n"
        materia_str += "Calificación: "+str(self.calificacion)
        return materia_str
    
    """
    Métodos consultores
    """
    def get_nombre(self)->str:
        return self.nombre
    
    def get_calificacion(self)->float:
        self.calificacion
    
    """
    Métodos modificadores
    """
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_calificacion(self, calificacion):
        self.calificacion = calificacion