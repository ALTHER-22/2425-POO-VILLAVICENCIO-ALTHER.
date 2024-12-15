# Programación Tradicional

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    """
    Permite al usuario ingresar las temperaturas diarias de la semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = []
    print("Por favor, ingresa las temperaturas diarias de la semana:")
    for i in range(7):  # Una semana tiene 7 días
        temp = float(input(f"Temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    :param temperaturas: Lista de temperaturas diarias.
    :return: Promedio de las temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)


# Función principal del programa
def main():
    """
    Función principal para ejecutar la lógica de programación tradicional.
    """
    print("Cálculo de promedio semanal - Programación Tradicional")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")


# Ejecutar el programa en modo tradicional
if __name__ == "__main__":
    main()


# Programación Orientada a Objetos (POO)

class Clima:
    """
    Clase que representa el registro de temperaturas de una semana.
    Contiene métodos para ingresar temperaturas y calcular el promedio.
    """

    def __init__(self):
        # Lista para almacenar las temperaturas diarias
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """
        Permite al usuario ingresar las temperaturas diarias de la semana.
        """
        print("Por favor, ingresa las temperaturas diarias de la semana:")
        for i in range(7):  # Una semana tiene 7 días
            temp = float(input(f"Temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Calcula el promedio semanal de las temperaturas ingresadas.
        :return: Promedio de las temperaturas.
        """
        if not self.temperaturas:
            raise ValueError("No se han ingresado temperaturas.")
        return sum(self.temperaturas) / len(self.temperaturas)


# Función principal del programa
def main():
    """
    Función principal para ejecutar la lógica orientada a objetos.
    """
    print("Cálculo de promedio semanal - Programación Orientada a Objetos")
    clima = Clima()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")


# Ejecutar el programa en modo POO
if __name__ == "__main__":
    main()
