"""
╔═══════════════════════════════════════════════════════════════╗
║     ANÁLISIS ESTADÍSTICO - TIENDA AURELION                     ║
║     Sprint 2 - Introducción a la IA - IBM                     ║
║                                                                ║
║     Autor: Martos Ludmila                                      ║
║     DNI: 34811650                                             ║
╚═══════════════════════════════════════════════════════════════╝

Script para realizar análisis estadístico completo:
- Estadísticas descriptivas básicas
- Identificación de distribución de variables
- Análisis de correlaciones
- Detección de outliers
- Generación de gráficos representativos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import normaltest, shapiro
import os
import sys
import warnings
warnings.filterwarnings('ignore')

# Configurar codificación UTF-8 para Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Configuración de gráficos
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

# Detectar rutas de archivos
def obtener_rutas_csv():
    """Obtiene las rutas correctas de los CSVs."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_dir, "..", "datos")
    return {
        'productos': os.path.join(base_dir, "productos.csv"),
        'clientes': os.path.join(base_dir, "clientes.csv"),
        'ventas': os.path.join(base_dir, "ventas.csv"),
        'detalle_ventas': os.path.join(base_dir, "detalle_ventas.csv")
    }

ARCHIVOS_CSV = obtener_rutas_csv()

# Cargar datos
print("=" * 80)
print("CARGANDO DATOS...")
print("=" * 80)

df_productos = pd.read_csv(ARCHIVOS_CSV['productos'], encoding='utf-8')
df_clientes = pd.read_csv(ARCHIVOS_CSV['clientes'], encoding='utf-8')
df_ventas = pd.read_csv(ARCHIVOS_CSV['ventas'], encoding='utf-8')
df_detalle = pd.read_csv(ARCHIVOS_CSV['detalle_ventas'], encoding='utf-8')

# Preparar datos combinados para análisis
df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'])
df_completo = df_detalle.merge(df_productos, left_on='id_producto', right_on='id', how='left')
df_completo = df_completo.merge(df_ventas, left_on='id_venta', right_on='id_venta', how='left')
df_completo = df_completo.merge(df_clientes, left_on='id_cliente', right_on='id', how='left')

print(f"✅ Productos cargados: {len(df_productos)}")
print(f"✅ Clientes cargados: {len(df_clientes)}")
print(f"✅ Ventas cargadas: {len(df_ventas)}")
print(f"✅ Detalles de ventas: {len(df_detalle)}")
print()

# ============================================================================
# 1. ESTADÍSTICAS DESCRIPTIVAS BÁSICAS
# ============================================================================
print("=" * 80)
print("1. ESTADÍSTICAS DESCRIPTIVAS BÁSICAS")
print("=" * 80)

# Variables numéricas principales
variables_numericas = ['precio', 'stock', 'cantidad', 'precio_unitario', 'subtotal', 'total']

print("\n📊 ESTADÍSTICAS DESCRIPTIVAS - PRODUCTOS")
print("-" * 80)
stats_productos = df_productos[['precio', 'stock']].describe()
print(stats_productos)
print(f"\n📈 Información adicional:")
print(f"   - Mediana de precio: {df_productos['precio'].median():.2f}")
print(f"   - Mediana de stock: {df_productos['stock'].median():.2f}")
print(f"   - Desviación estándar precio: {df_productos['precio'].std():.2f}")
print(f"   - Desviación estándar stock: {df_productos['stock'].std():.2f}")
print(f"   - Rango precio: {df_productos['precio'].max() - df_productos['precio'].min()}")
print(f"   - Rango stock: {df_productos['stock'].max() - df_productos['stock'].min()}")

print("\n📊 ESTADÍSTICAS DESCRIPTIVAS - VENTAS")
print("-" * 80)
stats_ventas = df_ventas[['total']].describe()
print(stats_ventas)
print(f"\n   - Mediana: {df_ventas['total'].median():.2f}")
print(f"   - Desviación estándar: {df_ventas['total'].std():.2f}")

print("\n📊 ESTADÍSTICAS DESCRIPTIVAS - DETALLE DE VENTAS")
print("-" * 80)
stats_detalle = df_detalle[['cantidad', 'precio_unitario', 'subtotal']].describe()
print(stats_detalle)

# ============================================================================
# 2. IDENTIFICACIÓN DEL TIPO DE DISTRIBUCIÓN DE VARIABLES
# ============================================================================
print("\n" + "=" * 80)
print("2. IDENTIFICACIÓN DEL TIPO DE DISTRIBUCIÓN DE VARIABLES")
print("=" * 80)

