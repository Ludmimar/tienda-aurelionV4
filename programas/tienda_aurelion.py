"""
╔═══════════════════════════════════════════════════════════════╗
║          TIENDA AURELION - SISTEMA DE GESTIÓN                 ║
║          Sistema de Inventario y Ventas Interactivo          ║
║          Sprint 2 - Introducción a la IA - IBM                ║
║                                                               ║
║          Autor: Martos Ludmila                                ║
║          DNI: 34811650                                        ║
╚═══════════════════════════════════════════════════════════════╝

Programa interactivo para gestionar el inventario y ventas de la Tienda Aurelion.
Permite consultar, buscar, agregar y actualizar productos, clientes y ventas.
"""

import csv
import os
from typing import List, Dict, Optional, Tuple

# Imports para Machine Learning
try:
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    ML_DISPONIBLE = True
except ImportError:
    ML_DISPONIBLE = False
    print("⚠️  Para usar Machine Learning, instala: pip install pandas numpy scikit-learn")

# Constantes
# Detectar automáticamente las rutas correctas de los CSVs
def obtener_rutas_csv():
    """Obtiene las rutas correctas de los CSVs independientemente de desde dónde se ejecute."""
    # Obtener el directorio actual del script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Rutas posibles relativas al script
    rutas_base = [
        os.path.join(script_dir, "..", "datos"),  # Ejecutando desde programas/
        os.path.join(script_dir, "datos"),          # Si datos está en mismo nivel
        "datos/",                                    # Ejecutando desde la carpeta del sprint
    ]
    
    # También buscar en directorio padre y abuelo
    parent_dir = os.path.dirname(script_dir)
    grandparent_dir = os.path.dirname(parent_dir)
    
    rutas_base.extend([
        os.path.join(parent_dir, "datos"),
        os.path.join(grandparent_dir, "datos"),
    ])
    
    # Buscar recursivamente si hay una carpeta "datos" cerca
    for base in rutas_base:
        try:
            base_path = os.path.abspath(base)
            productos_path = os.path.join(base_path, "productos.csv")
            clientes_path = os.path.join(base_path, "clientes.csv")
            ventas_path = os.path.join(base_path, "ventas.csv")
            detalle_path = os.path.join(base_path, "detalle_ventas.csv")
            
            if all(os.path.exists(p) for p in [productos_path, clientes_path, ventas_path, detalle_path]):
                return {
                    'productos': productos_path,
                    'clientes': clientes_path,
                    'ventas': ventas_path,
                    'detalle_ventas': detalle_path
                }
        except:
            continue
    
    # Por defecto: relativo al script
    default_base = os.path.join(script_dir, "..", "datos")
    return {
        'productos': os.path.join(default_base, "productos.csv"),
        'clientes': os.path.join(default_base, "clientes.csv"),
        'ventas': os.path.join(default_base, "ventas.csv"),
        'detalle_ventas': os.path.join(default_base, "detalle_ventas.csv")
    }

ARCHIVOS_CSV = obtener_rutas_csv()
UMBRAL_STOCK_BAJO = 20


