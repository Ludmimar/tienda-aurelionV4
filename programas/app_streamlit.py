"""
╔═══════════════════════════════════════════════════════════════╗
║          TIENDA AURELION - APLICACIÓN WEB                     ║
║          Sistema de Gestión de Inventario con Streamlit       ║
║          Sprint 4 - Power BI - IBM                            ║
║                                                               ║
║          Autor: Martos Ludmila                                ║
║          DNI: 34811650                                        ║
╚═══════════════════════════════════════════════════════════════╝

Aplicación web interactiva para gestionar el inventario de la Tienda Aurelion.

Instalación de Streamlit:
    pip install streamlit

Ejecución:
    streamlit run app_streamlit.py
"""

import streamlit as st
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import normaltest, shapiro
import os
from typing import List, Dict, Tuple
import warnings
warnings.filterwarnings('ignore')

# Imports para Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Configuración de la página
st.set_page_config(
    page_title="Tienda Aurelion",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #FFD700;
        text-shadow: 2px 2px 4px #000000;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #667eea;
    }
    .stock-bajo {
        color: #ff4444;
        font-weight: bold;
    }
    .stock-ok {
        color: #00C851;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def cargar_datos() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Carga los datos de los 4 archivos CSV y los convierte en DataFrames de pandas.
    
    Returns:
        Tuple con (productos, clientes, ventas, detalle_ventas)
    """
    try:
        # Cargar productos
        df_productos = pd.read_csv(ARCHIVOS_CSV['productos'], encoding='utf-8')
        df_productos['id'] = df_productos['id'].astype(int)
        df_productos['precio'] = df_productos['precio'].astype(int)
        df_productos['stock'] = df_productos['stock'].astype(int)
        
        # Cargar clientes
        df_clientes = pd.read_csv(ARCHIVOS_CSV['clientes'], encoding='utf-8')
        df_clientes['id'] = df_clientes['id'].astype(int)
        
        # Cargar ventas
        df_ventas = pd.read_csv(ARCHIVOS_CSV['ventas'], encoding='utf-8')
        df_ventas['id_venta'] = df_ventas['id_venta'].astype(int)
        df_ventas['id_cliente'] = df_ventas['id_cliente'].astype(int)
        df_ventas['total'] = df_ventas['total'].astype(float)
        df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'])
        
        # Cargar detalle de ventas
        df_detalle = pd.read_csv(ARCHIVOS_CSV['detalle_ventas'], encoding='utf-8')
        df_detalle['id_detalle'] = df_detalle['id_detalle'].astype(int)
        df_detalle['id_venta'] = df_detalle['id_venta'].astype(int)
        df_detalle['id_producto'] = df_detalle['id_producto'].astype(int)
        df_detalle['cantidad'] = df_detalle['cantidad'].astype(int)
        df_detalle['precio_unitario'] = df_detalle['precio_unitario'].astype(float)
        df_detalle['subtotal'] = df_detalle['subtotal'].astype(float)
        
        return df_productos, df_clientes, df_ventas, df_detalle
        
    except FileNotFoundError as e:
        st.error(f"❌ No se encontró uno de los archivos CSV: {e}")
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    except Exception as e:
        st.error(f"❌ Error al cargar datos: {e}")
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()


def guardar_productos(df: pd.DataFrame):
    """Guarda el DataFrame de productos en el archivo CSV."""
    try:
        df.to_csv(ARCHIVOS_CSV['productos'], index=False, encoding='utf-8')
        return True
    except Exception as e:
        st.error(f"❌ Error al guardar productos: {e}")
        return False


def guardar_clientes(df: pd.DataFrame):
    """Guarda el DataFrame de clientes en el archivo CSV."""
    try:
        df.to_csv(ARCHIVOS_CSV['clientes'], index=False, encoding='utf-8')
        return True
    except Exception as e:
        st.error(f"❌ Error al guardar clientes: {e}")
        return False


def guardar_ventas(df: pd.DataFrame):
    """Guarda el DataFrame de ventas en el archivo CSV."""
    try:
        df.to_csv(ARCHIVOS_CSV['ventas'], index=False, encoding='utf-8')
        return True
    except Exception as e:
        st.error(f"❌ Error al guardar ventas: {e}")
        return False


def guardar_detalle_ventas(df: pd.DataFrame):
    """Guarda el DataFrame de detalle de ventas en el archivo CSV."""
    try:
        df.to_csv(ARCHIVOS_CSV['detalle_ventas'], index=False, encoding='utf-8')
        return True
    except Exception as e:
        st.error(f"❌ Error al guardar detalle de ventas: {e}")
        return False


def mostrar_header():
    """Muestra el encabezado principal de la aplicación."""
    st.markdown(
        '<div class="main-header">⚔️ TIENDA AURELION ⚔️<br><small style="font-size:1.2rem;">Sistema de Gestión de Inventario y Ventas</small></div>',
        unsafe_allow_html=True
    )


def mostrar_metricas_principales(df_productos: pd.DataFrame, df_clientes: pd.DataFrame, df_ventas: pd.DataFrame):
    """Muestra las métricas principales en tarjetas."""
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        st.metric(
            label="📦 Total Productos",
            value=len(df_productos)
        )
    
    with col2:
        stock_total = df_productos['stock'].sum()
        st.metric(
            label="📊 Stock Total",
            value=f"{stock_total:,}",
            help="Unidades totales en inventario"
        )
    
    with col3:
        valor_total = (df_productos['precio'] * df_productos['stock']).sum()
        st.metric(
            label="💰 Valor Inventario",
            value=f"{valor_total:,}",
            help="Monedas de oro"
        )
    
    with col4:
        st.metric(
            label="👥 Total Clientes",
            value=len(df_clientes)
        )
    
    with col5:
        total_ventas = df_ventas['total'].sum()
        st.metric(
            label="💵 Total Ventas",
            value=f"{total_ventas:,.0f}",
            help="Monedas de oro"
        )
    
    with col6:
        productos_bajo_stock = len(df_productos[df_productos['stock'] <= UMBRAL_STOCK_BAJO])
        st.metric(
            label="⚠️ Stock Bajo",
            value=productos_bajo_stock,
            delta=f"-{productos_bajo_stock}" if productos_bajo_stock > 0 else "OK",
            delta_color="inverse"
        )


def pagina_inicio(df_productos: pd.DataFrame, df_clientes: pd.DataFrame, df_ventas: pd.DataFrame, df_detalle: pd.DataFrame):
    """Página de inicio con resumen general."""
    st.header("📊 Panel de Control General")
    
    # Métricas principales
    mostrar_metricas_principales(df_productos, df_clientes, df_ventas)
    
    st.markdown("---")
    
    # Tres columnas para gráficos
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📈 Productos por Categoría")
        categoria_counts = df_productos['categoria'].value_counts()
        st.bar_chart(categoria_counts)
        
        st.subheader("💵 Distribución de Precios")
        precio_dist = pd.cut(df_productos['precio'], bins=[0, 500, 2000, 10000], 
                            labels=['Económico (<500)', 'Medio (500-2000)', 'Premium (>2000)'])
        st.bar_chart(precio_dist.value_counts())
    
    with col2:
        st.subheader("🏪 Productos por Proveedor")
        proveedor_counts = df_productos['proveedor'].value_counts()
        st.bar_chart(proveedor_counts)
        
        st.subheader("💎 Top 5 Más Valiosos")
        df_valor = df_productos.copy()
        df_valor['valor_total'] = df_valor['precio'] * df_valor['stock']
        top5 = df_valor.nlargest(5, 'valor_total')[['nombre', 'valor_total']]
        top5 = top5.set_index('nombre')
        st.bar_chart(top5)
    
    with col3:
        st.subheader("📅 Ventas por Fecha")
        df_ventas_fecha = df_ventas.copy()
        df_ventas_fecha['fecha'] = pd.to_datetime(df_ventas_fecha['fecha'])
        df_ventas_fecha = df_ventas_fecha.groupby(df_ventas_fecha['fecha'].dt.date)['total'].sum()
        st.line_chart(df_ventas_fecha)
        
        st.subheader("👥 Top 5 Clientes")
        ventas_cliente = df_ventas.groupby('id_cliente')['total'].sum().sort_values(ascending=False).head(5)
        clientes_top = df_clientes[df_clientes['id'].isin(ventas_cliente.index)][['nombre', 'id']]
        clientes_top = clientes_top.merge(ventas_cliente.reset_index(), left_on='id', right_on='id_cliente')
        clientes_top = clientes_top.set_index('nombre')[['total']]
        st.bar_chart(clientes_top)
    
    # Alerta de productos con stock bajo
    if len(df_productos[df_productos['stock'] <= UMBRAL_STOCK_BAJO]) > 0:
        st.markdown("---")
        st.warning("⚠️ **ALERTA: Productos con Stock Bajo**")
        productos_criticos = df_productos[df_productos['stock'] <= UMBRAL_STOCK_BAJO].sort_values('stock')
        st.dataframe(
            productos_criticos[['nombre', 'categoria', 'stock', 'proveedor']],
            use_container_width=True,
            hide_index=True
        )


def pagina_productos(df_productos: pd.DataFrame):
    """Página para ver y buscar productos."""
    st.header("🔍 Explorar Productos")
    
    # Filtros en la barra lateral
    st.sidebar.subheader("🎛️ Filtros")
    
    # Filtro por categoría
    categorias = ['Todas'] + sorted(df_productos['categoria'].unique().tolist())
    categoria_seleccionada = st.sidebar.selectbox("Categoría", categorias)
    
    # Filtro por proveedor
    proveedores = ['Todos'] + sorted(df_productos['proveedor'].unique().tolist())
    proveedor_seleccionado = st.sidebar.selectbox("Proveedor", proveedores)
    
    # Filtro por rango de precio
    precio_min, precio_max = st.sidebar.slider(
        "Rango de Precio (monedas)",
        min_value=int(df_productos['precio'].min()),
        max_value=int(df_productos['precio'].max()),
        value=(int(df_productos['precio'].min()), int(df_productos['precio'].max()))
    )
    
    # Filtro por stock
    stock_filter = st.sidebar.radio(
        "Estado de Stock",
        ["Todos", "Stock Bajo (≤20)", "Stock Saludable (>20)"]
    )
    
    # Búsqueda por nombre
    busqueda = st.sidebar.text_input("🔎 Buscar por nombre", "")
    
    # Aplicar filtros
    df_filtrado = df_productos.copy()
    
    if categoria_seleccionada != 'Todas':
        df_filtrado = df_filtrado[df_filtrado['categoria'] == categoria_seleccionada]
    
    if proveedor_seleccionado != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['proveedor'] == proveedor_seleccionado]
    
    df_filtrado = df_filtrado[
        (df_filtrado['precio'] >= precio_min) & 
        (df_filtrado['precio'] <= precio_max)
    ]
    
    if stock_filter == "Stock Bajo (≤20)":
        df_filtrado = df_filtrado[df_filtrado['stock'] <= UMBRAL_STOCK_BAJO]
    elif stock_filter == "Stock Saludable (>20)":
        df_filtrado = df_filtrado[df_filtrado['stock'] > UMBRAL_STOCK_BAJO]
    
    if busqueda:
        df_filtrado = df_filtrado[
            df_filtrado['nombre'].str.contains(busqueda, case=False, na=False)
        ]
    
    # Mostrar resultados
    st.subheader(f"📦 Resultados: {len(df_filtrado)} producto(s)")
    
    if len(df_filtrado) > 0:
        # Agregar columna de estado de stock
        df_display = df_filtrado.copy()
        df_display['Estado'] = df_display['stock'].apply(
            lambda x: '⚠️ BAJO' if x <= UMBRAL_STOCK_BAJO else '✅ OK'
        )
        
        # Mostrar tabla
        st.dataframe(
            df_display[['id', 'nombre', 'categoria', 'precio', 'stock', 'Estado', 'proveedor', 'descripcion']],
            use_container_width=True,
            hide_index=True
        )
        
        # Estadísticas de los resultados filtrados
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Stock Total", f"{df_filtrado['stock'].sum():,}")
        with col2:
            valor = (df_filtrado['precio'] * df_filtrado['stock']).sum()
            st.metric("Valor Total", f"{valor:,} 💰")
        with col3:
            precio_prom = df_filtrado['precio'].mean()
            st.metric("Precio Promedio", f"{precio_prom:.0f} 💰")
    else:
        st.info("No se encontraron productos con los filtros seleccionados.")


def pagina_estadisticas(df_productos: pd.DataFrame, df_clientes: pd.DataFrame, df_ventas: pd.DataFrame, df_detalle: pd.DataFrame):
    """Página de estadísticas y análisis."""
    st.header("📊 Estadísticas y Análisis")
    
    # Estadísticas generales
    st.subheader("📈 Estadísticas Generales")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Productos", len(df_productos))
        st.metric("Categorías Únicas", df_productos['categoria'].nunique())
    
    with col2:
        st.metric("Stock Total", f"{df_productos['stock'].sum():,}")
        st.metric("Stock Promedio", f"{df_productos['stock'].mean():.1f}")
    
    with col3:
        valor_total = (df_productos['precio'] * df_productos['stock']).sum()
        st.metric("Valor Total", f"{valor_total:,} 💰")
        st.metric("Precio Promedio", f"{df_productos['precio'].mean():.0f} 💰")
    
    with col4:
        st.metric("Proveedores Únicos", df_productos['proveedor'].nunique())
        productos_bajo = len(df_productos[df_productos['stock'] <= UMBRAL_STOCK_BAJO])
        st.metric("Productos Stock Bajo", productos_bajo)
    
    st.markdown("---")
    
    # Análisis por categoría
    st.subheader("🏷️ Análisis por Categoría")
    
    analisis_categoria = df_productos.groupby('categoria').agg({
        'id': 'count',
        'stock': 'sum',
        'precio': 'mean'
    }).rename(columns={
        'id': 'Cantidad Productos',
        'stock': 'Stock Total',
        'precio': 'Precio Promedio'
    })
    
    analisis_categoria['Valor Total'] = df_productos.groupby('categoria').apply(
        lambda x: (x['precio'] * x['stock']).sum()
    )
    
    st.dataframe(
        analisis_categoria.style.format({
            'Stock Total': '{:,.0f}',
            'Precio Promedio': '{:,.0f} 💰',
            'Valor Total': '{:,.0f} 💰'
        }),
        use_container_width=True
    )
    
    st.markdown("---")
    
    # Análisis por proveedor
    st.subheader("🏪 Análisis por Proveedor")
    
    analisis_proveedor = df_productos.groupby('proveedor').agg({
        'id': 'count',
        'stock': 'sum',
        'categoria': lambda x: x.nunique()
    }).rename(columns={
        'id': 'Productos',
        'stock': 'Stock Total',
        'categoria': 'Categorías'
    })
    
    analisis_proveedor['Valor Total'] = df_productos.groupby('proveedor').apply(
        lambda x: (x['precio'] * x['stock']).sum()
    )
    
    analisis_proveedor = analisis_proveedor.sort_values('Productos', ascending=False)
    
    st.dataframe(
        analisis_proveedor.style.format({
            'Stock Total': '{:,.0f}',
            'Valor Total': '{:,.0f} 💰'
        }),
        use_container_width=True
    )
    
    st.markdown("---")
    
    # Análisis de ventas
    st.subheader("💵 Análisis de Ventas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Ventas", len(df_ventas))
        st.metric("Ingresos Totales", f"{df_ventas['total'].sum():,.0f} 💰")
        st.metric("Venta Promedio", f"{df_ventas['total'].mean():.0f} 💰")
    
    with col2:
        # Productos más vendidos
        productos_vendidos = df_detalle.groupby('id_producto')['cantidad'].sum().sort_values(ascending=False).head(5)
        productos_top = df_productos[df_productos['id'].isin(productos_vendidos.index)][['nombre', 'id']]
        productos_top = productos_top.merge(productos_vendidos.reset_index(), left_on='id', right_on='id_producto')
        productos_top = productos_top.set_index('nombre')[['cantidad']]
        st.subheader("🏆 Top 5 Productos Más Vendidos")
        st.dataframe(productos_top, use_container_width=True)
    
    st.markdown("---")
    
    # Productos destacados
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💎 Producto Más Caro")
        mas_caro = df_productos.loc[df_productos['precio'].idxmax()]
        st.info(f"""
        **{mas_caro['nombre']}**
        - Precio: {mas_caro['precio']:,} monedas
        - Categoría: {mas_caro['categoria']}
        - Stock: {mas_caro['stock']} unidades
        - Proveedor: {mas_caro['proveedor']}
        """)
    
    with col2:
        st.subheader("🎯 Producto Más Económico")
        mas_barato = df_productos.loc[df_productos['precio'].idxmin()]
        st.info(f"""
        **{mas_barato['nombre']}**
        - Precio: {mas_barato['precio']:,} monedas
        - Categoría: {mas_barato['categoria']}
        - Stock: {mas_barato['stock']} unidades
        - Proveedor: {mas_barato['proveedor']}
        """)


def pagina_gestionar(df_productos: pd.DataFrame):
    """Página para gestionar el inventario (agregar/actualizar)."""
    st.header("✏️ Gestionar Inventario")
    
    tab1, tab2 = st.tabs(["➕ Agregar Producto", "🔄 Actualizar Stock"])
    
    with tab1:
        st.subheader("Agregar Nuevo Producto")
        
        with st.form("form_agregar"):
            col1, col2 = st.columns(2)
            
            with col1:
                nombre = st.text_input("📦 Nombre del Producto *")
                categorias = sorted(df_productos['categoria'].unique().tolist())
                categoria = st.selectbox("🏷️ Categoría", categorias)
                precio = st.number_input("💰 Precio (monedas)", min_value=1, value=100)
            
            with col2:
                stock = st.number_input("📊 Stock Inicial", min_value=0, value=10)
                proveedores = sorted(df_productos['proveedor'].unique().tolist())
                proveedor = st.selectbox("🏪 Proveedor", proveedores)
                descripcion = st.text_area("📝 Descripción *")
            
            submitted = st.form_submit_button("✅ Agregar Producto")
            
            if submitted:
                if not nombre or not descripcion:
                    st.error("❌ El nombre y la descripción son obligatorios")
                else:
                    nuevo_id = df_productos['id'].max() + 1
                    nuevo_producto = pd.DataFrame([{
                        'id': nuevo_id,
                        'nombre': nombre,
                        'categoria': categoria,
                        'precio': precio,
                        'stock': stock,
                        'descripcion': descripcion,
                        'proveedor': proveedor
                    }])
                    
                    df_actualizado = pd.concat([df_productos, nuevo_producto], ignore_index=True)
                    
                    if guardar_productos(df_actualizado):
                        st.success(f"✅ Producto '{nombre}' agregado exitosamente con ID {nuevo_id}")
                        st.cache_data.clear()
                        st.rerun()
    
    with tab2:
        st.subheader("Actualizar Stock de Producto")
        
        # Selector de producto
        productos_dict = dict(zip(df_productos['nombre'], df_productos['id']))
        producto_seleccionado = st.selectbox(
            "Selecciona un producto",
            options=list(productos_dict.keys())
        )
        
        if producto_seleccionado:
            producto_id = productos_dict[producto_seleccionado]
            producto = df_productos[df_productos['id'] == producto_id].iloc[0]
            
            st.info(f"""
            **Información actual:**
            - Stock actual: **{producto['stock']}** unidades
            - Precio: {producto['precio']} monedas
            - Categoría: {producto['categoria']}
            """)
            
            with st.form("form_actualizar"):
                operacion = st.radio(
                    "Tipo de operación",
                    ["➕ Agregar stock (recepción)", "➖ Reducir stock (venta)", "🔄 Establecer nuevo stock"]
                )
                
                if operacion == "🔄 Establecer nuevo stock":
                    nuevo_stock = st.number_input("Nuevo stock", min_value=0, value=int(producto['stock']))
                else:
                    cantidad = st.number_input("Cantidad", min_value=1, value=1)
                
                submitted = st.form_submit_button("💾 Actualizar Stock")
                
                if submitted:
                    if operacion == "➕ Agregar stock (recepción)":
                        nuevo_stock = producto['stock'] + cantidad
                        mensaje = f"Se agregaron {cantidad} unidades"
                    elif operacion == "➖ Reducir stock (venta)":
                        if cantidad > producto['stock']:
                            st.error(f"❌ No hay suficiente stock. Disponible: {producto['stock']}")
                            nuevo_stock = None
                        else:
                            nuevo_stock = producto['stock'] - cantidad
                            mensaje = f"Se redujeron {cantidad} unidades"
                    else:
                        mensaje = f"Stock establecido en {nuevo_stock} unidades"
                    
                    if nuevo_stock is not None:
                        df_productos.loc[df_productos['id'] == producto_id, 'stock'] = nuevo_stock
                        
                        if guardar_productos(df_productos):
                            st.success(f"✅ {mensaje}. Nuevo stock: {nuevo_stock} unidades")
                            if nuevo_stock <= UMBRAL_STOCK_BAJO:
                                st.warning("⚠️ ADVERTENCIA: Stock bajo. Considerar reabastecimiento.")
                            st.cache_data.clear()
                            st.rerun()


def pagina_ventas(df_ventas: pd.DataFrame, df_detalle: pd.DataFrame, df_productos: pd.DataFrame, df_clientes: pd.DataFrame):
    """Página para ver ventas."""
    st.header("💰 Gestión de Ventas")
    
    # Unir datos para mostrar información completa
    ventas_completo = df_ventas.merge(df_clientes, left_on='id_cliente', right_on='id', how='left')
    
    # Mostrar tabla de ventas
    st.subheader("📋 Historial de Ventas")
    st.dataframe(
        ventas_completo[['id_venta', 'nombre', 'fecha', 'total']].rename(columns={
            'nombre': 'Cliente',
            'fecha': 'Fecha',
            'total': 'Total (💰)'
        }),
        use_container_width=True,
        hide_index=True
    )
    
    # Seleccionar una venta para ver detalles
    st.markdown("---")
    st.subheader("🔍 Detalle de Venta")
    
    venta_seleccionada = st.selectbox(
        "Selecciona una venta:",
        options=df_ventas['id_venta'].tolist()
    )
    
    if venta_seleccionada:
        venta = df_ventas[df_ventas['id_venta'] == venta_seleccionada].iloc[0]
        cliente = df_clientes[df_clientes['id'] == venta['id_cliente']].iloc[0]
        detalles = df_detalle[df_detalle['id_venta'] == venta_seleccionada]
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"""
            **Venta #{venta_seleccionada}**
            - Cliente: {cliente['nombre']}
            - Fecha: {venta['fecha'].strftime('%Y-%m-%d')}
            - Total: {venta['total']:,.0f} 💰
            """)
        
        # Detalles de productos
        detalles_completo = detalles.merge(df_productos, left_on='id_producto', right_on='id', how='left')
        st.subheader("🛒 Productos Vendidos")
        st.dataframe(
            detalles_completo[['nombre', 'cantidad', 'precio_unitario', 'subtotal']].rename(columns={
                'nombre': 'Producto',
                'cantidad': 'Cantidad',
                'precio_unitario': 'Precio Unitario',
                'subtotal': 'Subtotal'
            }),
            use_container_width=True,
            hide_index=True
        )


def pagina_clientes(df_clientes: pd.DataFrame, df_ventas: pd.DataFrame):
    """Página para ver clientes."""
    st.header("👥 Gestión de Clientes")
    
    # Mostrar tabla de clientes
    st.subheader("📋 Lista de Clientes")
    st.dataframe(
        df_clientes[['id', 'nombre', 'email', 'telefono', 'ciudad', 'fecha_registro']],
        use_container_width=True,
        hide_index=True
    )
    
    # Estadísticas de clientes
    st.markdown("---")
    st.subheader("📊 Estadísticas de Clientes")
    
    # Clientes con más compras
    ventas_por_cliente = df_ventas.groupby('id_cliente').agg({
        'id_venta': 'count',
        'total': 'sum'
    }).rename(columns={
        'id_venta': 'Cantidad Ventas',
        'total': 'Total Gastado'
    }).sort_values('Total Gastado', ascending=False)
    
    clientes_top = df_clientes[df_clientes['id'].isin(ventas_por_cliente.index)].merge(
        ventas_por_cliente.reset_index(), left_on='id', right_on='id_cliente'
    )[['nombre', 'Cantidad Ventas', 'Total Gastado']]
    
    st.dataframe(
        clientes_top.style.format({
            'Total Gastado': '{:,.0f} 💰'
        }),
        use_container_width=True,
        hide_index=True
    )


def analizar_distribucion_streamlit(data, nombre_var):
    """Analiza la distribución de una variable para Streamlit."""
    data_clean = data.dropna()
    
    # Estadísticas de forma
    skewness = stats.skew(data_clean)
    kurtosis = stats.kurtosis(data_clean)
    
    # Test de normalidad
    if len(data_clean) <= 50:
        stat, p_value = shapiro(data_clean)
        test_name = "Shapiro-Wilk"
    else:
        stat, p_value = normaltest(data_clean)
        test_name = "D'Agostino-Pearson"
    
    # Interpretación
    if p_value > 0.05:
        tipo_dist = "Normal"
    elif skewness > 1:
        tipo_dist = "Asimétrica Positiva"
    elif skewness < -1:
        tipo_dist = "Asimétrica Negativa"
    else:
        tipo_dist = "No Normal"
    
    return {
        'tipo_dist': tipo_dist,
        'skewness': skewness,
        'kurtosis': kurtosis,
        'stat': stat,
        'p_value': p_value,
        'test_name': test_name
    }


def detectar_outliers_iqr_streamlit(data, nombre_var):
    """Detecta outliers usando el método IQR para Streamlit."""
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    
    return {
        'outliers': outliers,
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound,
        'count': len(outliers)
    }


def pagina_analisis_estadistico(df_productos: pd.DataFrame, df_clientes: pd.DataFrame, 
                                 df_ventas: pd.DataFrame, df_detalle: pd.DataFrame):
    """Página de análisis estadístico completo."""
    st.header("📈 Análisis Estadístico Completo")
    st.markdown("---")
    
    # Preparar datos combinados
    df_completo = df_detalle.merge(df_productos, left_on='id_producto', right_on='id', how='left')
    df_completo = df_completo.merge(df_ventas, left_on='id_venta', right_on='id_venta', how='left')
    
    # Tabs para organizar el análisis
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Estadísticas Descriptivas",
        "📈 Distribución de Variables",
        "🔗 Análisis de Correlaciones",
        "⚠️ Detección de Outliers",
        "📉 Gráficos Representativos"
    ])
    
    # ============================================================================
    # TAB 1: ESTADÍSTICAS DESCRIPTIVAS
    # ============================================================================
    with tab1:
        st.subheader("📊 Estadísticas Descriptivas Básicas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Productos")
            stats_productos = df_productos[['precio', 'stock']].describe()
            st.dataframe(stats_productos, use_container_width=True)
            
            st.markdown("**Información adicional:**")
            col1a, col1b = st.columns(2)
            with col1a:
                st.metric("Mediana Precio", f"{df_productos['precio'].median():.2f}")
                st.metric("Desv. Est. Precio", f"{df_productos['precio'].std():.2f}")
                st.metric("Rango Precio", f"{df_productos['precio'].max() - df_productos['precio'].min()}")
            with col1b:
                st.metric("Mediana Stock", f"{df_productos['stock'].median():.2f}")
                st.metric("Desv. Est. Stock", f"{df_productos['stock'].std():.2f}")
                st.metric("Rango Stock", f"{df_productos['stock'].max() - df_productos['stock'].min()}")
        
        with col2:
            st.markdown("### Ventas")
            stats_ventas = df_ventas[['total']].describe()
            st.dataframe(stats_ventas, use_container_width=True)
            
            st.markdown("**Información adicional:**")
            col2a, col2b = st.columns(2)
            with col2a:
                st.metric("Mediana Total", f"{df_ventas['total'].median():.2f}")
                st.metric("Desv. Est. Total", f"{df_ventas['total'].std():.2f}")
            with col2b:
                st.metric("Venta Máxima", f"{df_ventas['total'].max():.2f}")
                st.metric("Venta Mínima", f"{df_ventas['total'].min():.2f}")
        
        st.markdown("---")
        st.markdown("### Detalle de Ventas")
        stats_detalle = df_detalle[['cantidad', 'precio_unitario', 'subtotal']].describe()
        st.dataframe(stats_detalle, use_container_width=True)
    
    # ============================================================================
    # TAB 2: DISTRIBUCIÓN DE VARIABLES
    # ============================================================================
    with tab2:
        st.subheader("📈 Identificación del Tipo de Distribución")
        
        variable_seleccionada = st.selectbox(
            "Selecciona una variable para analizar:",
            ["Precio de Productos", "Stock de Productos", "Total de Ventas"]
        )
        
        if variable_seleccionada == "Precio de Productos":
            data = df_productos['precio']
            nombre = "Precio de Productos"
        elif variable_seleccionada == "Stock de Productos":
            data = df_productos['stock']
            nombre = "Stock de Productos"
        else:
            data = df_ventas['total']
            nombre = "Total de Ventas"
        
        # Análisis de distribución
        resultado = analizar_distribucion_streamlit(data, nombre)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Estadísticas de Forma")
            st.metric("Asimetría (Skewness)", f"{resultado['skewness']:.4f}")
            
            if abs(resultado['skewness']) < 0.5:
                st.success("✅ Distribución simétrica")
            elif resultado['skewness'] > 0:
                st.warning("⚠️ Distribución asimétrica positiva (sesgada a la derecha)")
            else:
                st.warning("⚠️ Distribución asimétrica negativa (sesgada a la izquierda)")
            
            st.metric("Curtosis (Kurtosis)", f"{resultado['kurtosis']:.4f}")
            if abs(resultado['kurtosis']) < 0.5:
                st.info("📊 Curtosis normal (similar a distribución normal)")
            elif resultado['kurtosis'] > 0:
                st.info("📊 Curtosis positiva (colas más pesadas)")
            else:
                st.info("📊 Curtosis negativa (colas más ligeras)")
        
        with col2:
            st.markdown("### Test de Normalidad")
            st.markdown(f"**Test utilizado:** {resultado['test_name']}")
            st.metric("Estadístico", f"{resultado['stat']:.4f}")
            st.metric("p-value", f"{resultado['p_value']:.4f}")
            
            if resultado['p_value'] > 0.05:
                st.success(f"✅ Los datos siguen una distribución normal (p > 0.05)")
            else:
                st.warning(f"⚠️ Los datos NO siguen una distribución normal (p ≤ 0.05)")
            
            st.markdown(f"**Tipo de distribución identificado:** {resultado['tipo_dist']}")
        
        # Gráfico de distribución
        st.markdown("---")
        st.markdown("### Visualización de la Distribución")
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Histograma
        axes[0].hist(data.dropna(), bins=20, edgecolor='black', alpha=0.7, color='skyblue')
        axes[0].set_title(f'Histograma de {nombre}')
        axes[0].set_xlabel(nombre)
        axes[0].set_ylabel('Frecuencia')
        axes[0].grid(True, alpha=0.3)
        
        # Box plot
        axes[1].boxplot(data.dropna(), vert=True)
        axes[1].set_title(f'Box Plot de {nombre}')
        axes[1].set_ylabel(nombre)
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Descripción del gráfico
        st.markdown("---")
        st.markdown("#### 📝 Interpretación del Gráfico")
        if variable_seleccionada == "Precio de Productos":
            st.info("""
            **Histograma:** Muestra la frecuencia de productos en diferentes rangos de precio. 
            La mayoría de productos se concentran en precios económicos y medios, con algunos productos premium 
            que elevan el promedio.
            
            **Box Plot:** Permite identificar valores atípicos (outliers) y mediana. Los puntos fuera de los bigotes 
            representan productos con precios excepcionalmente altos o bajos.
            """)
        elif variable_seleccionada == "Stock de Productos":
            st.info("""
            **Histograma:** Revela la distribución del inventario. La mayoría de productos tienen stock bajo o medio, 
            mientras que algunos productos de consumo masivo (como municiones) tienen stock muy alto.
            
            **Box Plot:** Muestra la dispersión del stock y ayuda a identificar productos con inventario 
            excepcionalmente alto o bajo que requieren atención especial.
            """)
        else:
            st.info("""
            **Histograma:** Muestra la distribución de los montos de venta. La mayoría de ventas son de montos moderados, 
            con algunas ventas grandes que representan compras importantes de equipamiento.
            
            **Box Plot:** Permite identificar el rango intercuartil y detectar ventas excepcionalmente grandes o pequeñas 
            que pueden requerir análisis adicional.
            """)
    
    # ============================================================================
    # TAB 3: ANÁLISIS DE CORRELACIONES
    # ============================================================================
    with tab3:
        st.subheader("🔗 Análisis de Correlaciones entre Variables")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Matriz de Correlación - Productos")
            corr_productos = df_productos[['precio', 'stock']].corr()
            
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(corr_productos, annot=True, fmt='.4f', cmap='coolwarm', 
                       center=0, square=True, linewidths=1, cbar_kws={"shrink": .8}, ax=ax)
            ax.set_title('Correlación Precio vs Stock')
            st.pyplot(fig)
            
            corr_precio_stock = corr_productos.loc['precio', 'stock']
            st.markdown(f"**Correlación Precio-Stock:** {corr_precio_stock:.4f}")
            
            if abs(corr_precio_stock) < 0.3:
                st.info("💡 Correlación débil o inexistente")
            elif abs(corr_precio_stock) < 0.7:
                st.info("💡 Correlación moderada")
            else:
                st.info("💡 Correlación fuerte")
            
            st.markdown("#### 📝 Interpretación")
            st.caption("""
            Este mapa de calor muestra la correlación entre precio y stock de productos. 
            Valores cercanos a 1 indican correlación positiva fuerte (a mayor precio, mayor stock), 
            mientras que valores cercanos a -1 indican correlación negativa (a mayor precio, menor stock). 
            Valores cercanos a 0 sugieren que no hay relación lineal entre estas variables.
            """)
        
        with col2:
            st.markdown("### Matriz de Correlación - Detalle de Ventas")
            corr_ventas = df_detalle[['cantidad', 'precio_unitario', 'subtotal']].corr()
            
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(corr_ventas, annot=True, fmt='.4f', cmap='coolwarm', 
                       center=0, square=True, linewidths=1, cbar_kws={"shrink": .8}, ax=ax)
            ax.set_title('Correlación entre Variables de Ventas')
            st.pyplot(fig)
            
            st.markdown("#### 📝 Interpretación")
            st.caption("""
            Este mapa de calor muestra las correlaciones entre cantidad vendida, precio unitario y subtotal. 
            Se espera una correlación fuerte entre precio_unitario y subtotal, ya que el subtotal es 
            cantidad × precio_unitario. La correlación entre cantidad y precio_unitario indica si los clientes 
            compran más cantidad cuando el precio es más alto o más bajo.
            """)
        
        st.markdown("---")
        st.markdown("### Correlación Precio vs Cantidad Vendida")
        
        # Preparar datos
        df_precio_cantidad = df_completo.groupby('id_producto').agg({
            'precio': 'first',
            'cantidad': 'sum'
        }).reset_index()
        
        corr_precio_cantidad = df_precio_cantidad[['precio', 'cantidad']].corr()
        corr_precio_cant = corr_precio_cantidad.loc['precio', 'cantidad']
        
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(df_precio_cantidad['precio'], df_precio_cantidad['cantidad'], 
                            alpha=0.6, s=100, c='steelblue', edgecolors='black', linewidth=0.5)
        ax.set_xlabel('Precio del Producto')
        ax.set_ylabel('Cantidad Total Vendida')
        ax.set_title(f'Relación Precio vs Cantidad Vendida (r={corr_precio_cant:.4f})')
        ax.grid(True, alpha=0.3)
        
        # Línea de tendencia
        z = np.polyfit(df_precio_cantidad['precio'], df_precio_cantidad['cantidad'], 1)
        p = np.poly1d(z)
        ax.plot(df_precio_cantidad['precio'], p(df_precio_cantidad['precio']), 
               "r--", alpha=0.8, linewidth=2, label='Tendencia')
        ax.legend()
        
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown(f"**Correlación Precio-Cantidad Vendida:** {corr_precio_cant:.4f}")
        
        st.markdown("#### 📝 Interpretación del Gráfico")
        st.info("""
        **Gráfico de Dispersión:** Cada punto representa un producto. El eje X muestra el precio del producto 
        y el eje Y muestra la cantidad total vendida.
        
        **Línea de Tendencia:** La línea roja muestra la tendencia general. Si la línea sube hacia la derecha, 
        los productos más caros se venden más. Si baja, los productos más baratos se venden más.
        
        **Insight:** Este análisis ayuda a determinar si existe una relación entre el precio y la demanda. 
        Una correlación negativa fuerte sugeriría que los productos más baratos son más populares, 
        mientras que una correlación positiva indicaría que los productos premium tienen buena aceptación.
        """)
        
        if corr_precio_cant < -0.3:
            st.warning("⚠️ Correlación negativa: productos más caros se venden menos")
        elif corr_precio_cant > 0.3:
            st.info("💡 Correlación positiva: productos más caros se venden más")
        else:
            st.info("💡 Correlación débil: el precio no influye mucho en la demanda")
    
    # ============================================================================
    # TAB 4: DETECCIÓN DE OUTLIERS
    # ============================================================================
    with tab4:
        st.subheader("⚠️ Detección de Outliers (Valores Extremos)")
        
        variable_outlier = st.selectbox(
            "Selecciona una variable para detectar outliers:",
            ["Precio de Productos", "Stock de Productos", "Total de Ventas"]
        )
        
        if variable_outlier == "Precio de Productos":
            data_outlier = df_productos['precio']
            nombre_outlier = "Precio de Productos"
        elif variable_outlier == "Stock de Productos":
            data_outlier = df_productos['stock']
            nombre_outlier = "Stock de Productos"
        else:
            data_outlier = df_ventas['total']
            nombre_outlier = "Total de Ventas"
        
        resultado_outlier = detectar_outliers_iqr_streamlit(data_outlier, nombre_outlier)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Métricas IQR")
            st.metric("Q1 (25%)", f"{resultado_outlier['Q1']:.2f}")
            st.metric("Q3 (75%)", f"{resultado_outlier['Q3']:.2f}")
            st.metric("IQR", f"{resultado_outlier['IQR']:.2f}")
            st.metric("Límite Inferior", f"{resultado_outlier['lower_bound']:.2f}")
            st.metric("Límite Superior", f"{resultado_outlier['upper_bound']:.2f}")
        
        with col2:
            st.markdown("### Resultados")
            st.metric("Outliers Detectados", resultado_outlier['count'])
            
            if resultado_outlier['count'] > 0:
                st.warning(f"⚠️ Se encontraron {resultado_outlier['count']} outliers")
                st.dataframe(
                    pd.DataFrame({
                        'Valor Outlier': resultado_outlier['outliers'].values,
                        'Índice': resultado_outlier['outliers'].index
                    }),
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.success("✅ No se detectaron outliers")
        
        # Visualización de outliers
        st.markdown("---")
        st.markdown("### Visualización de Outliers")
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Box plot con outliers marcados
        bp = axes[0].boxplot(data_outlier.dropna(), vert=True, patch_artist=True)
        bp['boxes'][0].set_facecolor('lightblue')
        axes[0].set_title(f'Box Plot de {nombre_outlier}')
        axes[0].set_ylabel(nombre_outlier)
        axes[0].grid(True, alpha=0.3)
        
        # Scatter plot con outliers destacados
        indices = np.arange(len(data_outlier))
        outliers_mask = (data_outlier < resultado_outlier['lower_bound']) | (data_outlier > resultado_outlier['upper_bound'])
        
        axes[1].scatter(indices[~outliers_mask], data_outlier[~outliers_mask], 
                       alpha=0.6, s=50, c='steelblue', label='Valores normales')
        axes[1].scatter(indices[outliers_mask], data_outlier[outliers_mask], 
                       alpha=0.8, s=100, c='red', marker='x', label='Outliers')
        axes[1].axhline(y=resultado_outlier['lower_bound'], color='orange', linestyle='--', label='Límite inferior')
        axes[1].axhline(y=resultado_outlier['upper_bound'], color='orange', linestyle='--', label='Límite superior')
        axes[1].set_xlabel('Índice')
        axes[1].set_ylabel(nombre_outlier)
        axes[1].set_title(f'Outliers Detectados en {nombre_outlier}')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Descripción del gráfico de outliers
        st.markdown("---")
        st.markdown("#### 📝 Interpretación del Gráfico")
        st.info("""
        **Box Plot (izquierda):** Muestra la distribución completa de los datos. Los puntos fuera de los bigotes 
        son valores atípicos detectados por el método IQR. El cuadro central representa el rango intercuartil (Q1-Q3), 
        y la línea dentro del cuadro es la mediana.
        
        **Scatter Plot (derecha):** Muestra cada valor individual identificado como outlier (marcados en rojo) 
        versus valores normales (azules). Las líneas naranjas horizontales indican los límites superior e inferior 
        para detectar outliers. Este gráfico ayuda a visualizar dónde se encuentran los valores extremos y 
        si forman patrones o son casos aislados.
        """)
    
    # ============================================================================
    # TAB 5: GRÁFICOS REPRESENTATIVOS
    # ============================================================================
    with tab5:
        st.subheader("📉 Gráficos Representativos del Análisis")
        
        # Gráfico 1: Histograma y Box Plot de Precios
        st.markdown("### Gráfico 1: Distribución de Precios de Productos")
        
        fig1, axes1 = plt.subplots(1, 2, figsize=(14, 5))
        
        axes1[0].hist(df_productos['precio'], bins=20, edgecolor='black', alpha=0.7, color='skyblue')
        axes1[0].set_title('Histograma de Precios')
        axes1[0].set_xlabel('Precio')
        axes1[0].set_ylabel('Frecuencia')
        axes1[0].grid(True, alpha=0.3)
        
        bp1 = axes1[1].boxplot(df_productos['precio'], vert=True, patch_artist=True)
        bp1['boxes'][0].set_facecolor('lightcoral')
        axes1[1].set_title('Box Plot de Precios')
        axes1[1].set_ylabel('Precio')
        axes1[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        st.pyplot(fig1)
        
        st.markdown("#### 📝 Interpretación del Gráfico")
        st.info("""
        **Histograma (izquierda):** Muestra la distribución de precios de todos los productos en el inventario. 
        Permite identificar patrones como concentración en rangos específicos de precio, presencia de productos premium, 
        y la simetría o asimetría de la distribución.
        
        **Box Plot (derecha):** Proporciona un resumen visual de la distribución de precios: mediana, cuartiles, 
        y valores extremos. Los puntos fuera de los bigotes representan productos con precios excepcionalmente altos 
        o bajos que pueden requerir análisis especial.
        
        **Aplicación práctica:** Este análisis ayuda a entender la estrategia de precios y identificar productos 
        que están fuera del rango esperado, lo cual puede indicar oportunidades de ajuste de precios o 
        productos especiales que requieren gestión diferenciada.
        """)
        
        # Gráfico 2: Heatmaps de correlación
        st.markdown("---")
        st.markdown("### Gráfico 2: Matrices de Correlación")
        
        fig2, axes2 = plt.subplots(1, 2, figsize=(14, 5))
        
        sns.heatmap(df_productos[['precio', 'stock']].corr(), annot=True, fmt='.4f', 
                   cmap='coolwarm', center=0, square=True, ax=axes2[0], cbar_kws={"shrink": .8})
        axes2[0].set_title('Correlación Productos')
        
        sns.heatmap(df_detalle[['cantidad', 'precio_unitario', 'subtotal']].corr(), 
                   annot=True, fmt='.4f', cmap='coolwarm', center=0, square=True, 
                   ax=axes2[1], cbar_kws={"shrink": .8})
        axes2[1].set_title('Correlación Ventas')
        
        plt.tight_layout()
        st.pyplot(fig2)
        
        st.markdown("#### 📝 Interpretación del Gráfico")
        st.info("""
        **Mapa de Calor de Productos (izquierda):** Muestra la correlación entre precio y stock de productos. 
        Un valor cercano a 0 indica que no hay relación lineal entre estas variables, lo cual es esperado 
        ya que el stock se gestiona según demanda y no necesariamente según precio.
        
        **Mapa de Calor de Ventas (derecha):** Revela las relaciones entre cantidad vendida, precio unitario y subtotal. 
        La correlación alta entre precio_unitario y subtotal es esperada (el subtotal es cantidad × precio_unitario). 
        La correlación entre cantidad y precio_unitario indica si los clientes compran más cuando los precios son altos o bajos.
        
        **Aplicación práctica:** Estas correlaciones ayudan a entender patrones de compra y a tomar decisiones sobre 
        estrategias de precios y gestión de inventario. Por ejemplo, si hay correlación negativa fuerte entre precio y cantidad, 
        podría indicar que los productos más baratos son más populares.
        """)
        
        # Gráfico 3: Análisis múltiple
        st.markdown("---")
        st.markdown("### Gráfico 3: Análisis de Outliers y Tendencias")
        
        fig3, axes3 = plt.subplots(2, 2, figsize=(14, 10))
        
        # Precio vs Stock con outliers
        outliers_precio = detectar_outliers_iqr_streamlit(df_productos['precio'], 'Precio')
        outliers_stock = detectar_outliers_iqr_streamlit(df_productos['stock'], 'Stock')
        
        precio_outlier_mask = (df_productos['precio'] < outliers_precio['lower_bound']) | (df_productos['precio'] > outliers_precio['upper_bound'])
        stock_outlier_mask = (df_productos['stock'] < outliers_stock['lower_bound']) | (df_productos['stock'] > outliers_stock['upper_bound'])
        
        axes3[0, 0].scatter(df_productos['precio'][~precio_outlier_mask], 
                           df_productos['stock'][~precio_outlier_mask], 
                           alpha=0.6, s=50, c='steelblue', label='Normal')
        axes3[0, 0].scatter(df_productos['precio'][precio_outlier_mask], 
                           df_productos['stock'][precio_outlier_mask], 
                           alpha=0.8, s=100, c='red', marker='x', label='Outlier Precio')
        axes3[0, 0].scatter(df_productos['precio'][stock_outlier_mask], 
                           df_productos['stock'][stock_outlier_mask], 
                           alpha=0.8, s=100, c='orange', marker='s', label='Outlier Stock')
        axes3[0, 0].set_xlabel('Precio')
        axes3[0, 0].set_ylabel('Stock')
        axes3[0, 0].set_title('Precio vs Stock (con Outliers)')
        axes3[0, 0].legend()
        axes3[0, 0].grid(True, alpha=0.3)
        
        # Box plot de ventas totales
        bp3 = axes3[0, 1].boxplot(df_ventas['total'], vert=True, patch_artist=True)
        bp3['boxes'][0].set_facecolor('lightgreen')
        axes3[0, 1].set_title('Distribución de Totales de Venta')
        axes3[0, 1].set_ylabel('Total Venta')
        axes3[0, 1].grid(True, alpha=0.3)
        
        # Ventas por fecha
        df_ventas_fecha = df_ventas.copy()
        df_ventas_fecha['fecha'] = pd.to_datetime(df_ventas_fecha['fecha'])
        ventas_por_fecha = df_ventas_fecha.groupby(df_ventas_fecha['fecha'].dt.date)['total'].sum()
        
        axes3[1, 0].plot(ventas_por_fecha.index, ventas_por_fecha.values, 
                        marker='o', linewidth=2, markersize=6, color='purple')
        axes3[1, 0].set_xlabel('Fecha')
        axes3[1, 0].set_ylabel('Total Ventas')
        axes3[1, 0].set_title('Evolución de Ventas por Fecha')
        axes3[1, 0].tick_params(axis='x', rotation=45)
        axes3[1, 0].grid(True, alpha=0.3)
        
        # Top 5 productos más vendidos
        productos_vendidos = df_detalle.groupby('id_producto')['cantidad'].sum().sort_values(ascending=False).head(5)
        productos_top = df_productos[df_productos['id'].isin(productos_vendidos.index)][['nombre', 'id']]
        productos_top = productos_top.merge(productos_vendidos.reset_index(), left_on='id', right_on='id_producto')
        
        axes3[1, 1].barh(productos_top['nombre'], productos_top['cantidad'], color='gold')
        axes3[1, 1].set_xlabel('Cantidad Vendida')
        axes3[1, 1].set_title('Top 5 Productos Más Vendidos')
        axes3[1, 1].grid(True, alpha=0.3, axis='x')
        
        plt.tight_layout()
        st.pyplot(fig3)
        
        st.markdown("#### 📝 Interpretación del Gráfico Completo")
        col_desc1, col_desc2 = st.columns(2)
        
        with col_desc1:
            st.markdown("**Panel Superior Izquierdo - Precio vs Stock con Outliers:**")
            st.caption("""
            Muestra la relación entre precio y stock, destacando productos con valores atípicos. 
            Los outliers en precio (rojos) pueden ser productos premium o económicos especiales. 
            Los outliers en stock (naranjas) pueden ser productos de consumo masivo o artículos únicos. 
            Este análisis ayuda a identificar productos que requieren gestión especial.
            """)
            
            st.markdown("**Panel Superior Derecho - Distribución de Totales de Venta:**")
            st.caption("""
            Muestra la distribución de los montos de venta mediante un box plot. Permite identificar 
            el rango típico de ventas, la mediana y valores extremos. Ventas muy altas pueden indicar 
            compras importantes de equipamiento, mientras que ventas muy bajas pueden ser compras de consumibles.
            """)
        
        with col_desc2:
            st.markdown("**Panel Inferior Izquierdo - Evolución de Ventas:**")
            st.caption("""
            Muestra la tendencia de ventas a lo largo del tiempo. Permite identificar patrones estacionales, 
            días de mayor venta, y tendencias generales. Una línea ascendente indica crecimiento, 
            mientras que picos y valles pueden indicar días especiales o eventos.
            """)
            
            st.markdown("**Panel Inferior Derecho - Top 5 Productos Más Vendidos:**")
            st.caption("""
            Identifica los productos con mayor volumen de ventas. Estos productos son clave para el negocio 
            y requieren atención especial en gestión de inventario, stock de seguridad y relación con proveedores. 
            Conocer estos productos ayuda a optimizar la estrategia de compras y marketing.
            """)
        
        # Resumen ejecutivo
        st.markdown("---")
        st.markdown("### 📋 Resumen Ejecutivo")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Distribuciones identificadas:**")
            dist_precio = analizar_distribucion_streamlit(df_productos['precio'], 'Precio')
            dist_stock = analizar_distribucion_streamlit(df_productos['stock'], 'Stock')
            dist_total = analizar_distribucion_streamlit(df_ventas['total'], 'Total')
            
            st.markdown(f"- Precio: {dist_precio['tipo_dist']}")
            st.markdown(f"- Stock: {dist_stock['tipo_dist']}")
            st.markdown(f"- Total Ventas: {dist_total['tipo_dist']}")
        
        with col2:
            st.markdown("**Correlaciones principales:**")
            corr_ps = df_productos[['precio', 'stock']].corr().loc['precio', 'stock']
            st.markdown(f"- Precio-Stock: {corr_ps:.4f}")
            
            df_precio_cant = df_completo.groupby('id_producto').agg({
                'precio': 'first',
                'cantidad': 'sum'
            }).reset_index()
            corr_pc = df_precio_cant[['precio', 'cantidad']].corr().loc['precio', 'cantidad']
            st.markdown(f"- Precio-Cantidad Vendida: {corr_pc:.4f}")
        
        with col3:
            st.markdown("**Outliers detectados:**")
            outliers_p = detectar_outliers_iqr_streamlit(df_productos['precio'], 'Precio')
            outliers_s = detectar_outliers_iqr_streamlit(df_productos['stock'], 'Stock')
            outliers_t = detectar_outliers_iqr_streamlit(df_ventas['total'], 'Total')
            
            st.markdown(f"- Precio: {outliers_p['count']} outliers")
            st.markdown(f"- Stock: {outliers_s['count']} outliers")
            st.markdown(f"- Total Ventas: {outliers_t['count']} outliers")


def pagina_power_bi():
    """Página con información y descarga del dashboard Power BI."""
    st.markdown("<h1 style='text-align: center; color: #D4AF37;'>📊 Dashboard Power BI - Tienda Aurelion</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Introducción
    st.markdown("""
    ### ⚔️ Dashboard Profesional en Power BI Desktop
    
    Además de esta aplicación web en Streamlit, el proyecto incluye un **dashboard profesional** 
    creado en **Microsoft Power BI Desktop** con visualizaciones interactivas avanzadas.
    """)
    
    # Resolución dinámica y robusta de rutas
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    # Rutas posibles para la imagen
    posibles_rutas_img = [
        os.path.join(project_root, "Power BI", "dashboard.jpg"),
        os.path.join(project_root, "Power BI", "dashboard.png"),
        os.path.join(project_root, "assets", "dashboard.jpg"),
        os.path.join(script_dir, "dashboard.jpg"),
    ]
    
    dashboard_img_path = next((p for p in posibles_rutas_img if os.path.exists(p)), None)

    if dashboard_img_path:
        st.image(
            dashboard_img_path,
            caption="Vista del Dashboard Power BI - Tienda Aurelion (Sprint 4)",
            use_container_width=True,  # Reemplazo de use_column_width
        )
    else:
        st.warning(
            "⚠️ No se encontró la imagen `dashboard.jpg` en la carpeta `Power BI/`. "
            "Verifica que el archivo exista en el repositorio para mostrar la vista previa."
        )
    
    # Columnas para layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        ### 🎯 Características del Dashboard
        
        #### 📄 Página: Overview (General)
        - **5 tarjetas KPI**: Total productos vendidos, valor inventario, stock total, total ventas, ingresos totales
        - **Gráfico de barras agrupadas**: Productos por categoría
        - **Gráfico de columnas**: Top 10 productos más valiosos
        - **Gráfico de anillo**: Distribución de stock por categoría
        - **Tabla con alertas**: Productos con stock bajo (< 20) con barras de datos
        - **Medidor (Gauge)**: Rotación de inventario
        
        #### 📊 Medidas DAX Implementadas
        - **11+ medidas** con diferentes tipos de función DAX
        - Funciones de Agregación: SUM, AVERAGE, COUNT, DISTINCTCOUNT
        - Funciones de Filtro: CALCULATE, FILTER
        - Funciones de Tiempo: DATEADD, DATESYTD, SAMEPERIODLASTYEAR
        - Funciones Lógicas: IF, SWITCH, VAR/RETURN
        - Funciones de Iteración: SUMX, AVERAGEX, COUNTROWS
        
        #### 🎯 KPIs
        - **Rotación de Inventario**: Con objetivo y estado
        - Análisis temporal (MoM, YoY, YTD)
        
        #### 🎨 Diseño Visual
        - **Tema medieval personalizado**: "Tienda Aurelion - Medieval Theme"
        - Colores: Dorado (#D4AF37), Rojo oscuro (#8B0000), Azul marino (#000080)
        - **Interactividad completa**: Cross-filtering entre visuales
        - **Relaciones entre 4 tablas**: Productos, Clientes, Ventas, Detalle_Ventas
        """)
    
    with col2:
        st.markdown("""
        ### 💾 Descargar Dashboard
        
        El dashboard está disponible en dos formatos:
        """)
        
        # Rutas posibles para el archivo .pbix
        posibles_rutas_pbix = [
            os.path.join(project_root, "Power BI", "Sprint4.pbix"),
            os.path.join(script_dir, "..", "Power BI", "Sprint4.pbix"),
            os.path.join(script_dir, "Sprint4.pbix"),
        ]
        
        pbix_path = next((p for p in posibles_rutas_pbix if os.path.exists(p)), None)
        
        if pbix_path:
            st.success("✅ Archivo de dashboard disponible")
            
            try:
                with open(pbix_path, "rb") as file:
                    st.download_button(
                        label="⬇️ Descargar Dashboard Sprint 4 (.pbix)",
                        data=file,
                        file_name="Sprint4.pbix",
                        mime="application/octet-stream"
                    )
                    
                st.info(f"""
                **📝 Tamaño del archivo**: {os.path.getsize(pbix_path) / 1024:.2f} KB
                
                **Formato**: .pbix (Power BI Desktop)
                
                **Ubicación**: `{os.path.relpath(pbix_path, project_root)}`
                """)
            except Exception as e:
                st.warning(f"El archivo existe pero hubo un error al preparar la descarga: {e}")
        else:
            st.warning("""
            ⚠️ **Archivo de dashboard no encontrado**
            
            El archivo `Sprint4.pbix` debe estar en la carpeta `Power BI/`
            
            **Para crear el dashboard:**
            1. Abre Power BI Desktop
            2. Sigue la guía: `Power BI/Guia_Paso_a_Paso_Medidas_DAX.md`
            3. Consulta: `Power BI/Documentacion_Sprint4.md`
            """)
        
        st.markdown("""
        ### 📥 Requisitos
        
        Para abrir el dashboard necesitas:
        - **[Power BI Desktop](https://powerbi.microsoft.com/desktop/)** (Gratis)
        - Windows 10/11 (recomendado)
        - Los archivos CSV en `datos/`
        """)
    
    st.markdown("---")
    
    # Instrucciones de uso
    st.markdown("""
    ### 🚀 Cómo Usar el Dashboard
    
    #### Opción 1: Archivo .pbix (Completo - Recomendado)
    1. Descarga el archivo `Sprint4.pbix` desde arriba
    2. Abre Power BI Desktop
    3. Doble click en el archivo `Sprint4.pbix`
    4. El dashboard se abrirá directamente con todos los datos y visualizaciones
    
    #### Opción 2: Crear desde Cero
    Si quieres crear o modificar el dashboard:
    1. **Leer el archivo actual**: `Power BI/Presentacion_Lectura_PowerBI.md`
    2. **Crear medidas DAX**: `Power BI/Guia_Paso_a_Paso_Medidas_DAX.md`
    3. **Código listo**: `Power BI/Codigo_DAX_Listo_Copiar.md`
    4. **Documentación completa**: `Power BI/Documentacion_Sprint4.md`
    5. **Ejemplos detallados**: `Power BI/Notebook_DAX_Ejemplos.md`
    """)
    
    st.markdown("---")
    
    # Información detallada del Sprint 4
    st.markdown("""
    ### 📊 Requisitos del Sprint 4
    
    Este dashboard cumple con los requisitos del Sprint 4:
    
    #### ✅ Jerarquías y Agrupaciones
    - **Jerarquía de Tiempo**: Año → Trimestre → Mes → Día
    - **Jerarquía de Productos**: Categoría → Proveedor → Producto
    - **Agrupaciones por Rangos**: Stock (Bajo/Medio/Alto) y Valor (Bajo/Medio/Alto)
    
    #### ✅ Medidas DAX (11+ medidas)
    - **Funciones de Agregación**: SUM, AVERAGE, COUNT, DISTINCTCOUNT, SUMX
    - **Funciones de Filtro**: CALCULATE, FILTER, VALUES
    - **Funciones de Tiempo**: DATEADD, DATESYTD, SAMEPERIODLASTYEAR, DATESINPERIOD
    - **Funciones Lógicas**: IF, SWITCH, VAR/RETURN
    - **Funciones de Texto**: CONCATENATEX
    - **Funciones de Iteración**: SUMX, AVERAGEX, COUNTROWS
    
    #### ✅ KPIs (3 KPIs completos)
    1. **Rotación de Inventario**: Valor actual, objetivo (2.5), estado
    2. **Margen de Utilidad**: Valor actual, objetivo (30%), estado
    3. **Nivel de Servicio**: Valor actual, objetivo (95%), estado
    
    #### ✅ Análisis Temporal
    - **Crecimiento Mes a Mes (MoM)**: Comparación con mes anterior
    - **Variación Interanual (YoY)**: Comparación con mismo período año anterior
    - **Ventas YTD**: Acumulado año a la fecha
    - **Promedios móviles**: Para identificar tendencias
    """)
    
    # KPIs y Métricas del Dashboard
    st.markdown("---")
    st.markdown("""
    ### 📊 KPIs y Métricas del Dashboard Sprint 4
    
    El dashboard incluye las siguientes métricas principales:
    """)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total Productos Vendidos", "Calculado con SUM")
        st.caption("Medida: -- Total de Productos Vendidos")
    with col2:
        st.metric("Valor Total Inventario", "Formato: Moneda")
        st.caption("Medida: -- Valor Total Inventario")
    with col3:
        st.metric("Stock Total", "Suma de stock")
        st.caption("Medida: -- Stock Total")
    with col4:
        st.metric("Total Ventas", "Cantidad de ventas")
        st.caption("Medida: -- Total de Ventas")
    with col5:
        st.metric("Ingresos Totales", "Formato: Moneda")
        st.caption("Medida: -- Ingresos Totales")
    
    st.markdown("---")
    st.markdown("""
    ### 🎯 KPIs con Objetivos
    
    | KPI | Valor Actual | Objetivo | Estado |
    |-----|--------------|----------|--------|
    | **Rotación de Inventario** | Calculado | 2.5 | ✅/⚠️/❌ |
    | **Margen de Utilidad** | Calculado | 30% | ✅/⚠️/❌ |
    | **Nivel de Servicio** | Calculado | 95% | ✅/⚠️/❌ |
    """)
    
    st.markdown("---")
    
    # Recursos adicionales
    st.markdown("""
    ### 📚 Recursos del Proyecto Sprint 4
    
    El proyecto incluye documentación completa y scripts:
    
    | Recurso | Descripción | Ubicación |
    |---------|-------------|-----------|
    | 📊 `Presentacion_Lectura_PowerBI.md` | Cómo leer y entender el archivo Power BI | `Power BI/` |
    | ⭐ `Guia_Paso_a_Paso_Medidas_DAX.md` | Guía paso a paso para crear medidas DAX | `Power BI/` |
    | 📋 `Codigo_DAX_Listo_Copiar.md` | Código DAX listo para copiar y pegar | `Power BI/` |
    | 📚 `Documentacion_Sprint4.md` | Documentación completa del proyecto | `Power BI/` |
    | 💡 `Notebook_DAX_Ejemplos.md` | Ejemplos detallados de código DAX | `Power BI/` |
    | 🐍 `procesamiento_datos.py` | **Script principal Python** para procesar datos | `Power BI/` |
    | 📖 `README_Sprint4.md` | Resumen ejecutivo y guía rápida | `Power BI/` |
    
    **Todos los archivos están en la carpeta `Power BI/`**
    
    **Para ejecutar el procesamiento de datos:**
    ```bash
    cd "tienda-aurelionV4/Power BI"
    python procesamiento_datos.py
    ```
    
    Los resultados se guardan en `Power BI/resultados/`
    """)
    
    # Comparación Streamlit vs Power BI
    st.markdown("---")
    st.markdown("""
    ### 🔄 Streamlit vs Power BI
    
    Ambas herramientas son excelentes para visualización de datos. Aquí una comparación:
    
    | Característica | Streamlit (Esta App) | Power BI Desktop |
    |----------------|----------------------|------------------|
    | **Plataforma** | Web (Python) | Desktop (Windows) |
    | **Instalación** | Ligera (pip install) | Requiere descarga (~500 MB) |
    | **Código** | Python (open source) | Interfaz gráfica + DAX |
    | **Interactividad** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
    | **Gráficos** | Matplotlib, Plotly | Visuales nativos de BI |
    | **Cross-filtering** | Manual | Automático |
    | **Medidas Calculadas** | Python/Pandas | DAX (más potente) |
    | **Compartir** | Deploy web fácil | Power BI Service (requiere cuenta) |
    | **Mejor para** | Análisis exploratorio, prototipos | Dashboards empresariales, KPIs |
    
    **💡 Recomendación**: Usa ambas herramientas según la situación:
    - **Streamlit**: Para análisis rápido, exploración de datos, demos online, ML
    - **Power BI**: Para reportes ejecutivos, presentaciones formales, análisis de negocio, KPIs
    """)
    
    st.markdown("---")
    
    # Información sobre procesamiento de datos
    st.markdown("""
    ### 🐍 Procesamiento de Datos con Python
    
    El proyecto incluye un script Python para procesar y analizar los datos:
    
    **Archivo**: `Power BI/procesamiento_datos.py`
    
    **Funcionalidades**:
    - ✅ Carga de datos desde CSV
    - ✅ Cálculo de métricas básicas
    - ✅ Análisis de rotación de inventario
    - ✅ Cálculo de margen de utilidad
    - ✅ Análisis temporal (MoM, YoY)
    - ✅ Creación de agrupaciones
    - ✅ Generación de archivos CSV procesados
    
    **Ejecución**:
    ```bash
    python "Power BI/procesamiento_datos.py"
    ```
    
    **Resultados**: Se guardan en `Power BI/resultados/`
    """)
    
    # Footer
    st.markdown("---")
    st.info("""
    **🎓 Sprint 4 - IBM - Power BI: Medidas, KPIs y Análisis Temporal**
    
    Proyecto completo con múltiples implementaciones:
    - ✅ Aplicación Web Streamlit (esta)
    - ✅ Dashboard Power BI Desktop con medidas DAX avanzadas
    - ✅ 11+ medidas DAX con diferentes funciones
    - ✅ 3 KPIs completos (valor, objetivo, estado)
    - ✅ Análisis temporal (MoM, YoY, YTD)
    - ✅ Jerarquías y agrupaciones
    - ✅ Scripts Python para procesamiento de datos
    - ✅ Documentación completa
    """)
    
    """Página con información y descarga del dashboard Power BI."""
    st.markdown("<h1 style='text-align: center; color: #D4AF37;'>📊 Dashboard Power BI - Tienda Aurelion</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Introducción
    st.markdown("""
    ### ⚔️ Dashboard Profesional en Power BI Desktop
    
    Además de esta aplicación web en Streamlit, el proyecto incluye un **dashboard profesional** 
    creado en **Microsoft Power BI Desktop** con visualizaciones interactivas avanzadas.
    """)
    
    # Mostrar imagen del dashboard si está disponible
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dashboard_img_path = os.path.join(script_dir, "..", "Power BI", "dashboard.jpg")

    if os.path.exists(dashboard_img_path):
        st.image(
            dashboard_img_path,
            caption="Vista del Dashboard Power BI - Tienda Aurelion (Sprint 4)",
            use_column_width=True,
        )
    else:
        st.warning(
            "⚠️ No se encontró la imagen `dashboard.jpg` en la carpeta `Power BI/`. "
            "Verifica que el archivo exista para mostrar la vista previa del dashboard."
        )
    
    # Columnas para layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        ### 🎯 Características del Dashboard
        
        #### 📄 Página: Overview (General)
        - **5 tarjetas KPI**: Total productos vendidos, valor inventario, stock total, total ventas, ingresos totales
        - **Gráfico de barras agrupadas**: Productos por categoría
        - **Gráfico de columnas**: Top 10 productos más valiosos
        - **Gráfico de anillo**: Distribución de stock por categoría
        - **Tabla con alertas**: Productos con stock bajo (< 20) con barras de datos
        - **Medidor (Gauge)**: Rotación de inventario
        
        #### 📊 Medidas DAX Implementadas
        - **11+ medidas** con diferentes tipos de función DAX
        - Funciones de Agregación: SUM, AVERAGE, COUNT, DISTINCTCOUNT
        - Funciones de Filtro: CALCULATE, FILTER
        - Funciones de Tiempo: DATEADD, DATESYTD, SAMEPERIODLASTYEAR
        - Funciones Lógicas: IF, SWITCH, VAR/RETURN
        - Funciones de Iteración: SUMX, AVERAGEX, COUNTROWS
        
        #### 🎯 KPIs
        - **Rotación de Inventario**: Con objetivo y estado
        - Análisis temporal (MoM, YoY, YTD)
        
        #### 🎨 Diseño Visual
        - **Tema medieval personalizado**: "Tienda Aurelion - Medieval Theme"
        - Colores: Dorado (#D4AF37), Rojo oscuro (#8B0000), Azul marino (#000080)
        - **Interactividad completa**: Cross-filtering entre visuales
        - **Relaciones entre 4 tablas**: Productos, Clientes, Ventas, Detalle_Ventas
        """)
    
    with col2:
        st.markdown("""
        ### 💾 Descargar Dashboard
        
        El dashboard está disponible en dos formatos:
        """)
        
        # Verificar si existe el archivo Sprint4.pbix
        pbix_path = os.path.join(script_dir, "..", "Power BI", "Sprint4.pbix")
        
        archivo_encontrado = os.path.exists(pbix_path)
        
        if archivo_encontrado:
            st.success("✅ Archivo de dashboard disponible")
            
            # Botón de descarga
            try:
                with open(pbix_path, "rb") as file:
                    btn = st.download_button(
                        label="⬇️ Descargar Dashboard Sprint 4 (.pbix)",
                        data=file,
                        file_name="Sprint4.pbix",
                        mime="application/octet-stream"
                    )
                    
                st.info(f"""
                **📝 Tamaño del archivo**: {os.path.getsize(pbix_path) / 1024:.2f} KB
                
                **Formato**: .pbix (Power BI Desktop)
                
                **Ubicación**: `Power BI/Sprint4.pbix`
                """)
            except Exception as e:
                st.warning(f"El archivo existe pero hubo un error al preparar la descarga: {e}")
        else:
            st.warning("""
            ⚠️ **Archivo de dashboard no encontrado**
            
            El archivo `Sprint4.pbix` debe estar en la carpeta `Power BI/`
            
            **Para crear el dashboard:**
            1. Abre Power BI Desktop
            2. Sigue la guía: `Power BI/Guia_Paso_a_Paso_Medidas_DAX.md`
            3. Consulta: `Power BI/Documentacion_Sprint4.md`
            """)
        
        st.markdown("""
        ### 📥 Requisitos
        
        Para abrir el dashboard necesitas:
        - **[Power BI Desktop](https://powerbi.microsoft.com/desktop/)** (Gratis)
        - Windows 10/11 (recomendado)
        - Los archivos CSV en `datos/`
        """)
    
    st.markdown("---")
    
    # Instrucciones de uso
    st.markdown("""
    ### 🚀 Cómo Usar el Dashboard
    
    #### Opción 1: Archivo .pbix (Completo - Recomendado)
    1. Descarga el archivo `Sprint4.pbix` desde arriba
    2. Abre Power BI Desktop
    3. Doble click en el archivo `Sprint4.pbix`
    4. El dashboard se abrirá directamente con todos los datos y visualizaciones
    
    #### Opción 2: Crear desde Cero
    Si quieres crear o modificar el dashboard:
    1. **Leer el archivo actual**: `Power BI/Presentacion_Lectura_PowerBI.md`
    2. **Crear medidas DAX**: `Power BI/Guia_Paso_a_Paso_Medidas_DAX.md`
    3. **Código listo**: `Power BI/Codigo_DAX_Listo_Copiar.md`
    4. **Documentación completa**: `Power BI/Documentacion_Sprint4.md`
    5. **Ejemplos detallados**: `Power BI/Notebook_DAX_Ejemplos.md`
    """)
    
    st.markdown("---")
    
    # Información detallada del Sprint 4
    st.markdown("""
    ### 📊 Requisitos del Sprint 4
    
    Este dashboard cumple con los requisitos del Sprint 4:
    
    #### ✅ Jerarquías y Agrupaciones
    - **Jerarquía de Tiempo**: Año → Trimestre → Mes → Día
    - **Jerarquía de Productos**: Categoría → Proveedor → Producto
    - **Agrupaciones por Rangos**: Stock (Bajo/Medio/Alto) y Valor (Bajo/Medio/Alto)
    
    #### ✅ Medidas DAX (11+ medidas)
    - **Funciones de Agregación**: SUM, AVERAGE, COUNT, DISTINCTCOUNT, SUMX
    - **Funciones de Filtro**: CALCULATE, FILTER, VALUES
    - **Funciones de Tiempo**: DATEADD, DATESYTD, SAMEPERIODLASTYEAR, DATESINPERIOD
    - **Funciones Lógicas**: IF, SWITCH, VAR/RETURN
    - **Funciones de Texto**: CONCATENATEX
    - **Funciones de Iteración**: SUMX, AVERAGEX, COUNTROWS
    
    #### ✅ KPIs (3 KPIs completos)
    1. **Rotación de Inventario**: Valor actual, objetivo (2.5), estado
    2. **Margen de Utilidad**: Valor actual, objetivo (30%), estado
    3. **Nivel de Servicio**: Valor actual, objetivo (95%), estado
    
    #### ✅ Análisis Temporal
    - **Crecimiento Mes a Mes (MoM)**: Comparación con mes anterior
    - **Variación Interanual (YoY)**: Comparación con mismo período año anterior
    - **Ventas YTD**: Acumulado año a la fecha
    - **Promedios móviles**: Para identificar tendencias
    """)
    
    # KPIs y Métricas del Dashboard
    st.markdown("---")
    st.markdown("""
    ### 📊 KPIs y Métricas del Dashboard Sprint 4
    
    El dashboard incluye las siguientes métricas principales:
    """)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total Productos Vendidos", "Calculado con SUM")
        st.caption("Medida: -- Total de Productos Vendidos")
    with col2:
        st.metric("Valor Total Inventario", "Formato: Moneda")
        st.caption("Medida: -- Valor Total Inventario")
    with col3:
        st.metric("Stock Total", "Suma de stock")
        st.caption("Medida: -- Stock Total")
    with col4:
        st.metric("Total Ventas", "Cantidad de ventas")
        st.caption("Medida: -- Total de Ventas")
    with col5:
        st.metric("Ingresos Totales", "Formato: Moneda")
        st.caption("Medida: -- Ingresos Totales")
    
    st.markdown("---")
    st.markdown("""
    ### 🎯 KPIs con Objetivos
    
    | KPI | Valor Actual | Objetivo | Estado |
    |-----|--------------|----------|--------|
    | **Rotación de Inventario** | Calculado | 2.5 | ✅/⚠️/❌ |
    | **Margen de Utilidad** | Calculado | 30% | ✅/⚠️/❌ |
    | **Nivel de Servicio** | Calculado | 95% | ✅/⚠️/❌ |
    """)
    
    st.markdown("---")
    
    # Recursos adicionales
    st.markdown("""
    ### 📚 Recursos del Proyecto Sprint 4
    
    El proyecto incluye documentación completa y scripts:
    
    | Recurso | Descripción | Ubicación |
    |---------|-------------|-----------|
    | 📊 `Presentacion_Lectura_PowerBI.md` | Cómo leer y entender el archivo Power BI | `Power BI/` |
    | ⭐ `Guia_Paso_a_Paso_Medidas_DAX.md` | Guía paso a paso para crear medidas DAX | `Power BI/` |
    | 📋 `Codigo_DAX_Listo_Copiar.md` | Código DAX listo para copiar y pegar | `Power BI/` |
    | 📚 `Documentacion_Sprint4.md` | Documentación completa del proyecto | `Power BI/` |
    | 💡 `Notebook_DAX_Ejemplos.md` | Ejemplos detallados de código DAX | `Power BI/` |
    | 🐍 `procesamiento_datos.py` | **Script principal Python** para procesar datos | `Power BI/` |
    | 📖 `README_Sprint4.md` | Resumen ejecutivo y guía rápida | `Power BI/` |
    
    **Todos los archivos están en la carpeta `Power BI/`**
    
    **Para ejecutar el procesamiento de datos:**
    ```bash
    cd "tienda-aurelionV4/Power BI"
    python procesamiento_datos.py
    ```
    
    Los resultados se guardan en `Power BI/resultados/`
    """)
    
    # Comparación Streamlit vs Power BI
    st.markdown("---")
    st.markdown("""
    ### 🔄 Streamlit vs Power BI
    
    Ambas herramientas son excelentes para visualización de datos. Aquí una comparación:
    
    | Característica | Streamlit (Esta App) | Power BI Desktop |
    |----------------|----------------------|------------------|
    | **Plataforma** | Web (Python) | Desktop (Windows) |
    | **Instalación** | Ligera (pip install) | Requiere descarga (~500 MB) |
    | **Código** | Python (open source) | Interfaz gráfica + DAX |
    | **Interactividad** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
    | **Gráficos** | Matplotlib, Plotly | Visuales nativos de BI |
    | **Cross-filtering** | Manual | Automático |
    | **Medidas Calculadas** | Python/Pandas | DAX (más potente) |
    | **Compartir** | Deploy web fácil | Power BI Service (requiere cuenta) |
    | **Mejor para** | Análisis exploratorio, prototipos | Dashboards empresariales, KPIs |
    
    **💡 Recomendación**: Usa ambas herramientas según la situación:
    - **Streamlit**: Para análisis rápido, exploración de datos, demos online, ML
    - **Power BI**: Para reportes ejecutivos, presentaciones formales, análisis de negocio, KPIs
    """)
    
    st.markdown("---")
    
    # Información sobre procesamiento de datos
    st.markdown("""
    ### 🐍 Procesamiento de Datos con Python
    
    El proyecto incluye un script Python para procesar y analizar los datos:
    
    **Archivo**: `Power BI/procesamiento_datos.py`
    
    **Funcionalidades**:
    - ✅ Carga de datos desde CSV
    - ✅ Cálculo de métricas básicas
    - ✅ Análisis de rotación de inventario
    - ✅ Cálculo de margen de utilidad
    - ✅ Análisis temporal (MoM, YoY)
    - ✅ Creación de agrupaciones
    - ✅ Generación de archivos CSV procesados
    
    **Ejecución**:
    ```bash
    python "Power BI/procesamiento_datos.py"
    ```
    
    **Resultados**: Se guardan en `Power BI/resultados/`
    """)
    
    # Footer
    st.markdown("---")
    st.info("""
    **🎓 Sprint 4 - IBM - Power BI: Medidas, KPIs y Análisis Temporal**
    
    Proyecto completo con múltiples implementaciones:
    - ✅ Aplicación Web Streamlit (esta)
    - ✅ Dashboard Power BI Desktop con medidas DAX avanzadas
    - ✅ 11+ medidas DAX con diferentes funciones
    - ✅ 3 KPIs completos (valor, objetivo, estado)
    - ✅ Análisis temporal (MoM, YoY, YTD)
    - ✅ Jerarquías y agrupaciones
    - ✅ Scripts Python para procesamiento de datos
    - ✅ Documentación completa
    """)


def pagina_machine_learning(df_productos: pd.DataFrame, df_clientes: pd.DataFrame, df_ventas: pd.DataFrame, df_detalle: pd.DataFrame):
    """Página de Machine Learning para predecir ventas."""
    st.header("🤖 Machine Learning - Predicción de Ventas")
    
    st.markdown("""
    ### 🎯 Objetivo del Modelo
    
    Predecir el **total de ventas** basándose en características de productos y patrones de compra usando **Random Forest Regressor**.
    
    **Características del modelo:**
    - 🌲 **Algoritmo**: Random Forest (100 árboles)
    - 📊 **Tipo**: Regresión supervisada
    - 🎯 **Variable objetivo**: Total de venta (monedas)
    - 📈 **Métricas**: MAE, RMSE, R², MAPE
    """)
    
    st.markdown("---")
    
    # Preparar datos para ML
    with st.spinner("🔄 Preparando datos y entrenando modelo..."):
        # Convertir fecha a datetime
        df_ventas_ml = df_ventas.copy()
        df_ventas_ml['fecha'] = pd.to_datetime(df_ventas_ml['fecha'])
        
        # Extraer características temporales
        df_ventas_ml['mes'] = df_ventas_ml['fecha'].dt.month
        df_ventas_ml['dia_semana'] = df_ventas_ml['fecha'].dt.dayofweek
        df_ventas_ml['dia_mes'] = df_ventas_ml['fecha'].dt.day
        
        # Unir detalle de ventas con productos
        df_detalle_productos = df_detalle.merge(
            df_productos[['id', 'categoria', 'precio']], 
            left_on='id_producto', 
            right_on='id'
        )
        
        # Calcular características agregadas por venta
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
        
        # Unir con datos de ventas
        df_ml = df_ventas_ml.merge(caracteristicas_ventas, on='id_venta')
        
        # Codificar categoría principal
        df_ml = pd.get_dummies(df_ml, columns=['categoria_principal'], prefix='cat')
        
        # Preparar X e y
        columnas_excluir = ['id_venta', 'id_cliente', 'fecha', 'total', 'subtotal_calculado']
        X = df_ml.drop(columns=columnas_excluir)
        y = df_ml['total']
        
        # División train/test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Entrenar modelo
        modelo = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
        modelo.fit(X_train, y_train)
        
        # Predicciones
        y_pred_train = modelo.predict(X_train)
        y_pred_test = modelo.predict(X_test)
        
        # Calcular métricas
        mae_test = mean_absolute_error(y_test, y_pred_test)
        rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
        r2_test = r2_score(y_test, y_pred_test)
        mape_test = np.mean(np.abs((y_test - y_pred_test) / y_test)) * 100
        
        mae_train = mean_absolute_error(y_train, y_pred_train)
        rmse_train = np.sqrt(mean_squared_error(y_train, y_pred_train))
        r2_train = r2_score(y_train, y_pred_train)
        mape_train = np.mean(np.abs((y_train - y_pred_train) / y_train)) * 100
    
    st.success("✅ Modelo entrenado exitosamente!")
    
    # Mostrar métricas
    st.subheader("📊 Métricas de Evaluación")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎓 Conjunto de Entrenamiento")
        metric_col1, metric_col2 = st.columns(2)
        with metric_col1:
            st.metric("R² Score", f"{r2_train:.4f}", help="Proporción de varianza explicada")
            st.metric("MAE", f"{mae_train:.2f} 💰", help="Error absoluto medio")
        with metric_col2:
            st.metric("RMSE", f"{rmse_train:.2f} 💰", help="Raíz del error cuadrático medio")
            st.metric("MAPE", f"{mape_train:.2f}%", help="Error porcentual medio")
    
    with col2:
        st.markdown("#### 🧪 Conjunto de Prueba")
        metric_col1, metric_col2 = st.columns(2)
        with metric_col1:
            st.metric("R² Score", f"{r2_test:.4f}", help="Proporción de varianza explicada")
            st.metric("MAE", f"{mae_test:.2f} 💰", help="Error absoluto medio")
        with metric_col2:
            st.metric("RMSE", f"{rmse_test:.2f} 💰", help="Raíz del error cuadrático medio")
            st.metric("MAPE", f"{mape_test:.2f}%", help="Error porcentual medio")
    
    # Interpretación
    st.info(f"""
    **💡 Interpretación del Modelo:**
    - El modelo explica el **{r2_test*100:.1f}%** de la variabilidad en las ventas
    - Error promedio de **{mae_test:.0f} monedas** por predicción
    - Error porcentual promedio de **{mape_test:.1f}%**
    """)
    
    st.markdown("---")
    
    # Gráficos
    st.subheader("📈 Visualizaciones del Modelo")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🎯 Predicciones vs Reales", 
        "📊 Distribución de Errores", 
        "🏆 Importancia de Características",
        "🔮 Predictor Interactivo"
    ])
    
    with tab1:
        st.markdown("#### Predicciones vs Valores Reales")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(y_test, y_pred_test, alpha=0.6, s=100, edgecolors='black', linewidth=0.5)
        ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 
                'r--', lw=2, label='Predicción Perfecta')
        ax.set_xlabel('Valor Real (monedas)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Predicción (monedas)', fontsize=12, fontweight='bold')
        ax.set_title('Predicciones vs Valores Reales (Conjunto de Prueba)', 
                     fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.text(0.05, 0.95, f'R² = {r2_test:.4f}', transform=ax.transAxes, 
                fontsize=12, verticalalignment='top', 
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        st.pyplot(fig)
        plt.close()
        
        st.markdown("""
        **Interpretación:**
        - Puntos cerca de la línea roja indican buenas predicciones
        - La dispersión muestra el error del modelo
        - R² indica qué tan bien el modelo explica la variabilidad
        """)
    
    with tab2:
        st.markdown("#### Distribución de Errores")
        errores = y_test - y_pred_test
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(errores, bins=15, edgecolor='black', alpha=0.7, color='skyblue')
        ax.axvline(x=0, color='red', linestyle='--', linewidth=2, label='Error = 0')
        ax.set_xlabel('Error (Real - Predicción)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Frecuencia', fontsize=12, fontweight='bold')
        ax.set_title('Distribución de Errores de Predicción', 
                     fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
        ax.text(0.05, 0.95, f'Media: {errores.mean():.2f}\nDesv. Est.: {errores.std():.2f}', 
                transform=ax.transAxes, fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        st.pyplot(fig)
        plt.close()
        
        st.markdown("""
        **Interpretación:**
        - Distribución centrada en 0 indica modelo sin sesgo
        - Forma de campana sugiere errores normales
        - Colas largas indican presencia de outliers
        """)
    
    with tab3:
        st.markdown("#### Importancia de Características")
        importancias = pd.DataFrame({
            'caracteristica': X.columns,
            'importancia': modelo.feature_importances_
        }).sort_values('importancia', ascending=False).head(10)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        colores = plt.cm.viridis(np.linspace(0, 1, len(importancias)))
        ax.barh(range(len(importancias)), importancias['importancia'], 
                color=colores, edgecolor='black')
        ax.set_yticks(range(len(importancias)))
        ax.set_yticklabels(importancias['caracteristica'])
        ax.set_xlabel('Importancia', fontsize=12, fontweight='bold')
        ax.set_ylabel('Característica', fontsize=12, fontweight='bold')
        ax.set_title('Top 10 Características Más Importantes', 
                     fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='x')
        ax.invert_yaxis()
        st.pyplot(fig)
        plt.close()
        
        st.markdown("**Top 5 Características:**")
        for i, row in importancias.head(5).iterrows():
            st.write(f"**{i+1}.** {row['caracteristica']}: {row['importancia']*100:.2f}%")
    
    with tab4:
        st.markdown("#### 🔮 Predictor Interactivo de Ventas")
        st.markdown("Ajusta los parámetros para predecir el total de una venta:")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            cantidad_total = st.slider("Cantidad de productos", 1, 50, 5)
            productos_unicos = st.slider("Productos únicos", 1, 10, 3)
        
        with col2:
            precio_promedio = st.slider("Precio promedio (💰)", 25, 5000, 500)
            mes = st.selectbox("Mes", list(range(1, 13)), index=4)
        
        with col3:
            dia_semana = st.selectbox("Día de la semana", 
                                      ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
                                      index=0)
            dia_mes = st.slider("Día del mes", 1, 31, 15)
        
        # Categoría principal
        categorias_disponibles = [col.replace('cat_', '') for col in X.columns if col.startswith('cat_')]
        categoria_seleccionada = st.selectbox("Categoría principal", categorias_disponibles)
        
        # Crear DataFrame para predicción
        nueva_venta = pd.DataFrame([{
            'cantidad_total': cantidad_total,
            'productos_unicos': productos_unicos,
            'precio_promedio': precio_promedio,
            'mes': mes,
            'dia_semana': ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"].index(dia_semana),
            'dia_mes': dia_mes
        }])
        
        # Agregar columnas de categorías (one-hot encoding)
        for col in X.columns:
            if col.startswith('cat_'):
                nueva_venta[col] = 1 if col == f'cat_{categoria_seleccionada}' else 0
        
        # Asegurar que todas las columnas estén presentes
        for col in X.columns:
            if col not in nueva_venta.columns:
                nueva_venta[col] = 0
        
        # Reordenar columnas para que coincidan con X
        nueva_venta = nueva_venta[X.columns]
        
        # Hacer predicción
        if st.button("🎯 Predecir Total de Venta", type="primary"):
            prediccion = modelo.predict(nueva_venta)[0]
            
            st.success(f"### 💰 Venta Estimada: **{prediccion:.2f} monedas**")
            
            # Mostrar rango de confianza (aproximado)
            margen = mae_test
            st.info(f"""
            **📊 Rango de Confianza (±MAE):**
            - Mínimo: {prediccion - margen:.2f} 💰
            - Máximo: {prediccion + margen:.2f} 💰
            
            *El modelo tiene un error promedio de {mae_test:.0f} monedas*
            """)
            
            # Comparar con ventas reales
            venta_min = y.min()
            venta_max = y.max()
            venta_promedio = y.mean()
            
            st.markdown("**📈 Comparación con Ventas Históricas:**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Venta Mínima", f"{venta_min:.0f} 💰")
            with col2:
                st.metric("Venta Promedio", f"{venta_promedio:.0f} 💰")
            with col3:
                st.metric("Venta Máxima", f"{venta_max:.0f} 💰")
    
    # Información adicional
    st.markdown("---")
    st.subheader("📚 Información del Modelo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🔧 Configuración del Modelo:**
        - Algoritmo: Random Forest Regressor
        - Número de árboles: 100
        - División: 80% entrenamiento, 20% prueba
        - Random state: 42 (reproducibilidad)
        """)
    
    with col2:
        st.markdown(f"""
        **📊 Datos Utilizados:**
        - Total de ventas: {len(df_ml)}
        - Entrenamiento: {len(X_train)} ventas
        - Prueba: {len(X_test)} ventas
        - Características: {X.shape[1]}
        """)
    
    st.markdown("""
    **💡 Recomendaciones:**
    - El modelo funciona mejor con ventas típicas (no extremas)
    - Actualizar el modelo periódicamente con nuevos datos
    - Usar las predicciones como estimaciones, no valores exactos
    - Considerar factores externos (promociones, temporadas)
    """)



def main():
    """Función principal de la aplicación."""
    # Cargar datos
    df_productos, df_clientes, df_ventas, df_detalle = cargar_datos()
    
    if df_productos.empty or df_clientes.empty or df_ventas.empty or df_detalle.empty:
        st.error("No se pudieron cargar los datos. Verifica que todos los archivos CSV existen.")
        return
    
    # Header
    mostrar_header()
    
    # Menú de navegación en sidebar
    st.sidebar.title("🎮 Navegación")
    pagina = st.sidebar.radio(
        "Selecciona una página:",
        ["🏠 Inicio", "🔍 Explorar Productos", "📊 Estadísticas", "📈 Análisis Estadístico", "🤖 Machine Learning", "✏️ Gestionar Inventario", "💰 Ventas", "👥 Clientes", "📊 Dashboard Power BI"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info(f"""
    **📊 Resumen Rápido**
    - Total productos: **{len(df_productos)}**
    - Total clientes: **{len(df_clientes)}**
    - Total ventas: **{len(df_ventas)}**
    - Stock total: **{df_productos['stock'].sum():,}**
    - Valor inventario: **{(df_productos['precio'] * df_productos['stock']).sum():,} 💰**
    - Ingresos totales: **{df_ventas['total'].sum():,.0f} 💰**
    """)
    
    # Mostrar página seleccionada
    if pagina == "🏠 Inicio":
        pagina_inicio(df_productos, df_clientes, df_ventas, df_detalle)
    elif pagina == "🔍 Explorar Productos":
        pagina_productos(df_productos)
    elif pagina == "📊 Estadísticas":
        pagina_estadisticas(df_productos, df_clientes, df_ventas, df_detalle)
    elif pagina == "📈 Análisis Estadístico":
        pagina_analisis_estadistico(df_productos, df_clientes, df_ventas, df_detalle)
    elif pagina == "🤖 Machine Learning":
        pagina_machine_learning(df_productos, df_clientes, df_ventas, df_detalle)
    elif pagina == "✏️ Gestionar Inventario":
        pagina_gestionar(df_productos)
    elif pagina == "💰 Ventas":
        pagina_ventas(df_ventas, df_detalle, df_productos, df_clientes)
    elif pagina == "👥 Clientes":
        pagina_clientes(df_clientes, df_ventas)
    elif pagina == "📊 Dashboard Power BI":
        pagina_power_bi()
    
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.8rem;'>
        ⚔️ <b>Tienda Aurelion</b><br>
        Sistema de Gestión v4.0<br>
        IBM - Sprint 4 - Power BI
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

