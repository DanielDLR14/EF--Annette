# Importar las clases necesarias para el sistema de gestión de inventario
from Venta import Venta
from Categoria import Categoria
from Producto import Producto
import locale
import datetime

# Configurar la localización
locale.setlocale(locale.LC_ALL, 'es_DO.UTF-8')

# Definir la lista de productos, categorías y ventas
lista_productos = []
lista_categorias = []
lista_ventas = []
sistema = {}
# Funciones auxiliares


def buscar_producto_por_nombre(nombre):
    for producto in lista_productos:
        if producto.nombre == nombre:
            return producto
    return None


def buscar_producto_por_categoria(categoria):
    productos_en_categoria = []
    for producto in lista_productos:
        if producto.categoria.nombre == categoria:
            productos_en_categoria.append(producto)
    return productos_en_categoria


def buscar_producto_por_precio(precio_min, precio_max):
    productos_en_precio = []
    for producto in lista_productos:
        if precio_min <= producto.precio <= precio_max:
            productos_en_precio.append(producto)
    return productos_en_precio

# Funciones para el menú de opciones


def mostrar_menu():
    print("╔══════════════════════════════════════════════════╗")
    print("║            Sistema de Gestión de Inventario      ║")
    print("╠══════════════╦═══════════════════════════════════╣")
    print("║   Acción     ║            Descripción            ║")
    print("╠══════════════╬═══════════════════════════════════╣")
    print("║     1        ║     Menu gestion de inventario    ║")
    print("║     2        ║     Informe de ventas por fecha   ║")
    print("║     3        ║ Informe ventas mayores a RD$1,200 ║")
    print("║     4        ║     Buscar producto por nombre    ║")
    print("║     5        ║     Buscar producto por categoria ║")
    print("║     6        ║     Buscar producto por precio    ║")
    print("║     7        ║               Salir               ║")
    print("╚══════════════╩═══════════════════════════════════╝")


def mostrar_submenu():
            print("╔══════════════════════════════════════════════════╗")
            print("║            Sistema de Gestión de Inventario      ║")
            print("╠══════════════╦═══════════════════════════════════╣")
            print("║   Acción     ║               Descripción         ║")
            print("╠══════════════╬═══════════════════════════════════╣")
            print("║     1        ║        Crear producto             ║")
            print("║     2        ║         Leer producto             ║")
            print("║     3        ║       Actualizar producto         ║")
            print("║     4        ║        Eliminar producto          ║")
            print("║     5        ║         Crear categoría           ║")
            print("║     6        ║         Leer categoría            ║")
            print("║     7        ║      Actualizar categoría         ║")
            print("║     8        ║       Eliminar categoría          ║")
            print("║     9        ║           Crear venta             ║")
            print("║     10       ║          Leer venta               ║")
            print("║     11       ║        Actualizar venta           ║")
            print("║     12       ║        Eliminar venta             ║")
            print("║     0        ║       Volver al menu principal    ║")
            print("╚══════════════╩═══════════════════════════════════╝")
            