def limpiar_pantalla():
    """Limpia la pantalla de la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_banner():
    """Muestra el banner principal de la aplicación."""
    print("\n" + "═" * 70)
    print("              ⚔️  TIENDA AURELION - SISTEMA DE GESTIÓN ⚔️")
    print("           Sistema de Inventario y Ventas - Sprint 2")
    print("═" * 70)
    print("    💡 Tip: Visualiza estos datos en Power BI Dashboard")
    print("       (ver GUIA_RAPIDA_DASHBOARD_POWERBI.md)")
    print("═" * 70 + "\n")


def cargar_datos() -> Tuple[List[Dict], List[Dict], List[Dict], List[Dict]]:
    """
    Carga los datos de los 4 archivos CSV y los convierte en listas de diccionarios.
    
    Returns:
        Tuple con (productos, clientes, ventas, detalle_ventas)
        Retorna listas vacías si hay error al cargar.
    """
    productos = []
    clientes = []
    ventas = []
    detalle_ventas = []
    
    # Cargar productos
    try:
        with open(ARCHIVOS_CSV['productos'], 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    fila['id'] = int(fila['id'])
                    fila['precio'] = int(fila['precio'])
                    fila['stock'] = int(fila['stock'])
                    productos.append(fila)
                except (ValueError, KeyError) as e:
                    print(f"⚠️  Advertencia: Error al procesar producto: {e}")
                    continue
        print(f"✅ Se cargaron {len(productos)} productos correctamente.")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{ARCHIVOS_CSV['productos']}'")
    except Exception as e:
        print(f"❌ Error al cargar productos: {e}")
    
    # Cargar clientes
    try:
        with open(ARCHIVOS_CSV['clientes'], 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    fila['id'] = int(fila['id'])
                    clientes.append(fila)
                except (ValueError, KeyError) as e:
                    print(f"⚠️  Advertencia: Error al procesar cliente: {e}")
                    continue
        print(f"✅ Se cargaron {len(clientes)} clientes correctamente.")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{ARCHIVOS_CSV['clientes']}'")
    except Exception as e:
        print(f"❌ Error al cargar clientes: {e}")
    
    # Cargar ventas
    try:
        with open(ARCHIVOS_CSV['ventas'], 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    fila['id_venta'] = int(fila['id_venta'])
                    fila['id_cliente'] = int(fila['id_cliente'])
                    fila['total'] = float(fila['total'])
                    ventas.append(fila)
                except (ValueError, KeyError) as e:
                    print(f"⚠️  Advertencia: Error al procesar venta: {e}")
                    continue
        print(f"✅ Se cargaron {len(ventas)} ventas correctamente.")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{ARCHIVOS_CSV['ventas']}'")
    except Exception as e:
        print(f"❌ Error al cargar ventas: {e}")
    
    # Cargar detalle de ventas
    try:
        with open(ARCHIVOS_CSV['detalle_ventas'], 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    fila['id_detalle'] = int(fila['id_detalle'])
                    fila['id_venta'] = int(fila['id_venta'])
                    fila['id_producto'] = int(fila['id_producto'])
                    fila['cantidad'] = int(fila['cantidad'])
                    fila['precio_unitario'] = float(fila['precio_unitario'])
                    fila['subtotal'] = float(fila['subtotal'])
                    detalle_ventas.append(fila)
                except (ValueError, KeyError) as e:
                    print(f"⚠️  Advertencia: Error al procesar detalle de venta: {e}")
                    continue
        print(f"✅ Se cargaron {len(detalle_ventas)} detalles de ventas correctamente.\n")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{ARCHIVOS_CSV['detalle_ventas']}'")
    except Exception as e:
        print(f"❌ Error al cargar detalle de ventas: {e}\n")
    
    return productos, clientes, ventas, detalle_ventas


def guardar_productos(productos: List[Dict]) -> bool:
    """Guarda la lista de productos en el archivo CSV."""
    try:
        if not productos:
            print("⚠️  No hay productos para guardar.")
            return False
        
        columnas = list(productos[0].keys())
        with open(ARCHIVOS_CSV['productos'], 'w', encoding='utf-8', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(productos)
        
        print("✅ Productos guardados correctamente.\n")
        return True
    except Exception as e:
        print(f"❌ Error al guardar productos: {e}\n")
        return False


def guardar_clientes(clientes: List[Dict]) -> bool:
    """Guarda la lista de clientes en el archivo CSV."""
    try:
        if not clientes:
            print("⚠️  No hay clientes para guardar.")
            return False
        
        columnas = list(clientes[0].keys())
        with open(ARCHIVOS_CSV['clientes'], 'w', encoding='utf-8', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(clientes)
        
        print("✅ Clientes guardados correctamente.\n")
        return True
    except Exception as e:
        print(f"❌ Error al guardar clientes: {e}\n")
        return False


def guardar_ventas(ventas: List[Dict]) -> bool:
    """Guarda la lista de ventas en el archivo CSV."""
    try:
        if not ventas:
            print("⚠️  No hay ventas para guardar.")
            return False
        
        columnas = list(ventas[0].keys())
        with open(ARCHIVOS_CSV['ventas'], 'w', encoding='utf-8', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(ventas)
        
        print("✅ Ventas guardadas correctamente.\n")
        return True
    except Exception as e:
        print(f"❌ Error al guardar ventas: {e}\n")
        return False


def guardar_detalle_ventas(detalle_ventas: List[Dict]) -> bool:
    """Guarda la lista de detalle de ventas en el archivo CSV."""
    try:
        if not detalle_ventas:
            print("⚠️  No hay detalles de ventas para guardar.")
            return False
        
        columnas = list(detalle_ventas[0].keys())
        with open(ARCHIVOS_CSV['detalle_ventas'], 'w', encoding='utf-8', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(detalle_ventas)
        
        print("✅ Detalles de ventas guardados correctamente.\n")
        return True
    except Exception as e:
        print(f"❌ Error al guardar detalles de ventas: {e}\n")
        return False


def validar_entrada_numerica(mensaje: str, minimo: int = 0, maximo: Optional[int] = None) -> int:
    """
    Solicita al usuario un número y valida que esté en el rango especificado.
    
    Args:
        mensaje: Mensaje a mostrar al usuario.
        minimo: Valor mínimo permitido.
        maximo: Valor máximo permitido (opcional).
    
    Returns:
        Número entero validado.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"⚠️  El valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"⚠️  El valor debe ser menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("⚠️  Por favor, ingresa un número válido.")


def mostrar_producto(producto: Dict, mostrar_indice: bool = False, indice: int = 0):
    """
    Muestra la información de un producto de forma formateada.
    
    Args:
        producto: Diccionario con los datos del producto.
        mostrar_indice: Si True, muestra el número de índice.
        indice: Número de índice a mostrar.
    """
    if mostrar_indice:
        print(f"\n{'─' * 70}")
        print(f"  Producto #{indice + 1}")
    print(f"{'─' * 70}")
    print(f"  🆔 ID:          {producto['id']}")
    print(f"  📦 Nombre:      {producto['nombre']}")
    print(f"  🏷️  Categoría:   {producto['categoria']}")
    print(f"  💰 Precio:      {producto['precio']} monedas de oro")
    print(f"  📊 Stock:       {producto['stock']} unidades", end="")
    
    # Alerta de stock bajo
    if producto['stock'] <= UMBRAL_STOCK_BAJO:
        print(" ⚠️  ¡STOCK BAJO!")
    else:
        print()
    
    print(f"  📝 Descripción: {producto['descripcion']}")
    print(f"  🏪 Proveedor:   {producto['proveedor']}")
    print(f"{'─' * 70}")


def listar_todos_productos(productos: List[Dict]):
    """Muestra todos los productos del inventario."""
    limpiar_pantalla()
    mostrar_banner()
    print("📋 LISTADO COMPLETO DE PRODUCTOS\n")
    
    if not productos:
        print("⚠️  No hay productos en el inventario.\n")
        return
    
    for i, producto in enumerate(productos):
        mostrar_producto(producto, mostrar_indice=True, indice=i)
    
    print(f"\n📊 Total de productos: {len(productos)}")


