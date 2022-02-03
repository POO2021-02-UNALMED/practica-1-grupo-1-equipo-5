#CLASE FIELDFRAME PARA LA CREACION DE FORMULARIOS
from tkinter import *
from tkinter import messagebox
from Admin import Admin
from excepciones.ErrorAplicacion import *
from excepciones.ErrorAsignacion import *
from excepciones.ErrorFormato  import *
class FieldFrame (Frame):

    #Constructor
    def __init__(self, parent, tituloCriterios, criterios, tituloValores, valoresIniciales, habilitado,tipo_esperado):
        super().__init__(parent)

        self.entradas = {} # Diccionario desde donde se podrá acceder a la entrada asociada a cada criterio
        self.valor_entradas =[] # Lista que contendra el valor de las entradas pasadas por el usuario
        self.pack()
        self.config(relief = "groove") 
        self.config(bd=20)
        self.config(borderwidth=2) 
        self.tipo_esperado = tipo_esperado
        #Titulos del formulario
        titulo1 = Label(self, text = tituloCriterios.upper() , anchor="center", borderwidth=2, font = ("Segoe UI", 11, 'bold'))
        titulo1.grid(row = 0, column = 0, ipadx=20, padx=30, pady = 2)
        
        titulo2 = Label(self, text = tituloValores.upper(), anchor="center", borderwidth=2, font = ("Segoe UI", 11, 'bold'))
        titulo2.grid(row = 0, column = 1, ipadx=20, padx=30, pady = 2)

        #Creacion de Label para los criterios y Entry para las entradas
        for i in range(0, len(criterios)):
              
            lab = Label(self, width = 22, text = criterios[i], anchor = "center", font = ("Segoe UI", 10))
            ent = Entry(self)

            #Verifica si hay valores por defecto para ponerlos en el Entry
            if valoresIniciales != None:
                ent.insert(0,valoresIniciales[i]) # Arg: posicion, string
                self.valor_entradas.append(valoresIniciales[i])

            #Verifica si hay lista de valores habilitados, para modificar las Entry de acuerdo a eso
            if habilitado != None:
                if habilitado[i]:
                    ent['state'] = NORMAL
                else:
                    ent['state'] = DISABLED

            #Posiciona dinamicamente el Label y Entry
            lab.grid(row = i+1, column = 0, ipadx=15, padx=10, pady = 2)
            ent.grid(row = i+1, column = 1, ipadx=10, padx=10, pady = 3)

            self.entradas[criterios[i]] = ent

        #Obtiene el numero de filas y de columnas del grid
        col_count, row_count = self.grid_size()

        #Boton aceptar
        self.botonAceptar = Button(self, width=10, text='Aceptar', font = ("Segoe UI", 10), relief=GROOVE, cursor='hand2', command=self.aceptar)
        self.botonAceptar.grid(row = row_count, column = 0, ipadx=20, padx=30, pady = 6)

        #Boton borrar
        self.botonBorrar = Button(self, width=10, text='Borrar', font = ("Segoe UI", 10), relief=GROOVE, cursor='hand2', command = self.borrarValores)
        self.botonBorrar.grid(row = row_count, column = 1, ipadx=20, padx=30, pady = 5)
    