def analizar_distribucion(data, nombre_var):
    """Analiza la distribución de una variable."""
    print(f"\n📈 Análisis de distribución: {nombre_var}")
    print("-" * 80)
    
    # Estadísticas de forma
    skewness = stats.skew(data.dropna())
    kurtosis = stats.kurtosis(data.dropna())
    
    print(f"   Asimetría (Skewness): {skewness:.4f}")
    print(f"   Curtosis (Kurtosis): {kurtosis:.4f}")
    
    # Test de normalidad (Shapiro-Wilk para muestras pequeñas)
    if len(data.dropna()) <= 50:
        stat, p_value = shapiro(data.dropna())
        test_name = "Shapiro-Wilk"
    else:
        stat, p_value = normaltest(data.dropna())
        test_name = "D'Agostino-Pearson"
    
    print(f"\n   Test de normalidad ({test_name}):")
    print(f"   - Estadístico: {stat:.4f}")
    print(f"   - p-value: {p_value:.4f}")
    
    # Interpretación
    if p_value > 0.05:
        print(f"   ✅ Los datos siguen una distribución normal (p > 0.05)")
        tipo_dist = "Normal"
    elif skewness > 1:
        print(f"   ⚠️  Distribución asimétrica positiva (sesgada a la derecha)")
        tipo_dist = "Asimétrica Positiva"
    elif skewness < -1:
        print(f"   ⚠️  Distribución asimétrica negativa (sesgada a la izquierda)")
        tipo_dist = "Asimétrica Negativa"
    else:
        print(f"   ⚠️  Distribución no normal")
        tipo_dist = "No Normal"
    
    return tipo_dist, skewness, kurtosis

distribuciones = {}
distribuciones['precio'], skew_precio, kurt_precio = analizar_distribucion(df_productos['precio'], 'Precio de Productos')
distribuciones['stock'], skew_stock, kurt_stock = analizar_distribucion(df_productos['stock'], 'Stock de Productos')
distribuciones['total'], skew_total, kurt_total = analizar_distribucion(df_ventas['total'], 'Total de Ventas')

# ============================================================================
# 3. ANÁLISIS DE CORRELACIONES ENTRE VARIABLES PRINCIPALES
# ============================================================================
print("\n" + "=" * 80)
print("3. ANÁLISIS DE CORRELACIONES ENTRE VARIABLES PRINCIPALES")
print("=" * 80)

# Matriz de correlación para variables numéricas de productos
print("\n📊 Matriz de Correlación - Variables de Productos")
print("-" * 80)
corr_productos = df_productos[['precio', 'stock']].corr()
print(corr_productos)
print(f"\n   Correlación Precio-Stock: {corr_productos.loc['precio', 'stock']:.4f}")

# Matriz de correlación para variables de ventas
print("\n📊 Matriz de Correlación - Variables de Ventas")
print("-" * 80)
corr_ventas = df_detalle[['cantidad', 'precio_unitario', 'subtotal']].corr()
print(corr_ventas)

# Correlación entre precio de producto y cantidad vendida
print("\n📊 Correlación Precio vs Cantidad Vendida")
print("-" * 80)
df_precio_cantidad = df_completo.groupby('id_producto').agg({
    'precio': 'first',
    'cantidad': 'sum'
}).reset_index()
corr_precio_cantidad = df_precio_cantidad[['precio', 'cantidad']].corr()
print(corr_precio_cantidad)
print(f"\n   Correlación Precio-Cantidad Vendida: {corr_precio_cantidad.loc['precio', 'cantidad']:.4f}")

# Interpretación de correlaciones
print("\n💡 Interpretación de Correlaciones:")
print("-" * 80)
corr_precio_stock = corr_productos.loc['precio', 'stock']
if abs(corr_precio_stock) < 0.3:
    print("   - Precio y Stock: Correlación débil o inexistente")
elif abs(corr_precio_stock) < 0.7:
    print("   - Precio y Stock: Correlación moderada")
else:
    print("   - Precio y Stock: Correlación fuerte")

corr_precio_cant = corr_precio_cantidad.loc['precio', 'cantidad']
if corr_precio_cant < -0.3:
    print("   - Precio y Cantidad Vendida: Correlación negativa (productos más caros se venden menos)")
elif corr_precio_cant > 0.3:
    print("   - Precio y Cantidad Vendida: Correlación positiva (productos más caros se venden más)")
else:
    print("   - Precio y Cantidad Vendida: Correlación débil (el precio no influye mucho en la demanda)")

