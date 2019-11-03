

class Cliente ():

    def __init__(self, nombre, apellido, dni, telefono):

        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono

    def registrar_cliente(self):

        fclientes = open("clientes.txt", "a")
        fclientes.write(self.nombre+"\t"+self.apellido+"\t"+str(self.dni)+"\t"+str(self.telefono)+"\n")
        fclientes.close()

    def eliminar_cliente(self):

        fclientes = open("clientes.txt", "w")
        fclientes.write("\t")

    def mostrar_clientes(self):

        fclientes = open("clientes.txt", "r")
        lineas = fclientes.read()
        print(lineas)
        fclientes.close()





