class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return str(self.nombre)


class Inventario:
    def __init__(self):
        self.categorias = []

    def crear_categoria(self):
        # Se solicita el nombre de la categoría a crear
        nombre = input("Nombre de la categoría a crear: ")
        # Se crea la categoría y se agrega a la lista de categorías del inventario
        categoria = Categoria(nombre)
        self.categorias.append(categoria)
        print("La categoría ha sido creada con éxito.")

    def leer_categorias(self):
        # Se muestran las categorías del inventario
        for categoria in self.categorias:
            print(categoria.nombre)

    def buscar_categoria_por_nombre(self, nombre):
    # Se busca una categoría por su nombre
        for categoria in self.categorias:
            if categoria.nombre == nombre:
                return categoria
        return None


    def actualizar_categoria(self):
        while True:
        # Se solicita el nombre de la categoría a actualizar
            nombre = input("Nombre de la categoría a actualizar: ")
        # Se busca la categoría en la lista de categorías
            categoria_existente = self.buscar_categoria_por_nombre(nombre)
            if categoria_existente is not None:
            # Se solicita el nuevo nombre de la categoría
                nuevo_nombre = input("Nuevo nombre de la categoría: ")
            # Se actualiza el nombre de la categoría
                categoria_existente.nombre = nuevo_nombre
                print("La categoría ha sido actualizada con éxito.")
                break
            else:
                print("La categoría no existe en el inventario. Por favor, inténtelo de nuevo.")


    def eliminar_categoria(self):
        # Se solicita el nombre de la categoría a eliminar
        nombre = input("Nombre de la categoría a eliminar: ")
        # Se busca la categoría en la lista de categorías
        categoria_existente = self.buscar_categoria_por_nombre(nombre)
        if categoria_existente is not None:
            # Se elimina la categoría de la lista de categorías del inventario
            self.categorias.remove(categoria_existente)
            print("La categoría ha sido eliminada del inventario.")
        else:
            print("La categoría no existe en el inventario.")
