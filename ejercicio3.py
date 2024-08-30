#Se almaceno las características del hotel y las prestaciones con las que puede contar en una clase como unicos atributos 
#luego de aborda mediante un menú principal las características de la reserva a ejecutarse por el usuario
#Dado a que se manejan diversas opciones es mas eficiente evaluarlas mediante números (del 1 al 3 usualmente) con un If que 
#Evalúe la respuesta, luego se recolectan los datos y se imprimirán en una función con los parámetros de las opciones seleccionadas
#Anteriormente en el menú.


class Hotel:
    def __init__(self):
        self.habitaciones = {
            'Sencilla': 50,
            'Doble': 80,
            'Suite': 120
        }
        
        self.servicios_extra = {
            'Piscina': 10,
            'Cancha de Golf': 20,
            'Gimnasio': 15
        }
#mostrar opciones de habitaciones y servicios
    def mostrar_habitaciones(self):
        print("Opciones de habitaciones disponibles:")
        for tipo, precio in self.habitaciones.items():
            print(f"{tipo}: ${precio} por noche")

    def mostrar_servicios_extra(self):
        print("Servicios extra disponibles:")
        for servicio, costo in self.servicios_extra.items():
            print(f"{servicio}: ${costo} adicional")
#calcular total
    def calcular_total(self, tipo_habitacion, noches, servicios_seleccionados):
        precio_noche = self.habitaciones[tipo_habitacion]
        costo_habitacion = precio_noche * noches
        costo_servicios = sum(self.servicios_extra[servicio] for servicio in servicios_seleccionados)
        total = costo_habitacion + costo_servicios
        return total
#emitir la factura
    def emitir_factura(self, nombre, tipo_habitacion, noches, servicios_seleccionados):
        total = self.calcular_total(tipo_habitacion, noches, servicios_seleccionados)
        print("\nFactura detallada:")
        print(f"Nombre del cliente: {nombre}")
        print(f"Tipo de habitación: {tipo_habitacion}")
        print(f"Número de noches: {noches}")
        print(f"Servicios adicionales: {', '.join(servicios_seleccionados) if servicios_seleccionados else 'Ninguno'}")
        print(f"Total a pagar: ${total}")

#Función de menú principal
def main():
    hotel = Hotel()
    
    hotel.mostrar_habitaciones()
    
    nombre = input("\nIngrese su nombre: ")
    tipo_habitacion_num = int(input("Seleccione el tipo de habitación (1: Sencilla $50, 2: Doble $80, 3: Suite $120): "))
    
    tipos_habitacion = list(hotel.habitaciones.keys())
    if 1 <= tipo_habitacion_num <= len(tipos_habitacion):
        tipo_habitacion = tipos_habitacion[tipo_habitacion_num - 1]
    else:
        print("Opción no válida. Se seleccionará la habitación más económica (Sencilla).")
        tipo_habitacion = 'Sencilla'
    
    noches = int(input("Número de noches que se hospedará: "))
    
    hotel.mostrar_servicios_extra()
    servicios = input("Ingrese los servicios extra deseados (separados por coma, por ejemplo: Piscina $10, Cancha de Golf $20, Gimnasio $15): ")
    servicios_seleccionados = [s.strip() for s in servicios.split(',') if s.strip() in hotel.servicios_extra]
    
    hotel.emitir_factura(nombre, tipo_habitacion, noches, servicios_seleccionados)

main()
print("Integrante 1: Oscar Rene Palacios Franco SMSS065523")
print("Integrante 2 : Gerson Manases Flores Quinteros SMSS040923")