def crear_producto():
    while True:
        try:
            # Pedimos los datos del producto al usuario
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = input("Ingrese el precio del producto: ")
            nombre_categoria = input("Ingrese la categoría del producto: ")
            
            # Validamos los datos ingresados
            if not nombre_producto.isalpha():
                raise ValueError("El nombre del producto solo puede contener letras.")
            if not precio_producto.isdigit():
                raise ValueError("El precio debe ser un número.")
            precio_producto = float(precio_producto)
            if not nombre_categoria.isalpha():
                raise ValueError("El nombre de la categoría solo puede contener letras.")
            
            # Buscamos la categoría en la lista de categorías
            categoria_existente = buscar_categoria_por_nombre(nombre_categoria)
            if categoria_existente is None:
                # Si la categoría no existe, le preguntamos al usuario si desea crearla
                while True:
                    print(f"La categoría '{nombre_categoria}' no existe en el sistema.")
                    crear_nueva_categoria = input("¿Desea crear una nueva categoría con este nombre? (s/n): ")
                    if crear_nueva_categoria.lower() == "s":
                        categoria_existente = crear_categoria()
                        break
                    elif crear_nueva_categoria.lower() == "n":
                        return
                    else:
                        print("Por favor ingrese 's' para crear una nueva categoría o 'n' para cancelar.")
            
            # Creamos el producto y lo agregamos a la lista de productos
            nuevo_producto = Producto(nombre_producto, precio_producto, categoria_existente)
            lista_productos.append(nuevo_producto)
            
            # Mostramos un mensaje de éxito al usuario
            precio_formateado = locale.currency(precio_producto, grouping=True)
            print(f"Se ha creado el producto {nuevo_producto.nombre} con un precio de {precio_formateado} y la categoría {nuevo_producto.categoria.nombre} exitosamente.")
            
            # Salimos de la función
            break
        
        except ValueError as e:
            # Si se produce un error de validación, informamos al usuario y volvemos al inicio del bucle
            print(f"Error: {e}. Intente de nuevo.")
            
        except Exception as e:
            # Si se produce un error inesperado, informamos al usuario y volvemos al inicio del bucle
            print(f"Ha ocurrido un error inesperado: {e}. Intente de nuevo.")



            





def leer_productos():
    # Establecer la configuración regional
    locale.setlocale(locale.LC_ALL, 'es_DO.UTF-8')
    print("\nLista de productos:")
    for producto in lista_productos:
        precio_formateado = locale.currency(producto.precio, grouping=True)
        print(
            f"Nombre: {producto.nombre}, Categoría: {producto.categoria}, Precio: {precio_formateado}")


def mostrar_productos():
    print("Lista de productos:")
    for producto in sistema.productos:
        print("Precio: " + str(producto.precio) + ", Categoría: " +
              str(producto.categoria) + ", Nombre: " + producto.nombre)


def actualizar_producto():
    # Se solicita el nombre del producto a actualizar
    nombre = input("Nombre del producto a actualizar: ")
    while True:
        try:
            # Se busca el producto en la lista de productos
            producto_existente = buscar_producto_por_nombre(nombre)
            if producto_existente is not None:
                # Se solicitan los nuevos datos del producto a actualizar
                print("Ingresa los nuevos datos del producto:")
                nuevo_nombre = input("Nombre: ")
                if not nuevo_nombre.isalpha():
                    raise ValueError("El nombre del producto solo puede contener letras.")
                nueva_categoria = input("Categoría: ")
                if not nueva_categoria.isalpha():
                    raise ValueError("El nombre de la categoría solo puede contener letras.")
                nuevo_precio = input("Precio: ")
                if not nuevo_precio.isdigit():
                    raise ValueError("El precio debe ser un número.")
                nuevo_precio = float(nuevo_precio)
                # Se actualiza el producto
                producto_existente.nombre = nuevo_nombre
                producto_existente.categoria = nueva_categoria
                producto_existente.precio = nuevo_precio
                print("El producto ha sido actualizado con éxito.")
                break
            else:
                print("El producto no existe en el inventario.")
                break
        except ValueError as e:
            print(f"Error: {e}. Intenta nuevamente.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}. Intenta nuevamente.")



def eliminar_producto():
    while True:
        try:
            # Se solicita el nombre del producto a eliminar
            nombre = input("Nombre del producto a eliminar: ")
            # Se busca el producto en la lista de productos
            producto_existente = buscar_producto_por_nombre(nombre)
            if producto_existente is not None:
                # Se elimina el producto
                lista_productos.remove(producto_existente)
                print("El producto ha sido eliminado del inventario.")
                break
            else:
                print("El producto no existe en el inventario.")
        except ValueError:
            print(
                "Error: el nombre del producto debe ser una cadena de texto. Intente de nuevo.")


