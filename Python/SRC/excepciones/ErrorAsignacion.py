

from excepciones.ErrorAplicacion import ErrorAplicacion


class ErrorAsignacion(ErrorAplicacion):
    
    def __init__(self, mensaje):
        self.mensaje_error_asigancion = f" Error de existencia: {mensaje}"
        super().__init__(self.mensaje_error_asigancion)


class ExcepcionAgregarAlojamiento(ErrorAsignacion):

    def __init__(self, id):
        self.mensaje_error = f"\nEl tiquete con ID {id} ya posee un alojamiento, si desea cambiarlo debe hacerlo desde la opcion <Modificar tiquete>"
        super().__init__(self.mensaje_error)

class ExcepcionModificarAlojamiento(ErrorAsignacion):
    
    def __init__(self, id):
        self.mensaje_error = f"\nEl tiquete con ID {id} aun no posee un alojamiento, si desea agregar uno debe hacerlo desde la opcion <Agregar alojamiento>"
        super().__init__(self.mensaje_error)

class ExcepcionIdVuelo(ErrorAsignacion):

     def __init__(self, id):
         self.mensaje_error = f"\nNo existe un vuelo con el ID: {id}"
         super().__init__(self.mensaje_error)

class ExcepcionIdTiquete(ErrorAsignacion):

    def __init__(self, id):
        self.mensaje_error = f"\nNo existe un tiquete con el ID: {id}"
        super().__init__(self.mensaje_error)