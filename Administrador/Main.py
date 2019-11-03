from Vehiculo import *
from Cliente import *
from Ventas import *




print("BIENVENIDO")
print("1.Ingresar nuevo vehiculo al negocio")
print("2.Borrar lista de vehiculos")
print("3.Mostrar vehiculos actuales del negocio")
print("4.Hacer backup de los vehiculos")

print("5.Registrar cliente")
print("6.Eliminar cliente")
print("7.Mostrar clientes")

print("8.Registrar venta")
print("9.Ver ventas")
print("10.Salir")

seleccion = int(input("Ingrese el numero de su opcion"))


while True:
    if seleccion == 1:



        while True:

            print("Ingrese los parametros del nuevo vehiculo: \n")

            id = int(input("ingrese el id"))
            tipo = input("ingrese el tipo de vehiculo")
            marca = input("ingrese la marca")
            modelo = input("ingrese el modelo")
            anio = int(input("ingrese el año"))
            motor = int(input("ingrese el tipo de motor"))
            color = input("ingrese el color")
            kilometros = int(input("ingrese los kilometros"))
            potencia = int(input("ingrese el valor de la potencia"))
            transmision = input("ingrese el tipo de transmision")
            puertas = int(input("ingrese la cantidad de puertas"))
            combustible = input("ingrese el tipo de combustible")
            monto = int(input("ingrese el valor"))



            nuevo_vehiculo = Vehiculo(id, tipo, marca, modelo, anio, motor, color, kilometros, potencia, transmision, puertas,
                                combustible, monto)

            nuevo_vehiculo.registrar_vehiculo()


            salir_vehiculo = input("Desea agregar otro vehiculo mas s/n")
            if salir_vehiculo == "n":
                exit()


    elif seleccion == 2:

        id = None
        tipo = None
        marca = None
        modelo = None
        anio = None
        motor = None
        color = None
        kilometros = None
        potencia = None
        transmision = None
        puertas = None
        combustible = None
        monto = None
        nuevo_vehiculo = Vehiculo(id, tipo, marca, modelo, anio, motor, color, kilometros, potencia, transmision, puertas,
                                  combustible, monto)

        nuevo_vehiculo.eliminar_vehiculo()
        exit()


    elif seleccion == 3:

        id = None
        tipo = None
        marca = None
        modelo = None
        anio = None
        motor = None
        color = None
        kilometros = None
        potencia = None
        transmision = None
        puertas = None
        combustible = None
        monto = None
        nuevo_vehiculo = Vehiculo(id, tipo, marca, modelo, anio, motor, color, kilometros, potencia, transmision, puertas,
                                  combustible, monto)

        nuevo_vehiculo.mostrar_vehiculos()
        exit()

    elif seleccion == 4:

        id = None
        tipo = None
        marca = None
        modelo = None
        anio = None
        motor = None
        color = None
        kilometros = None
        potencia = None
        transmision = None
        puertas = None
        combustible = None
        monto = None
        nuevo_vehiculo = Vehiculo(id, tipo, marca, modelo, anio, motor, color, kilometros, potencia, transmision,
                                  puertas, combustible, monto)
        nuevo_vehiculo.backup()
        exit()

    elif seleccion == 5:

        while True:

            print("Ingrese los datos del nuevo cliente: \n")

            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            dni = int(input("Ingrese el dni: "))
            telefono = int(input("Ingrese el telefono"))

            nuevo_cliente = Cliente(nombre, apellido, dni, telefono)

            nuevo_cliente.registrar_cliente()

            salir_cliente = input("Desea agregar otro cliente mas s/n")
            if salir_cliente == "n":
                exit()






    elif seleccion == 6:

        nombre = None
        apellido = None
        dni = None
        telefono = None
        nuevo_cliente = Cliente(nombre, apellido, dni, telefono)

        nuevo_cliente.eliminar_cliente()
        exit()



    elif seleccion == 7:

        nombre = None
        apellido = None
        dni = None
        telefono = None
        nuevo_cliente = Cliente(nombre, apellido, dni, telefono)

        nuevo_cliente.mostrar_clientes()
        exit()


    elif seleccion == 8:

        print("Ingrese los datos de la nueva venta: \n")

        cliente = input("Ingrese el cliente: ")
        ide = int(input("Ingrese el id: "))
        vehiculo = input("Ingrese el vehiculo: ")
        monto = int(input("Ingrese el monto"))

        venta = Ventas(cliente, ide, vehiculo, monto)
        venta.registrar_venta()
        exit()



    elif seleccion == 9:

        cliente = None
        id = None
        vehiculo = None
        monto = None

        venta = Ventas(cliente, id, vehiculo, monto)
        venta.ver_ventas()
        exit()


    elif seleccion == 10:
        exit()