# ============================================================================
# 4. DETECCIÓN DE OUTLIERS (VALORES EXTREMOS)
# ============================================================================
print("\n" + "=" * 80)
print("4. DETECCIÓN DE OUTLIERS (VALORES EXTREMOS)")
print("=" * 80)

def detectar_outliers_iqr(data, nombre_var):
    """Detecta outliers usando el método IQR."""
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    
    print(f"\n📊 Detección de Outliers: {nombre_var}")
    print("-" * 80)
    print(f"   Q1 (25%): {Q1:.2f}")
    print(f"   Q3 (75%): {Q3:.2f}")
    print(f"   IQR: {IQR:.2f}")
    print(f"   Límite inferior: {lower_bound:.2f}")
    print(f"   Límite superior: {upper_bound:.2f}")
    print(f"   Outliers detectados: {len(outliers)}")
    
    if len(outliers) > 0:
        print(f"   Valores outliers:")
        for idx, val in outliers.items():
            print(f"     - {val:.2f}")
    else:
        print(f"   ✅ No se detectaron outliers")
    
    return outliers

outliers_precio = detectar_outliers_iqr(df_productos['precio'], 'Precio de Productos')
outliers_stock = detectar_outliers_iqr(df_productos['stock'], 'Stock de Productos')
outliers_total = detectar_outliers_iqr(df_ventas['total'], 'Total de Ventas')

# ============================================================================
# 5. GRÁFICOS REPRESENTATIVOS
# ============================================================================
print("\n" + "=" * 80)
print("5. GENERANDO GRÁFICOS REPRESENTATIVOS")
print("=" * 80)

# Crear carpeta para gráficos si no existe
output_dir = os.path.join(os.path.dirname(__file__), "..", "graficos")
os.makedirs(output_dir, exist_ok=True)

# GRÁFICO 1: Distribución de Precios con Histograma y Curva Normal
print("\n📊 Generando Gráfico 1: Distribución de Precios...")
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Histograma de precios
axes[0].hist(df_productos['precio'], bins=15, edgecolor='black', alpha=0.7, color='skyblue')
axes[0].axvline(df_productos['precio'].mean(), color='red', linestyle='--', linewidth=2, label=f'Media: {df_productos["precio"].mean():.2f}')
axes[0].axvline(df_productos['precio'].median(), color='green', linestyle='--', linewidth=2, label=f'Mediana: {df_productos["precio"].median():.2f}')
axes[0].set_xlabel('Precio (monedas de oro)', fontsize=12)
axes[0].set_ylabel('Frecuencia', fontsize=12)
axes[0].set_title('Distribución de Precios de Productos', fontsize=14, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Box plot de precios
box_data = [df_productos['precio']]
axes[1].boxplot(box_data, labels=['Precio'])
axes[1].set_ylabel('Precio (monedas de oro)', fontsize=12)
axes[1].set_title('Box Plot - Precios de Productos', fontsize=14, fontweight='bold')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'grafico1_distribucion_precios.png'), dpi=300, bbox_inches='tight')
print("   ✅ Guardado: grafico1_distribucion_precios.png")
plt.close()

# GRÁFICO 2: Correlación entre Variables Principales
print("📊 Generando Gráfico 2: Matriz de Correlación...")
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Matriz de correlación productos
corr_mat_productos = df_productos[['precio', 'stock']].corr()
sns.heatmap(corr_mat_productos, annot=True, fmt='.3f', cmap='coolwarm', center=0,
            square=True, linewidths=2, ax=axes[0], cbar_kws={"shrink": 0.8})
axes[0].set_title('Correlación: Precio vs Stock', fontsize=14, fontweight='bold')

# Matriz de correlación ventas
corr_mat_ventas = df_detalle[['cantidad', 'precio_unitario', 'subtotal']].corr()
sns.heatmap(corr_mat_ventas, annot=True, fmt='.3f', cmap='coolwarm', center=0,
            square=True, linewidths=2, ax=axes[1], cbar_kws={"shrink": 0.8})
axes[1].set_title('Correlación: Variables de Ventas', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'grafico2_matriz_correlacion.png'), dpi=300, bbox_inches='tight')
print("   ✅ Guardado: grafico2_matriz_correlacion.png")
plt.close()

