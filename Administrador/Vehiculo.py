import shutil


class Vehiculo():


    def __init__(self, id, tipo, marca, modelo, anio, motor, color, kilometros, potencia, transmision, puertas, combustible, monto):

        self.id = id
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.motor = motor
        self.color = color
        self.kilometros = kilometros
        self.potencia = potencia
        self.transmision = transmision
        self.puertas = puertas
        self.combustible = combustible
        self.monto = monto

    def registrar_vehiculo(self):
        fvehiculos = open("vehiculos.txt", "a")
        fvehiculos.write("\n"+str(self.id)+"\t"+self.tipo+"\t"+self.marca+"\t"+self.modelo+"\t"+str(self.anio)+"\t"+str(self.motor)+"\t"+self.color+"\t"+str(self.kilometros)+"\t"+str(+self.potencia)+"\t"+self.transmision+"\t"+str(self.puertas)+"\t"+self.combustible+"\t"+str(self.monto)+"\n")
        fvehiculos.close()

    def eliminar_vehiculo(self):

        fvehiculos = open("vehiculos.txt","w")
        fvehiculos.write("\t")

    def backup(self):

        shutil.copy("vehiculos.txt", "backup.txt")

    def mostrar_vehiculos(self):

        fvehiculos = open("vehiculos.txt", "r")
        lineas = fvehiculos.read()
        print(lineas)
        fvehiculos.close()


