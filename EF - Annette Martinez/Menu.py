# Importar las clases necesarias para el sistema de gestión de inventario
from Venta import Venta
from Categoria import Categoria
from Producto import Producto
import locale
import datetime
import csv
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
    print("║     1        ║    Menu gestion de inventario     ║")
    print("║     2        ║    Menu busqueda de productos     ║")
    print("║     3        ║    Menu importacion y exportacion ║")
    print("║     4        ║ Informe ventas mayores a RD$1,200 ║")
    print("║     5        ║               Salir               ║")
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


def mostrar_submenu2():
    print("╔══════════════════════════════════════════════════╗")
    print("║            Sistema de Gestión de Inventario      ║")
    print("╠══════════════╦═══════════════════════════════════╣")
    print("║   Acción     ║               Descripción         ║")
    print("╠══════════════╬═══════════════════════════════════╣")
    print("║     1        ║      Buscar producto por nombre   ║")
    print("║     2        ║   Buscar producto por categoria   ║")
    print("║     3        ║      Buscar producto por precio   ║")
    print("║     4        ║       Volver al menu principal    ║")
    print("╚══════════════╩═══════════════════════════════════╝")

def mostrar_submenu3():
    print("╔══════════════════════════════════════════════════╗")
    print("║            Sistema de Gestión de Inventario      ║")
    print("╠══════════════╦═══════════════════════════════════╣")
    print("║   Acción     ║               Descripción         ║")
    print("╠══════════════╬═══════════════════════════════════╣")
    print("║     1        ║         Importar productos        ║")
    print("║     2        ║         Importar categorias       ║")
    print("║     3        ║         Importar ventas           ║")
    print("║     4        ║         Exportar productos        ║")
    print("║     5        ║         Exportar categorias       ║")
    print("║     6        ║         Exportar ventas           ║")
    print("║     7        ║       Volver al menu principal    ║")
    print("╚══════════════╩═══════════════════════════════════╝")
    
    