def buscar_por_categoria(productos: List[Dict]):
    """Busca y muestra productos de una categoría específica."""
    limpiar_pantalla()
    mostrar_banner()
    print("🏷️  BUSCAR POR CATEGORÍA\n")
    
    # Obtener categorías únicas
    categorias = sorted(set(p['categoria'] for p in productos))
    
    print("Categorías disponibles:")
    for i, cat in enumerate(categorias, 1):
        print(f"  {i}. {cat}")
    
    print(f"\n{'─' * 70}\n")
    categoria = input("Ingresa el nombre de la categoría: ").strip()
    
    # Buscar productos
    resultados = [p for p in productos if p['categoria'].lower() == categoria.lower()]
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} producto(s) en la categoría '{categoria}':\n")
        for i, producto in enumerate(resultados):
            mostrar_producto(producto, mostrar_indice=True, indice=i)
    else:
        print(f"\n❌ No se encontraron productos en la categoría '{categoria}'.")


def buscar_por_id(productos: List[Dict]):
    """Busca un producto por su ID."""
    limpiar_pantalla()
    mostrar_banner()
    print("🆔 BUSCAR POR ID\n")
    
    id_buscar = validar_entrada_numerica("Ingresa el ID del producto: ", minimo=1)
    
    # Buscar producto
    for producto in productos:
        if producto['id'] == id_buscar:
            print("\n✅ Producto encontrado:\n")
            mostrar_producto(producto)
            return
    
    print(f"\n❌ No se encontró ningún producto con ID {id_buscar}.")


def buscar_por_nombre(productos: List[Dict]):
    """Busca productos por nombre (búsqueda parcial)."""
    limpiar_pantalla()
    mostrar_banner()
    print("📦 BUSCAR POR NOMBRE\n")
    
    nombre = input("Ingresa el nombre (o parte del nombre) a buscar: ").strip().lower()
    
    if not nombre:
        print("⚠️  Debes ingresar un nombre para buscar.")
        return
    
    # Buscar productos que contengan el texto en el nombre
    resultados = [p for p in productos if nombre in p['nombre'].lower()]
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} producto(s):\n")
        for i, producto in enumerate(resultados):
            mostrar_producto(producto, mostrar_indice=True, indice=i)
    else:
        print(f"\n❌ No se encontraron productos con '{nombre}' en el nombre.")


def buscar_por_rango_precios(productos: List[Dict]):
    """Busca productos dentro de un rango de precios."""
    limpiar_pantalla()
    mostrar_banner()
    print("💰 BUSCAR POR RANGO DE PRECIOS\n")
    
    precio_min = validar_entrada_numerica("Ingresa el precio mínimo: ", minimo=0)
    precio_max = validar_entrada_numerica("Ingresa el precio máximo: ", minimo=precio_min)
    
    # Buscar productos en el rango
    resultados = [p for p in productos if precio_min <= p['precio'] <= precio_max]
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} producto(s) entre {precio_min} y {precio_max} monedas:\n")
        for i, producto in enumerate(resultados):
            mostrar_producto(producto, mostrar_indice=True, indice=i)
    else:
        print(f"\n❌ No se encontraron productos en ese rango de precios.")


def productos_bajo_stock(productos: List[Dict]):
    """Muestra productos con stock bajo que necesitan reabastecimiento."""
    limpiar_pantalla()
    mostrar_banner()
    print("⚠️  PRODUCTOS CON BAJO STOCK\n")
    
    print(f"Umbral de stock bajo: {UMBRAL_STOCK_BAJO} unidades\n")
    
    # Filtrar productos con stock bajo
    resultados = [p for p in productos if p['stock'] <= UMBRAL_STOCK_BAJO]
    
    if resultados:
        print(f"⚠️  Se encontraron {len(resultados)} producto(s) con stock bajo:\n")
        for i, producto in enumerate(sorted(resultados, key=lambda x: x['stock'])):
            mostrar_producto(producto, mostrar_indice=True, indice=i)
        print(f"\n💡 Sugerencia: Contacta a los proveedores para reabastecer estos productos.")
    else:
        print("✅ ¡Excelente! Todos los productos tienen stock adecuado.")


def estadisticas_inventario(productos: List[Dict]):
    """Muestra estadísticas generales del inventario."""
    limpiar_pantalla()
    mostrar_banner()
    print("📊 ESTADÍSTICAS DEL INVENTARIO\n")
    
    if not productos:
        print("⚠️  No hay productos para analizar.\n")
        return
    
    # Calcular estadísticas
    total_productos = len(productos)
    stock_total = sum(p['stock'] for p in productos)
    valor_total = sum(p['precio'] * p['stock'] for p in productos)
    categorias_unicas = len(set(p['categoria'] for p in productos))
    proveedores_unicos = len(set(p['proveedor'] for p in productos))
    
    # Producto más caro y más barato
    producto_mas_caro = max(productos, key=lambda x: x['precio'])
    producto_mas_barato = min(productos, key=lambda x: x['precio'])
    
    # Precio promedio
    precio_promedio = sum(p['precio'] for p in productos) / total_productos
    
    # Stock promedio
    stock_promedio = stock_total / total_productos
    
    # Productos por categoría
    productos_por_categoria = {}
    for producto in productos:
        cat = producto['categoria']
        productos_por_categoria[cat] = productos_por_categoria.get(cat, 0) + 1
    
    # Mostrar estadísticas
    print(f"{'═' * 70}")
    print("  ESTADÍSTICAS GENERALES")
    print(f"{'═' * 70}")
    print(f"  📦 Total de productos:        {total_productos}")
    print(f"  🏷️  Categorías únicas:         {categorias_unicas}")
    print(f"  🏪 Proveedores únicos:        {proveedores_unicos}")
    print(f"  📊 Stock total:               {stock_total} unidades")
    print(f"  💰 Valor total inventario:    {valor_total:,} monedas de oro")
    print(f"{'─' * 70}")
    print(f"  💵 Precio promedio:           {precio_promedio:.2f} monedas")
    print(f"  📈 Stock promedio:            {stock_promedio:.2f} unidades")
    print(f"{'═' * 70}\n")
    
    print(f"{'═' * 70}")
    print("  PRODUCTOS DESTACADOS")
    print(f"{'═' * 70}")
    print(f"  💎 Producto más caro:")
    print(f"     • {producto_mas_caro['nombre']}")
    print(f"     • Precio: {producto_mas_caro['precio']} monedas")
    print(f"{'─' * 70}")
    print(f"  🎯 Producto más económico:")
    print(f"     • {producto_mas_barato['nombre']}")
    print(f"     • Precio: {producto_mas_barato['precio']} monedas")
    print(f"{'═' * 70}\n")
    
    print(f"{'═' * 70}")
    print("  PRODUCTOS POR CATEGORÍA")
    print(f"{'═' * 70}")
    for cat, cantidad in sorted(productos_por_categoria.items(), key=lambda x: x[1], reverse=True):
        barra = "█" * (cantidad * 3)
        print(f"  {cat:20s} │ {barra} {cantidad}")
    print(f"{'═' * 70}")


