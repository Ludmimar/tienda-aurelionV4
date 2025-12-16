"""
Validador de Datos para Dashboard Power BI - Tienda Aurelion Sprint 2

Este script verifica que todos los datos CSV estén correctos antes de 
cargarlos en Power BI Desktop.

Autor: Martos Ludmila
DNI: 34811650
Sprint: 2 - IBM 2025
"""

import pandas as pd
import os
from pathlib import Path

# Colores para consola
class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    """Imprime encabezado con estilo"""
    print(f"\n{Color.BOLD}{Color.BLUE}{'='*60}{Color.END}")
    print(f"{Color.BOLD}{Color.BLUE}{text:^60}{Color.END}")
    print(f"{Color.BOLD}{Color.BLUE}{'='*60}{Color.END}\n")

def print_success(text):
    """Imprime mensaje de éxito"""
    print(f"{Color.GREEN}✓ {text}{Color.END}")

def print_error(text):
    """Imprime mensaje de error"""
    print(f"{Color.RED}✗ {text}{Color.END}")

def print_warning(text):
    """Imprime mensaje de advertencia"""
    print(f"{Color.YELLOW}⚠ {text}{Color.END}")

def print_info(text):
    """Imprime información"""
    print(f"{Color.BLUE}ℹ {text}{Color.END}")

def verificar_archivo_existe(ruta):
    """Verifica si un archivo existe"""
    if os.path.exists(ruta):
        print_success(f"Archivo encontrado: {ruta}")
        return True
    else:
        print_error(f"Archivo NO encontrado: {ruta}")
        return False

def validar_productos():
    """Valida el archivo productos.csv"""
    print_header("VALIDANDO PRODUCTOS.CSV")
    
    ruta = "../datos/productos.csv"
    if not verificar_archivo_existe(ruta):
        return False
    
    try:
        df = pd.read_csv(ruta)
        
        # Verificar columnas esperadas
        columnas_esperadas = ['id', 'nombre', 'categoria', 'precio', 'stock', 'descripcion', 'proveedor']
        if list(df.columns) == columnas_esperadas:
            print_success(f"Columnas correctas: {', '.join(columnas_esperadas)}")
        else:
            print_error(f"Columnas incorrectas. Esperadas: {columnas_esperadas}")
            print_error(f"Encontradas: {list(df.columns)}")
            return False
        
        # Verificar cantidad de filas
        print_info(f"Total de productos: {len(df)}")
        if len(df) != 80:
            print_warning(f"Se esperaban 80 productos, se encontraron {len(df)}")
        
        # Verificar tipos de datos
        if df['id'].dtype in ['int64', 'int32']:
            print_success("Campo 'id' es numérico")
        else:
            print_error(f"Campo 'id' tiene tipo incorrecto: {df['id'].dtype}")
        
        if df['precio'].dtype in ['int64', 'int32', 'float64']:
            print_success("Campo 'precio' es numérico")
        else:
            print_error(f"Campo 'precio' tiene tipo incorrecto: {df['precio'].dtype}")
        
        if df['stock'].dtype in ['int64', 'int32']:
            print_success("Campo 'stock' es numérico")
        else:
            print_error(f"Campo 'stock' tiene tipo incorrecto: {df['stock'].dtype}")
        
        # Verificar valores nulos
        nulos = df.isnull().sum()
        if nulos.sum() == 0:
            print_success("No hay valores nulos")
        else:
            print_warning(f"Valores nulos encontrados:\n{nulos[nulos > 0]}")
        
        # Verificar duplicados en ID
        duplicados = df['id'].duplicated().sum()
        if duplicados == 0:
            print_success("No hay IDs duplicados")
        else:
            print_error(f"Se encontraron {duplicados} IDs duplicados")
        
        # Estadísticas básicas
        print_info(f"Precio mínimo: ${df['precio'].min()}")
        print_info(f"Precio máximo: ${df['precio'].max()}")
        print_info(f"Stock total: {df['stock'].sum()} unidades")
        print_info(f"Categorías únicas: {df['categoria'].nunique()}")
        print_info(f"Proveedores únicos: {df['proveedor'].nunique()}")
        
        # Productos con stock bajo
        stock_bajo = df[df['stock'] <= 20]
        print_warning(f"Productos con stock bajo (≤20): {len(stock_bajo)}")
        
        return True
        
    except Exception as e:
        print_error(f"Error al validar productos.csv: {str(e)}")
        return False