def crear_producto():
    while True:
        try:
            # Pedimos los datos del producto al usuario
            nombre_producto = input(
                "Ingrese el nombre del producto o escriba 'cancelar' para volver al menú: ")
            if nombre_producto.lower() == "cancelar":
                return
            precio_producto = input(
                "Ingrese el precio del producto o escriba 'cancelar' para volver al menú: ")
            if precio_producto.lower() == "cancelar":
                return
            nombre_categoria = input(
                "Ingrese la categoría del producto o escriba 'cancelar' para volver al menú: ")
            if nombre_categoria.lower() == "cancelar":
                return

            # Validamos los datos ingresados
            if not nombre_producto.isalpha():
                raise ValueError(
                    "El nombre del producto solo puede contener letras.")
            if not precio_producto.isdigit():
                raise ValueError("El precio debe ser un número.")
            precio_producto = float(precio_producto)
            if not nombre_categoria.isalpha():
                raise ValueError(
                    "El nombre de la categoría solo puede contener letras.")

            # Buscamos la categoría en la lista de categorías
            categoria_existente = buscar_categoria_por_nombre(nombre_categoria)
            if categoria_existente is None:
                # Si la categoría no existe, preguntamos al usuario si desea crearla
                print(
                    f"La categoría '{nombre_categoria}' no existe en el sistema.")
                crear_nueva_categoria = input(
                    "¿Desea crear una nueva categoría con este nombre? (s/n): ")
                if crear_nueva_categoria.lower() == "s":
                    categoria_existente = crear_categoria()
                elif crear_nueva_categoria.lower() == "n":
                    return
                else:
                    print(
                        "Por favor ingrese 's' para crear una nueva categoría o 'n' para cancelar.")

            # Creamos el producto y lo agregamos a la lista de productos
            nuevo_producto = Producto(
                nombre_producto, precio_producto, categoria_existente)
            lista_productos.append(nuevo_producto)

            # Mostramos un mensaje de éxito al usuario
            precio_formateado = locale.currency(precio_producto, grouping=True)
            print(
                f"Se ha creado el producto {nuevo_producto.nombre} con un precio de {precio_formateado} y la categoría {nuevo_producto.categoria.nombre} exitosamente.")

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
    if len(lista_productos) == 0:
        print("No hay ningún producto en el sistema.")
    else:
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
    nombre = input(
        "Nombre del producto a actualizar (escribe 'cancelar' para volver al menú): ")

    # Se utiliza un bucle while para permitir al usuario volver a intentar si ocurre un error
    while True:
        try:
            # Si el usuario escribe "cancelar", se informa al usuario y se regresa al menú
            if nombre.lower() == "cancelar":
                print("Actualización cancelada. Regresando al menú...")
                return

            # Se busca el producto en la lista de productos utilizando la función buscar_producto_por_nombre
            producto_existente = buscar_producto_por_nombre(nombre)
            if producto_existente is not None:
                # Se solicitan los nuevos datos del producto a actualizar
                print("Ingresa los nuevos datos del producto:")

                # Se solicita el nuevo nombre del producto y se verifica que solo contenga letras
                nuevo_nombre = input("Nombre: ")
                if not nuevo_nombre.isalpha():
                    raise ValueError(
                        "El nombre del producto solo puede contener letras.")

                # Se solicita la nueva categoría del producto y se verifica que solo contenga letras
                nueva_categoria = input("Categoría: ")
                if not nueva_categoria.isalpha():
                    raise ValueError(
                        "El nombre de la categoría solo puede contener letras.")

                # Se solicita el nuevo precio del producto y se verifica que sea un número
                nuevo_precio = input("Precio: ")
                if not nuevo_precio.isdigit():
                    raise ValueError("El precio debe ser un número.")
                nuevo_precio = float(nuevo_precio)

                # Se actualiza el producto con los nuevos datos
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
            # Si ocurre un error, se le pedirá al usuario que vuelva a intentar
            nombre = input(
                "Nombre del producto a actualizar (escribe 'cancelar' para volver al menú): ")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}. Intenta nuevamente.")
            # Si ocurre un error, se le pedirá al usuario que vuelva a intentar
            nombre = input(
                "Nombre del producto a actualizar (escribe 'cancelar' para volver al menú): ")


def eliminar_producto():
    while True:
        try:
            # Se solicita el nombre del producto a eliminar
            nombre = input(
                "Nombre del producto a eliminar (escribe 'cancelar' para volver al menú): ")

            # Si el usuario escribe "cancelar", se informa al usuario y se regresa al menú
            if nombre.lower() == "cancelar":
                print("Eliminación cancelada. Regresando al menú...")
                return

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


def crear_categoria(nombre_categoria=None):
    while True:
        try:
            if nombre_categoria is None:
                nombre_categoria = input(
                    "Ingrese por primera vez o nuevamente el nombre de la categoria (escribe 'cancelar' para volver al menú): ")

                # Si el usuario escribe "cancelar", se informa al usuario y se regresa al menú
                if nombre_categoria.lower() == "cancelar":
                    print("Creación de categoría cancelada. Regresando al menú...")
                    return None

            if not nombre_categoria.isalpha():
                raise ValueError(
                    "El nombre de la categoría solo puede contener letras.")
            categoria_existente = buscar_categoria_por_nombre(nombre_categoria)
            if categoria_existente is not None:
                print(
                    f"La categoría '{nombre_categoria}' ya existe en el sistema. Por favor ingrese otro nombre.")
                continue
            nueva_categoria = Categoria(nombre_categoria)
            lista_categorias.append(nueva_categoria)
            print(
                f"Se ha creado la categoría '{nueva_categoria.nombre}' exitosamente.")
            return nueva_categoria
        except ValueError as e:
            print(f"Error: {e}. Intente de nuevo.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}. Intente de nuevo.")


def leer_categorias():
    if len(lista_categorias) == 0:
        print("No hay ninguna categoría en el sistema.")
    else:
        print("Lista de categorías:")
        for categoria in lista_categorias:
            print(categoria.nombre)


