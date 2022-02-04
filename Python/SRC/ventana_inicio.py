from VentanaPrincipal import VentanaSecundaria
from tkinter import *
from Admin import Admin
class ventana_inicio(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # CONFIGURACION PARAMETROS PRINCIPALES DE LA VENTANA
        self.geometry("800x500")
        self.title("Inicio")
        self.option_add("*tearOff", False)
        self.iconbitmap('./imagenes/icono.ico')
        self.resizable(0,0)
        # CONFIGURACION VR--TEXTO HDV DESARROLLADORES
        self.varHDV = StringVar()
        self.varHDV.set("Desarrolladores")

        self.hola =StringVar()
        self.hola.set('')
        # CONFIGURACION ZONA DE MENU
        self.menubar = Menu(self)
        self.menuInicio = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menuInicio, label="Inicio")
        self.menuInicio.add_command(label="Descripcion",command=self.desno)
        self.menuInicio.add_command(label="Salir",command=self.salir)
        self["menu"] = self.menubar

        #CONFIGURACION ZONA FRAMES

        self.P1 = Frame(self, width=400, height=500, bg="Gray95")
        self.P1.pack(side=LEFT)
        self.P3 = Frame(self.P1, width=400, height=150)
        self.P3.grid(row=0, column=0)
        self.saludo = Label(self.P3, text="Bienvenido al sistema de reservas de vuelo\n""Haz click en la imagen para empezar\n""⇣", font=("Segoe UI", 12))
        self.P4 = Frame(self.P1, width=400, height=350, bg="black")
        self.P4.grid(row=1, column=0)
        self.contenedorImagen = Label(self.P4)
        self.ImagenAplicacion =PhotoImage(file='./imagenes/--x1.png')
        self.contenedorImagen["image"] = self.ImagenAplicacion
        self.P2 = Frame(self, width=400, height=500, bg="yellow")
        self.P2.pack(side=RIGHT)
        self.P5 = Frame(self.P2, width=400, height=150, bg="Gray")
        self.P5.grid(row=0, column=0)
        self.textoHDV = Label(self.P5, textvariable=self.varHDV, font = ("Segoe UI", 8))
        self.textoHDV.bind('<ButtonPress-1>', self.cambioHDV)
        self.textoHDV.place(x=200, y=75, anchor="center")
        self.P6 = Frame(self.P2, width=400, height=350, bg="Gray")
        self.P6.grid(row = 1, column = 0)
        self.saludo.place(x=200, y=75, anchor="center")
        self.W1 = Frame(self.P6, width=200, height=170, bg="Blue")
        self.W1.place(x=0, y=0)
        self.W2 = Frame(self.P6, width=200, height=170, bg="White")
        self.W2.place(x=200, y=0)
        self.W3 = Frame(self.P6, width=200, height=180, bg="Green")
        self.W3.place(x=0, y=170)
        self.W4 = Frame(self.P6, width=200, height=180, bg="Black")
        self.W4.place(x=200, y=170)
        self.holla = Label(self.P3, textvariable=self.hola, font=("Segoe UI", 8))
        self.holla.place(x=200, y=120, anchor="center")

        #CONTADORES CAMBIO DE CASOS METODOS
        self.acumulador = 0
        self.numClicksHDV = 0

        # LISTA MENEJO IMAGENES DESARROLLADORES
        self.direcciones = ['./imagenes/--r1.png', './imagenes/--r2.png', './imagenes/--r3.png', './imagenes/--r4.png','./imagenes/--c1.png', './imagenes/--c2.png', './imagenes/--c3.png', './imagenes/--c4.png','./imagenes/--m1.png', './imagenes/--m2.png', './imagenes/--m3.png', './imagenes/--m4.png','./imagenes/--q1.png', './imagenes/--q2.png', './imagenes/--q3.png', './imagenes/--q4.png','./imagenes/--yu.png']
        self.cambio_posiciones = []

        # LISTA MANEJO DE IMAGENES DEL SISTEMA
        self.lineas = ['./imagenes/--x1.png', './imagenes/--x2.png', './imagenes/--x3.png','./imagenes/--x4.png', './imagenes/--x5.png']
        self.chang_posiciones = []

        #RECORRIDO SOBRE LA LISTA direcciones PARA OBTENER LAS IMAGENES SEGUN LA REFERENIA DEL DESARROLLADOR
        for i in self.direcciones:
            imagen = PhotoImage(file=i)
            self.cambio_posiciones.append(imagen)

        self.im_desa_pos1 = Label(self.W1)
        self.im_desa_pos2 = Label(self.W2)
        self.im_desa_pos3 = Label(self.W3)
        self.im_desa_pos4 = Label(self.W4)
        self.im_desa_pos1["image"] = self.cambio_posiciones[16]
        self.im_desa_pos1.pack()
        self.im_desa_pos2["image"] = self.cambio_posiciones[16]
        self.im_desa_pos2.pack()
        self.im_desa_pos3["image"] = self.cambio_posiciones[16]
        self.im_desa_pos3.pack()
        self.im_desa_pos4["image"] = self.cambio_posiciones[16]
        self.im_desa_pos4.pack()
        self.contador = 0

        #RECORRIDO SOBRE LA LISTA lineas PARA ABRIR DETERMINADA IMAGEN SEGUN LA REFERENCIA DEL EVENTO PARA CAMBIO DE IMAGEN
        for i in self.lineas:
            imagen = PhotoImage(file=i)
            self.chang_posiciones.append(imagen)

        # CONFIGURACION BOTON APERTURA DE LA VENTANA PRINCIPAL Y CAMBIO DE IMAGEN
        self.nueva_ventana = Button(self.P4, image=self.chang_posiciones[0],command=self.abrirVentanaSecundaria)
        self.nueva_ventana.pack()
        self.nueva_ventana.bind('<Enter>', self.cambio)

    #GENERA LA SALIDA DEL TEXTO DE EN LA DESCRIPCION
    def desno(self):
        self.hola.set("Permite la compra de un tiquete para un vuelo, con seleccion de\n" "silla y alojamiento, ademas de la ejecucion de opciones de administrador ✈")


    #GENERA LA SALIDA DE LA VENTANA DE INICIO DANDO CULMINADO EL FUNCIONAMIENTO DE LA APLICACION
    def salir(self):
        Admin.salirDelSistema()
        return super().destroy()

    #OCASIONA LA APERTURA DE LA VENTANAPRINCIAL
    def abrirVentanaSecundaria(self):
         if not VentanaSecundaria.en_uso:
            self.ventana_secundaria = VentanaSecundaria()
            self.ventana_secundaria.ventanaInicio = self
            self.iconify()

    #SUSCITA EL CAMBIO DE INFORMACIÓN DE LA HOJA DE VIDA E IMAGENES DE LOS DESARROLLADORES
    def cambioHDV(self,b):
        self.numClicksHDV += 1
        if (self.numClicksHDV == 1):
            self.varHDV.set("Nombre: Jerónimo Salazar Salazar \n""Edad : 19 años \n""Programa: Ciencias de la computación\n")
            self.evento(12)
        elif (self.numClicksHDV == 2):
            self.varHDV.set("Karen Vanessa Rivera Giraldo \n""Edad: 18 años \n" "Programa: Ingeniería de sistemas\n")
            self.evento(12)
        elif (self.numClicksHDV == 3):
            self.varHDV.set("Nombre: Álvaro Javier Guerrero  \n""Edad : 25 años \n""Programa: Ciencias de la computación\n")
            self.evento(12)
        elif (self.numClicksHDV == 4):
            self.varHDV.set("Nombre: David Esteban Martin Acosta \n""Edad : 18 años \n""Programa: Ciencias de la computación\n")
            self.evento(12)
            self.numClicksHDV = 0

    #PROVOCA LA APERTURA DE LAS IMAGENES DE CADA DESARROLLADOR SEGUN SU IDENTIFICADOR POSICIONAL
    def evento(self,c):
        y1 = 0
        y2 = 0
        y3 = 0
        y4 = 0
        self.contador += 1
        if self.contador == 1:
            y1 = self.contador - 1
            y2 = self.contador
            y3 = self.contador + 1
            y4 = self.contador + 2
        elif self.contador == 2:
            y1 = self.contador + 2
            y2 = self.contador + 3
            y3 = self.contador + 4
            y4 = self.contador + 5
        elif self.contador == 3:
            y1 = self.contador + 5
            y2 = self.contador + 6
            y3 = self.contador + 7
            y4 = self.contador + 8
        elif self.contador == 4:
            y1 = self.contador + 8
            y2 = self.contador + 9
            y3 = self.contador + 10
            y4 = self.contador + 11
        self.im_desa_pos1.config(image=self.cambio_posiciones[y1])
        self.im_desa_pos2.config(image=self.cambio_posiciones[y2])
        self.im_desa_pos3.config(image=self.cambio_posiciones[y3])
        self.im_desa_pos4.config(image=self.cambio_posiciones[y4])
        if self.contador == 4:
            self.contador = 0

    # OCASIONA EL CAMBIO EN LA POSICION DE LAS IMAGENES DEL SISTEMA
    def cambio(self,a):
        self.acumulador += 1
        if self.acumulador == 5:
            self.acumulador = 0
        self.nueva_ventana.config(image=self.chang_posiciones[self.acumulador])

if __name__ == "__main__":
    ventana_inicios = ventana_inicio()
    ventana_inicios.mainloop()
