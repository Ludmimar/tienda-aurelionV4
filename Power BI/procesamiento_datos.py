"""
Script de Procesamiento de Datos para Tienda Aurelion
Sprint 4 - Power BI

Este script procesa los datos para el análisis de inventario y ventas.
"""

import pandas as pd
import numpy as np
import sys
import os
from datetime import datetime, timedelta

# Configurar encoding para Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# ============================================================================
# CONFIGURACIÓN Y CARGA DE DATOS
# ============================================================================

def cargar_datos():
    """
    Carga los datos desde archivos CSV o base de datos.
    Ajustar según la fuente de datos real.
    """
    # Obtener el directorio del script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Rutas posibles para los datos
    rutas_posibles = [
        os.path.join(script_dir, "..", "datos"),  # Desde Power BI/ hacia datos/
        os.path.join(script_dir, "datos"),        # Si datos está en mismo nivel
        "datos",                                   # Relativo al directorio actual
    ]
    
    for ruta_base in rutas_posibles:
        try:
            productos_path = os.path.join(ruta_base, "productos.csv")
            ventas_path = os.path.join(ruta_base, "ventas.csv")
            detalle_path = os.path.join(ruta_base, "detalle_ventas.csv")
            clientes_path = os.path.join(ruta_base, "clientes.csv")
            
            if all(os.path.exists(p) for p in [productos_path, ventas_path, detalle_path, clientes_path]):
                productos = pd.read_csv(productos_path, encoding='utf-8')
                ventas = pd.read_csv(ventas_path, encoding='utf-8')
                detalle_ventas = pd.read_csv(detalle_path, encoding='utf-8')
                clientes = pd.read_csv(clientes_path, encoding='utf-8')
                print(f"   [INFO] Datos cargados desde: {ruta_base}")
                return productos, ventas, detalle_ventas, clientes
        except Exception as e:
            continue
    
    # Si no se encontraron archivos, generar datos de ejemplo
    print(f"   [INFO] No se encontraron archivos CSV. Generando datos de ejemplo...")
    return generar_datos_ejemplo()


def generar_datos_ejemplo():
    """
    Genera datos de ejemplo para pruebas y desarrollo.
    """
    np.random.seed(42)
    
    # Productos
    categorias = ['Armas', 'Armaduras', 'Pociones', 'Libros', 'Accesorios']
    proveedores = ['Proveedor A', 'Proveedor B', 'Proveedor C']
    
    productos = pd.DataFrame({
        'id': range(1, 51),
        'nombre': [f'Producto {i}' for i in range(1, 51)],
        'categoria': np.random.choice(categorias, 50),
        'stock': np.random.randint(5, 200, 50),
        'precio_unitario': np.random.uniform(10, 500, 50).round(2),
        'precio_costo': np.random.uniform(5, 400, 50).round(2),
        'proveedor': np.random.choice(proveedores, 50)
    })
    
    # Calcular valor_inventario
    productos['valor_inventario'] = productos['stock'] * productos['precio_unitario']
    
    # Clientes
    clientes = pd.DataFrame({
        'id': range(1, 21),
        'nombre': [f'Cliente {i}' for i in range(1, 21)],
        'email': [f'cliente{i}@email.com' for i in range(1, 21)]
    })
    
    # Ventas (últimos 12 meses)
    fecha_inicio = datetime.now() - timedelta(days=365)
    fechas = [fecha_inicio + timedelta(days=i) for i in range(365)]
    
    ventas = pd.DataFrame({
        'id': range(1, 201),
        'fecha': np.random.choice(fechas, 200),
        'cliente_id': np.random.randint(1, 21, 200),
        'total': np.random.uniform(50, 2000, 200).round(2)
    })
    
    # Detalle Ventas
    detalle_ventas = []
    for venta_id in range(1, 201):
        num_productos = np.random.randint(1, 5)
        productos_venta = np.random.choice(productos['id'].values, num_productos, replace=False)
        for producto_id in productos_venta:
            cantidad = np.random.randint(1, 5)
            precio = productos[productos['id'] == producto_id]['precio_unitario'].values[0]
            detalle_ventas.append({
                'venta_id': venta_id,
                'producto_id': producto_id,
                'cantidad': cantidad,
                'precio_unitario': precio,
                'subtotal': cantidad * precio
            })
    
    detalle_ventas = pd.DataFrame(detalle_ventas)
    
    return productos, ventas, detalle_ventas, clientes


