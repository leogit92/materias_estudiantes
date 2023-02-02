#Importa la clase Materia
from modelo.materia import Materia

#Clase que me representa a un estudiante
class Estudiante:
    #Método constructor
    def __init__(self, nombre: str, apellido: str, cedula: str, sexo: str) -> None:
        #Atributos de la clase
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.cedula: str = cedula
        self.sexo: str = sexo
        self.materias: list = []

    def __str__(self) -> str:
        str_estudiante: str = "Nombre: "+self.nombre+"\n"
        str_estudiante += "Apellido: "+self.apellido+"\n"
        str_estudiante += "Cédula: "+self.cedula+"\n"
        str_estudiante += "Sexo: "+self.sexo+"\n"
        str_estudiante += "-----------Materias-----------"
        #str_estudiante += "Materias: ".join(self.materias)
        str_estudiante += "-------------------------------"
        return str_estudiante
    
    """
    Métodos consultores
    """
    def get_nombre(self)->str:
        return self.nombre

    def get_apellido(self)->str:
        return self.apellido
    
    def get_cedula(self)->str:
        return self.cedula
    
    def get_sexo(self)->str:
        return self.sexo
    
    def get_materias(self)->list:
        return self.materias
    
    """
    Métodos modificadores
    """
    def set_nombre(self, nombre: str):
        self.nombre = nombre
    
    def set_apellido(self, apellido: str):
        self.apellido = apellido
    
    def set_sexo(self, sexo: str):
        self.sexo = sexo
    
    def set_materias(self, materias: list):
        self.materias = materias
    
    #Método para agregar una nueva materia
    def agregar_materia(self, nueva_materia: Materia):
        self.materias.append(nueva_materia)
    
    #Método para eliminar una materia
    def eliminar_materia(self, nombre_materia: str):
        #Filtrar la materia a eliminar
        lista_m_eliminar = list(filter(lambda materia: materia.get_nombre().lower() == nombre_materia.lower(), self.materias) )
        #Obtención del indice del objeto en la lista
        i = self.materias.index(lista_m_eliminar[0])
        #Eliminar el objeto con el indice obtenido de la lista
        self.materias.pop(i)

    #método convertir el objeto en un diccionario
    def convertir_a_diccionario(self):
        dict_estudiante: dict = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "cedula": self.cedula,
            "sexo": self.sexo
        }
        return dict_estudiante