def buscar_por_proveedor(productos: List[Dict]):
    """Busca productos de un proveedor específico."""
    limpiar_pantalla()
    mostrar_banner()
    print("🏪 BUSCAR POR PROVEEDOR\n")
    
    # Obtener proveedores únicos
    proveedores = sorted(set(p['proveedor'] for p in productos))
    
    print("Proveedores disponibles:")
    for i, prov in enumerate(proveedores, 1):
        print(f"  {i}. {prov}")
    
    print(f"\n{'─' * 70}\n")
    proveedor = input("Ingresa el nombre del proveedor: ").strip()
    
    # Buscar productos
    resultados = [p for p in productos if p['proveedor'].lower() == proveedor.lower()]
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} producto(s) del proveedor '{proveedor}':\n")
        for i, producto in enumerate(resultados):
            mostrar_producto(producto, mostrar_indice=True, indice=i)
        
        # Estadísticas del proveedor
        stock_total = sum(p['stock'] for p in resultados)
        valor_total = sum(p['precio'] * p['stock'] for p in resultados)
        print(f"\n{'═' * 70}")
        print(f"  📊 Estadísticas del proveedor '{proveedor}':")
        print(f"  • Total productos: {len(resultados)}")
        print(f"  • Stock total: {stock_total} unidades")
        print(f"  • Valor total: {valor_total:,} monedas de oro")
        print(f"{'═' * 70}")
    else:
        print(f"\n❌ No se encontraron productos del proveedor '{proveedor}'.")


