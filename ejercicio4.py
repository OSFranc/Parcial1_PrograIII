"""
Una empresa de renta de transporte tiene varios tipos de vehículos a su
disposición cada uno con sus características y coste de renta. La
empresa periódicamente registra los nuevos vehículos que ingresan al
lote para su posterior puesta en renta.
 Implementa la funcionalidad de rentar los vehículos disponibles
tomando en cuenta los datos del cliente."""

#Continuando la secuencia del ejercicio 3, mediante un menú en un ciclo While tenemos 3 opciones principales 
#Al seleccionar añadir vehículo se crea un nuevo objeto de la clase Vehículo que almacena todos los atributos de dicho vehículo
#para usarse posteriormente, y ser llamados en un ciclo for, estos objetos se van almacenando en un array.
#Al comenzar la renta del vehículo se llama nuevamente al ciclo for para mostrar un listado de vehículos
#y se toma la opción del número del vehículo mostrado (Su posición en la lista)
#Se pregunta el número de días a alquilar y se multiplica por el precio de renta del vehículo (establecido como atributo)

# Lista para almacenar los vehículos
listadoVehiculos = []

# Definición de la clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año, transmision, capacidad, categoria, precioRenta):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.transmision = transmision
        self.capacidad = capacidad
        self.categoria = categoria
        self.precioRenta = precioRenta
        self.estado = "Disponible"
    
# Imprime los detalles del vehículo
    def datosVehiculo(self):
        print("***************** Datos del Vehículo *******************")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año : {self.año}")
        print(f"Transmisión : {self.transmision}")
        print(f"Capacidad: {self.capacidad} pasajeros")
        print(f"Categoría: {self.categoria}")
        print(f"Precio de Renta (día): ${self.precioRenta}")
        
# Actualiza el estado del vehículo a "Rentado"
    def actualizarEstado(self):
        self.estado="Rentado"

 # Crea un nuevo objeto Vehiculo y lo añade a la lista
def nuevoVehiculo():
    print("*********** Ingresar un Nuevo Vehículo ************")
    marca = input("Marca del Vehículo: ")
    modelo = input("Modelo del Vehículo: ")
    año = input("Año: ")
    while True:
        transmision = input("Tipo de Transmisión (1. Manual 2. Automática): ")
        if transmision == "1":
            transmision = "Manual"
            break
        elif transmision == "2":
            transmision = "Automática"
            break
        else:
            print("Opción no válida, ingrese el número 1 o 2.")
    capacidad = int(input("Capacidad de pasajeros (número): "))
    categoria = input("Categoría del Vehículo (Sedán, SUV, Pickup, Camioneta...): ")
    precioRenta = float(input("Precio de renta (día): $"))
    
    vehiculo = Vehiculo(marca, modelo, año, transmision, capacidad, categoria, precioRenta)
    listadoVehiculos.append(vehiculo)
    print("Vehículo añadido exitosamente.\n")

# Función para mostrar todos los vehículos en la lista
def mostrarVehiculos():
    if listadoVehiculos:
        print("\n*********** Lista de Vehículos ************")
        for i, vehiculo in enumerate(listadoVehiculos, 1):
            print(f"\n*********** Vehículo {i} *************")
            vehiculo.datosVehiculo()
    else:
        print("No hay vehículos registrados.")

 # Función para alquilar un vehículo
def alquilarVehículo():
    print("A continuación, se muestran las opciones disponibles para renta: ")
    if listadoVehiculos:
        print("\n*********** Lista de Vehículos ************")
        for i, vehiculo in enumerate(listadoVehiculos, 1):
            print(f"\n*********** Vehículo {i} *************")
            vehiculo.datosVehiculo()
    else:
        print("No hay vehículos registrados.")
    
    numVehiculo= int(input("Seleccione el número del vehículo a alquilar: "))
    print("Desea alquilar el siguiente Vehículo?: ")
    listadoVehiculos[numVehiculo].datosVehiculo()
    respRenta= input("S/N :").upper()
    if respRenta=="S":
        diasRenta= int(input(f"Número de días a alquilar (precio: ${listadoVehiculos[numVehiculo].precioRenta}): "))
        print("Total a Cancelar: $", listadoVehiculos[numVehiculo].precioRenta*diasRenta)
        listadoVehiculos[numVehiculo].actualizarEstado()
        print("********* Gracias por su Confianza!*********")
    
        
    
    
 # Menú principal del programa
def menuPrincipal():
    while True:
        print("--- Menú Principal ---")
        print("1. Añadir un nuevo vehículo")
        print("2. Mostrar vehículos registrados")
        print("3. Alquilar un Vehículo")
        print("4. Finalizar programa")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nuevoVehiculo()
        elif opcion == "2":
            mostrarVehiculos()
        elif opcion == "3":
            print("Alquilar Vehículo")
            alquilarVehículo()
        elif opcion == "4":
            print("Finalizando Programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

menuPrincipal()
print("Integrante 1: Oscar Rene Palacios Franco SMSS065523")
print("Integrante 2 : Gerson Manases Flores Quinteros SMSS040923")

        