def validar_clientes():
    """Valida el archivo clientes.csv"""
    print_header("VALIDANDO CLIENTES.CSV")
    
    ruta = "../datos/clientes.csv"
    if not verificar_archivo_existe(ruta):
        return False
    
    try:
        df = pd.read_csv(ruta)
        
        # Verificar columnas esperadas
        columnas_esperadas = ['id', 'nombre', 'email', 'telefono', 'ciudad', 'fecha_registro']
        if list(df.columns) == columnas_esperadas:
            print_success(f"Columnas correctas: {', '.join(columnas_esperadas)}")
        else:
            print_error(f"Columnas incorrectas. Esperadas: {columnas_esperadas}")
            print_error(f"Encontradas: {list(df.columns)}")
            return False
        
        # Verificar cantidad de filas
        print_info(f"Total de clientes: {len(df)}")
        if len(df) != 50:
            print_warning(f"Se esperaban 50 clientes, se encontraron {len(df)}")
        
        # Verificar tipos de datos
        if df['id'].dtype in ['int64', 'int32']:
            print_success("Campo 'id' es numérico")
        else:
            print_error(f"Campo 'id' tiene tipo incorrecto: {df['id'].dtype}")
        
        # Verificar valores nulos
        nulos = df.isnull().sum()
        if nulos.sum() == 0:
            print_success("No hay valores nulos")
        else:
            print_warning(f"Valores nulos encontrados:\n{nulos[nulos > 0]}")
        
        # Verificar duplicados en ID
        duplicados = df['id'].duplicated().sum()
        if duplicados == 0:
            print_success("No hay IDs duplicados")
        else:
            print_error(f"Se encontraron {duplicados} IDs duplicados")
        
        # Verificar emails duplicados
        emails_duplicados = df['email'].duplicated().sum()
        if emails_duplicados == 0:
            print_success("No hay emails duplicados")
        else:
            print_warning(f"Se encontraron {emails_duplicados} emails duplicados")
        
        # Estadísticas básicas
        print_info(f"Ciudades únicas: {df['ciudad'].nunique()}")
        print_info(f"Ciudades: {', '.join(df['ciudad'].unique()[:5])}...")
        
        # Convertir fecha_registro a datetime
        df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])
        print_info(f"Fecha registro más antigua: {df['fecha_registro'].min().strftime('%Y-%m-%d')}")
        print_info(f"Fecha registro más reciente: {df['fecha_registro'].max().strftime('%Y-%m-%d')}")
        
        return True
        
    except Exception as e:
        print_error(f"Error al validar clientes.csv: {str(e)}")
        return False

def validar_ventas():
    """Valida el archivo ventas.csv"""
    print_header("VALIDANDO VENTAS.CSV")
    
    ruta = "../datos/ventas.csv"
    if not verificar_archivo_existe(ruta):
        return False
    
    try:
        df = pd.read_csv(ruta)
        
        # Verificar columnas esperadas
        columnas_esperadas = ['id_venta', 'id_cliente', 'fecha', 'total']
        if list(df.columns) == columnas_esperadas:
            print_success(f"Columnas correctas: {', '.join(columnas_esperadas)}")
        else:
            print_error(f"Columnas incorrectas. Esperadas: {columnas_esperadas}")
            print_error(f"Encontradas: {list(df.columns)}")
            return False
        
        # Verificar cantidad de filas
        print_info(f"Total de ventas: {len(df)}")
        if len(df) != 100:
            print_warning(f"Se esperaban 100 ventas, se encontraron {len(df)}")
        
        # Verificar tipos de datos
        if df['id_venta'].dtype in ['int64', 'int32']:
            print_success("Campo 'id_venta' es numérico")
        else:
            print_error(f"Campo 'id_venta' tiene tipo incorrecto: {df['id_venta'].dtype}")
        
        if df['id_cliente'].dtype in ['int64', 'int32']:
            print_success("Campo 'id_cliente' es numérico")
        else:
            print_error(f"Campo 'id_cliente' tiene tipo incorrecto: {df['id_cliente'].dtype}")
        
        if df['total'].dtype in ['int64', 'int32', 'float64']:
            print_success("Campo 'total' es numérico")
        else:
            print_error(f"Campo 'total' tiene tipo incorrecto: {df['total'].dtype}")
        
        # Verificar valores nulos
        nulos = df.isnull().sum()
        if nulos.sum() == 0:
            print_success("No hay valores nulos")
        else:
            print_warning(f"Valores nulos encontrados:\n{nulos[nulos > 0]}")
        
        # Verificar duplicados en id_venta
        duplicados = df['id_venta'].duplicated().sum()
        if duplicados == 0:
            print_success("No hay IDs de venta duplicados")
        else:
            print_error(f"Se encontraron {duplicados} IDs de venta duplicados")
        
        # Estadísticas básicas
        print_info(f"Ingresos totales: ${df['total'].sum():,.2f}")
        print_info(f"Ticket promedio: ${df['total'].mean():,.2f}")
        print_info(f"Venta mínima: ${df['total'].min()}")
        print_info(f"Venta máxima: ${df['total'].max()}")
        print_info(f"Clientes únicos con compras: {df['id_cliente'].nunique()}")
        
        # Convertir fecha a datetime
        df['fecha'] = pd.to_datetime(df['fecha'])
        print_info(f"Fecha venta más antigua: {df['fecha'].min().strftime('%Y-%m-%d')}")
        print_info(f"Fecha venta más reciente: {df['fecha'].max().strftime('%Y-%m-%d')}")
        
        return True
        
    except Exception as e:
        print_error(f"Error al validar ventas.csv: {str(e)}")
        return False

