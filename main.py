from src.logical.Operaciones import Operaciones

if __name__ == '__main__':
    operacion = Operaciones ()
    opcion = 0
    while(opcion != 5):
        print ("Operaciones")
        print ("1. Suma.")
        print ("2. Resta.")
        print ("3. Multiplicacion.")
        print ("4. Division.")
        print ("5. Salir.")
        opcion = operacion.validarOpcion()

        if((opcion>0)&(opcion<5)):
            numero1 = operacion.ingresoDatos ()

        if ((opcion>0)&(opcion<4)):
            numero2 = operacion.ingresoDatos ()

        if(opcion==1):
            resultado = operacion.suma(numero1,numero2)
            print ("{0:.2f} + {1:.2f} = {2:.2f}".format (numero1,numero2, resultado))

        if (opcion == 2):
            resultado = operacion.resta (numero1,numero2)
            print ("{0:.2f} - {1:.2f} = {2:.2f}".format (numero1,numero2, resultado))

        if (opcion == 3):
            resultado = operacion.multiplicacion (numero1,numero2)
            print ("{0:.2f} * {1:.2f} = {2:.2f}".format (numero1,numero2, resultado))

        if (opcion == 4):
            numero2 = operacion.validarDivisor ()
            resultado = operacion.division (numero1,numero2)
            print ("{0:.2f} / {1:.2f} = {2:.2f}".format (numero1,numero2, resultado))