def actualizar_categoria():
    while True:
        try:
            nombre = input(
                "Nombre de la categoría a actualizar (escribe 'cancelar' para volver al menú): ")

            # Si el usuario escribe "cancelar", se informa al usuario y se regresa al menú
            if nombre.lower() == "cancelar":
                print("Actualización de categoría cancelada. Regresando al menú...")
                return

            if not nombre.isalpha():
                raise ValueError(
                    "El nombre de la categoría sólo puede contener letras.")
            categoria_existente = buscar_categoria_por_nombre(nombre)
            if categoria_existente is not None:
                nuevo_nombre = input("Nuevo nombre de la categoría: ")
                if not nuevo_nombre.isalpha():
                    raise ValueError(
                        "El nuevo nombre de la categoría sólo puede contener letras.")
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
            print(
                "Ocurrió un error al actualizar la categoría. Por favor, inténtalo de nuevo.")
            continue


def buscar_categoria_por_nombre(nombre):
    for categoria in lista_categorias:
        if categoria.nombre == nombre:
            return categoria
    return None


def eliminar_categoria():
    while True:
        nombre = input(
            "Nombre de la categoría a eliminar (escribe 'cancelar' para volver al menú): ")

        # Si el usuario escribe "cancelar", se informa al usuario y se regresa al menú
        if nombre.lower() == "cancelar":
            print("Eliminación de categoría cancelada. Regresando al menú...")
            return

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


def imprimir_venta(venta):
    total = venta.calcular_total()
    total_str = "RD${:,.2f}".format(total)
    print(f"ID Venta: {venta.id_venta} - Producto: {venta.producto.nombre} - Cantidad: {venta.cantidad} - Fecha: {venta.fecha} - Total: {total_str}")


def leer_ventas():
    if len(lista_ventas) == 0:
        print("No se ha realizado ninguna venta.")
    else:
        print("Ventas realizadas:")
        for venta in lista_ventas:
            if venta.producto is not None:
                total = venta.calcular_total()
                total_str = "RD${:,.2f}".format(total)
                print(
                    f"ID Venta: {venta.id_venta} - Producto: {venta.producto.nombre} - Cantidad: {venta.cantidad} - Fecha: {venta.fecha} - Total: {total_str}")
            else:
                print(
                    f"ID Venta: {venta.id_venta} - Producto no disponible - Total: RD$0.00")


def crear_venta():
    datos_correctos = False
    while not datos_correctos:
        try:
            id_venta = input(
                "Ingrese el ID de la venta (escribe 'cancelar' para volver al menú): ")

            # Si el usuario escribe "cancelar", se informa al usuario y se regresa al menú
            if id_venta.lower() == "cancelar":
                print("Creación de venta cancelada. Regresando al menú...")
                return

            if not id_venta.isdigit():
                print("Error: El ID de la venta debe ser un número.")
                continue

            id_venta = int(id_venta)
            if buscar_venta_por_id(id_venta) is not None:
                print("Error: Ya existe una venta con ese ID.")
                continue

            nombre_producto = input("Ingrese el nombre del producto: ")
            if not nombre_producto.isalpha():
                print("Error: El nombre del producto debe contener solo letras.")
                continue

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

    return


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
        id_venta = input(
            "Ingrese el ID de la venta que desea actualizar (escribe 'cancelar' para volver al menú): ")

        # Si el usuario escribe "cancelar", se informa al usuario y se regresa al menú
        if id_venta.lower() == "cancelar":
            print("Actualización de venta cancelada. Regresando al menú...")
            return

        id_venta = int(id_venta)
        venta_existente = buscar_venta_por_id(id_venta)
        if venta_existente is not None:
            nuevo_producto = buscar_producto_por_nombre(
                input("Ingrese el nuevo nombre del producto: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad vendida: "))
            nueva_fecha = input(
                "Ingrese la nueva fecha de la venta (formato: yyyy-mm-dd): ")
            venta_existente.actualizar_venta(
                nuevo_producto, nueva_cantidad, nueva_fecha)
            print("La venta ha sido actualizada exitosamente.")
        else:
            print("La venta no existe.")
    except ValueError:
        print("Error: Debe ingresar un valor numérico en el campo ID de venta y cantidad.")
    except Exception as e:
        print("Error inesperado:", e)


