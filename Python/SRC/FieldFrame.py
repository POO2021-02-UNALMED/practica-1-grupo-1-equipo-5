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
 
    #Guarda los datos puestos en los cuadros de texto en la lista valor_entradas
    #Ademas, verifica que todos los textos tengan un valor, y en caso de que falte alguno se disparara una excepcion
    #en la que por medio de una ventana de advertencia se le indicara al usuario cuales campos le faltan por llenar.
 
    def aceptar(self):
        self.valor_entradas=[] 
        for criterio in self.entradas:
            self.valor_entradas.append(self.getValue(criterio))
        try:
            valores_vacios = ""
            hay_excepcion = False
            for i in range (len(self.valor_entradas)):
                if self.valor_entradas[i] == "":
                    hay_excepcion = True
                    valores_vacios += "\n"+list(self.entradas.keys())[i]+","
            if hay_excepcion:
                raise ExcepcionEntradasVacias(valores_vacios)
                
        except ExcepcionEntradasVacias as uwu:
            messagebox.showwarning(title="Aviso",message=uwu.mensaje_error_inicio)
            return hay_excepcion

            
        for i in range (len(self.valor_entradas)):
            if self.tipo_esperado[i] == "int": 
                
                if not self.valor_entradas[i].isdigit():
                    Admin.isFloat(self.valor_entradas[i])
                    raise ExcepcionEnteroString(self.valor_entradas[i])

            elif self.tipo_esperado[i] == "string":
                
                if self.valor_entradas[i].isdigit():
                    raise ExcepcionStringNumero(self.valor_entradas[i])
                
        self.borrarValores()
        return hay_excepcion
            

    #Permite borrar  todos los campos de los cuadros de texto
    def borrarValores(self):
        for criterio in self.entradas:
            entrada = self.entradas[criterio]
            entrada.delete(0, "end")
    
    #Retorna el valor del criterio del argumento(criterio) que se le pase
    def getValue(self, criterio):
        entrada = self.entradas[criterio]
        return entrada.get()
    