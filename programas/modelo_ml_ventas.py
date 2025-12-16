"""
🤖 MODELO DE MACHINE LEARNING - TIENDA AURELION
Sprint 3 - Machine Learning - IBM

Modelo de Regresión para Predecir Total de Ventas
Algoritmo: Random Forest Regressor

Autor: Martos Ludmila
Fecha: 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os
from datetime import datetime

# Configuración de estilo para gráficos
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ============================================================================
# 1. CARGA DE DATOS
# ============================================================================

print("=" * 80)
print("🤖 MODELO DE MACHINE LEARNING - PREDICCIÓN DE VENTAS")
print("=" * 80)
print("\n📂 Paso 1: Cargando datos desde archivos CSV...\n")

# Rutas de los archivos
ruta_base = os.path.join(os.path.dirname(__file__), '..', 'datos')
ruta_productos = os.path.join(ruta_base, 'productos.csv')
ruta_clientes = os.path.join(ruta_base, 'clientes.csv')
ruta_ventas = os.path.join(ruta_base, 'ventas.csv')
ruta_detalle = os.path.join(ruta_base, 'detalle_ventas.csv')

# Cargar datos
df_productos = pd.read_csv(ruta_productos)
df_clientes = pd.read_csv(ruta_clientes)
df_ventas = pd.read_csv(ruta_ventas)
df_detalle = pd.read_csv(ruta_detalle)

print(f"✅ Productos cargados: {len(df_productos)} registros")
print(f"✅ Clientes cargados: {len(df_clientes)} registros")
print(f"✅ Ventas cargadas: {len(df_ventas)} registros")
print(f"✅ Detalles de ventas cargados: {len(df_detalle)} registros")

# ============================================================================
# 2. INGENIERÍA DE CARACTERÍSTICAS
# ============================================================================

print("\n" + "=" * 80)
print("🔧 Paso 2: Ingeniería de Características")
print("=" * 80)

# Convertir fecha a datetime
df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'])

# Extraer características temporales
df_ventas['mes'] = df_ventas['fecha'].dt.month
df_ventas['dia_semana'] = df_ventas['fecha'].dt.dayofweek
df_ventas['dia_mes'] = df_ventas['fecha'].dt.day

# Unir detalle de ventas con productos para obtener categorías
df_detalle_productos = df_detalle.merge(df_productos[['id', 'categoria', 'precio']], 
                                         left_on='id_producto', 
                                         right_on='id')

# Calcular características agregadas por venta
caracteristicas_ventas = df_detalle_productos.groupby('id_venta').agg({
    'cantidad': 'sum',                    # Total de productos vendidos
    'id_producto': 'nunique',             # Número de productos únicos
    'precio_unitario': 'mean',            # Precio promedio
    'subtotal': 'sum',                    # Total de la venta (para verificar)
    'categoria': lambda x: x.mode()[0] if len(x.mode()) > 0 else x.iloc[0]  # Categoría más frecuente
}).reset_index()

caracteristicas_ventas.columns = ['id_venta', 'cantidad_total', 'productos_unicos', 
                                    'precio_promedio', 'subtotal_calculado', 'categoria_principal']

# Unir con datos de ventas
df_ml = df_ventas.merge(caracteristicas_ventas, on='id_venta')

# Codificar categoría principal (One-Hot Encoding)
df_ml = pd.get_dummies(df_ml, columns=['categoria_principal'], prefix='cat')

print(f"\n✅ Dataset ML creado con {len(df_ml)} registros")
print(f"✅ Características creadas: {df_ml.shape[1]} columnas")
print("\n📊 Características principales:")
print("   - cantidad_total: Total de productos en la venta")
print("   - productos_unicos: Número de productos diferentes")
print("   - precio_promedio: Precio promedio de productos")
print("   - mes: Mes de la venta (1-12)")
print("   - dia_semana: Día de la semana (0=Lunes, 6=Domingo)")
print("   - dia_mes: Día del mes (1-31)")
print("   - cat_*: Categoría principal de productos (codificada)")

# ============================================================================
# 3. PREPARACIÓN DE DATOS PARA EL MODELO
# ============================================================================

print("\n" + "=" * 80)
print("📊 Paso 3: Preparación de Datos")
print("=" * 80)

# Seleccionar características (X) y variable objetivo (y)
columnas_excluir = ['id_venta', 'id_cliente', 'fecha', 'total', 'subtotal_calculado']
X = df_ml.drop(columns=columnas_excluir)
y = df_ml['total']

print(f"\n✅ Variables de entrada (X): {X.shape[1]} características")
print(f"✅ Variable objetivo (y): total de venta")
print(f"\n📋 Características utilizadas:")
for i, col in enumerate(X.columns, 1):
    print(f"   {i}. {col}")

# ============================================================================
# 4. DIVISIÓN TRAIN/TEST
# ============================================================================

print("\n" + "=" * 80)
print("✂️ Paso 4: División Train/Test")
print("=" * 80)

# Dividir datos: 80% entrenamiento, 20% prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\n✅ Conjunto de entrenamiento: {len(X_train)} registros ({len(X_train)/len(X)*100:.1f}%)")
print(f"✅ Conjunto de prueba: {len(X_test)} registros ({len(X_test)/len(X)*100:.1f}%)")
print(f"\n📊 Estadísticas de la variable objetivo (total):")
print(f"   - Media: {y.mean():.2f} monedas")
print(f"   - Mediana: {y.median():.2f} monedas")
print(f"   - Mínimo: {y.min():.2f} monedas")
print(f"   - Máximo: {y.max():.2f} monedas")
print(f"   - Desviación estándar: {y.std():.2f} monedas")

# ============================================================================
# 5. ENTRENAMIENTO DEL MODELO
# ============================================================================

print("\n" + "=" * 80)
print("🎓 Paso 5: Entrenamiento del Modelo")
print("=" * 80)

print("\n🌲 Algoritmo: Random Forest Regressor")
print("   - Número de árboles: 100")
print("   - Profundidad máxima: None (sin límite)")
print("   - Random state: 42 (reproducibilidad)")

# Crear y entrenar el modelo
modelo = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1  # Usar todos los procesadores disponibles
)

print("\n⏳ Entrenando modelo...")
modelo.fit(X_train, y_train)
print("✅ ¡Modelo entrenado exitosamente!")

# ============================================================================
# 6. PREDICCIONES
# ============================================================================

print("\n" + "=" * 80)
print("🔮 Paso 6: Generación de Predicciones")
print("=" * 80)

# Realizar predicciones
y_pred_train = modelo.predict(X_train)
y_pred_test = modelo.predict(X_test)

print(f"\n✅ Predicciones generadas para {len(y_pred_test)} ventas de prueba")
print("\n📊 Ejemplos de predicciones vs valores reales:")
print("-" * 60)
print(f"{'Real (monedas)':<20} {'Predicción (monedas)':<25} {'Error':<15}")
print("-" * 60)
for i in range(min(10, len(y_test))):
    real = y_test.iloc[i]
    pred = y_pred_test[i]
    error = abs(real - pred)
    print(f"{real:<20.2f} {pred:<25.2f} {error:<15.2f}")

# ============================================================================
# 7. MÉTRICAS DE EVALUACIÓN
# ============================================================================

print("\n" + "=" * 80)
print("📈 Paso 7: Evaluación del Modelo")
print("=" * 80)

# Calcular métricas para conjunto de entrenamiento
mae_train = mean_absolute_error(y_train, y_pred_train)
rmse_train = np.sqrt(mean_squared_error(y_train, y_pred_train))
r2_train = r2_score(y_train, y_pred_train)
mape_train = np.mean(np.abs((y_train - y_pred_train) / y_train)) * 100

# Calcular métricas para conjunto de prueba
mae_test = mean_absolute_error(y_test, y_pred_test)
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
r2_test = r2_score(y_test, y_pred_test)
mape_test = np.mean(np.abs((y_test - y_pred_test) / y_test)) * 100

print("\n📊 MÉTRICAS EN CONJUNTO DE ENTRENAMIENTO:")
print("-" * 60)
print(f"   MAE (Error Absoluto Medio):        {mae_train:.2f} monedas")
print(f"   RMSE (Raíz del Error Cuadrático): {rmse_train:.2f} monedas")
print(f"   R² Score (Coef. Determinación):    {r2_train:.4f} ({r2_train*100:.2f}%)")
print(f"   MAPE (Error Porcentual Medio):     {mape_train:.2f}%")

print("\n📊 MÉTRICAS EN CONJUNTO DE PRUEBA:")
print("-" * 60)
print(f"   MAE (Error Absoluto Medio):        {mae_test:.2f} monedas")
print(f"   RMSE (Raíz del Error Cuadrático): {rmse_test:.2f} monedas")
print(f"   R² Score (Coef. Determinación):    {r2_test:.4f} ({r2_test*100:.2f}%)")
print(f"   MAPE (Error Porcentual Medio):     {mape_test:.2f}%")

print("\n💡 Interpretación de métricas:")
print(f"   - El modelo explica el {r2_test*100:.1f}% de la variabilidad en las ventas")
print(f"   - Error promedio de {mae_test:.0f} monedas por predicción")
print(f"   - Error porcentual promedio de {mape_test:.1f}%")

# Importancia de características
importancias = pd.DataFrame({
    'caracteristica': X.columns,
    'importancia': modelo.feature_importances_
}).sort_values('importancia', ascending=False)

print("\n🎯 TOP 5 CARACTERÍSTICAS MÁS IMPORTANTES:")
print("-" * 60)
for i, row in importancias.head(5).iterrows():
    print(f"   {row['caracteristica']:<30} {row['importancia']:.4f} ({row['importancia']*100:.2f}%)")

# ============================================================================
# 8. GENERACIÓN DE GRÁFICOS
# ============================================================================

print("\n" + "=" * 80)
print("📊 Paso 8: Generación de Gráficos")
print("=" * 80)

# Crear carpeta de gráficos si no existe
ruta_graficos = os.path.join(os.path.dirname(__file__), '..', 'graficos')
os.makedirs(ruta_graficos, exist_ok=True)

# Configurar figura con 4 subplots
fig = plt.figure(figsize=(16, 12))

# ---- GRÁFICO 1: Predicciones vs Valores Reales ----
ax1 = plt.subplot(2, 2, 1)
plt.scatter(y_test, y_pred_test, alpha=0.6, s=100, edgecolors='black', linewidth=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 
         'r--', lw=2, label='Predicción Perfecta')
plt.xlabel('Valor Real (monedas)', fontsize=12, fontweight='bold')
plt.ylabel('Predicción (monedas)', fontsize=12, fontweight='bold')
plt.title('Predicciones vs Valores Reales\n(Conjunto de Prueba)', 
          fontsize=14, fontweight='bold', pad=15)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# Añadir R² al gráfico
plt.text(0.05, 0.95, f'R² = {r2_test:.4f}', 
         transform=ax1.transAxes, fontsize=12, 
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# ---- GRÁFICO 2: Distribución de Errores ----
ax2 = plt.subplot(2, 2, 2)
errores = y_test - y_pred_test
plt.hist(errores, bins=20, edgecolor='black', alpha=0.7, color='skyblue')
plt.axvline(x=0, color='red', linestyle='--', linewidth=2, label='Error = 0')
plt.xlabel('Error (Real - Predicción)', fontsize=12, fontweight='bold')
plt.ylabel('Frecuencia', fontsize=12, fontweight='bold')
plt.title('Distribución de Errores de Predicción\n(Conjunto de Prueba)', 
          fontsize=14, fontweight='bold', pad=15)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3, axis='y')

# Añadir estadísticas
plt.text(0.05, 0.95, f'Media: {errores.mean():.2f}\nDesv. Est.: {errores.std():.2f}', 
         transform=ax2.transAxes, fontsize=10, 
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# ---- GRÁFICO 3: Importancia de Características ----
ax3 = plt.subplot(2, 2, 3)
top_features = importancias.head(10)
colores = plt.cm.viridis(np.linspace(0, 1, len(top_features)))
plt.barh(range(len(top_features)), top_features['importancia'], color=colores, edgecolor='black')
plt.yticks(range(len(top_features)), top_features['caracteristica'])
plt.xlabel('Importancia', fontsize=12, fontweight='bold')
plt.ylabel('Característica', fontsize=12, fontweight='bold')
plt.title('Top 10 Características Más Importantes\n(Random Forest)', 
          fontsize=14, fontweight='bold', pad=15)
plt.grid(True, alpha=0.3, axis='x')
plt.gca().invert_yaxis()

# ---- GRÁFICO 4: Residuos vs Predicciones ----
ax4 = plt.subplot(2, 2, 4)
plt.scatter(y_pred_test, errores, alpha=0.6, s=100, edgecolors='black', linewidth=0.5)
plt.axhline(y=0, color='red', linestyle='--', linewidth=2, label='Error = 0')
plt.xlabel('Predicción (monedas)', fontsize=12, fontweight='bold')
plt.ylabel('Residuo (Real - Predicción)', fontsize=12, fontweight='bold')
plt.title('Residuos vs Predicciones\n(Conjunto de Prueba)', 
          fontsize=14, fontweight='bold', pad=15)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# Añadir MAE al gráfico
plt.text(0.05, 0.95, f'MAE = {mae_test:.2f}', 
         transform=ax4.transAxes, fontsize=12, 
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Ajustar espaciado
plt.tight_layout()

# Guardar gráfico
ruta_grafico = os.path.join(ruta_graficos, 'modelo_ml_resultados.png')
plt.savefig(ruta_grafico, dpi=300, bbox_inches='tight')
print(f"\n✅ Gráfico guardado: {ruta_grafico}")

# ============================================================================
# RESUMEN FINAL
# ============================================================================

print("\n" + "=" * 80)
print("✅ RESUMEN FINAL")
print("=" * 80)

print(f"""
📊 MODELO DE MACHINE LEARNING COMPLETADO

