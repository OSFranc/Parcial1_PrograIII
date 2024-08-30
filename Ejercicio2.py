# Creamos una lista donde se almacenan los codigos
listaCodigos = []

# Creamos una clase que almacene todos los datos de la tarjeta
class Tarjeta:
    def __init__(self, nombre, institucion, codigo, libro, fechaPrestamo, diasPrestamo):
        self.nombre = nombre
        self.institucion = institucion
        self.codigo = codigo
        self.libro = libro
        self.fechaPrestamo = fechaPrestamo
        self.diasPrestamo = int(diasPrestamo)

#Muestra los datos de la tarjeta en una instanacia de clase
    def mostrarDatos(self):
        print("Nombre: ", self.nombre)
        print("Institución: ", self.institucion)
        print("Código: ", self.codigo)
        print("Libro: ", self.libro)
        print("Fecha de Préstamo: ", self.fechaPrestamo)
        print("Días de préstamo: ", self.diasPrestamo)

#Determinar si se ha excedido de los dias de prestamos, comparando dias de prestamo con el tiempo transcurrido
    def calcularDiasTranscurridos(self):
        diasTranscurridos= int(input("Ingrese el numero de dias desde el prestamo: "))
        if diasTranscurridos>self.diasPrestamo:
            print("Ha excedido el limite de prestamo, se ha aplicado una sancion")
        else: print("Aun se encuentra dentro de los dias disponibles de devolucion")
        
#Funcion para ingresar una nueva tarjeta
def nuevaTarjeta():
    nombre = input("Ingrese su nombre: ")
    institucion = input("Ingrese su Institución: ")
    codigo = input("Ingrese su código: ")

#Evalua si la tarjeta tiene un prestamo pendiente
    resp = input("¿Desea prestar un libro? S/N: ").upper()
    if resp == "S":
        libro = input("Ingrese el nombre del libro: ")
        fechaPrestamo = input("Ingrese la fecha de préstamo (YYYY-MM-DD): ")
        diasPrestamo = input("Ingrese la cantidad de días de préstamo: ")
    else:
        libro = "Ninguno"
        fechaPrestamo = "Ninguno"
        diasPrestamo = "0"

    nuevaTarjeta = Tarjeta(nombre, institucion, codigo, libro, fechaPrestamo, diasPrestamo)
    nuevaTarjeta.mostrarDatos()
    listaCodigos.append(nuevaTarjeta)
    return nuevaTarjeta

# Crear una nueva tarjeta de préstamo
tarjeta1 = nuevaTarjeta()

# Verificar si hay sanción al devolver el libro
tarjeta1.calcularDiasTranscurridos()
print("Integrante 1: Oscar Rene Palacios Franco SMSS065523")
print("Integrante 2 : Gerson Manases Flores Quinteros SMSS040923")



