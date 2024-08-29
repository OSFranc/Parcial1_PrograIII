from datetime import datetime

class Vehiculo:
    def __init__(self):
        self.origen = ""
        self.capacidad = 0
        self.__ruedas = 4
        self.marca = ""
        self.modelo = ""
        self.color = ""
        self.categoria = ""
        self.transmision = ""
        self.numeroDePuertas = 0
        self.tipoCombustible = ""
        self.precioRenta = 0
        self.fecha_inicio_alquiler = None
        self.fecha_fin_alquiler = None

    def ruedas(self):
        return self.__ruedas

    def iniciar_alquiler(self, fecha_inicio):
        self.fecha_inicio_alquiler = fecha_inicio
        self.fecha_fin_alquiler = None

    def finalizar_alquiler(self, fecha_fin):
        self.fecha_fin_alquiler = fecha_fin

    def calcular_costo_alquiler(self):
        if self.fecha_inicio_alquiler and self.fecha_fin_alquiler:
            dias = (self.fecha_fin_alquiler - self.fecha_inicio_alquiler).days
            if dias > 0:
                return dias * self.precioRenta
        return 0

def pasarDatos(vehiculo, origenPais, marcaVh, modeloVh, colorVh, categoriaVh, transmisionVh, numeroDePuertas, capacidadVh, tipoCombustible, precioDelVh):
    vehiculo.origen = origenPais
    vehiculo.marca = marcaVh
    vehiculo.modelo = modeloVh
    vehiculo.color = colorVh
    vehiculo.categoria = categoriaVh
    vehiculo.transmision = transmisionVh
    vehiculo.numeroDePuertas = numeroDePuertas
    vehiculo.tipoCombustible = tipoCombustible
    vehiculo.precioRenta = precioDelVh
    vehiculo.capacidad = capacidadVh