def agregar_producto(productos: List[Dict]):
    """Permite agregar un nuevo producto al inventario."""
    limpiar_pantalla()
    mostrar_banner()
    print("➕ AGREGAR NUEVO PRODUCTO\n")
    
    print(f"{'═' * 70}\n")
    
    # Generar nuevo ID
    nuevo_id = max(p['id'] for p in productos) + 1 if productos else 1
    
    # Solicitar datos del nuevo producto
    print(f"🆔 ID asignado automáticamente: {nuevo_id}\n")
    
    nombre = input("📦 Nombre del producto: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return
    
    # Mostrar categorías existentes
    categorias = sorted(set(p['categoria'] for p in productos))
    if categorias:
        print("\n🏷️  Categorías existentes:")
        for cat in categorias:
            print(f"   • {cat}")
    
    categoria = input("\n🏷️  Categoría: ").strip()
    if not categoria:
        print("❌ La categoría no puede estar vacía.")
        return
    
    precio = validar_entrada_numerica("💰 Precio (monedas de oro): ", minimo=1)
    stock = validar_entrada_numerica("📊 Stock inicial (unidades): ", minimo=0)
    
    descripcion = input("📝 Descripción: ").strip()
    if not descripcion:
        print("❌ La descripción no puede estar vacía.")
        return
    
    # Mostrar proveedores existentes
    proveedores = sorted(set(p['proveedor'] for p in productos))
    if proveedores:
        print("\n🏪 Proveedores existentes:")
        for prov in proveedores:
            print(f"   • {prov}")
    
    proveedor = input("\n🏪 Proveedor: ").strip()
    if not proveedor:
        print("❌ El proveedor no puede estar vacío.")
        return
    
    # Crear nuevo producto
    nuevo_producto = {
        'id': nuevo_id,
        'nombre': nombre,
        'categoria': categoria,
        'precio': precio,
        'stock': stock,
        'descripcion': descripcion,
        'proveedor': proveedor
    }
    
    # Confirmar antes de agregar
    print(f"\n{'═' * 70}")
    print("  CONFIRMAR NUEVO PRODUCTO")
    print(f"{'═' * 70}")
    mostrar_producto(nuevo_producto)
    
    confirmacion = input("\n¿Deseas agregar este producto? (s/n): ").strip().lower()
    
    if confirmacion == 's':
        productos.append(nuevo_producto)
        if guardar_productos(productos):
            print("✅ Producto agregado exitosamente al inventario.")
    else:
        print("❌ Operación cancelada. El producto no fue agregado.")


def actualizar_stock(productos: List[Dict]):
    """Permite actualizar el stock de un producto existente."""
    limpiar_pantalla()
    mostrar_banner()
    print("🔄 ACTUALIZAR STOCK DE PRODUCTO\n")
    
    id_buscar = validar_entrada_numerica("Ingresa el ID del producto: ", minimo=1)
    
    # Buscar producto
    producto_encontrado = None
    for producto in productos:
        if producto['id'] == id_buscar:
            producto_encontrado = producto
            break
    
    if not producto_encontrado:
        print(f"\n❌ No se encontró ningún producto con ID {id_buscar}.")
        return
    
    # Mostrar producto actual
    print("\n📦 Producto encontrado:\n")
    mostrar_producto(producto_encontrado)
    
    print(f"\n{'═' * 70}\n")
    print(f"Stock actual: {producto_encontrado['stock']} unidades\n")
    print("Opciones:")
    print("  1. Agregar stock (recibir mercancía)")
    print("  2. Reducir stock (venta)")
    print("  3. Establecer stock nuevo (inventario)")
    print("  4. Cancelar")
    
    opcion = validar_entrada_numerica("\nSelecciona una opción: ", minimo=1, maximo=4)
    
    if opcion == 4:
        print("❌ Operación cancelada.")
        return
    
    if opcion == 1:
        cantidad = validar_entrada_numerica("\nCantidad a agregar: ", minimo=1)
        nuevo_stock = producto_encontrado['stock'] + cantidad
        accion = f"agregaron {cantidad} unidades"
    elif opcion == 2:
        cantidad = validar_entrada_numerica(
            "\nCantidad a reducir: ", 
            minimo=1, 
            maximo=producto_encontrado['stock']
        )
        nuevo_stock = producto_encontrado['stock'] - cantidad
        accion = f"redujeron {cantidad} unidades"
    else:  # opcion == 3
        nuevo_stock = validar_entrada_numerica("\nNuevo stock: ", minimo=0)
        accion = f"estableció en {nuevo_stock} unidades"
    
    # Confirmar actualización
    print(f"\n{'═' * 70}")
    print(f"  Stock actual:  {producto_encontrado['stock']} unidades")
    print(f"  Stock nuevo:   {nuevo_stock} unidades")
    if nuevo_stock <= UMBRAL_STOCK_BAJO:
        print(f"  ⚠️  ADVERTENCIA: Stock bajo (≤ {UMBRAL_STOCK_BAJO})")
    print(f"{'═' * 70}")
    
    confirmacion = input("\n¿Confirmar actualización? (s/n): ").strip().lower()
    
    if confirmacion == 's':
        producto_encontrado['stock'] = nuevo_stock
        if guardar_productos(productos):
            print(f"✅ Stock actualizado exitosamente. Se {accion}.")
    else:
        print("❌ Operación cancelada. El stock no fue modificado.")


def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n" + "╔" + "═" * 68 + "╗")
    print("║" + " " * 25 + "MENÚ PRINCIPAL" + " " * 29 + "║")
    print("╠" + "═" * 68 + "╣")
    print("║  🔍 CONSULTAS Y BÚSQUEDAS                                        ║")
    print("║     1. Listar todos los productos                               ║")
    print("║     2. Buscar por categoría                                     ║")
    print("║     3. Buscar por ID                                             ║")
    print("║     4. Buscar por nombre                                         ║")
    print("║     5. Buscar por rango de precios                               ║")
    print("║     6. Ver productos con bajo stock                              ║")
    print("║     7. Ver estadísticas del inventario                            ║")
    print("║     8. Buscar por proveedor                                      ║")
    print("╠" + "═" * 68 + "╣")
    print("║  ✏️  GESTIÓN DE INVENTARIO                                       ║")
    print("║     9. Agregar nuevo producto                                    ║")
    print("║    10. Actualizar stock de producto                              ║")
    print("╠" + "═" * 68 + "╣")
    print("║  💰 GESTIÓN DE VENTAS                                            ║")
    print("║    11. Ver todas las ventas                                      ║")
    print("║    12. Ver detalle de una venta                                 ║")
    print("║    13. Ver estadísticas de ventas                                ║")
    print("╠" + "═" * 68 + "╣")
    print("║  👥 GESTIÓN DE CLIENTES                                          ║")
    print("║    14. Listar todos los clientes                                 ║")
    print("║    15. Ver estadísticas de clientes                              ║")
    print("╠" + "═" * 68 + "╣")
    print("║  🤖 MACHINE LEARNING                                             ║")
    print("║    16. Entrenar modelo de predicción de ventas                  ║")
    print("║    17. Predecir total de una venta                              ║")
    print("╠" + "═" * 68 + "╣")
    print("║     0. Salir del sistema                                        ║")
    print("╚" + "═" * 68 + "╝\n")


def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\n📌 Presiona Enter para continuar...")


def ver_ventas(ventas: List[Dict], clientes: List[Dict]):
    """Muestra todas las ventas."""
    limpiar_pantalla()
    mostrar_banner()
    print("💰 HISTORIAL DE VENTAS\n")
    
    if not ventas:
        print("⚠️  No hay ventas registradas.\n")
        return
    
    # Crear diccionario de clientes para búsqueda rápida
    clientes_dict = {c['id']: c for c in clientes}
    
    print(f"{'═' * 90}")
    print(f"{'ID':<8} {'Cliente':<25} {'Fecha':<12} {'Total':>15}")
    print(f"{'═' * 90}")
    
    for venta in ventas:
        cliente_nombre = clientes_dict.get(venta['id_cliente'], {}).get('nombre', 'Desconocido')
        print(f"{venta['id_venta']:<8} {cliente_nombre:<25} {venta['fecha']:<12} {venta['total']:>15,.0f} 💰")
    
    print(f"{'═' * 90}")
    print(f"\nTotal de ventas: {len(ventas)}")
    total_general = sum(v['total'] for v in ventas)
    print(f"Ingresos totales: {total_general:,.0f} 💰\n")


def ver_detalle_venta(ventas: List[Dict], detalle_ventas: List[Dict], productos: List[Dict], clientes: List[Dict]):
    """Muestra el detalle de una venta específica."""
    limpiar_pantalla()
    mostrar_banner()
    print("🔍 DETALLE DE VENTA\n")
    
    if not ventas:
        print("⚠️  No hay ventas registradas.\n")
        return
    
    id_venta = validar_entrada_numerica("Ingresa el ID de la venta: ", minimo=1)
    
    # Buscar venta
    venta_encontrada = None
    for venta in ventas:
        if venta['id_venta'] == id_venta:
            venta_encontrada = venta
            break
    
    if not venta_encontrada:
        print(f"\n❌ No se encontró ninguna venta con ID {id_venta}.")
        return
    
    # Buscar cliente
    cliente = next((c for c in clientes if c['id'] == venta_encontrada['id_cliente']), None)
    
    # Buscar detalles
    detalles = [d for d in detalle_ventas if d['id_venta'] == id_venta]
    
    print(f"\n{'═' * 90}")
    print(f"  VENTA #{id_venta}")
    print(f"{'═' * 90}")
    print(f"  Cliente: {cliente['nombre'] if cliente else 'Desconocido'}")
    print(f"  Fecha: {venta_encontrada['fecha']}")
    print(f"  Total: {venta_encontrada['total']:,.0f} 💰")
    print(f"{'═' * 90}\n")
    
    if detalles:
        # Crear diccionario de productos
        productos_dict = {p['id']: p for p in productos}
        
        print("  PRODUCTOS VENDIDOS:")
        print(f"{'─' * 90}")
        print(f"{'Producto':<30} {'Cantidad':>10} {'Precio Unit.':>15} {'Subtotal':>15}")
        print(f"{'─' * 90}")
        
        for detalle in detalles:
            producto = productos_dict.get(detalle['id_producto'], {})
            nombre_producto = producto.get('nombre', 'Desconocido')
            print(f"{nombre_producto:<30} {detalle['cantidad']:>10} {detalle['precio_unitario']:>15,.0f} {detalle['subtotal']:>15,.0f} 💰")
        
        print(f"{'═' * 90}\n")


def estadisticas_ventas(ventas: List[Dict], detalle_ventas: List[Dict], productos: List[Dict]):
    """Muestra estadísticas de ventas."""
    limpiar_pantalla()
    mostrar_banner()
    print("📊 ESTADÍSTICAS DE VENTAS\n")
    
    if not ventas:
        print("⚠️  No hay ventas para analizar.\n")
        return
    
    total_ventas = len(ventas)
    ingresos_totales = sum(v['total'] for v in ventas)
    venta_promedio = ingresos_totales / total_ventas if total_ventas > 0 else 0
    
    print(f"{'═' * 70}")
    print("  ESTADÍSTICAS GENERALES")
    print(f"{'═' * 70}")
    print(f"  💰 Total de ventas:        {total_ventas}")
    print(f"  💵 Ingresos totales:        {ingresos_totales:,.0f} 💰")
    print(f"  📊 Venta promedio:          {venta_promedio:,.0f} 💰")
    print(f"{'═' * 70}\n")
    
    # Productos más vendidos
    productos_dict = {p['id']: p for p in productos}
    ventas_por_producto = {}
    
    for detalle in detalle_ventas:
        producto_id = detalle['id_producto']
        cantidad = detalle['cantidad']
        if producto_id not in ventas_por_producto:
            ventas_por_producto[producto_id] = 0
        ventas_por_producto[producto_id] += cantidad
    
    if ventas_por_producto:
        print(f"{'═' * 70}")
        print("  TOP 5 PRODUCTOS MÁS VENDIDOS")
        print(f"{'═' * 70}")
        
        productos_ordenados = sorted(ventas_por_producto.items(), key=lambda x: x[1], reverse=True)[:5]
        
        for i, (producto_id, cantidad) in enumerate(productos_ordenados, 1):
            producto = productos_dict.get(producto_id, {})
            nombre = producto.get('nombre', 'Desconocido')
            print(f"  {i}. {nombre:<40} {cantidad:>5} unidades")
        
        print(f"{'═' * 70}\n")


def listar_clientes(clientes: List[Dict]):
    """Muestra todos los clientes."""
    limpiar_pantalla()
    mostrar_banner()
    print("👥 LISTADO DE CLIENTES\n")
    
    if not clientes:
        print("⚠️  No hay clientes registrados.\n")
        return
    
    print(f"{'═' * 90}")
    print(f"{'ID':<6} {'Nombre':<30} {'Email':<25} {'Teléfono':<12} {'Ciudad':<15}")
    print(f"{'═' * 90}")
    
    for cliente in clientes:
        print(f"{cliente['id']:<6} {cliente['nombre']:<30} {cliente['email']:<25} {cliente['telefono']:<12} {cliente['ciudad']:<15}")
    
    print(f"{'═' * 90}")
    print(f"\nTotal de clientes: {len(clientes)}\n")


def estadisticas_clientes(clientes: List[Dict], ventas: List[Dict]):
    """Muestra estadísticas de clientes."""
    limpiar_pantalla()
    mostrar_banner()
    print("📊 ESTADÍSTICAS DE CLIENTES\n")
    
    if not clientes:
        print("⚠️  No hay clientes para analizar.\n")
        return
    
    total_clientes = len(clientes)
    
    # Calcular ventas por cliente
    ventas_por_cliente = {}
    for venta in ventas:
        cliente_id = venta['id_cliente']
        if cliente_id not in ventas_por_cliente:
            ventas_por_cliente[cliente_id] = {'cantidad': 0, 'total': 0.0}
        ventas_por_cliente[cliente_id]['cantidad'] += 1
        ventas_por_cliente[cliente_id]['total'] += venta['total']
    
    print(f"{'═' * 70}")
    print("  ESTADÍSTICAS GENERALES")
    print(f"{'═' * 70}")
    print(f"  👥 Total de clientes:       {total_clientes}")
    print(f"  💰 Clientes con compras:    {len(ventas_por_cliente)}")
    print(f"{'═' * 70}\n")
    
    if ventas_por_cliente:
        print(f"{'═' * 90}")
        print(f"{'Cliente':<30} {'Ventas':>10} {'Total Gastado':>20}")
        print(f"{'═' * 90}")
        
        clientes_ordenados = sorted(ventas_por_cliente.items(), key=lambda x: x[1]['total'], reverse=True)[:10]
        
        clientes_dict = {c['id']: c for c in clientes}
        
        for cliente_id, datos in clientes_ordenados:
            cliente = clientes_dict.get(cliente_id, {})
            nombre = cliente.get('nombre', 'Desconocido')
            print(f"{nombre:<30} {datos['cantidad']:>10} {datos['total']:>20,.0f} 💰")
        
        print(f"{'═' * 90}\n")


# ============================================================================
# MACHINE LEARNING - PREDICCIÓN DE VENTAS
# ============================================================================

def entrenar_modelo_ml(productos: List[Dict], ventas: List[Dict], detalle_ventas: List[Dict]):
    """Entrena un modelo de Machine Learning para predecir ventas."""
    limpiar_pantalla()
    mostrar_banner()
    print("🤖 MACHINE LEARNING - PREDICCIÓN DE VENTAS\n")
    
    if not ML_DISPONIBLE:
        print("❌ Machine Learning no está disponible.")
        print("   Instala las dependencias con: pip install pandas numpy scikit-learn")
        return None
    
    print("⏳ Preparando datos y entrenando modelo...")
    print("-" * 70)
    
    # Convertir a DataFrames
    df_productos = pd.DataFrame(productos)
    df_ventas = pd.DataFrame(ventas)
    df_detalle = pd.DataFrame(detalle_ventas)
    
    # Convertir fecha
    df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'])
    
    # Extraer características temporales
    df_ventas['mes'] = df_ventas['fecha'].dt.month
    df_ventas['dia_semana'] = df_ventas['fecha'].dt.dayofweek
    df_ventas['dia_mes'] = df_ventas['fecha'].dt.day
    
    # Unir detalle con productos
    df_detalle_productos = df_detalle.merge(
        df_productos[['id', 'categoria', 'precio']], 
        left_on='id_producto', 
        right_on='id'
    )
    
    # Calcular características por venta
    caracteristicas_ventas = df_detalle_productos.groupby('id_venta').agg({
        'cantidad': 'sum',
        'id_producto': 'nunique',
        'precio_unitario': 'mean',
        'subtotal': 'sum',
        'categoria': lambda x: x.mode()[0] if len(x.mode()) > 0 else x.iloc[0]
    }).reset_index()
    
    caracteristicas_ventas.columns = [
        'id_venta', 'cantidad_total', 'productos_unicos', 
        'precio_promedio', 'subtotal_calculado', 'categoria_principal'
    ]
    
    # Unir con ventas
    df_ml = df_ventas.merge(caracteristicas_ventas, on='id_venta')
    
    # One-Hot Encoding para categoría
    df_ml = pd.get_dummies(df_ml, columns=['categoria_principal'], prefix='cat')
    
    # Preparar X e y
    columnas_excluir = ['id_venta', 'id_cliente', 'fecha', 'total', 'subtotal_calculado']
    X = df_ml.drop(columns=columnas_excluir)
    y = df_ml['total']
    
    # División train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"\n📊 Datos preparados:")
    print(f"   - Total de registros: {len(df_ml)}")
    print(f"   - Entrenamiento: {len(X_train)} ({len(X_train)/len(X)*100:.0f}%)")
    print(f"   - Prueba: {len(X_test)} ({len(X_test)/len(X)*100:.0f}%)")
    
    # Entrenar modelo
    print("\n🌲 Entrenando Random Forest Regressor (100 árboles)...")
    modelo = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    modelo.fit(X_train, y_train)
    
    # Predicciones y métricas
    y_pred_test = modelo.predict(X_test)
    mae_test = mean_absolute_error(y_test, y_pred_test)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
    r2_test = r2_score(y_test, y_pred_test)
    mape_test = np.mean(np.abs((y_test - y_pred_test) / y_test)) * 100
    
    print("\n✅ ¡Modelo entrenado exitosamente!")
    
    print(f"\n{'═' * 70}")
    print("  📊 MÉTRICAS DE EVALUACIÓN (Test)")
    print(f"{'═' * 70}")
    print(f"  • R² Score: {r2_test:.4f} ({r2_test*100:.2f}%)")
    print(f"  • MAE: {mae_test:.2f} monedas")
    print(f"  • RMSE: {rmse_test:.2f} monedas")
    print(f"  • MAPE: {mape_test:.2f}%")
    
    print(f"\n💡 El modelo explica el {r2_test*100:.1f}% de la variabilidad en ventas")
    print(f"   Error promedio: {mae_test:.0f} monedas por predicción")
    
    # Importancia de características
    importancias = pd.DataFrame({
        'caracteristica': X.columns,
        'importancia': modelo.feature_importances_
    }).sort_values('importancia', ascending=False)
    
    print(f"\n{'═' * 70}")
    print("  🎯 TOP 5 CARACTERÍSTICAS MÁS IMPORTANTES")
    print(f"{'═' * 70}")
    for i, (_, row) in enumerate(importancias.head(5).iterrows(), 1):
        barra = "█" * int(row['importancia'] * 40)
        print(f"  {i}. {row['caracteristica']:<25} {barra} {row['importancia']*100:.1f}%")
    
    return {
        'modelo': modelo,
        'X_columns': X.columns.tolist(),
        'metricas': {'r2': r2_test, 'mae': mae_test, 'rmse': rmse_test, 'mape': mape_test}
    }


def predecir_venta_interactivo(modelo_info: dict, productos: List[Dict]):
    """Permite hacer predicciones interactivas."""
    limpiar_pantalla()
    mostrar_banner()
    print("🔮 PREDICTOR INTERACTIVO DE VENTAS\n")
    
    if not ML_DISPONIBLE:
        print("❌ Machine Learning no está disponible.")
        return
    
    if modelo_info is None:
        print("⚠️  Primero debes entrenar el modelo (opción 16).")
        return
    
    print("Ingresa los parámetros de la venta:\n")
    
    cantidad = validar_entrada_numerica("  📦 Cantidad total de productos: ", minimo=1, maximo=100)
    productos_unicos = validar_entrada_numerica("  🔢 Productos únicos: ", minimo=1, maximo=20)
    precio_prom = validar_entrada_numerica("  💰 Precio promedio: ", minimo=25, maximo=5000)
    mes = validar_entrada_numerica("  📅 Mes (1-12): ", minimo=1, maximo=12)
    dia_semana = validar_entrada_numerica("  📆 Día semana (0=Lun, 6=Dom): ", minimo=0, maximo=6)
    dia_mes = validar_entrada_numerica("  📅 Día del mes: ", minimo=1, maximo=31)
    
    # Crear DataFrame para predicción
    nueva_venta = pd.DataFrame([{
        'cantidad_total': cantidad,
        'productos_unicos': productos_unicos,
        'precio_promedio': precio_prom,
        'mes': mes,
        'dia_semana': dia_semana,
        'dia_mes': dia_mes
    }])
    
    # Agregar columnas de categorías (todas en 0, usar la primera como default)
    for col in modelo_info['X_columns']:
        if col not in nueva_venta.columns:
            nueva_venta[col] = 0
    
    # Poner una categoría en 1
    cat_cols = [c for c in modelo_info['X_columns'] if c.startswith('cat_')]
    if cat_cols:
        nueva_venta[cat_cols[0]] = 1
    
    nueva_venta = nueva_venta[modelo_info['X_columns']]
    
    # Hacer predicción
    prediccion = modelo_info['modelo'].predict(nueva_venta)[0]
    margen = modelo_info['metricas']['mae']
    
    print(f"\n{'═' * 70}")
    print("  🎯 RESULTADO DE LA PREDICCIÓN")
    print(f"{'═' * 70}")
    print(f"\n  💰 Total de venta estimado: {prediccion:,.2f} monedas")
    print(f"\n  📊 Rango de confianza (±MAE):")
    print(f"     • Mínimo: {prediccion - margen:,.2f} monedas")
    print(f"     • Máximo: {prediccion + margen:,.2f} monedas")
    print(f"\n  ℹ️  Error promedio del modelo: {margen:.0f} monedas")
    print(f"{'═' * 70}")


def main():
    """Función principal del programa."""
    limpiar_pantalla()
    mostrar_banner()
    
    print("Cargando datos del sistema...\n")
    productos, clientes, ventas, detalle_ventas = cargar_datos()
    
    if not productos:
        print("❌ No se pudieron cargar los productos. Verifica los archivos CSV.")
        return
    
    pausar()
    
    # Variable para el modelo ML
    modelo_ml = None
    
    # Bucle principal del menú
    while True:
        limpiar_pantalla()
        mostrar_banner()
        mostrar_menu()
        
        opcion = validar_entrada_numerica("Selecciona una opción: ", minimo=0, maximo=17)
        
        if opcion == 0:
            limpiar_pantalla()
            mostrar_banner()
            print("╔" + "═" * 68 + "╗")
            print("║" + " " * 15 + "¡Gracias por usar Tienda Aurelion!" + " " * 18 + "║")
            print("║" + " " * 20 + "¡Que tengas un gran día! ⚔️" + " " * 21 + "║")
            print("╠" + "═" * 68 + "╣")
            print("║  💡 Recuerda: También puedes visualizar estos datos en:       ║")
            print("║     • Dashboard Power BI (ver documentacion/)                  ║")
            print("║     • Aplicación Streamlit (ejecuta app_streamlit.py)        ║")
            print("╚" + "═" * 68 + "╝\n")
            break
        elif opcion == 1:
            listar_todos_productos(productos)
        elif opcion == 2:
            buscar_por_categoria(productos)
        elif opcion == 3:
            buscar_por_id(productos)
        elif opcion == 4:
            buscar_por_nombre(productos)
        elif opcion == 5:
            buscar_por_rango_precios(productos)
        elif opcion == 6:
            productos_bajo_stock(productos)
        elif opcion == 7:
            estadisticas_inventario(productos)
        elif opcion == 8:
            buscar_por_proveedor(productos)
        elif opcion == 9:
            agregar_producto(productos)
        elif opcion == 10:
            actualizar_stock(productos)
        elif opcion == 11:
            ver_ventas(ventas, clientes)
        elif opcion == 12:
            ver_detalle_venta(ventas, detalle_ventas, productos, clientes)
        elif opcion == 13:
            estadisticas_ventas(ventas, detalle_ventas, productos)
        elif opcion == 14:
            listar_clientes(clientes)
        elif opcion == 15:
            estadisticas_clientes(clientes, ventas)
        elif opcion == 16:
            modelo_ml = entrenar_modelo_ml(productos, ventas, detalle_ventas)
        elif opcion == 17:
            predecir_venta_interactivo(modelo_ml, productos)
        
        pausar()


if __name__ == "__main__":
    main()

