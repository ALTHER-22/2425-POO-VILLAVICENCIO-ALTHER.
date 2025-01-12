# Sistema de Reservas de Habitaciones en un Hotel

class Habitacion:
    """Clase que representa una habitación en un hotel."""

    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo  # Puede ser "sencilla", "doble", "suite"
        self.precio = precio
        self.ocupada = False

    def reservar(self):
        """Marca la habitación como ocupada si está disponible."""
        if not self.ocupada:
            self.ocupada = True
            return True
        return False

    def liberar(self):
        """Marca la habitación como disponible."""
        self.ocupada = False

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitación {self.numero} ({self.tipo}): ${self.precio} - {estado}"


class Cliente:
    """Clase que representa a un cliente del hotel."""

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}, Teléfono: {self.telefono}"


class Hotel:
    """Clase que representa el hotel y gestiona las habitaciones y reservas."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación al inventario del hotel."""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        """Muestra todas las habitaciones disponibles para reservar."""
        disponibles = [hab for hab in self.habitaciones if not hab.ocupada]
        if disponibles:
            print("Habitaciones disponibles:")
            for hab in disponibles:
                print(hab)
        else:
            print("No hay habitaciones disponibles.")

    def reservar_habitacion(self, numero, cliente):
        """Reserva una habitación si está disponible."""
        for hab in self.habitaciones:
            if hab.numero == numero:
                if hab.reservar():
                    print(f"\nReserva confirmada para {cliente.nombre} en la habitación {numero}.")
                    return True
                else:
                    print(f"\nLa habitación {numero} ya está ocupada.")
                    return False
        print(f"\nLa habitación {numero} no existe en el hotel.")
        return False

    def liberar_habitacion(self, numero):
        """Libera una habitación para que esté disponible nuevamente."""
        for hab in self.habitaciones:
            if hab.numero == numero:
                if hab.ocupada:
                    hab.liberar()
                    print(f"\nLa habitación {numero} ha sido liberada y ahora está disponible.")
                    return True
                else:
                    print(f"\nLa habitación {numero} ya estaba disponible.")
                    return False
        print(f"\nLa habitación {numero} no existe en el hotel.")
        return False


# Ejemplo de uso
if __name__ == "__main__":
    # Crear el hotel
    mi_hotel = Hotel("Hotel Paradiso")

    # Agregar habitaciones
    mi_hotel.agregar_habitacion(Habitacion(101, "sencilla", 50))
    mi_hotel.agregar_habitacion(Habitacion(102, "doble", 75))
    mi_hotel.agregar_habitacion(Habitacion(201, "suite", 150))

    # Crear cliente
    cliente1 = Cliente("Ana Pérez", "0987654321")

    # Mostrar habitaciones disponibles
    mi_hotel.mostrar_habitaciones_disponibles()

    # Reservar una habitación
    mi_hotel.reservar_habitacion(101, cliente1)

    # Mostrar habitaciones disponibles después de reservar
    mi_hotel.mostrar_habitaciones_disponibles()

    # Liberar una habitación
    mi_hotel.liberar_habitacion(101)

    # Mostrar habitaciones disponibles después de liberar
    mi_hotel.mostrar_habitaciones_disponibles()
