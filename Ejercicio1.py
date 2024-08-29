"""
Un consultorio médico atiende a una serie de pacientes, solo está una
secretaria y en el consultorio hay varios doctores cada paciente llega y
deja sus datos además del motivo de su consulta y posteriormente la
secretaria les asigna la fecha de su consulta.
 En el caso que una persona ya tenga una consulta previa en lugar
de tomar datos se le pasará a sala de esperas. Implementa esta
problemática a tu código.
"""

#Creamos una clase llamada paciente para ingresar nuevos pacientes
class Paciente():
    def __init__(self, nombre=""):
        self.nombre = nombre
        self.edad = 0
        self.peso = 0
        self.bpm = 0
        self.PA = ""
        self.motivoConsulta = ""
        self.__estado = "Registrado"
        self.fechaConsulta = ""

    def cambiarEstado(self):
        self.__estado = "Sala de Esperas"
        return self.__estado

#Guardamos un listado donde se almacenan los nombres de cada Paciente
listadoPacientes = []

#Funcion para mostrar los datos de cada paciente
def mostrarDatos(paciente):
    print("Nombre: ", paciente.nombre)
    print("Edad: ", paciente.edad)
    print("Motivo de Consulta: ", paciente.motivoConsulta)
    print("Fecha de consulta: ", paciente.fechaConsulta)
    print("Estado: ", paciente.cambiarEstado())

#Funcion que obtiene los datos de cada paciente
def obtenerDatos(paciente):
    print("***** Registro Paciente *******")
    paciente.edad = input(f"Ingrese la edad: ")
    paciente.peso = input("Peso del paciente (kg): ")
    paciente.bpm = input("Frecuencia cardiaca del paciente (bpm): ")
    paciente.PA = input("Presion Arterial: ")
    paciente.motivoConsulta = input("Motivo de consulta: ")
    paciente.fechaConsulta = input("Fecha de Consulta: ")
    print("***** Registrado Satisfactoriamente *****")

#Evalua si el nombre del paciente existe ya en el sistema
while True:
    print("****** Sistema de gestion de Pacientes ******")
    nombrePaciente = input("Ingrese el nombre del paciente: ")

    pacienteEncontrado = None
    for paciente in listadoPacientes:
#Si el paciente existe, cambia su estado
        if paciente.nombre == nombrePaciente:
            pacienteEncontrado = paciente
            break
    
    if pacienteEncontrado:
        print("***** Paciente encontrado *******")
        mostrarDatos(pacienteEncontrado)

#Si no lo encuentra, comienza el registro del paciente
    else:
        print("***** Paciente no encontrado, registrando nuevo paciente *******")
        nuevoPaciente = Paciente(nombre=nombrePaciente)
        obtenerDatos(nuevoPaciente)
        listadoPacientes.append(nuevoPaciente)
        print(f"Paciente {nuevoPaciente.nombre} registrado exitosamente.")