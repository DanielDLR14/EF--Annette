

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.lista_productos = []

    def __repr__(self):
        return f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}"

    def crear_producto(self):
        self.lista_productos.append(self)

    def leer_producto(self):
        return f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}"

    def actualizar_producto(self, nuevo_nombre, nueva_categoria, nuevo_precio):
        self.nombre = nuevo_nombre
        self.categoria = nueva_categoria
        self.precio = nuevo_precio

    def eliminar_producto(self):
        self.lista_productos.remove(self)
    
    
