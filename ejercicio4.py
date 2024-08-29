"""
Una empresa de renta de transporte tiene varios tipos de vehículos a su
disposición cada uno con sus características y coste de renta. La
empresa periódicamente registra los nuevos vehículos que ingresan al
lote para su posterior puesta en renta.
"""
class Renta:
    def _init_(self, marcaAuto, modeloAuto, anioAuto, colorAuto, tipoMotorAuto, 
                 transmisionAuto, PrecioCompra, kilometrajeAuto, placaAuto, renta):
        self.marca = marcaAuto
        self.modelo = modeloAuto
        self.anio = anioAuto
        self.color = colorAuto
        self.tipoMotor = tipoMotorAuto
        self.transmision = transmisionAuto
        self.precioCompra = float(PrecioCompra)
        self.kilometraje = kilometrajeAuto
        self.placa = placaAuto.upper()
        self.renta = float(renta)

    def salidaAutosNuevos(self):
        print(f"---------------------------------------------\n"+
              "Datos del auto: \n"+
              "..............................................\n"+
              f"Marca: {self.marca}\n"+
              f"Modelo: {self.modelo}\n"+
              f"Color: {self.color}\n"+
              f"Tipo de motor: {self.tipoMotor}\n"+
              f"Kilometraje: {self.kilometraje} KM\n"+
              f"Placa: {self.placa}\n"+
              f"Año: {self.anio}\n"+
              f"Transmisión: {self.transmision}\n"+
              f"Precio de Compra: {self.precioCompra}\n"+
              f"Precio de Renta: {self.renta}\n"+
              "..............................................\n")


def registrarAuto():
    A_marca = input("Ingrese la marca del auto: ")
    A_modelo = input("Ingrese el modelo del auto: ")
    A_anio = input("Ingrese el año del auto: ")
    A_color = input("Ingrese el color del auto: ")
    A_motor = input("Ingrese el tipo de motor del auto: ")
    A_transmision = input("Ingrese el tipo de transmisión del auto: ")
    A_kilometraje = input("Ingrese el kilometraje del auto: ")
    A_placa = input("Ingrese el número de placa del auto: ")
    A_precio = input("Ingrese el precio de compra del auto: ")
    A_renta = input("Ingrese el precio de renta: ")
    return Renta(A_marca, A_modelo, A_anio, A_color, A_motor,
                 A_transmision, A_precio, A_kilometraje, A_placa, A_renta)


def registrarCliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    dui = input("Ingrese su DUI: ")
    return nombre, apellido, edad, dui


def inicial():
    registrados = []
    while True:
        tipo_usuario = input("¿Es usted un cliente (Ingrese C) o administrador (Ingrese A)? ").upper()
        if tipo_usuario == "A":
            auto = registrarAuto()
            registrados.append(auto)
            auto.salidaAutosNuevos()
        elif tipo_usuario == "C":
            if not registrados:
                print("No hay autos disponibles para alquilar.")
            else:
                nombre, apellido, edad, dui = registrarCliente()
                print("Autos disponibles:")
                for index, auto in enumerate(registrados):
                    print(f"{index + 1}. {auto.marca} {auto.modelo} ({auto.anio}) - {auto.color}")
                seleccionAuto = int(input("Ingrese el número del auto que desea alquilar: ")) - 1
                if 0 <= seleccionAuto < len(registrados):
                    autoSeleccionado = registrados[seleccionAuto]
                    print("------------------------------------------"+
                          "\nHas seleccionado el siguiente auto:")
                    autoSeleccionado.salidaAutosNuevos()
                    print(f"Datos del cliente:\nNombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDUI: {dui}\n"+
                          "------------------------------------------")
                    break
                else:
                    print("Selección no válida.")
        else:
            print("Opción no válida. Intente nuevamente.")
inicial()