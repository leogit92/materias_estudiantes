from modelo.materia import Materia
from modelo.estudiante import Estudiante
from modelo.universidad import Universidad
import json
#Clase que me representa el controlador
class Controlador:
    #Método constructor
    def __init__(self) -> None:
        self.universidad: Universidad = Universidad('UTP')
        #self.cargar_estudiante()

    #método consultor
    def get_universidad(self):
        return self.universidad

    #Crear un estudiante
    def crear_estudiante(self, nombre, apellido, cedula, sexo) -> Estudiante:
        estudiante: Estudiante = Estudiante(nombre, apellido, cedula, sexo)
        self.universidad.agregar_estudiante(estudiante)
        return estudiante

    def crear_materias(self, nombre_materia: str, estudiante: Estudiante) -> Materia:
        #Construimos un objeto de tipo materia
        materia: Materia = Materia(nombre_materia)
        #Añadimos la materia al estudiante
        estudiante.agregar_materia(materia)
        return materia

    def asignar_nota_materia(self, calificacion: float, materia: Materia):
        materia.set_calificacion(calificacion)

    def guardar_estudiante(self, estudiante: Estudiante):
        var_est = []
        with open ("materias_estudiantes/modelo/universidad.json") as arch:
            recev = json.load(arch)
            if len(recev) > 0:
                for ind in recev:
                    var_est.append(ind)
            else:
                pass
        try:
            #Referenciamos un fichero
            with open("materias_estudiantes/modelo/universidad.json", "w") as archivo:
                #print(var_est)
                #Guardamos la información en el fichero
                #json.dump(estudiante.convertir_a_diccionario(), archivo)
                var_est.append(estudiante.convertir_a_diccionario())
                #print(var_est)
                json.dump(var_est, archivo)
        except:
            print("Error al guardar la información")

    def cargar_estudiante(self):
        try:
            #Referenciamos un fichero
            #with open("modelo/universidad.json") as archivo:
            with open("materias_estudiantes/modelo/universidad.json") as archivo:
                est_json = json.load(archivo)
                list_recv = []
                if len(est_json) > 0:
                    for est in est_json:
                        obj_estudiante: Estudiante = Estudiante(est["nombre"], est["apellido"], est["cedula"], est["sexo"])
                        list_recv.append(obj_estudiante.convertir_a_diccionario())

                    #print(list_recv)
                    #obj_estudiante: Estudiante = Estudiante(est_json["nombre"], est_json["apellido"], est_json["cedula"], est_json["sexo"])
                    #print(obj_estudiante)
                    return list_recv
                else:
                    pass
        except:
            print("Error al cagar la información")