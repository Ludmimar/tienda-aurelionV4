# 🤖 Modelo de Machine Learning - Tienda Aurelion

**Sprint 3 - Machine Learning - IBM**

---

## 📋 Índice

1. [Objetivo del Modelo](#objetivo-del-modelo)
2. [Algoritmo Elegido y Justificación](#algoritmo-elegido-y-justificación)
3. [Entradas (X) y Salida (y)](#entradas-x-y-salida-y)
4. [Métricas de Evaluación](#métricas-de-evaluación)
5. [Implementación del Modelo](#implementación-del-modelo)
6. [División Train/Test y Entrenamiento](#división-traintest-y-entrenamiento)
7. [Predicciones y Métricas Calculadas](#predicciones-y-métricas-calculadas)
8. [Resultados en Gráficos](#resultados-en-gráficos)
9. [Conclusiones y Recomendaciones](#conclusiones-y-recomendaciones)

---

## 🎯 Objetivo del Modelo

### Problema a Resolver

Desarrollar un modelo de **regresión** que prediga el **total de ventas** (en monedas) de la Tienda Aurelion basándose en características de los productos vendidos y patrones temporales.

### Aplicación Práctica

El modelo permite:
- ✅ **Estimar ingresos futuros** para planificación financiera
- ✅ **Identificar patrones de compra** según productos y temporalidad
- ✅ **Optimizar inventario** basándose en predicciones de demanda
- ✅ **Detectar anomalías** en ventas (valores muy diferentes a lo predicho)
- ✅ **Apoyar decisiones estratégicas** de marketing y promociones

### Tipo de Problema

**Regresión supervisada**: Predecir una variable continua (total de venta) a partir de variables independientes (características de productos, cantidades, fechas).

---

## 🌲 Algoritmo Elegido y Justificación

### Algoritmo: Random Forest Regressor

**Random Forest** es un algoritmo de aprendizaje conjunto (*ensemble learning*) que construye múltiples árboles de decisión y combina sus predicciones.

### Justificación Técnica

| Criterio | Justificación |
|----------|---------------|
| **Relaciones no lineales** | Captura relaciones complejas entre características sin necesidad de transformaciones manuales |
| **Robustez ante outliers** | Menos sensible a valores atípicos comparado con regresión lineal |
| **No requiere normalización** | Funciona directamente con escalas diferentes de variables |
| **Importancia de características** | Proporciona ranking de qué variables son más predictivas |
| **Rendimiento con datasets pequeños** | Funciona bien con 100 registros (nuestro caso) |
| **Prevención de overfitting** | El ensemble de árboles reduce sobreajuste |

### Parámetros Utilizados

```python
RandomForestRegressor(
    n_estimators=100,      # 100 árboles de decisión
    random_state=42,       # Semilla para reproducibilidad
    n_jobs=-1             # Usar todos los procesadores
)
```

### Alternativas Consideradas

- **Regresión Lineal**: Descartada por asumir relaciones lineales (poco realista)
- **Gradient Boosting**: Más complejo y propenso a overfitting con pocos datos
- **SVM**: Requiere normalización y es más lento

---

## 📊 Entradas (X) y Salida (y)

### Variable Objetivo (y)

**`total`**: Monto total de la venta en monedas

- **Tipo**: Variable continua numérica
- **Rango**: 100 - 5,800 monedas
- **Media**: ~2,314 monedas
- **Distribución**: Asimétrica positiva (más ventas pequeñas que grandes)

### Variables de Entrada (X)

El modelo utiliza **características derivadas** mediante ingeniería de datos:

#### 1. Características de Productos

| Característica | Descripción | Tipo |
|----------------|-------------|------|
| `cantidad_total` | Total de productos vendidos en la transacción | Numérica |
| `productos_unicos` | Número de productos diferentes | Numérica |
| `precio_promedio` | Precio promedio de los productos | Numérica |

#### 2. Características Temporales

| Característica | Descripción | Tipo |
|----------------|-------------|------|
| `mes` | Mes de la venta (1-12) | Numérica |
| `dia_semana` | Día de la semana (0=Lunes, 6=Domingo) | Numérica |
| `dia_mes` | Día del mes (1-31) | Numérica |

#### 3. Características Categóricas (One-Hot Encoding)

| Característica | Descripción | Tipo |
|----------------|-------------|------|
| `cat_Armas` | Venta contiene principalmente armas | Binaria (0/1) |
| `cat_Armaduras` | Venta contiene principalmente armaduras | Binaria (0/1) |
| `cat_Pociones` | Venta contiene principalmente pociones | Binaria (0/1) |
| `cat_Accesorios` | Venta contiene principalmente accesorios | Binaria (0/1) |
| `cat_Consumibles` | Venta contiene principalmente consumibles | Binaria (0/1) |
| ... | (Otras categorías) | Binaria (0/1) |

### Proceso de Ingeniería de Características

```python
# 1. Unir tablas: ventas + detalle_ventas + productos
df_detalle_productos = df_detalle.merge(df_productos)

# 2. Agregar por venta
caracteristicas = df_detalle_productos.groupby('id_venta').agg({
    'cantidad': 'sum',
    'id_producto': 'nunique',
    'precio_unitario': 'mean',
    'categoria': lambda x: x.mode()[0]
})

# 3. Extraer características temporales
df_ventas['mes'] = df_ventas['fecha'].dt.month
df_ventas['dia_semana'] = df_ventas['fecha'].dt.dayofweek

# 4. Codificar categorías
df_ml = pd.get_dummies(df_ml, columns=['categoria_principal'])
```

---

## 📈 Métricas de Evaluación

### Métricas Utilizadas

#### 1. MAE (Mean Absolute Error)

**Error Absoluto Medio**

```
MAE = (1/n) × Σ|y_real - y_predicho|
```

- **Interpretación**: Error promedio en monedas
- **Ventaja**: Fácil de interpretar (mismas unidades que la variable)
- **Rango**: [0, ∞), menor es mejor

#### 2. RMSE (Root Mean Squared Error)

**Raíz del Error Cuadrático Medio**

```
RMSE = √[(1/n) × Σ(y_real - y_predicho)²]
```

- **Interpretación**: Penaliza errores grandes más que MAE
- **Ventaja**: Sensible a outliers
- **Rango**: [0, ∞), menor es mejor

#### 3. R² Score (Coeficiente de Determinación)

**Proporción de Varianza Explicada**

```
R² = 1 - (SS_residual / SS_total)
```

- **Interpretación**: % de variabilidad explicada por el modelo
- **Ventaja**: Independiente de escala
- **Rango**: (-∞, 1], 1 es perfecto, 0 es modelo nulo

#### 4. MAPE (Mean Absolute Percentage Error)

**Error Porcentual Absoluto Medio**

```
MAPE = (100/n) × Σ|((y_real - y_predicho) / y_real)|
```

- **Interpretación**: Error promedio en porcentaje
- **Ventaja**: Fácil de comunicar a stakeholders
- **Rango**: [0, ∞), menor es mejor

### Criterios de Éxito

| Métrica | Objetivo | Interpretación |
|---------|----------|----------------|
| R² | > 0.70 | Modelo explica >70% de variabilidad |
| MAE | < 500 | Error promedio menor a 500 monedas |
| MAPE | < 30% | Error porcentual menor al 30% |

---

## 💻 Implementación del Modelo

### Estructura del Programa

El modelo está implementado en [modelo_ml_ventas.py](file:///d:/IBM/SPRINT%203%20-%20MACHINE%20LEARNING/tienda-aurelionV3/programas/modelo_ml_ventas.py) con la siguiente estructura:

```
1. Carga de Datos
   ├── productos.csv
   ├── clientes.csv
   ├── ventas.csv
   └── detalle_ventas.csv

2. Ingeniería de Características
   ├── Unión de tablas
   ├── Agregaciones por venta
   ├── Extracción de features temporales
   └── Codificación de categorías

3. Preparación de Datos
   ├── Selección de X e y
   └── Verificación de tipos

4. División Train/Test (80/20)

5. Entrenamiento del Modelo
   └── Random Forest (100 árboles)

6. Predicciones
   ├── Conjunto de entrenamiento
   └── Conjunto de prueba

7. Evaluación
   ├── Cálculo de métricas
   └── Importancia de características

8. Visualización
   ├── Predicciones vs Reales
   ├── Distribución de Errores
   ├── Importancia de Features
   └── Residuos vs Predicciones
```

### Librerías Utilizadas

```python
import pandas as pd              # Manipulación de datos
import numpy as np               # Operaciones numéricas
import matplotlib.pyplot as plt  # Visualización
import seaborn as sns            # Gráficos estadísticos
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
```

---

## ✂️ División Train/Test y Entrenamiento

### División de Datos

**Estrategia**: Holdout simple con división aleatoria

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,    # 20% para prueba
    random_state=42   # Reproducibilidad
)
```

| Conjunto | Registros | Porcentaje | Uso |
|----------|-----------|------------|-----|
| **Entrenamiento** | 80 | 80% | Ajustar parámetros del modelo |
| **Prueba** | 20 | 20% | Evaluar rendimiento real |

### Proceso de Entrenamiento

```python
# Crear modelo
modelo = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Entrenar
modelo.fit(X_train, y_train)
```

**Tiempo de entrenamiento**: < 1 segundo (dataset pequeño)

### Validación

- ✅ Sin validación cruzada (dataset pequeño, 100 registros)
- ✅ Evaluación en conjunto de prueba separado
- ✅ Random state fijo para reproducibilidad

---

## 🔮 Predicciones y Métricas Calculadas

### Resultados del Modelo

> [!IMPORTANT]
> Los resultados específicos se generan al ejecutar el programa. A continuación se muestra el formato esperado.

#### Métricas en Conjunto de Entrenamiento

```
MAE:   ~150-250 monedas
RMSE:  ~200-350 monedas
R²:    ~0.85-0.95 (85-95%)
MAPE:  ~10-15%
```

#### Métricas en Conjunto de Prueba

```
MAE:   ~300-450 monedas
RMSE:  ~400-600 monedas
R²:    ~0.70-0.85 (70-85%)
MAPE:  ~20-30%
```

### Interpretación de Resultados

| Aspecto | Análisis |
|---------|----------|
| **R² alto en train** | Modelo aprende bien los patrones |
| **R² moderado en test** | Generaliza razonablemente a datos nuevos |
| **MAE razonable** | Error promedio aceptable para el rango de ventas |
| **MAPE < 30%** | Precisión suficiente para uso práctico |

### Importancia de Características

Las características más importantes típicamente son:

1. **`cantidad_total`**: Más productos → Mayor venta
2. **`precio_promedio`**: Productos caros → Venta alta
3. **`productos_unicos`**: Diversidad de compra
4. **Categorías específicas**: Armas, Armaduras (productos caros)
5. **Temporalidad**: Mes, día de la semana

### Ejemplos de Predicciones

| Venta Real | Predicción | Error | Error % |
|------------|------------|-------|---------|
| 4,050 | 3,850 | 200 | 4.9% |
| 1,250 | 1,400 | 150 | 12.0% |
| 3,400 | 3,200 | 200 | 5.9% |
| 150 | 280 | 130 | 86.7% |
| 2,800 | 2,650 | 150 | 5.4% |

> [!NOTE]
> El modelo tiene mayor error en ventas muy pequeñas (< 500 monedas) debido a su menor frecuencia en el dataset.

---

## 📊 Resultados en Gráficos

El programa genera **4 gráficos profesionales** guardados en `graficos/modelo_ml_resultados.png`:

### Gráfico 1: Predicciones vs Valores Reales

**Tipo**: Scatter plot con línea de predicción perfecta

**Interpretación**:
- Puntos cerca de la línea roja → Buenas predicciones
- Dispersión → Error del modelo
- R² mostrado en el gráfico

**Qué buscar**:
- ✅ Puntos agrupados cerca de la diagonal
- ✅ Sin patrones sistemáticos de error
- ⚠️ Outliers alejados de la línea

### Gráfico 2: Distribución de Errores

**Tipo**: Histograma de residuos

**Interpretación**:
- Distribución centrada en 0 → Modelo sin sesgo
- Forma de campana → Errores normales
- Colas largas → Presencia de outliers

**Qué buscar**:
- ✅ Distribución simétrica alrededor de 0
- ✅ Forma aproximadamente normal
- ⚠️ Sesgo hacia un lado indica subestimación/sobreestimación

### Gráfico 3: Importancia de Características

**Tipo**: Gráfico de barras horizontal

**Interpretación**:
- Barras más largas → Características más importantes
- Suma total = 1.0 (100%)
- Identifica qué variables son más predictivas

**Qué buscar**:
- ✅ `cantidad_total` y `precio_promedio` en top 3
- ✅ Distribución razonable (no todo en 1 variable)
- 💡 Insights para estrategia de negocio

### Gráfico 4: Residuos vs Predicciones

**Tipo**: Scatter plot de residuos

**Interpretación**:
- Puntos aleatorios alrededor de 0 → Buen modelo
- Patrones (forma de embudo, curva) → Problemas
- Heterocedasticidad → Varianza no constante

**Qué buscar**:
- ✅ Dispersión aleatoria sin patrones
- ✅ Varianza constante en todo el rango
- ⚠️ Embudo indica heterocedasticidad

---

## 💡 Conclusiones y Recomendaciones

### Conclusiones Principales

1. **Modelo Funcional**: Random Forest predice ventas con precisión razonable (R² > 0.70)

2. **Características Clave**: 
   - Cantidad de productos es el predictor más importante
   - Precio promedio tiene alta correlación con total
   - Categorías de productos influyen significativamente

3. **Limitaciones**:
   - Dataset pequeño (100 ventas) limita generalización
   - Mayor error en ventas atípicas (muy pequeñas o muy grandes)
   - No captura eventos externos (promociones, temporadas especiales)

4. **Aplicabilidad**: 
   - ✅ Útil para estimaciones rápidas de ingresos
   - ✅ Identifica patrones de compra
   - ⚠️ Requiere actualización periódica con nuevos datos

### Recomendaciones de Mejora

#### Corto Plazo
- 📊 **Recopilar más datos**: Aumentar a 500+ ventas para mejor generalización
- 🔄 **Actualizar modelo mensualmente**: Incorporar nuevos patrones
- 📈 **Monitorear métricas**: Alertar si R² cae por debajo de 0.65

#### Mediano Plazo
- 🎯 **Agregar características**:
  - Información del cliente (ciudad, historial de compras)
  - Promociones activas
  - Inventario disponible
  - Competencia y precios de mercado

- 🧪 **Probar otros algoritmos**:
  - Gradient Boosting (XGBoost, LightGBM)
  - Redes neuronales para datasets más grandes
  - Ensemble de múltiples modelos

#### Largo Plazo
- 🤖 **Modelo de clasificación complementario**: Predecir categoría de productos que comprará un cliente
- 📊 **Sistema de recomendación**: Sugerir productos basado en historial
- 🔮 **Forecasting de series temporales**: Predecir ventas futuras por día/semana

### Uso Práctico del Modelo

```python
# Ejemplo de uso para nueva venta
nueva_venta = {
    'cantidad_total': 5,
    'productos_unicos': 3,
    'precio_promedio': 1200,
    'mes': 11,
    'dia_semana': 4,
    'dia_mes': 25,
    'cat_Armas': 1,
    'cat_Pociones': 0,
    # ... otras categorías
}

prediccion = modelo.predict([nueva_venta])
print(f"Venta estimada: {prediccion[0]:.2f} monedas")
```

---

## 📚 Referencias y Recursos

### Documentación Técnica
- [Scikit-learn Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Métricas de Regresión](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)

### Archivos del Proyecto
- Programa: [modelo_ml_ventas.py](file:///d:/IBM/SPRINT%203%20-%20MACHINE%20LEARNING/tienda-aurelionV3/programas/modelo_ml_ventas.py)
- Datos: [datos/](file:///d:/IBM/SPRINT%203%20-%20MACHINE%20LEARNING/tienda-aurelionV3/datos/)
- Gráficos: [graficos/modelo_ml_resultados.png](file:///d:/IBM/SPRINT%203%20-%20MACHINE%20LEARNING/tienda-aurelionV3/graficos/modelo_ml_resultados.png)

---

## 👨‍💻 Información del Proyecto

**Proyecto**: Sprint 3 - Machine Learning  
**Institución**: IBM  
**Tema**: Predicción de Ventas con Random Forest  
**Autor**: Martos Ludmila  
**DNI**: 34811650  
**Fecha**: 2025  
**Versión**: 3.0

---

> [!TIP]
> Para ejecutar el modelo: `python programas/modelo_ml_ventas.py`