# GRÁFICO 3: Análisis de Outliers y Tendencias de Ventas
print("📊 Generando Gráfico 3: Análisis de Outliers y Ventas...")
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Scatter plot Precio vs Stock con outliers marcados
axes[0, 0].scatter(df_productos['precio'], df_productos['stock'], alpha=0.6, s=100, color='steelblue')
# Marcar outliers de precio
if len(outliers_precio) > 0:
    outliers_df = df_productos[df_productos['precio'].isin(outliers_precio)]
    axes[0, 0].scatter(outliers_df['precio'], outliers_df['stock'], color='red', s=150, marker='x', 
                       label='Outliers', linewidths=3)
axes[0, 0].set_xlabel('Precio (monedas)', fontsize=11)
axes[0, 0].set_ylabel('Stock (unidades)', fontsize=11)
axes[0, 0].set_title('Precio vs Stock (Outliers marcados)', fontsize=12, fontweight='bold')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Box plot de total de ventas
axes[0, 1].boxplot([df_ventas['total']], labels=['Total Ventas'])
axes[0, 1].set_ylabel('Total (monedas)', fontsize=11)
axes[0, 1].set_title('Distribución de Totales de Ventas', fontsize=12, fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)

# Ventas por fecha
df_ventas_fecha = df_ventas.groupby(df_ventas['fecha'].dt.date)['total'].sum().reset_index()
df_ventas_fecha['fecha'] = pd.to_datetime(df_ventas_fecha['fecha'])
axes[1, 0].plot(df_ventas_fecha['fecha'], df_ventas_fecha['total'], marker='o', linewidth=2, markersize=8, color='green')
axes[1, 0].set_xlabel('Fecha', fontsize=11)
axes[1, 0].set_ylabel('Total Ventas (monedas)', fontsize=11)
axes[1, 0].set_title('Evolución de Ventas por Fecha', fontsize=12, fontweight='bold')
axes[1, 0].tick_params(axis='x', rotation=45)
axes[1, 0].grid(True, alpha=0.3)

# Top 5 productos más vendidos
productos_vendidos = df_detalle.groupby('id_producto')['cantidad'].sum().sort_values(ascending=False).head(5)
productos_top = df_productos[df_productos['id'].isin(productos_vendidos.index)][['nombre', 'id']]
productos_top = productos_top.merge(productos_vendidos.reset_index(), left_on='id', right_on='id_producto')
axes[1, 1].barh(productos_top['nombre'], productos_top['cantidad'], color='coral')
axes[1, 1].set_xlabel('Cantidad Vendida', fontsize=11)
axes[1, 1].set_title('Top 5 Productos Más Vendidos', fontsize=12, fontweight='bold')
axes[1, 1].grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'grafico3_outliers_ventas.png'), dpi=300, bbox_inches='tight')
print("   ✅ Guardado: grafico3_outliers_ventas.png")
plt.close()

print("\n✅ Todos los gráficos generados exitosamente en la carpeta 'graficos/'")

# ============================================================================
# 6. RESUMEN EJECUTIVO
# ============================================================================
print("\n" + "=" * 80)
print("RESUMEN EJECUTIVO DEL ANÁLISIS")
print("=" * 80)

print("\n📊 VARIABLES ANALIZADAS:")
print(f"   - Precio de productos: {len(df_productos)} registros")
print(f"   - Stock de productos: {len(df_productos)} registros")
print(f"   - Total de ventas: {len(df_ventas)} registros")
print(f"   - Detalles de ventas: {len(df_detalle)} registros")

print("\n📈 DISTRIBUCIONES IDENTIFICADAS:")
for var, tipo in distribuciones.items():
    print(f"   - {var.capitalize()}: {tipo}")

print("\n🔗 CORRELACIONES PRINCIPALES:")
print(f"   - Precio vs Stock: {corr_productos.loc['precio', 'stock']:.4f}")
print(f"   - Precio vs Cantidad Vendida: {corr_precio_cantidad.loc['precio', 'cantidad']:.4f}")

print("\n⚠️  OUTLIERS DETECTADOS:")
print(f"   - Precio: {len(outliers_precio)} valores extremos")
print(f"   - Stock: {len(outliers_stock)} valores extremos")
print(f"   - Total Ventas: {len(outliers_total)} valores extremos")

print("\n" + "=" * 80)
print("ANÁLISIS COMPLETADO EXITOSAMENTE")
print("=" * 80)

print("\n💡 VISUALIZACIÓN INTERACTIVA:")
print("   Los datos de este análisis también están disponibles en:")
print("   • Dashboard Power BI Desktop (ver Sprint-2/documentacion/GUIA_RAPIDA_DASHBOARD_POWERBI.md)")
print("   • Aplicación Streamlit (ejecuta: streamlit run programas/app_streamlit.py)")
print("\n" + "=" * 80)

