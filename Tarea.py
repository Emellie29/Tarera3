class Cliente:
    def _init_(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.mascotas = []

    def agregarMascota(self, mascota):
        self.mascotas.append(mascota)

class Mascota:
    def _init_(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.historial = []

    def agregar_cita(self, cita):
        self.historial.append(cita)

class Citamedica:
    def _init_(self, fecha, motivo, diagnostico):
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostico = diagnostico

class Veterinaria:
    def _init_(self):
        self.Clientes = []

    def Registrar_Cliente(self, nombre, telefono, correo):
        cliente = Cliente(nombre, telefono, correo)
        self.Clientes.append(cliente)
        print("Cliente registrado correctamente")

    def buscar_cliente(self, nombre):
        for cliente in self.Clientes:
            if cliente.nombre.lower() == nombre.lower():
                return cliente
        return None

    def Registrar_Mascota(self, nombre_Cliente, nombre_Mascota, especie, raza, edad):
        cliente = self.buscar_cliente(nombre_Cliente)
        if cliente:
            mascota = Mascota(nombre_Mascota, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            print("Mascota registrada correctamente")
        else:
            print("Cliente no existe")

    def AgendarMascota(self, nombre_Cliente, nombre_Mascota, diagnostico, motivo, fecha):
        cliente = self.buscar_cliente(nombre_Cliente)
        if cliente:
            for mascota in cliente.mascotas:
                if mascota.nombre.lower() == nombre_Mascota.lower():
                    cita = Citamedica(fecha, motivo, diagnostico)
                    mascota.agregar_cita(cita)
                    print("Mascota agregada correctamente")
                    return
                print("Mascota no existe")
            else:
                print("Cliente no existe")

    def mostrar_historial(self, nombre_cliente, nombre_mascota):
        cliente = self.buscar_cliente(nombre_cliente)
        if cliente:
            for mascota in cliente.mascotas:
                if mascota.nombre.lower() == nombre_mascota.lower():
                    if mascota.historial:
                        print(f"Historial médico de {mascota.nombre}:")
                        for cita in mascota.historial:
                            print(f"- {cita.fecha}: {cita.motivo} → {cita.diagnostico}")
                    else:
                         print("ℹ No hay citas registradas.")
                    return
            print("Mascota no encontrada.")
        else:
             print("Cliente no encontrado.")

    def Ver_clientesMascotas(self):
        for cliente in self.Clientes:
            print(f"{cliente.nombre}  ({cliente.telefono}, {cliente.correo})")
            for mascota in cliente.mascotas:
                print(f"{mascota.nombre}, {mascota.especie}, {mascota.raza}, {mascota.edad} años")

veterinaria = Veterinaria()

while True:
    print("Bienvenido a la clinica ")
    print("1 Registrar nuevo Cliente")
    print("2 Registrar nuevo Mascota")
    print("3 agendar cita medica")
    print("4. ver historial de citas")
    print("5. Ver clientes y Mascotas")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre = input("Nombre del cliente: ")
        telefono = input("Telefono del cliente: ")
        correo = input("Correo del cliente: ")
        veterinaria.Registrar_Cliente(nombre, telefono, correo)

    elif opcion == "2":
        nombre_Cliente = input("Nombre del cliente: ")
        nombre_mascota = input("Nombre del mascota: ")
        especie = input("Especie: ")
        raza = input("Raza: ")
        edad = input("Edad: ")
        veterinaria.Registrar_Mascota(nombre_Cliente, nombre_mascota, especie, raza, edad)

    elif opcion == "3":
        nombre_Cliente = input("Nombre del cliente: ")
        nombre_mascota = input("Nombre del mascota: ")
        fecha = input("Fecha de la cita (DD/MM/AAAA): ")
        motivo = input("Motivo de la consulta: ")
        diagnostico = input("Diagnostico: ")
        veterinaria.AgendarMascota(nombre_Cliente, nombre_mascota, fecha, motivo, diagnostico)

    elif opcion == "4":
        nombre_Cliente = input("Nombre del cliente: ")
        nombre_mascota = input("Nombre del mascota: ")
        veterinaria.mostrar_historial(nombre_Cliente, nombre_mascota)

    elif opcion == "5":
        veterinaria.Ver_clientesMascotas()

    elif opcion == "6":
        print("Gracias por usar el sistema de la veterinaria")
        break
    else:
        print("Opcion no valida")