def obtenerDatos():
    print("********* Ingresar Datos *************")
    
    while True:
        origenPais = input("Origen (L: Local / I: Importado): ").lower()
        if origenPais == "l":
            origenPais = "Local"
            break
        elif origenPais == "i":
            origenPais = "Importado"
            break
        else:
            print("Respuesta no válida, ingrese L o I")
    
    marcaVh = input("Marca: ")
    modeloVh = input("Modelo: ")
    colorVh = input("Color: ")
    
    categorias = ["Sedan", "SUV", "Hatchback", "Coupe", "Convertible", "Pickup", "Van"]
    print("\nSeleccione la categoría del vehículo:")
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat}")
    
    while True:
        try:
            opcionCategoria = int(input("\nIngrese el número de la categoría: "))
            if 1 <= opcionCategoria <= len(categorias):
                categoriaVh = categorias[opcionCategoria - 1]
                break
            else:
                print("Opción no válida. Por favor, seleccione un número de la lista.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    
    while True:
        transmisionVh = input("Transmisión del Vehículo (Manual/Automática): ").capitalize()
        if transmisionVh in ["Manual", "Automática"]:
            break
        else:
            print("Respuesta no válida, ingrese Manual o Automática.")
    
    while True:
        try:
            numeroDePuertas = int(input("Número de Puertas: "))
            if numeroDePuertas > 0:
                break
            else:
                print("Número de puertas no válido.")
        except ValueError:
            print("Por favor ingrese un número válido para el número de puertas.")

    while True:
        try:
            capacidadVh = int(input("Capacidad del vehículo: "))
            if capacidadVh > 0:
                break
            else:
                print("Capacidad no válida.")
        except ValueError:
            print("Por favor ingrese un número válido para la capacidad.")
    
    tiposCombustible = ["Gasolina", "Diésel", "Eléctrico", "Híbrido"]
    while True:
        tipoCombustible = input("Tipo de Combustible (Gasolina, Diésel, Eléctrico, Híbrido): ").capitalize()
        if tipoCombustible in tiposCombustible:
            break
        else:
            print(f"Tipo de combustible no válido. Las opciones válidas son: {', '.join(tiposCombustible)}.")
    
    while True:
        try:
            precioDelVh = float(input("Ingrese el precio de renta por día: $"))
            if precioDelVh >= 0:
                break
            else:
                print("El precio debe ser un valor positivo.")
        except ValueError:
            print("Por favor ingrese un número válido para el precio de renta.")
    
    return origenPais, marcaVh, modeloVh, colorVh, categoriaVh, transmisionVh, numeroDePuertas, capacidadVh, tipoCombustible, precioDelVh

def mostrarDatos(vehiculo):
    print("""
   ---------------------------.
 `/""""/""""/|""|'|""||""|   ' \.
 /    /    / |__| |__||__|      |
/----------=====================|
| \  /V\  /    _.               |
|()\ \W/ /()   _            _   |
|   \   /     / \          / \  |-( )
=C========C==_| ) |--------| ) _/==] _-(__)
 \_\_/__..  \_\_/_ \_\_/ \_\_/__.__.""")

    print(f"- Origen: {vehiculo.origen}")
    print(f"- Marca: {vehiculo.marca}")
    print(f"- Modelo: {vehiculo.modelo}")
    print(f"- Categoría: {vehiculo.categoria}")
    print(f"- Número de Ruedas: {vehiculo.ruedas()}")
    print(f"- Color: {vehiculo.color}")
    print(f"- Transmisión: {vehiculo.transmision}")
    print(f"- Número de Puertas: {vehiculo.numeroDePuertas}")
    print(f"- Capacidad: {vehiculo.capacidad}")
    print(f"- Tipo de Combustible: {vehiculo.tipoCombustible}")
    print(f"- Precio de renta por día: ${vehiculo.precioRenta:.2f}")

def iniciar_alquiler(self, fecha_inicio):
    self.fecha_inicio_alquiler = fecha_inicio
    self.fecha_fin_alquiler = None

def finalizar_alquiler(self, fecha_fin):
    self.fecha_fin_alquiler = fecha_fin


def calcular_costo_alquiler(self):
    if self.fecha_inicio_alquiler and self.fecha_fin_alquiler:
        dias = (self.fecha_fin_alquiler - self.fecha_inicio_alquiler).days
        if dias > 0:
            return dias * self.precioRenta
    return 0


def mostrar_costo_alquiler(vehiculo):
    costo = vehiculo.calcular_costo_alquiler()
    if costo > 0:
        print(f"El costo total del alquiler es: ${costo:.2f}")
    else:
        print("No se puede calcular el costo del alquiler. Asegúrese de que las fechas de inicio y fin del alquiler estén correctamente establecidas.")

def añadir_vehiculo(lista_vehiculos):
    print("********* Añadir Nuevo Vehículo *************")
    nuevo_vehiculo = Vehiculo()
    datos = obtenerDatos()
    pasarDatos(nuevo_vehiculo, *datos)
    lista_vehiculos.append(nuevo_vehiculo)
    print("Vehículo añadido exitosamente.")

def seleccionar_vehiculo(lista_vehiculos):
    if not lista_vehiculos:
        print("No hay vehículos disponibles.")
        return None

    print("\nSeleccione un vehículo:")
    for i, vh in enumerate(lista_vehiculos, 1):
        print(f"{i}. {vh.marca} {vh.modelo} ({vh.categoria})")
    
    while True:
        try:
            seleccion = int(input("Ingrese el número del vehículo: "))
            if 1 <= seleccion <= len(lista_vehiculos):
                return lista_vehiculos[seleccion - 1]
            else:
                print("Opción no válida. Por favor, seleccione un número de la lista.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Lista de vehículos registrados
vehiculos_registrados = []

def menu():
    lista_vehiculos = []
    while True:
        print("\n--- Sistema de Renta de Vehículos ---")
        print("1. Añadir vehículo")
        print("2. Alquilar vehículo")
        print("3. Salir")
        
        try:
            opcion = int(input("Ingrese el número de la opción: "))
            
            if opcion == 1:
                añadir_vehiculo(lista_vehiculos)
            elif opcion == 2:
                vehiculo = seleccionar_vehiculo(lista_vehiculos)
                if vehiculo:
                    while True:
                        print("\n--- Opciones de Alquiler ---")
                        print("1. Iniciar alquiler")
                        print("2. Finalizar alquiler")
                        print("3. Mostrar costo del alquiler")
                        print("4. Volver al menú principal")
                        
                        try:
                            alquiler_opcion = int(input("Ingrese el número de la opción: "))
                            
                            if alquiler_opcion == 1:
                                iniciar_alquiler(vehiculo)
                            elif alquiler_opcion == 2:
                                finalizar_alquiler(vehiculo)
                            elif alquiler_opcion == 3:
                                mostrar_costo_alquiler(vehiculo)
                            elif alquiler_opcion == 4:
                                break
                            else:
                                print("Opción no válida. Por favor, seleccione una opción válida.")
                        except ValueError:
                            print("Entrada no válida. Por favor, ingrese un número.")
            elif opcion == 3:
                print("¡Gracias por usar el Sistema de Renta de Vehículos!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Llamada al menú para iniciar el programa
if __name__ == "__main__":
    menu()