def validar_detalle_ventas():
    """Valida el archivo detalle_ventas.csv"""
    print_header("VALIDANDO DETALLE_VENTAS.CSV")
    
    ruta = "../datos/detalle_ventas.csv"
    if not verificar_archivo_existe(ruta):
        return False
    
    try:
        df = pd.read_csv(ruta)
        
        # Verificar columnas esperadas
        columnas_esperadas = ['id_detalle', 'id_venta', 'id_producto', 'cantidad', 'precio_unitario', 'subtotal']
        if list(df.columns) == columnas_esperadas:
            print_success(f"Columnas correctas: {', '.join(columnas_esperadas)}")
        else:
            print_error(f"Columnas incorrectas. Esperadas: {columnas_esperadas}")
            print_error(f"Encontradas: {list(df.columns)}")
            return False
        
        # Verificar cantidad de filas
        print_info(f"Total de detalles de venta: {len(df)}")
        
        # Verificar tipos de datos
        for col in ['id_detalle', 'id_venta', 'id_producto', 'cantidad', 'precio_unitario', 'subtotal']:
            if df[col].dtype in ['int64', 'int32', 'float64']:
                print_success(f"Campo '{col}' es numérico")
            else:
                print_error(f"Campo '{col}' tiene tipo incorrecto: {df[col].dtype}")
        
        # Verificar valores nulos
        nulos = df.isnull().sum()
        if nulos.sum() == 0:
            print_success("No hay valores nulos")
        else:
            print_warning(f"Valores nulos encontrados:\n{nulos[nulos > 0]}")
        
        # Verificar duplicados en id_detalle
        duplicados = df['id_detalle'].duplicated().sum()
        if duplicados == 0:
            print_success("No hay IDs de detalle duplicados")
        else:
            print_error(f"Se encontraron {duplicados} IDs de detalle duplicados")
        
        # Verificar consistencia cantidad * precio_unitario = subtotal
        df['subtotal_calculado'] = df['cantidad'] * df['precio_unitario']
        inconsistentes = (df['subtotal'] != df['subtotal_calculado']).sum()
        if inconsistentes == 0:
            print_success("Todos los subtotales son consistentes (cantidad × precio_unitario)")
        else:
            print_warning(f"Se encontraron {inconsistentes} subtotales inconsistentes")
        
        # Estadísticas básicas
        print_info(f"Ventas únicas: {df['id_venta'].nunique()}")
        print_info(f"Productos únicos vendidos: {df['id_producto'].nunique()}")
        print_info(f"Total unidades vendidas: {df['cantidad'].sum()}")
        print_info(f"Ingresos totales (suma subtotales): ${df['subtotal'].sum():,.2f}")
        
        return True
        
    except Exception as e:
        print_error(f"Error al validar detalle_ventas.csv: {str(e)}")
        return False

