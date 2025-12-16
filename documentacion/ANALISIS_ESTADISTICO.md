# 📊 ANÁLISIS ESTADÍSTICO - TIENDA AURELION

**Sprint 3 - Machine Learning - IBM**

> **Autor:** Martos Ludmila  
> **DNI:** 34811650  
> **Fecha:** 2025

---

## 📋 Índice

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Estadísticas Descriptivas Básicas](#estadisticas-descriptivas)
3. [Identificación del Tipo de Distribución de Variables](#distribuciones)
4. [Análisis de Correlaciones](#correlaciones)
5. [Detección de Outliers](#outliers)
6. [Gráficos Representativos](#graficos)
7. [Interpretación de Resultados Orientada al Problema](#interpretacion)

---

## 1. Resumen Ejecutivo {#resumen-ejecutivo}

Este documento presenta un análisis estadístico completo de la base de datos de la Tienda Aurelion, enfocado en entender las relaciones entre productos, ventas y comportamiento del mercado. El análisis incluye:

- **80 productos** distribuidos en 10 categorías
- **50 clientes** registrados
- **100 ventas** realizadas desde mayo hasta agosto 2024
- **273 detalles de ventas** con información completa

### Objetivos del Análisis

1. Comprender la distribución de precios y stock de productos
2. Identificar relaciones entre variables clave (precio, stock, ventas)
3. Detectar valores anómalos que puedan afectar la toma de decisiones
4. Generar insights accionables para mejorar la gestión del inventario

---

## 2. Estadísticas Descriptivas Básicas {#estadisticas-descriptivas}

### 2.1 Variables de Productos

#### Precio de Productos

| Estadística | Valor |
|-------------|-------|
| **Media** | 1,090 monedas |
| **Mediana** | 900 monedas |
| **Desviación Estándar** | 1,247.67 monedas |
| **Mínimo** | 25 monedas |
| **Máximo** | 5,000 monedas |
| **Rango** | 4,975 monedas |
| **Coeficiente de Variación** | 114.5% |

**Interpretación:** Los precios muestran una alta variabilidad (CV > 100%), indicando una amplia gama de productos desde económicos hasta premium. La mediana (900) es menor que la media (1,090), sugiriendo algunos productos muy caros que elevan el promedio.

#### Stock de Productos

| Estadística | Valor |
|-------------|-------|
| **Media** | 57.3 unidades |
| **Mediana** | 35 unidades |
| **Desviación Estándar** | 107.95 unidades |
| **Mínimo** | 3 unidades |
| **Máximo** | 500 unidades |
| **Rango** | 497 unidades |
| **Coeficiente de Variación** | 188.4% |

**Interpretación:** El stock presenta una variabilidad extremadamente alta, principalmente debido a productos de consumo masivo (como Flechas Mágicas con 500 unidades) versus productos únicos o raros (como Gema de Resurrección con solo 3 unidades).

### 2.2 Variables de Ventas

#### Total de Ventas

| Estadística | Valor |
|-------------|-------|
| **Media** | 2,315 monedas |
| **Mediana** | 1,950 monedas |
| **Desviación Estándar** | 1,434.07 monedas |
| **Mínimo** | 100 monedas |
| **Máximo** | 5,800 monedas |
| **Ingresos Totales** | 231,485 monedas |

**Interpretación:** Las ventas muestran una distribución asimétrica positiva, con ventas grandes que representan casos excepcionales. El rango de ventas va desde pequeñas compras de pociones hasta grandes adquisiciones de equipamiento premium.

#### Cantidad Vendida por Producto

| Estadística | Valor |
|-------------|-------|
| **Media** | 2.48 unidades |
| **Mediana** | 1 unidad |
| **Máximo** | 15 unidades (Poción de Vida) |

---

## 3. Identificación del Tipo de Distribución de Variables {#distribuciones}

### 3.1 Distribución de Precios

**Tipo de Distribución:** **Asimétrica Positiva** (sesgada a la derecha)

- **Asimetría (Skewness):** 2.87
- **Curtosis:** 9.45 (distribución leptocúrtica - picos más altos que la normal)
- **Test de Normalidad:** No sigue distribución normal (p < 0.05)

**Análisis:**
- La distribución está sesgada hacia la derecha, indicando que hay más productos económicos que productos premium
- La alta curtosis sugiere que la mayoría de productos se concentran en un rango de precios medio, con algunos outliers muy caros

**Implicaciones para el negocio:**
- La estrategia de precios está bien diferenciada (productos básicos y premium)
- Los productos premium (como Gema de Resurrección a 5,000 monedas) son escasos pero de alto valor

### 3.2 Distribución de Stock

**Tipo de Distribución:** **Altamente Asimétrica Positiva**

- **Asimetría (Skewness):** 3.89
- **Curtosis:** 16.28 (distribución muy leptocúrtica)

**Análisis:**
- Distribución extremadamente sesgada debido a productos de consumo masivo
- La mayoría de productos tienen stock bajo (entre 3-60 unidades)
- Solo algunos productos tienen stock muy alto (Flechas Mágicas con 500 unidades)

**Implicaciones:**
- Necesidad de estrategias diferenciadas de gestión de inventario
- Productos de consumo masivo requieren mayor rotación
- Productos únicos requieren control más estricto

### 3.3 Distribución de Totales de Ventas

**Tipo de Distribución:** **Asimétrica Positiva**

- **Asimetría (Skewness):** 1.24
- **Curtosis:** 2.15

**Análisis:**
- Distribución moderadamente sesgada
- La mayoría de ventas están en el rango medio (500-3,000 monedas)
- Existen algunas ventas excepcionales muy altas

---

## 4. Análisis de Correlaciones entre Variables Principales {#correlaciones}

### 4.1 Correlación Precio vs Stock

**Correlación de Pearson:** -0.098 (correlación débil negativa)

**Interpretación:**
- No existe una relación significativa entre el precio de un producto y su nivel de stock
- Esto sugiere que el stock se gestiona independientemente del precio, lo cual es apropiado para diferentes tipos de productos

**Recomendación:**
- Los productos premium (altos precios) pueden tener bajo stock por ser artículos especiales
- Los productos económicos pueden tener alto stock por ser de consumo frecuente

### 4.2 Correlación Precio vs Cantidad Vendida

**Correlación de Pearson:** -0.352 (correlación moderada negativa)

**Interpretación:**
- Existe una correlación moderada negativa: **productos más caros tienden a venderse menos**
- Esto es consistente con la teoría económica: productos premium tienen menor demanda

**Implicaciones estratégicas:**
- ✅ Confirmación de estrategia de precios: productos premium son de nicho
- ⚠️ Considerar estrategias de marketing para productos premium
- 💡 Los productos económicos son los más vendidos (Poción de Vida lidera)

### 4.3 Correlación Cantidad vs Precio Unitario vs Subtotal

**Matriz de Correlación:**

| Variable | Cantidad | Precio Unitario | Subtotal |
|----------|----------|----------------|----------|
| **Cantidad** | 1.000 | 0.145 | 0.632 |
| **Precio Unitario** | 0.145 | 1.000 | 0.956 |
| **Subtotal** | 0.632 | 0.956 | 1.000 |

**Hallazgos clave:**
- **Precio Unitario ↔ Subtotal:** Correlación muy fuerte (0.956) - esperado, ya que el subtotal depende del precio
- **Cantidad ↔ Subtotal:** Correlación moderada (0.632) - las ventas grandes aumentan el subtotal
- **Cantidad ↔ Precio Unitario:** Correlación débil (0.145) - los clientes compran diferentes cantidades independientemente del precio

---

## 5. Detección de Outliers (Valores Extremos) {#outliers}

### 5.1 Outliers en Precios de Productos

**Método:** Rango Intercuartílico (IQR)

**Valores Outliers Detectados:**
- **Gema de Resurrección:** 5,000 monedas (muy por encima del límite superior)
- **Armadura de Dragón:** 3,000 monedas (límite superior)

**Análisis:**
- Estos productos son intencionalmente premium y representan artículos de alto valor
- No son errores de datos, sino productos estratégicamente posicionados

**Acción recomendada:**
- ✅ Mantener estos productos como artículos exclusivos
- 📊 Monitorear su rotación para asegurar que son rentables
- 💡 Considerar estrategias de marketing para estos productos premium

### 5.2 Outliers en Stock

**Valores Outliers Detectados:**
- **Flechas Mágicas:** 500 unidades (muy por encima del límite superior)
- **Poción de Vida:** 200 unidades
- **Poción de Maná:** 150 unidades

**Análisis:**
- Estos son productos de consumo masivo con alta rotación esperada
- El stock alto es apropiado para productos básicos de alta demanda

**Acción recomendada:**
- ✅ Mantener niveles altos de stock para productos de consumo frecuente
- 📊 Monitorear rotación para optimizar puntos de reorden

### 5.3 Outliers en Totales de Ventas

**Valores Outliers Detectados:**
- **Venta #7:** 5,000 monedas (compra de Gema de Resurrección)
- **Venta #1:** 4,500 monedas (múltiples productos premium)

**Análisis:**
- Estas ventas representan transacciones importantes de clientes premium
- Son casos legítimos que indican éxito en ventas de alto valor

**Acción recomendada:**
- ✅ Identificar y cultivar relaciones con clientes de alto valor
- 💡 Desarrollar estrategias para aumentar frecuencia de compras premium

---

## 6. Gráficos Representativos {#graficos}

### Gráfico 1: Distribución de Precios

**Tipo:** Histograma + Box Plot

**Insights:**
- La distribución muestra una cola larga hacia la derecha
- La mayoría de productos están en el rango 25-2,000 monedas
- Los productos premium (outliers) están claramente diferenciados

**Ubicación:** `graficos/grafico1_distribucion_precios.png`

### Gráfico 2: Matriz de Correlación

**Tipo:** Heatmap de Correlaciones

**Insights:**
- Visualización clara de relaciones entre variables
- Confirma la correlación fuerte entre precio unitario y subtotal
- Muestra la correlación negativa moderada entre precio y cantidad vendida

**Ubicación:** `graficos/grafico2_matriz_correlacion.png`

### Gráfico 3: Análisis de Outliers y Tendencias

**Tipo:** Multi-panel (Scatter Plot, Box Plot, Serie Temporal, Barras)

**Insights:**
- Scatter plot muestra outliers de precio claramente marcados
- Serie temporal muestra fluctuaciones en ventas diarias
- Gráfico de barras identifica productos más vendidos

**Ubicación:** `graficos/grafico3_outliers_ventas.png`

---

## 7. Interpretación de Resultados Orientada al Problema {#interpretacion}

### 7.1 Problema Original

La Tienda Aurelion enfrentaba:
- ❌ Gestión manual ineficiente
- ❌ Falta de visibilidad en inventario
- ❌ Control de stock deficiente
- ❌ Sin análisis de datos

### 7.2 Insights Clave del Análisis Estadístico

#### 7.2.1 Gestión de Inventario

**Hallazgo:** El stock muestra una distribución altamente asimétrica con productos de consumo masivo (500 unidades) versus productos únicos (3 unidades).

**Recomendación:**
- ✅ Implementar gestión diferenciada por categoría de producto
- ✅ Para productos de consumo masivo (Flechas, Pociones): mantener stock alto y reorden automático
- ✅ Para productos premium (Gemas, Grimorios): control estricto y rotación más lenta es aceptable

#### 7.2.2 Estrategia de Precios

**Hallazgo:** Correlación negativa moderada (-0.352) entre precio y cantidad vendida confirma que productos más caros se venden menos.

**Recomendación:**
- ✅ Estrategia de precios diferenciada es apropiada
- 💡 Considerar estrategias de marketing para productos premium:
  - Marketing dirigido a clientes de alto valor
  - Paquetes promocionales que combinen productos premium y básicos
  - Programas de fidelización para clientes frecuentes

#### 7.2.3 Identificación de Clientes de Alto Valor

**Hallazgo:** Ventas outliers (5,000 monedas) representan clientes premium que compran productos exclusivos.

**Recomendación:**
- ✅ Identificar y segmentar clientes por valor de compra
- ✅ Desarrollar estrategias de retención para clientes premium
- ✅ Crear programas especiales para clientes de alto valor

#### 7.2.4 Optimización de Stock

**Hallazgo:** 
- Productos con stock bajo (≤20 unidades) representan riesgo de desabastecimiento
- Productos con stock extremadamente alto pueden generar costos de almacenamiento

**Recomendación:**
- ✅ Implementar sistema de alertas automáticas para stock bajo
- ✅ Revisar políticas de reorden basadas en historial de ventas
- ✅ Considerar análisis ABC para clasificar productos por importancia

### 7.3 Métricas Clave para Monitoreo Continuo

1. **Rotación de Inventario:** Monitorear frecuencia de ventas por producto
2. **Margen de Contribución:** Analizar rentabilidad por categoría
3. **Tasa de Conversión de Stock:** Medir eficiencia en ventas vs stock disponible
4. **Valor Promedio de Transacción:** Trackear evolución de ventas promedio

### 7.4 Acciones Inmediatas Recomendadas

1. **Corto Plazo (1-2 semanas):**
   - Reabastecer productos con stock crítico (≤10 unidades)
   - Implementar alertas automáticas para stock bajo
   - Analizar productos más vendidos para optimizar stock

2. **Mediano Plazo (1-3 meses):**
   - Desarrollar estrategia de marketing para productos premium
   - Implementar programa de fidelización de clientes
   - Optimizar niveles de stock basados en análisis de correlaciones

3. **Largo Plazo (3-6 meses):**
   - Implementar sistema de análisis predictivo de demanda
   - Desarrollar estrategias de pricing dinámico
   - Expansión de categorías basada en análisis de correlaciones

---

## 📚 Conclusión

El análisis estadístico revela patrones importantes en la gestión de la Tienda Aurelion:

1. **Gestión diferenciada es necesaria:** Los productos muestran características muy distintas que requieren estrategias específicas
2. **Estrategia de precios es efectiva:** La correlación negativa entre precio y cantidad es esperada y positiva para el negocio
3. **Oportunidades de optimización:** Identificación de productos críticos y clientes de alto valor permite acciones estratégicas
4. **Base de datos limpia:** Los datos están preparados para análisis más avanzados y machine learning

Este análisis proporciona una base sólida para la toma de decisiones basada en datos y la optimización continua del negocio.

---

**Para ejecutar el análisis completo:**

```bash
python programas/analisis_estadistico.py
```

Los gráficos se generarán automáticamente en la carpeta `graficos/`.

---

**Autor:** Martos Ludmila  
**DNI:** 34811650  
**Sprint:** 2 - Introducción a la Inteligencia Artificial  
**Institución:** IBM  
**Año:** 2025

