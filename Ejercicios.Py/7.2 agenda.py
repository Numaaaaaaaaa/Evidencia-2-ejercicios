class AgendaTelefonica:
    def __init__(self):
        self.agenda = {}

    def mostrar_menu(self):
        print("\nMenú de opciones:")
        print("1. Agregar una persona")
        print("2. Modificar una persona")
        print("3. Eliminar una persona")
        print("4. Mostrar toda la agenda")
        print("5. Salir")

    def agregar_persona(self):
        apellido = input("Ingrese el apellido de la persona: ")
        nombre = input("Ingrese el nombre de la persona: ")
        dni = input("Ingrese el DNI de la persona: ")
        email = input("Ingrese el email de la persona: ")
        telefono = input("Ingrese el número de teléfono de la persona: ")
        self.agenda[dni] = {"apellido": apellido, "nombre": nombre, "email": email, "telefono": telefono}
        print("Persona agregada exitosamente.")

    def modificar_persona(self):
        dni = input("Ingrese el DNI de la persona que desea modificar: ")
        if dni in self.agenda:
            print("Datos actuales de la persona:")
            print(self.agenda[dni])
            opcion = input("¿Desea modificar esta persona? (s/n): ")
            if opcion.lower() == 's':
                self.agenda[dni]["apellido"] = input("Ingrese el nuevo apellido de la persona: ")
                self.agenda[dni]["nombre"] = input("Ingrese el nuevo nombre de la persona: ")
                self.agenda[dni]["email"] = input("Ingrese el nuevo email de la persona: ")
                self.agenda[dni]["telefono"] = input("Ingrese el nuevo número de teléfono de la persona: ")
                print("Persona modificada exitosamente.")
            else:
                print("No se realizaron modificaciones.")
        else:
            print("El DNI ingresado no corresponde a ninguna persona en la agenda.")

    def eliminar_persona(self):
        dni = input("Ingrese el DNI de la persona que desea eliminar: ")
        if dni in self.agenda:
            del self.agenda[dni]
            print("Persona eliminada exitosamente.")
        else:
            print("El DNI ingresado no corresponde a ninguna persona en la agenda.")

    def mostrar_agenda(self):
        print("\nAgenda Telefónica:")
        for dni, persona in self.agenda.items():
            print(f"DNI: {dni}, Apellido: {persona['apellido']}, Nombre: {persona['nombre']}, Email: {persona['email']}, Teléfono: {persona['telefono']}")

    def main(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.agregar_persona()
            elif opcion == '2':
                self.modificar_persona()
            elif opcion == '3':
                self.eliminar_persona()
            elif opcion == '4':
                self.mostrar_agenda()
            elif opcion == '5':
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")


if __name__ == "__main__":
    agenda = AgendaTelefonica()
    agenda.main()