# ============================================================================
# ANÁLISIS Y TRANSFORMACIONES
# ============================================================================

def calcular_metricas_basicas(productos, ventas, detalle_ventas):
    """
    Calcula métricas básicas del negocio.
    """
    metricas = {
        'total_productos': len(productos),
        'total_ventas': len(ventas),
        'total_ingresos': ventas['total'].sum(),
        'productos_vendidos': detalle_ventas['cantidad'].sum(),
        'stock_total': productos['stock'].sum(),
        'valor_inventario_total': productos['valor_inventario'].sum(),
        'promedio_stock': productos['stock'].mean(),
        'productos_stock_bajo': len(productos[productos['stock'] < 20])
    }
    
    return metricas


def calcular_rotacion_inventario(productos, detalle_ventas):
    """
    Calcula la rotación de inventario por producto.
    """
    ventas_por_producto = detalle_ventas.groupby('producto_id')['cantidad'].sum().reset_index()
    ventas_por_producto.columns = ['id', 'cantidad_vendida']
    
    rotacion = productos.merge(ventas_por_producto, on='id', how='left')
    rotacion['cantidad_vendida'] = rotacion['cantidad_vendida'].fillna(0)
    rotacion['rotacion'] = rotacion.apply(
        lambda x: x['cantidad_vendida'] / x['stock'] if x['stock'] > 0 else 0,
        axis=1
    )
    
    return rotacion[['id', 'nombre', 'categoria', 'stock', 'cantidad_vendida', 'rotacion']]


def calcular_margen_utilidad(ventas, detalle_ventas, productos):
    """
    Calcula el margen de utilidad por venta.
    """
    # Unir datos
    detalle_completo = detalle_ventas.merge(
        productos[['id', 'precio_costo']],
        left_on='producto_id',
        right_on='id',
        how='left'
    )
    
    # Calcular costos y utilidades
    detalle_completo['costo_total'] = detalle_completo['cantidad'] * detalle_completo['precio_costo']
    detalle_completo['utilidad'] = detalle_completo['subtotal'] - detalle_completo['costo_total']
    detalle_completo['margen'] = detalle_completo['utilidad'] / detalle_completo['subtotal']
    
    # Agrupar por venta
    margen_por_venta = detalle_completo.groupby('venta_id').agg({
        'subtotal': 'sum',
        'costo_total': 'sum',
        'utilidad': 'sum'
    }).reset_index()
    
    margen_por_venta['margen_porcentaje'] = (
        margen_por_venta['utilidad'] / margen_por_venta['subtotal'] * 100
    ).round(2)
    
    return margen_por_venta


def analisis_temporal(ventas):
    """
    Realiza análisis temporal de ventas.
    """
    ventas['fecha'] = pd.to_datetime(ventas['fecha'])
    ventas['año'] = ventas['fecha'].dt.year
    ventas['mes'] = ventas['fecha'].dt.month
    ventas['trimestre'] = ventas['fecha'].dt.quarter
    ventas['año_mes'] = ventas['fecha'].dt.to_period('M')
    
    # Ventas por mes
    ventas_mensuales = ventas.groupby('año_mes').agg({
        'total': ['sum', 'mean', 'count']
    }).reset_index()
    
    # Crecimiento mes a mes
    ventas_mensuales['crecimiento_mom'] = ventas_mensuales[('total', 'sum')].pct_change() * 100
    
    return ventas_mensuales