def eliminar_venta():
    try:
        id_venta = input(
            "Ingrese el ID de la venta a eliminar (escribe 'cancelar' para volver al menú): ")

        # Si el usuario escribe "cancelar", se informa al usuario y se regresa al menú
        if id_venta.lower() == "cancelar":
            print("Eliminación de venta cancelada. Regresando al menú...")
            return

        id_venta = int(id_venta)
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
        fecha = input(
            "Ingrese la fecha para la que desea generar el informe (escribe 'cancelar' para volver al menú, formato: yyyy-mm-dd): ")

        # Si el usuario escribe "cancelar", se informa al usuario y se regresa al menú
        if fecha.lower() == "cancelar":
            print("Generación de informe de ventas cancelada. Regresando al menú...")
            return

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
            productos_con_ventas_mayores_a_1200.append(
                (producto, total_vendido))

    if len(productos_con_ventas_mayores_a_1200) > 0:
        print("Productos con ventas mayores a RD$1,200.00:")
        for producto, total_vendido in productos_con_ventas_mayores_a_1200:
            print(f"{producto}: RD${total_vendido:.2f}")
    else:
        print("No hay productos con ventas mayores a RD$1,200.00.")


def buscar_producto():
    nombre_producto = input(
        "Ingrese el nombre del producto que desea buscar (escribe 'cancelar' para volver al menú): ")

    # Si el usuario escribe "cancelar", se informa al usuario y se regresa al menú
    if nombre_producto.lower() == "cancelar":
        print("Búsqueda de producto cancelada. Regresando al menú...")
        return

    producto_encontrado = buscar_producto_por_nombre(nombre_producto)
    if producto_encontrado:
        print(
            f"El producto '{nombre_producto}' ha sido encontrado en la lista de productos.")
        # Aquí puedes hacer lo que quieras con el producto encontrado
    else:
        print(
            f"No se ha encontrado ningún producto con el nombre '{nombre_producto}'.")


def buscar_productos_por_categoria():
    # Obtener lista de categorías existentes
    categorias = set(
        [producto.categoria.nombre for producto in lista_productos])

    # Pedir al usuario que ingrese el nombre de la categoría o escriba "cancelar" para volver al menú
    nombre_categoria = input(
        "Ingrese el nombre de la categoría que desea buscar (escribe 'cancelar' para volver al menú): ")

    # Si el usuario escribe "cancelar", se informa al usuario y se regresa al menú
    if nombre_categoria.lower() == "cancelar":
        print("Búsqueda de productos por categoría cancelada. Regresando al menú...")
        return []

    # Verificar si la categoría existe en la lista de categorías
    if nombre_categoria not in categorias:
        print(f"No se ha encontrado la categoría '{nombre_categoria}'.")
        return []

    # Buscar productos correspondientes a la categoría especificada
    productos_encontrados = []
    for producto in lista_productos:
        if producto.categoria.nombre == nombre_categoria:
            productos_encontrados.append(producto)

    if productos_encontrados:
        print(
            f"Se han encontrado los siguientes productos en la categoría '{nombre_categoria}':")
        for producto in productos_encontrados:
            print(f"- {producto.nombre}")
    else:
        print(
            f"No se han encontrado productos en la categoría '{nombre_categoria}'.")
    return productos_encontrados


