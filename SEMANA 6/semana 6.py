# Clase base: Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo público
        self.modelo = modelo  # Atributo público

    def arrancar(self):
        return f"El vehículo {self.marca} {self.modelo} está arrancando."

# Clase derivada: Coche (hereda de Vehiculo)
class Coche(Vehiculo):
    def __init__(self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.numero_puertas = numero_puertas  # Atributo adicional específico de Coche

    def arrancar(self):
        # Sobrescritura del método arrancar para personalizarlo
        return f"El coche {self.marca} {self.modelo} con {self.numero_puertas} puertas está arrancando."

# Clase encapsulada: CuentaBancaria
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado para encapsular el saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depositado: {cantidad}. Nuevo saldo: {self.__saldo}"
        else:
            return "La cantidad a depositar debe ser positiva."

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retirado: {cantidad}. Nuevo saldo: {self.__saldo}"
        else:
            return "Fondos insuficientes."

    def obtener_saldo(self):
        return self.__saldo  # Método getter para acceder al saldo

# Clase base: DispositivoElectronico
class DispositivoElectronico:
    def encender(self):
        return "Dispositivo electrónico encendido"

# Clase derivada: Telefono
class Telefono(DispositivoElectronico):
    def encender(self):
        # Sobrescritura del método encender (Polimorfismo)
        return "Teléfono encendido y listo para usar"

# Clase derivada: Computadora
class Computadora(DispositivoElectronico):
    def encender(self):
        # Sobrescritura del método encender (Polimorfismo)
        return "Computadora arrancando, bienvenido"

# Programa principal
def main():
    # Herencia
    mi_coche = Coche("Toyota", "Corolla", 4)
    print(mi_coche.arrancar())

    # Encapsulación
    mi_cuenta = CuentaBancaria(1000)
    print(mi_cuenta.obtener_saldo())  # Consultar saldo inicial
    print(mi_cuenta.depositar(500))  # Realizar un depósito
    print(mi_cuenta.retirar(200))  # Realizar un retiro

    # Polimorfismo
    mi_telefono = Telefono()
    mi_computadora = Computadora()
    print(mi_telefono.encender())  # Método sobrescrito en Telefono
    print(mi_computadora.encender())  # Método sobrescrito en Computadora

if __name__ == "__main__":
    main()