def crear_agrupaciones(productos):
    """
    Crea agrupaciones y categorizaciones de productos.
    """
    productos['stock_rango'] = pd.cut(
        productos['stock'],
        bins=[0, 20, 50, float('inf')],
        labels=['Stock Bajo', 'Stock Medio', 'Stock Alto']
    )
    
    productos['valor_segmento'] = pd.cut(
        productos['valor_inventario'],
        bins=[0, 1000, 5000, float('inf')],
        labels=['Bajo Valor', 'Valor Medio', 'Alto Valor']
    )
    
    return productos


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que ejecuta el procesamiento completo.
    """
    print("=" * 60)
    print("PROCESAMIENTO DE DATOS - TIENDA AURELION")
    print("Sprint 4 - Power BI")
    print("=" * 60)
    
    # Cargar datos
    print("\n1. Cargando datos...")
    productos, ventas, detalle_ventas, clientes = cargar_datos()
    print(f"   [OK] Productos cargados: {len(productos)}")
    print(f"   [OK] Ventas cargadas: {len(ventas)}")
    print(f"   [OK] Detalle ventas: {len(detalle_ventas)}")
    print(f"   [OK] Clientes cargados: {len(clientes)}")
    
    # Calcular métricas básicas
    print("\n2. Calculando metricas basicas...")
    metricas = calcular_metricas_basicas(productos, ventas, detalle_ventas)
    for clave, valor in metricas.items():
        print(f"   - {clave}: {valor:,.2f}" if isinstance(valor, float) else f"   - {clave}: {valor}")
    
    # Calcular rotación de inventario
    print("\n3. Calculando rotacion de inventario...")
    rotacion = calcular_rotacion_inventario(productos, detalle_ventas)
    print(f"   [OK] Rotacion promedio: {rotacion['rotacion'].mean():.2f}")
    
    # Calcular margen de utilidad
    print("\n4. Calculando margen de utilidad...")
    margen = calcular_margen_utilidad(ventas, detalle_ventas, productos)
    print(f"   [OK] Margen promedio: {margen['margen_porcentaje'].mean():.2f}%")
    
    # Análisis temporal
    print("\n5. Realizando analisis temporal...")
    ventas_temporales = analisis_temporal(ventas)
    print(f"   [OK] Periodos analizados: {len(ventas_temporales)}")
    
    # Crear agrupaciones
    print("\n6. Creando agrupaciones...")
    productos = crear_agrupaciones(productos)
    print("   [OK] Agrupaciones creadas: Stock por Rango, Valor por Segmento")
    
    # Guardar resultados (opcional)
    print("\n7. Guardando resultados...")
    try:
        # Guardar en la carpeta resultados relativa al script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        resultados_dir = os.path.join(script_dir, 'resultados')
        
        if not os.path.exists(resultados_dir):
            os.makedirs(resultados_dir)
            print(f"   [INFO] Carpeta resultados creada: {resultados_dir}")
        
        productos.to_csv(os.path.join(resultados_dir, 'productos_procesados.csv'), 
                        index=False, encoding='utf-8-sig')
        ventas_temporales.to_csv(os.path.join(resultados_dir, 'ventas_temporales.csv'), 
                                index=False, encoding='utf-8-sig')
        rotacion.to_csv(os.path.join(resultados_dir, 'rotacion_inventario.csv'), 
                       index=False, encoding='utf-8-sig')
        margen.to_csv(os.path.join(resultados_dir, 'margen_utilidad.csv'), 
                     index=False, encoding='utf-8-sig')
        print(f"   [OK] Archivos guardados en: {resultados_dir}")
    except Exception as e:
        print(f"   [ADVERTENCIA] No se pudieron guardar los archivos: {e}")
    
    print("\n" + "=" * 60)
    print("PROCESAMIENTO COMPLETADO")
    print("=" * 60)
    
    return productos, ventas, detalle_ventas, clientes, metricas


if __name__ == "__main__":
    productos, ventas, detalle_ventas, clientes, metricas = main()

