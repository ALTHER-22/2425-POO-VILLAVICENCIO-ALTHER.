class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (titulo, autor)  # Tupla para mantener título y autor inmutables
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.datos[0]} por {self.datos[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para almacenar libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya está en la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario.nombre}")
        else:
            print("El ID de usuario ya está registrado.")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)  # Removemos el libro de la biblioteca
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.datos[0]}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro  # Devolvemos el libro a la biblioteca
                    print(f"Libro '{libro.datos[0]}' devuelto por {usuario.nombre}.")
                    return
        print("No se encontró el libro prestado.")

    def buscar_libro(self, keyword):
        resultados = [libro for libro in self.libros.values()
                      if keyword.lower() in libro.datos[0].lower()
                      or keyword.lower() in libro.datos[1].lower()
                      or keyword.lower() in libro.categoria.lower()]
        if resultados:
            print("Resultados de búsqueda:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("Este usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Pruebas del sistema
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("1984", "George Orwell", "Ficción", "12345")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", "67890")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Carlos Pérez", "U001")
usuario2 = Usuario("Ana Gómez", "U002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("U001", "12345")

# Listar libros prestados
biblioteca.listar_libros_prestados("U001")

# Devolver libros
biblioteca.devolver_libro("U001", "12345")

# Buscar libros
biblioteca.buscar_libro("realismo")
