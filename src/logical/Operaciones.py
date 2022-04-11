
class Operaciones():

    def ingresoDatos(self):
        while True:
            numero= input("Escribe un numero: ")
            try:
                numero = float (numero)
                return numero
            except ValueError:
                print("Tipo de dato no valido, escribe un numero entero o decimal.")


    def validarDivisor(self):
        while True:
            divisor = float(self.ingresoDatos ())
            if (divisor != 0):
                return divisor
                break
            else:
                print ("El divisor debe ser diferente de 0.")

    def validarOpcion(self):
        while True:
            opcion = self.ingresoDatos ()
            if ((opcion >= 0)&(opcion <= 5)):
                return opcion
                break
            else:
                print ("Numero de opcion invalida.")

    def suma(self,sumando1,sumando2 ):
        resultado = sumando1 + sumando2
        return resultado

    def resta(self, minuendo, sustraendo):
        resultado = minuendo - sustraendo
        return resultado

    def multiplicacion(self, multiplicando, multiplicador):
        resultado = multiplicando * multiplicador
        return resultado

    def division(self, dividendo, divisor):
        resultado = dividendo / divisor
        return resultado