🎯 Objetivo: Predecir el total de ventas
🌲 Algoritmo: Random Forest Regressor
📈 Registros totales: {len(df_ml)}
✂️ Train/Test: {len(X_train)}/{len(X_test)} ({len(X_train)/len(X)*100:.0f}%/{len(X_test)/len(X)*100:.0f}%)

📊 MÉTRICAS DE RENDIMIENTO (Test):
   • R² Score: {r2_test:.4f} ({r2_test*100:.2f}%)
   • MAE: {mae_test:.2f} monedas
   • RMSE: {rmse_test:.2f} monedas
   • MAPE: {mape_test:.2f}%

🎯 CARACTERÍSTICAS MÁS IMPORTANTES:
   1. {importancias.iloc[0]['caracteristica']}: {importancias.iloc[0]['importancia']*100:.2f}%
   2. {importancias.iloc[1]['caracteristica']}: {importancias.iloc[1]['importancia']*100:.2f}%
   3. {importancias.iloc[2]['caracteristica']}: {importancias.iloc[2]['importancia']*100:.2f}%

📁 ARCHIVOS GENERADOS:
   • Gráficos: graficos/modelo_ml_resultados.png

""")

print("=" * 80)
print("🎉 ¡PROCESO COMPLETADO EXITOSAMENTE!")
print("=" * 80)

# Mostrar gráfico
plt.show()