def buscar_producto_por_precio():
    while True:
        try:
            # Pedimos el precio del producto al usuario o que escriba "cancelar" para volver al menú
            precio_producto = input(
                "Ingrese el precio del producto que desea buscar (escribe 'cancelar' para volver al menú): ")

            # Si el usuario escribe "cancelar", se informa al usuario y se regresa al menú
            if precio_producto.lower() == "cancelar":
                print("Búsqueda de producto por precio cancelada. Regresando al menú...")
                return

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
                print(
                    f"No se encontró ningún producto con el precio {precio_producto}.")
                continue

            # Si se encontró el producto, mostramos sus detalles al usuario y salimos de la función
            precio_formateado = locale.currency(
                producto_encontrado.precio, grouping=True)
            print(
                f"El producto encontrado es '{producto_encontrado.nombre}' con un precio de {precio_formateado} y la categoría {producto_encontrado.categoria.nombre}.")
            break

        except ValueError as e:
            # Si se produce un error de validación, informamos al usuario y volvemos al inicio del bucle
            print(f"Error: {e}. Intente de nuevo.")

        except Exception as e:
            # Si se produce un error inesperado, informamos al usuario y volvemos al inicio del bucle
            print(f"Ha ocurrido un error inesperado: {e}. Intente de nuevo.")