def crear_categoria():
    while True:
        try:
            nombre_categoria = input("Ingrese el nombre de la categoría: ")
            if not nombre_categoria.isalpha():
                raise ValueError("El nombre de la categoría solo puede contener letras.")
            categoria_existente = buscar_categoria_por_nombre(nombre_categoria)
            if categoria_existente is not None:
                print(f"La categoría '{nombre_categoria}' ya existe en el sistema. Por favor ingrese otro nombre.")
                continue
            nueva_categoria = Categoria(nombre_categoria)
            lista_categorias.append(nueva_categoria)
            print(f"Se ha creado la categoría '{nueva_categoria.nombre}' exitosamente.")
            return nueva_categoria
        except ValueError as e:
            print(f"Error: {e}. Intente de nuevo.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}. Intente de nuevo.") 

    




def leer_categorias():
    print("Lista de categorías:")
    for categoria in lista_categorias:
        print(categoria.nombre)


def actualizar_categoria():
    while True:
        try:
            nombre = input("Nombre de la categoría a actualizar: ")
            if not nombre.isalpha():
                raise ValueError("El nombre de la categoría sólo puede contener letras.")
            categoria_existente = buscar_categoria_por_nombre(nombre)
            if categoria_existente is not None:
                nuevo_nombre = input("Nombre de la categoría: ")
                if not nuevo_nombre.isalpha():
                    raise ValueError("El nuevo nombre de la categoría sólo puede contener letras.")
                categoria_existente.nombre = nuevo_nombre
                print("La categoría ha sido actualizada con éxito.")
                break
            else:
                print("La categoría no existe en el sistema.")
                continue
        except ValueError as e:
            print(f"Error: {e}. Por favor, inténtalo de nuevo.")
            continue
        except:
            print("Ocurrió un error al actualizar la categoría. Por favor, inténtalo de nuevo.")
            continue



def buscar_categoria_por_nombre(nombre):
    for categoria in lista_categorias:
        if categoria.nombre == nombre:
            return categoria
    return None


def eliminar_categoria():
    while True:
        nombre = input("Nombre de la categoría a eliminar: ")
        if not nombre.isalpha():
            print("El nombre de la categoría solo puede contener letras.")
            continue
        try:
            categoria_existente = buscar_categoria_por_nombre(nombre)
            if categoria_existente is not None:
                lista_categorias.remove(categoria_existente)
                print("La categoría ha sido eliminada del sistema.")
                break
            else:
                print("La categoría no existe en el sistema.")
        except:
            print("Ocurrió un error al eliminar la categoría. Intente de nuevo.")






