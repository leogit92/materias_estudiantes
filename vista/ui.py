from controlador.controlador_univ import Controlador
#Clase que me representa la interfaz de usuario
class Ui:
    #Método constructor
    def __init__(self) -> None:
        self.controlador = Controlador()
        self.menu()

    def menu(self):
        print("--------------------------")
        print("1 --> Crear estudiante")
        print("2 --> Consultar estudiante")
        print("0 --> Salir")
        print("--------------------------")
        opc = int(input("Por favor ingrese una opcion: "))

        if opc == 1:
            #Solicitamos los datos al usuario
            """
            nombre_est: str = input("Por favor ingrese el nombre del estudiante: ")
            apellido_est: str = input("Por favor ingrese el apellido del estudiante: ")
            Cedula: str = input("Por favor ingrese la cédula del estudiante: ")
            sexo: str = input("Por favor ingrese el sexo del estudiante: ")
            """
            #Creamos el objeto estudiante con los datos por consola 
            obj_est = self.controlador.crear_estudiante("juan", "quintana", "123456", "M")
            self.controlador.guardar_estudiante(obj_est)
            #Obtenemos el nombre materia
            #nombre_materia: str = input(f"Materia a inscribir para {nombre_est}: ")
            #Creamos el objeto materia con el dato obtenido por consola
            #obj_materia = self.controlador.crear_materias(nombre_materia, obj_est)
            #Asignamos una nota
            #self.controlador.asignar_nota_materia(5, obj_materia)
        elif opc == 2:
            cedula: str = input("Ingrese la cédula del  estudiante: ")
            #Consultar estudiante
            est = self.controlador.get_universidad().consultar_estudiante(cedula)
            print(est)
            print("--------Materias--------")
            materias = est.get_materias()
            for m in materias:
                print(m)






#Ui()

"""
1 -> Crear un estudiante:
    >>> Nombre:
    >>> Apellido:
    >>> Cedula:
    >>> Sexo:
"""