def validar_relaciones():
    """Valida las relaciones entre tablas"""
    print_header("VALIDANDO RELACIONES ENTRE TABLAS")
    
    try:
        # Cargar todos los archivos
        productos = pd.read_csv("../datos/productos.csv")
        clientes = pd.read_csv("../datos/clientes.csv")
        ventas = pd.read_csv("../datos/ventas.csv")
        detalle = pd.read_csv("../datos/detalle_ventas.csv")
        
        # Validar relación Clientes → Ventas
        clientes_en_ventas = ventas['id_cliente'].unique()
        clientes_validos = clientes['id'].unique()
        clientes_sin_match = set(clientes_en_ventas) - set(clientes_validos)
        
        if len(clientes_sin_match) == 0:
            print_success("Relación Clientes → Ventas: Todos los id_cliente existen en tabla Clientes")
        else:
            print_error(f"Relación Clientes → Ventas: {len(clientes_sin_match)} clientes no encontrados: {clientes_sin_match}")
        
        # Validar relación Ventas → Detalle_Ventas
        ventas_en_detalle = detalle['id_venta'].unique()
        ventas_validas = ventas['id_venta'].unique()
        ventas_sin_match = set(ventas_en_detalle) - set(ventas_validas)
        
        if len(ventas_sin_match) == 0:
            print_success("Relación Ventas → Detalle_Ventas: Todos los id_venta existen en tabla Ventas")
        else:
            print_error(f"Relación Ventas → Detalle_Ventas: {len(ventas_sin_match)} ventas no encontradas: {ventas_sin_match}")
        
        # Validar relación Productos → Detalle_Ventas
        productos_en_detalle = detalle['id_producto'].unique()
        productos_validos = productos['id'].unique()
        productos_sin_match = set(productos_en_detalle) - set(productos_validos)
        
        if len(productos_sin_match) == 0:
            print_success("Relación Productos → Detalle_Ventas: Todos los id_producto existen en tabla Productos")
        else:
            print_error(f"Relación Productos → Detalle_Ventas: {len(productos_sin_match)} productos no encontrados: {productos_sin_match}")
        
        # Validar consistencia total de ventas
        # Suma de subtotales por venta debe coincidir con total de venta
        totales_calculados = detalle.groupby('id_venta')['subtotal'].sum()
        ventas_con_total = ventas.set_index('id_venta')['total']
        
        diferencias = abs(totales_calculados - ventas_con_total) > 0.01
        ventas_inconsistentes = diferencias.sum()
        
        if ventas_inconsistentes == 0:
            print_success("Consistencia Ventas-Detalle: Todos los totales coinciden")
        else:
            print_warning(f"Consistencia Ventas-Detalle: {ventas_inconsistentes} ventas tienen totales inconsistentes")
        
        return True
        
    except Exception as e:
        print_error(f"Error al validar relaciones: {str(e)}")
        return False

def main():
    """Función principal"""
    print("\n")
    print(f"{Color.BOLD}{Color.BLUE}╔═══════════════════════════════════════════════════════════╗{Color.END}")
    print(f"{Color.BOLD}{Color.BLUE}║                                                           ║{Color.END}")
    print(f"{Color.BOLD}{Color.BLUE}║        ⚔️  VALIDADOR DE DATOS - TIENDA AURELION ⚔️        ║{Color.END}")
    print(f"{Color.BOLD}{Color.BLUE}║              Dashboard Power BI - Sprint 2                ║{Color.END}")
    print(f"{Color.BOLD}{Color.BLUE}║                                                           ║{Color.END}")
    print(f"{Color.BOLD}{Color.BLUE}╚═══════════════════════════════════════════════════════════╝{Color.END}")
    
    print_info("Iniciando validación de datos...")
    print_info("Directorio de trabajo: " + os.getcwd())
    
    # Validar cada archivo
    resultados = []
    resultados.append(("Productos", validar_productos()))
    resultados.append(("Clientes", validar_clientes()))
    resultados.append(("Ventas", validar_ventas()))
    resultados.append(("Detalle Ventas", validar_detalle_ventas()))
    resultados.append(("Relaciones", validar_relaciones()))
    
    # Resumen final
    print_header("RESUMEN DE VALIDACIÓN")
    
    exitosas = sum(1 for _, resultado in resultados if resultado)
    total = len(resultados)
    
    for nombre, resultado in resultados:
        if resultado:
            print_success(f"{nombre}: VÁLIDO")
        else:
            print_error(f"{nombre}: ERROR")
    
    print("\n" + "="*60)
    if exitosas == total:
        print(f"{Color.GREEN}{Color.BOLD}✓ TODOS LOS DATOS SON VÁLIDOS ({exitosas}/{total}){Color.END}")
        print(f"{Color.GREEN}Los archivos están listos para cargar en Power BI Desktop{Color.END}")
    else:
        print(f"{Color.RED}{Color.BOLD}✗ ALGUNOS DATOS TIENEN ERRORES ({exitosas}/{total}){Color.END}")
        print(f"{Color.RED}Corrige los errores antes de cargar en Power BI{Color.END}")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()



