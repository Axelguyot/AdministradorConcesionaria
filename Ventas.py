

class Ventas():

    def __init__(self, cliente, ide, vehiculo, monto):

        self.cliente = cliente
        self.ide = ide
        self.vehiculo = vehiculo
        self.monto = monto

    def registrar_venta(self):
        fventas = open("ventas.txt", "a")
        fventas.write(self.cliente + "\t" + str(self.ide) + "\t" + self.vehiculo + "\t" + str(self.monto) + "\n")
        fventas.close()


    def ver_ventas(self):

        fventas = open("ventas.txt", "r")
        lineas = fventas.read()
        print(lineas)
        fventas.close()

