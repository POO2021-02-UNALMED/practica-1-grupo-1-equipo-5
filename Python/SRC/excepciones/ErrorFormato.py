from excepciones.ErrorAplicacion import ErrorAplicacion
class ErrorFormato(ErrorAplicacion):

    def __init__(self, mensaje):
        self.mensaje_error_fromato = " Error por formato " + mensaje 
        super().__init__(self.mensaje_error_fromato)

class ExcepcionStringNumero(ErrorFormato):
    def __init__(self,valor):
        self.mensaje_error = f"la entrada {valor}  solo consta de digitos, por favor modifiquela."
        super().__init__(self.mensaje_error)

class ExcepcionEnteroString(ErrorFormato):
    def __init__(self,valor):
        self.mensaje_error=f"\n{valor} es un texto, por favor modifiquelo a un numero entero." 
        super().__init__(self.mensaje_error)

class ExcepcionEnteroFloat(ErrorFormato):

    def __init__(self,valor):
        self.mensaje_error=f"\n{valor} es un numero flotante, por favor modifiquelo a un entero."
        super().__init__(self.mensaje_error)

class ExcepcionEntradasVacias(ErrorFormato):

    def __init__(self,entradas):
        self.mensaje_error = f"\nFaltan por llenar las entradas: {entradas} \nPor favor ingreselas e intente de nuevo"
        super().__init__(self.mensaje_error)