def es_fecha_valida(fecha):
    try:
        datetime.datetime.strptime(fecha, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def leer_ventas():
    print("Ventas realizadas:")
    for venta in lista_ventas:
        total = venta.calcular_total()
        total_str = "RD${:,.2f}".format(total)
        print(f"ID Venta: {venta.id_venta} - Producto: {venta.producto.nombre} - Cantidad: {venta.cantidad} - Fecha: {venta.fecha} - Total: {total_str}")




def crear_venta():
    datos_correctos = False
    while not datos_correctos:
        try:
            id_venta = int(input("Ingrese el ID de la venta: "))
            if buscar_venta_por_id(id_venta) is not None:
                print("Error: Ya existe una venta con ese ID.")
                continue
            nombre_producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad vendida: "))
            fecha_venta = input(
                "Ingrese la fecha de la venta (formato: yyyy-mm-dd): ")
            datetime.datetime.strptime(fecha_venta, '%Y-%m-%d')
            producto_existente = buscar_producto_por_nombre(nombre_producto)
            if producto_existente is not None:
                nueva_venta = Venta(
                    id_venta, producto_existente, cantidad, fecha_venta)
                lista_ventas.append(nueva_venta)
                print("La venta ha sido creada exitosamente.")
                datos_correctos = True
            else:
                print("El producto no existe en el inventario.")
        except ValueError:
            print("Error: Por favor introduzca cada dato correctamente.")
        except Exception as e:
            print("Error inesperado:", e)
            
def calcular_total(self):
    if self.producto is not None and self.producto.precio is not None:
        return self.cantidad * self.producto.precio
    else:
        return 0



def buscar_venta_por_id(id_venta):
    for venta in lista_ventas:
        if venta.id_venta == id_venta:
            return venta
    return None

def actualizar_venta():
    try:
        id_venta = int(input("Ingrese el ID de la venta que desea actualizar: "))
        venta_existente = buscar_venta_por_id(id_venta)
        if venta_existente is not None:
            nuevo_producto = buscar_producto_por_nombre(input("Ingrese el nuevo nombre del producto: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad vendida: "))
            nueva_fecha = input("Ingrese la nueva fecha de la venta (formato: yyyy-mm-dd): ")
            venta_existente.actualizar_venta(nuevo_producto, nueva_cantidad, nueva_fecha)
            print("La venta ha sido actualizada exitosamente.")
        else:
            print("La venta no existe.")
    except ValueError:
        print("Error: Debe ingresar un valor numérico en el campo ID de venta y cantidad.")
    except Exception as e:
        print("Error inesperado:", e)


def eliminar_venta():
    try:
        id_venta = int(input("Ingrese el ID de la venta a eliminar: "))
        venta_existente = buscar_venta_por_id(id_venta)
        if venta_existente is not None:
            lista_ventas.remove(venta_existente)
            print("La venta ha sido eliminada del sistema.")
        else:
            print("La venta no existe en el sistema.")
    except ValueError:
        print("Error: Debe ingresar un valor numérico en el campo ID de venta.")
    except Exception as e:
        print("Error inesperado:", e)
        

def informe_ventas_por_fecha():
    while True:
        fecha = input("Ingrese la fecha para la que desea generar el informe (formato: yyyy-mm-dd): ")
        try:
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
            break
        except ValueError:
            print("Fecha inválida. Por favor ingrese una fecha en formato yyyy-mm-dd.")
    
    ventas = Venta.ventas_por_fecha(fecha, lista_ventas)

    if not ventas:
        print("No se encontraron ventas para la fecha indicada.")
    else:
        total_ventas = 0
        print(f"Informe de ventas para la fecha {fecha}:\n")
        for venta in ventas:
            print(f"ID de venta: {venta.id_venta}")
            print(f"Producto: {venta.producto.nombre}")
            print(f"Cantidad: {venta.cantidad}")
            print(f"Precio unitario: ${venta.producto.precio}")
            print(f"Subtotal: ${venta.cantidad * venta.producto.precio}\n")
            total_ventas += venta.cantidad * venta.producto.precio

        print(f"Total de ventas para la fecha {fecha}: ${total_ventas}")


        
def informe_ventas_mayores_1200(valor_minimo, lista_ventas):
        productos_ventas_altas = []
        for producto, total_venta in lista_ventas:
            if total_venta > valor_minimo:
                productos_ventas_altas.append((producto, total_venta))
        return productos_ventas_altas

def generar_informe_ventas():
    ventas_por_producto = {}
    for venta in lista_ventas:
        producto = venta.producto
        total_vendido = producto.precio * venta.cantidad
        if producto.nombre in ventas_por_producto:
            ventas_por_producto[producto.nombre] += total_vendido
        else:
            ventas_por_producto[producto.nombre] = total_vendido
    
    productos_con_ventas_mayores_a_1200 = []
    for producto, total_vendido in ventas_por_producto.items():
        if total_vendido > 1200:
            productos_con_ventas_mayores_a_1200.append((producto, total_vendido))
    
    if len(productos_con_ventas_mayores_a_1200) > 0:
        print("Productos con ventas mayores a RD$1,200.00:")
        for producto, total_vendido in productos_con_ventas_mayores_a_1200:
            print(f"{producto}: RD${total_vendido:.2f}")
    else:
        print("No hay productos con ventas mayores a RD$1,200.00.")


def buscar_producto():
    nombre_producto = input("Ingrese el nombre del producto que desea buscar: ")
    producto_encontrado = buscar_producto_por_nombre(nombre_producto)
    if producto_encontrado:
        print(f"El producto '{nombre_producto}' ha sido encontrado en la lista de productos.")
        # Aquí puedes hacer lo que quieras con el producto encontrado
    else:
        print(f"No se ha encontrado ningún producto con el nombre '{nombre_producto}'.")

def buscar_productos_por_categoria(nombre_categoria):
    productos_encontrados = []
    for producto in lista_productos:
        if producto.categoria.nombre == nombre_categoria:
            productos_encontrados.append(producto)
    if productos_encontrados:
        print(f"Se han encontrado los siguientes productos en la categoría '{nombre_categoria}':")
        for producto in productos_encontrados:
            print(f"- {producto.nombre}")
    else:
        print(f"No se han encontrado productos en la categoría '{nombre_categoria}'.")
    return productos_encontrados
    
def buscar_producto_por_precio():
    while True:
        try:
            # Pedimos el precio del producto al usuario
            precio_producto = input("Ingrese el precio del producto que desea buscar: ")

            # Validamos el precio ingresado
            if not precio_producto.isdigit():
                raise ValueError("El precio debe ser un número.")
            precio_producto = float(precio_producto)

            # Buscamos el producto en la lista de productos
            producto_encontrado = None
            for producto in lista_productos:
                if producto.precio == precio_producto:
                    producto_encontrado = producto
                    break

            if producto_encontrado is None:
                # Si no se encuentra el producto, mostramos un mensaje al usuario y volvemos al inicio del bucle
                print(f"No se encontró ningún producto con el precio {precio_producto}.")
                continue

            # Si se encontró el producto, mostramos sus detalles al usuario y salimos de la función
            precio_formateado = locale.currency(producto_encontrado.precio, grouping=True)
            print(f"El producto encontrado es '{producto_encontrado.nombre}' con un precio de {precio_formateado} y la categoría {producto_encontrado.categoria.nombre}.")

            break

        except ValueError as e:
            # Si se produce un error de validación, informamos al usuario y volvemos al inicio del bucle
            print(f"Error: {e}. Intente de nuevo.")

        except Exception as e:
            # Si se produce un error inesperado, informamos al usuario y volvemos al inicio del bucle
            print(f"Ha ocurrido un error inesperado: {e}. Intente de nuevo.")






while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        while True:
            mostrar_submenu()
            opcion_submenu = input("Ingrese una opción: ")
            if opcion_submenu == "1":
                crear_producto()
            elif opcion_submenu == "2":
                leer_productos()
            elif opcion_submenu == "3":
                actualizar_producto()
            elif opcion_submenu == "4":
                eliminar_producto()
            elif opcion_submenu == "5":
                crear_categoria()
            elif opcion_submenu == "6":
                leer_categorias()
            elif opcion_submenu == "7":
                actualizar_categoria()
            elif opcion_submenu == "8":
                eliminar_categoria()
            elif opcion_submenu == "9":
                crear_venta()
            elif opcion_submenu == "10":
                leer_ventas()
            elif opcion_submenu == "11":
                actualizar_venta()
            elif opcion_submenu == "12":
                eliminar_venta()
            elif opcion_submenu == "0":
                break # salir del bucle del submenú y volver al menú principal
            else:
                print("Opción no válida. Intente nuevamente.")
    elif opcion == "2":
        informe_ventas_por_fecha()
    elif opcion == "3":
        generar_informe_ventas()    
    elif opcion == "4":
        buscar_producto()  
    elif opcion == "5":
        buscar_productos_por_categoria()  
    elif opcion == "6":
        buscar_producto()
    elif opcion == "7":
        break 
    else:
        print("Opción no válida. Intente nuevamente.")


