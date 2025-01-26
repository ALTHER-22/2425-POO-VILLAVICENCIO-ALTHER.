# Clase que representa un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor):
        """Constructor que inicializa el título y el autor del libro."""
        self.titulo = titulo
        self.autor = autor
        print(f"Libro '{self.titulo}' de {self.autor} creado.")

    def __del__(self):
        """Destructor que se activa al eliminar un libro."""
        print(f"Libro '{self.titulo}' de {self.autor} eliminado.")

# Clase que simula una conexión a una base de datos
class BaseDeDatos:
    def __init__(self, nombre):
        """Constructor que inicializa la conexión a la base de datos."""
        self.nombre = nombre
        self.conectado = True
        print(f"Conexión a la base de datos '{self.nombre}' establecida.")

    def __del__(self):
        """Destructor que se activa al cerrar la conexión."""
        if self.conectado:
            print(f"Conexión a la base de datos '{self.nombre}' cerrada.")
            self.conectado = False

# Clase principal que gestiona los libros y la base de datos
class Biblioteca:
    def __init__(self, nombre):
        """Constructor que inicializa la biblioteca y su base de datos."""
        self.nombre = nombre
        self.base_datos = BaseDeDatos(f"DB_{nombre}")
        self.libros = []
        print(f"Biblioteca '{self.nombre}' inicializada.")

    def agregar_libro(self, titulo, autor):
        """Agrega un libro a la biblioteca."""
        libro = Libro(titulo, autor)
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        """Elimina un libro de la biblioteca si existe."""
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                del libro
                print(f"Libro '{titulo}' eliminado de la biblioteca.")
                return
        print(f"Libro '{titulo}' no encontrado.")

    def __del__(self):
        """Destructor que se activa al cerrar la biblioteca."""
        print(f"Cerrando biblioteca '{self.nombre}'.")
        for libro in self.libros:
            del libro
        del self.base_datos
        print(f"Biblioteca '{self.nombre}' cerrada.")

# Ejemplo de uso
def main():
    # Crear una biblioteca
    mi_biblioteca = Biblioteca("Central")

    # Agregar libros a la biblioteca
    mi_biblioteca.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez")
    mi_biblioteca.agregar_libro("El Principito", "Antoine de Saint-Exupéry")

    # Eliminar un libro
    mi_biblioteca.eliminar_libro("El Principito")

    # Cerrar la biblioteca (se activan los destructores)
    del mi_biblioteca

if __name__ == "__main__":
    main()