def exportar_productos_a_csv():
    """
    Exporta los productos a un archivo CSV.
    """
    # Abrir el archivo para escribir los datos
    with open('productos.csv', mode='w', newline='') as archivo_csv:
        # Crear el escritor CSV
        escritor_csv = csv.writer(
            archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Escribir la cabecera del archivo CSV
        escribir_cabecera_csv(escritor_csv)

        # Escribir los datos de cada producto en el archivo CSV
        escribir_productos_csv(escritor_csv)


def escribir_cabecera_csv(escritor_csv):
    """
    Escribe la cabecera del archivo CSV.

    :param escritor_csv: El escritor CSV a utilizar.
    """
    escritor_csv.writerow(['Nombre', 'Categoria', 'Precio'])


def escribir_productos_csv(escritor_csv):
    """
    Escribe los datos de cada producto en el archivo CSV.

    :param escritor_csv: El escritor CSV a utilizar.
    """
    # Ordenar los productos por nombre, categoría y precio
    productos_ordenados = sorted(
        lista_productos, key=lambda p: (p.nombre, p.categoria.nombre, p.precio))

    # Escribir los datos de cada producto en el archivo CSV
    for producto in productos_ordenados:
        nombre_producto = producto.nombre
        nombre_categoria = producto.categoria.nombre
        precio_producto = producto.precio

        escritor_csv.writerow(
            [nombre_producto, nombre_categoria, precio_producto])


def exportar_categorias_a_csv():
    """
    Exporta las categorías a un archivo CSV en orden alfabético por categoría.
    """
    # Ordenar las categorías por nombre
    categorias_ordenadas = sorted(lista_categorias, key=lambda c: c.nombre)

    # Abrir el archivo para escribir los datos
    with open('categorias.csv', mode='w', newline='') as archivo_csv:
        # Crear el escritor CSV
        escritor_csv = csv.writer(
            archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Escribir la cabecera del archivo CSV
        escritor_csv.writerow(['Categoria'])

        # Escribir los datos de cada categoría en el archivo CSV
        for categoria in categorias_ordenadas:
            nombre_categoria = categoria.nombre
            escritor_csv.writerow([nombre_categoria])


def exportar_ventas_a_csv():
    """
    Exporta las ventas a un archivo CSV en orden por ID de venta, producto, cantidad, fecha y total.
    """
    # Ordenar las ventas por ID de venta, producto, cantidad, fecha y total
    ventas_ordenadas = sorted(lista_ventas, key=lambda v: (
        v.id_venta, v.producto.nombre, v.cantidad, v.fecha, v.total))

    # Abrir el archivo para escribir los datos
    with open('ventas.csv', mode='w', newline='') as archivo_csv:
        # Crear el escritor CSV
        escritor_csv = csv.writer(
            archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Escribir la cabecera del archivo CSV
        escritor_csv.writerow(
            ['ID Venta', 'Producto', 'Cantidad', 'Fecha', 'Total'])

        # Escribir los datos de cada venta en el archivo CSV
        for venta in ventas_ordenadas:
            id_venta = venta.id_venta
            nombre_producto = venta.producto.nombre
            cantidad = venta.cantidad
            fecha_venta = venta.fecha
            total = venta.total

            escritor_csv.writerow(
                [id_venta, nombre_producto, cantidad, fecha_venta, total])


def importar_productos():
    try:
        with open('Producto.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            # saltar la primera línea que contiene los nombres de las columnas
            next(reader)
            for row in reader:
                nombre_producto = row[0]
                nombre_categoria = row[1]
                precio_producto = float(row[2])
                categoria_existente = buscar_categoria_por_nombre(
                    nombre_categoria)
                if categoria_existente is None:
                    categoria_existente = crear_categoria(nombre_categoria)
                nuevo_producto = Producto(
                    nombre_producto, precio_producto, categoria_existente)
                lista_productos.append(nuevo_producto)
        print("Los productos han sido importados exitosamente.")
    except FileNotFoundError:
        print("No se pudo encontrar el archivo Producto.csv")
    except Exception as e:
        print(f"Ha ocurrido un error al importar los productos: {e}")


def importar_categorias():
    try:
        with open('Categorias.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            # saltar la primera línea que contiene los nombres de las columnas
            next(reader)
            for row in reader:
                nombre_categoria = row[0]
                categoria_existente = buscar_categoria_por_nombre(
                    nombre_categoria)
                if categoria_existente is None:
                    nueva_categoria = Categoria(nombre_categoria)
                    lista_categorias.append(nueva_categoria)
        print("Las categorías han sido importadas exitosamente.")
    except FileNotFoundError:
        print("No se pudo encontrar el archivo Categorias.csv")
    except Exception as e:
        print(f"Ha ocurrido un error al importar las categorías: {e}")

def importar_ventas():
    try:
        with open('ventas.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            # saltar la primera línea que contiene los nombres de las columnas
            next(reader)
            for row in reader:
                id_venta = int(row[0])
                nombre_producto = row[1]
                cantidad = int(row[2])
                fecha = datetime.datetime.strptime(row[3], '%Y-%m-%d')
                total = float(row[4])
                producto = buscar_producto_por_nombre(nombre_producto)
                if producto is None:
                    print(f"No se ha encontrado el producto {nombre_producto}. La venta {id_venta} no se ha importado.")
                    continue
                nueva_venta = Venta(id_venta, producto, cantidad, fecha, total)
                lista_ventas.append(nueva_venta)
        print("Las ventas han sido importadas exitosamente.")
    except FileNotFoundError:
        print("No se pudo encontrar el archivo Ventas.csv")







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
                break  # salir del bucle del submenú y volver al menú principal
            else:
                print("Opción no válida. Intente nuevamente.")
    elif opcion == "2":
        while True:
            mostrar_submenu2()
            opcion_submenu2 = input("Ingrese una opción: ")

            if opcion_submenu2 == "1":
                buscar_producto()

            elif opcion_submenu2 == "2":
                buscar_productos_por_categoria()

            elif opcion_submenu2 == "3":
                buscar_producto_por_precio()

            elif opcion_submenu2 == "4":
                break

            else:
                print("Opción no válida. Intente nuevamente.")

    elif opcion == "3":
        while True:
            mostrar_submenu3()
            opcion_submenu3 = input("Ingrese una opción: ")
        
            if opcion_submenu3 == "1":
                importar_productos()
            elif opcion_submenu3 == "2":
                importar_categorias()
            elif opcion_submenu3 == "3":
                importar_ventas()
            elif opcion_submenu3 == "4":
                exportar_productos_a_csv()
            elif opcion_submenu3 == "5":
                exportar_categorias_a_csv()
            elif opcion_submenu3 == "6":
                exportar_ventas_a_csv()
            elif opcion_submenu3 == "7":
                break
            
    elif opcion == "4":
        generar_informe_ventas()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Intente nuevamente.")
