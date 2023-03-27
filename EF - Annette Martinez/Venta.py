class Venta:
    
    def __init__(self, id_venta, producto, cantidad, fecha):
        self.id_venta = id_venta
        self.producto = producto
        self.cantidad = cantidad
        self.fecha = fecha
    
    def leer_venta(self):
        total = self.calcular_total()
        return f"ID Venta: {self.id_venta} - Producto: {self.producto.nombre} - Cantidad: {self.cantidad} - Fecha: {self.fecha} - Total: {total}"

    def calcular_total(self):
        return self.cantidad * self.producto.precio

    def actualizar_venta(self, nuevo_producto, nueva_cantidad, nueva_fecha):
        self.producto = nuevo_producto
        self.cantidad = nueva_cantidad
        self.fecha = nueva_fecha

    def eliminar_venta(self, lista_ventas):
        lista_ventas.remove(self)

    @staticmethod
    def ventas_por_fecha(fecha, lista_ventas):
        ventas_fecha = []
        for venta in lista_ventas:
            if venta.fecha == fecha:
                ventas_fecha.append(venta)
        return ventas_fecha
    
    
    