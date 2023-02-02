#Importamos tkinter
from tkinter import *
#Importamos widgets
from tkinter.ttk import *
from controlador.controlador_univ import Controlador

class Gui:
    #Método constructor
    def __init__(self) -> None:
        self.controlador: Controlador = Controlador()
        #index de los registros en la tabla estudiante
        self.index_est = 0
        #Identificador único de cada item(registro) de la tabla estudiante
        self.uiid_est = 0
        #Construir ventana
        self.window = Tk()
        self.window.title("Software universitario")
        self.crear_form_estudiante()
        self.crear_form_materia()
        self.crear_tabla_estudiantes()
        self.crear_tabla_materias()
        self.estud = self.controlador.cargar_estudiante()
        self.obtener_estudiantes(self.estud)
        self.mostrar_ventana()
        
    """
    Crea y agrupar elementos del formulario matricular estudiante
    """
    def crear_form_estudiante(self):
        self.lbl_nombre_est = Label(self.window, text="Nombre: ")
        self.entry_nombre_est = Entry(self.window, width=15)
        self.lbl_apellido = Label(self.window, text="Apellido: ")
        self.entry_apellido = Entry(self.window, width=15)
        self.lbl_cedula = Label(self.window, text="Cédula: ")
        self.entry_cedula = Entry(self.window, width=15)
        self.lbl_sexo = Label(self.window, text="Sexo: ")
        self.entry_sexo = Entry(self.window, width=15)
        self.btn_estudiante = Button(self.window, text="Matricular estudiante", command=self.matricular_estudiante)
    
    """
    Método para crear los elementos del formulario 'matricular materia'
    """
    def crear_form_materia(self):
        self.lbl_cedula_mat = Label(self.window, text="Cédula estudiante: ")
        self.entry_cedula_materia = Entry(self.window, width=15)
        self.lbl_materia = Label(self.window, text="Nombre materia: ")
        self.entry_materia = Entry(self.window, width=15)
        self.btn_materia = Button(self.window, text="Matricular materia")

    """
    Tabla estudiantes
    """
    def crear_tabla_estudiantes(self):
        self.tabla_est = Treeview(self.window, columns=4)
        self.tabla_est["columns"] = ["nombre", "apellido", "cedula", "sexo"]
        #Únicamente muestra las cabeceras
        self.tabla_est["show"] = "headings"
        #Texto que mostrará la cabecera de la tabla
        self.tabla_est.heading("nombre", text="Nombre")
        self.tabla_est.heading("apellido", text="Apellido")
        self.tabla_est.heading("cedula", text="Cédula")
        self.tabla_est.heading("sexo", text="Sexo")
        #Botón para consultar las materias de un estudiante
        self.btn_consultar_mat = Button(self.window, text="Consultar materias", command=self.get_estudiante_select)
    

    """
    Tabla materias
    """
    def crear_tabla_materias(self):
        self.tabla_mat = Treeview(self.window, columns=2)
        self.tabla_mat["columns"] = ["nombre", "nota"]
        self.tabla_mat["show"] = "headings"
        self.tabla_mat.heading("nombre", text="Materia")
        self.tabla_mat.heading("nota", text="Calificación")

    """
    Ubicación de los elementos en pantalla y mostrar la ventana
    """
    def mostrar_ventana(self):
        """
        Ubicación de los elementos 'matricular estudiante'
        """
        self.lbl_nombre_est.grid(column=0, row=0)
        self.entry_nombre_est.grid(column=1, row=0)
        self.lbl_apellido.grid(column=0, row=1)
        self.entry_apellido.grid(column=1, row=1)
        self.lbl_cedula.grid(column=0, row=2)
        self.entry_cedula.grid(column=1, row=2)
        self.lbl_sexo.grid(column=0, row=3)
        self.entry_sexo.grid(column=1, row=3)
        self.btn_estudiante.grid(column=1, row=4)
        """
        Ubicación de los elementos 'matricular materia'
        """
        self.lbl_cedula_mat.grid(column=2, row=0)
        self.entry_cedula_materia.grid(column=3, row=0)
        self.lbl_materia.grid(column=2, row=1)
        self.entry_materia.grid(column=3, row=1)
        self.btn_materia.grid(column=3, row=2)
        """
        Ubicación de la tabla estudiantes
        """
        self.tabla_est.place(x=75, y=150)
        self.btn_consultar_mat.place(x=150, y=380)
        """
        Ubicación de la tabla materias
        """
        self.tabla_mat.place(x=75, y=450)
        #Tamaño de la ventana
        self.window.geometry("1200x700")
        #Mostrar ventana
        self.window.mainloop()
    
    def matricular_estudiante(self):
        #Obtener los datos de los campos de texto
        nombre: str = self.entry_nombre_est.get()
        apellido: str = self.entry_apellido.get()
        cedula: str = self.entry_cedula.get()
        sexo: str = self.entry_sexo.get()
        #Crear un estudiante
        obj_est = self.controlador.crear_estudiante(nombre, apellido, cedula, sexo)
        self.controlador.guardar_estudiante(obj_est)
        #Insertar el registro en la tabla
        tupla_est = (nombre, apellido, cedula, sexo)
        self.tabla_est.insert('', self.index_est, self.uiid_est, values=tupla_est)
        self.index_est += 1
        self.uiid_est += 1
        self.limpiar_form_estudiante()
    
    #Método para limpiar los campos del formulario matricular estudiante
    def limpiar_form_estudiante(self):
        self.entry_nombre_est.delete(0, 'end')
        self.entry_apellido.delete(0, 'end')
        self.entry_cedula.delete(0, 'end')
        self.entry_sexo.delete(0, 'end')

    #Obtener los elementos de la tabla
    def get_estudiante_select(self):
        data = self.tabla_est.item( self.tabla_est.focus() )
        print(data)

    def obtener_estudiantes(self, estud):
        #Insertar el registro en la tabla
        for est in self.estud:
            nombre: str = str(est["nombre"])
            apellido: str = str(est["apellido"])
            cedula: str = str(est["cedula"])
            sexo: str = str(est["sexo"])
            tup_est = (nombre, apellido, cedula, sexo)
            self.tabla_est.insert('', self.index_est, self.uiid_est, values=tup_est)
            self.index_est += 1
            self.uiid_est += 1
