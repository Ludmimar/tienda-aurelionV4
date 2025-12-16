# 📊 Presentación: Cómo Leer y Entender tu Archivo Power BI
## Tienda Aurelion - Sprint4.pbix

---

## 🎯 Objetivo de esta Guía

Esta presentación te ayudará a:
- ✅ Entender la estructura de tu archivo Power BI
- ✅ Identificar qué contiene el dashboard
- ✅ Conocer las medidas DAX existentes
- ✅ Entender las visualizaciones actuales
- ✅ Saber cómo navegar y explorar el archivo

---

## 📋 ÍNDICE

1. [Información General del Archivo](#1-información-general-del-archivo)
2. [Modelo de Datos](#2-modelo-de-datos)
3. [Medidas DAX Existentes](#3-medidas-dax-existentes)
4. [Visualizaciones en el Dashboard](#4-visualizaciones-en-el-dashboard)
5. [Cómo Abrir y Navegar el Archivo](#5-cómo-abrir-y-navegar-el-archivo)
6. [Análisis Detallado de Componentes](#6-análisis-detallado-de-componentes)
7. [Checklist de Revisión](#7-checklist-de-revisión)

---

## 1. Información General del Archivo

### 📁 Detalles del Archivo
- **Nombre**: `Sprint4.pbix`
- **Tamaño**: ~103 KB
- **Versión Power BI**: 2025.11
- **Origen**: Cloud (creado desde la nube)
- **Última modificación**: 9 de diciembre de 2025

### 🎨 Tema Personalizado
- **Nombre**: "Tienda Aurelion - Medieval Theme"
- **Estilo**: Tema medieval con colores dorados, rojos oscuros y azules marinos
- **Paleta de colores**: Dorado (#D4AF37), Rojo oscuro (#8B0000), Azul marino (#000080)

---

## 2. Modelo de Datos

### 📊 Tablas Principales

Tu archivo contiene **4 tablas principales**:

#### 2.1 Tabla: Productos
**Ubicación en el modelo**: Derecha central
**Contiene información sobre**:
- ID de producto
- Nombre del producto
- Categoría
- Stock disponible
- Valor de inventario
- Proveedor

#### 2.2 Tabla: Clientes
**Ubicación en el modelo**: Centro inferior
**Contiene información sobre**:
- ID de cliente
- Datos de clientes

#### 2.3 Tabla: Ventas
**Ubicación en el modelo**: Izquierda superior
**Contiene información sobre**:
- ID de venta
- Fecha de venta
- Total de la venta
- Relación con clientes

#### 2.4 Tabla: Detalle_Ventas
**Ubicación en el modelo**: Centro superior
**Contiene información sobre**:
- Detalles específicos de cada venta
- Cantidad vendida
- Precio unitario
- Relación con productos y ventas

### 🔗 Relaciones entre Tablas

```
Ventas (1) ────────> (N) Detalle_Ventas
   │                       │
   │                       │
   │                       └──────> Productos (N)
   │
   └──────> Clientes (N)
```

**Tipo de relaciones**:
- **Ventas → Clientes**: Uno a muchos (1:N)
- **Ventas → Detalle_Ventas**: Uno a muchos (1:N)
- **Detalle_Ventas → Productos**: Muchos a uno (N:1)

---

## 3. Medidas DAX Existentes

### 📈 Medidas Identificadas en el Archivo

#### Tabla: Productos

1. **-- Total de Productos Vendidos**
   - **Tipo**: Agregación (SUM)
   - **Ubicación**: Visual Card (Tarjeta)
   - **Descripción**: Suma total de productos vendidos

2. **-- Valor Total Inventario**
   - **Tipo**: Agregación (SUM)
   - **Formato**: Moneda ($)
   - **Ubicación**: Visual Card (Tarjeta)
   - **Descripción**: Valor total del inventario

3. **-- Stock Total**
   - **Tipo**: Agregación (SUM)
   - **Formato**: Número entero
   - **Ubicación**: Visual Card (Tarjeta)
   - **Descripción**: Suma total de stock disponible

4. **-- Total de Ventas**
   - **Tipo**: Agregación
   - **Formato**: Número
   - **Ubicación**: Visual Card (Tarjeta)
   - **Descripción**: Total de ventas realizadas

5. **-- Rotación de Inventario**
   - **Tipo**: Medida calculada (DIVIDE)
   - **Formato**: Número decimal (0.00)
   - **Ubicación**: Visual Gauge (Medidor)
   - **Descripción**: Tasa de rotación de inventario

#### Tabla: Ventas

6. **-- Ingresos Totales**
   - **Tipo**: Agregación (SUM)
   - **Formato**: Moneda (€)
   - **Ubicación**: Visual Card (Tarjeta)
   - **Descripción**: Ingresos totales por ventas

### ⚠️ Nota sobre Medidas

Algunas medidas pueden estar usando nombres diferentes o pueden necesitar ajustes. Es importante verificar en Power BI Desktop qué medidas realmente existen.

---

## 4. Visualizaciones en el Dashboard

### 📄 Página: "Overview"

Tu dashboard tiene **1 página principal** llamada "Overview" con las siguientes visualizaciones:

#### 4.1 Tarjetas (Cards) - 5 visualizaciones

**Tarjeta 1: Total Productos**
- **Medida**: -- Total de Productos Vendidos
- **Ubicación**: Esquina superior derecha
- **Tamaño**: 248.57 x 210 píxeles
- **Formato**: Número entero

**Tarjeta 2: Valor Total Inventario**
- **Medida**: -- Valor Total Inventario
- **Ubicación**: Esquina superior izquierda
- **Tamaño**: 272.86 x 210 píxeles
- **Formato**: Moneda ($)

**Tarjeta 3: Stock Total**
- **Medida**: -- Stock Total
- **Ubicación**: Centro superior
- **Tamaño**: 221.43 x 210 píxeles
- **Formato**: Número entero

**Tarjeta 4: Total Ventas**
- **Medida**: -- Total de Ventas
- **Ubicación**: Centro-derecha superior
- **Tamaño**: 230 x 210 píxeles
- **Formato**: Número

**Tarjeta 5: Ingresos Totales**
- **Medida**: -- Ingresos Totales
- **Ubicación**: Centro superior
- **Tamaño**: 268.57 x 210 píxeles
- **Formato**: Moneda (€)

#### 4.2 Gráfico de Barras Agrupadas

**Gráfico: Productos por Categoría**
- **Tipo**: Clustered Bar Chart
- **Eje X (Categoría)**: Productos.categoria
- **Eje Y (Valor)**: CountNonNull(Productos.id)
- **Ubicación**: Parte inferior izquierda
- **Tamaño**: 368.33 x 225 píxeles
- **Descripción**: Muestra la cantidad de productos por categoría

#### 4.3 Gráfico de Columnas

**Gráfico: Top 10 Productos Más Valiosos**
- **Tipo**: Column Chart
- **Eje X (Categoría)**: Productos.nombre (Top 10)
- **Eje Y (Valor)**: Suma de valor_inventario
- **Ubicación**: Parte inferior izquierda-central
- **Tamaño**: 367.61 x 267.22 píxeles
- **Filtro**: Top 10 productos por valor de inventario
- **Descripción**: Muestra los 10 productos con mayor valor de inventario

#### 4.4 Gráfico de Anillo (Donut)

**Gráfico: Distribución de Stock por Categoría**
- **Tipo**: Donut Chart
- **Categoría**: Productos.categoria
- **Valor**: Recuento de stock
- **Ubicación**: Centro
- **Tamaño**: 383.33 x 263.33 píxeles
- **Descripción**: Muestra la distribución del stock por categoría de producto

#### 4.5 Tabla

**Tabla: Productos con Stock Bajo**
- **Tipo**: TableEx
- **Columnas**:
  - nombre
  - categoria
  - stock (con barras de datos en color dorado #D4AF37)
  - proveedor
- **Filtro**: Stock < 20
- **Ordenamiento**: Por categoría (ascendente)
- **Ubicación**: Parte derecha
- **Tamaño**: 528.75 x 491.25 píxeles
- **Descripción**: Lista productos con stock menor a 20 unidades

#### 4.6 Medidor (Gauge)

**Medidor: Rotación de Inventario**
- **Tipo**: Gauge
- **Medida**: -- Rotación de Inventario
- **Ubicación**: Parte inferior central
- **Tamaño**: 383.85 x 228.84 píxeles
- **Formato**: Número decimal (0.00)
- **Descripción**: Muestra visualmente la tasa de rotación de inventario

#### 4.7 Botón de Acción

**Botón: Retroceso**
- **Tipo**: Action Button (Back)
- **Ubicación**: Esquina superior izquierda
- **Tamaño**: 100 x 40 píxeles
- **Función**: Navegación hacia atrás entre páginas

---

## 5. Cómo Abrir y Navegar el Archivo

### Paso 1: Abrir Power BI Desktop

1. **Buscar Power BI Desktop**
   - En el menú de inicio de Windows
   - O desde el escritorio si tienes acceso directo

2. **Abrir el archivo**
   - Click en **Archivo** → **Abrir** → **Examinar**
   - Navega hasta: `D:\IBM\SPRINT 4 - POWER BI\Sprint4.pbix`
   - Click en **Abrir**

### Paso 2: Explorar las Vistas Principales

Power BI tiene 3 vistas principales (iconos en el panel izquierdo):

#### 🔍 Vista de Informes (Report View)
- **Ícono**: Página con gráfico
- **Ubicación**: Primer icono a la izquierda
- **Qué verás**: Las visualizaciones del dashboard
- **Uso**: Para ver y editar las visualizaciones

#### 📊 Vista de Datos (Data View)
- **Ícono**: Tabla
- **Ubicación**: Segundo icono
- **Qué verás**: Los datos de las tablas
- **Uso**: Para ver los datos sin procesar

#### 🗂️ Vista de Modelo (Model View)
- **Ícono**: Tres cuadrados conectados
- **Ubicación**: Tercer icono
- **Qué verás**: El modelo de datos con relaciones
- **Uso**: Para entender y modificar relaciones entre tablas

### Paso 3: Navegar por el Panel de Campos

**Panel de Campos** (lado derecho):
- Muestra todas las tablas
- Expande cada tabla para ver:
  - **Columnas** (📋 ícono de tabla)
  - **Medidas** (🧮 ícono de calculadora)

### Paso 4: Explorar las Medidas

1. **En el panel de campos**, expande una tabla (ej: Productos)
2. **Busca medidas** (ícono de calculadora 🧮)
3. **Click derecho en una medida** para:
   - Editar medida
   - Copiar
   - Eliminar
   - Ver dependencias

---

## 6. Análisis Detallado de Componentes

### 6.1 Análisis de las Medidas Existentes

#### Medida: -- Total de Productos Vendidos
```
Consulta esperada:
SUM(Detalle_Ventas[cantidad])
```
**Verificación**:
- ¿La medida existe?
- ¿Usa la columna correcta?
- ¿Muestra valores?

#### Medida: -- Valor Total Inventario
```
Consulta esperada:
SUM(Productos[valor_inventario])
o
SUMX(Productos, Productos[stock] * Productos[precio_unitario])
```
**Verificación**:
- ¿Existe la columna valor_inventario?
- ¿O necesita calcularse?

#### Medida: -- Rotación de Inventario
```
Consulta esperada:
DIVIDE(
    [-- Total de Productos Vendidos],
    [-- Stock Total],
    0
)
```
**Verificación**:
- ¿Depende de otras medidas?
- ¿Tiene objetivo configurado?

### 6.2 Análisis de Visualizaciones

#### Visualizaciones que Funcionan Bien:
✅ **Tarjetas**: Muestran métricas clave de forma clara
✅ **Gráfico de Barras**: Productos por categoría es útil
✅ **Tabla con Filtros**: Productos con stock bajo es práctica
✅ **Top 10**: Destaca productos importantes

#### Visualizaciones que Podrían Mejorarse:
⚠️ **Gauge**: Podría tener objetivo visual
⚠️ **Gráfico de Anillo**: Podría mostrar porcentajes
⚠️ **Faltan KPIs visuales**: No hay indicadores de estado

### 6.3 Identificación de Faltantes

#### ❌ Lo que FALTA según los Requisitos:

1. **Jerarquías**:
   - ❌ Jerarquía de Tiempo (Año → Trimestre → Mes)
   - ❌ Jerarquía de Productos (Categoría → Proveedor → Producto)

2. **Medidas Adicionales**:
   - ❌ Medidas de análisis temporal (MoM, YoY, YTD)
   - ❌ Más medidas con diferentes funciones DAX

3. **KPIs Completos**:
   - ⚠️ Hay rotación de inventario, pero falta:
     - Objetivo visual
     - Indicador de estado
   - ❌ Margen de utilidad (KPI)
   - ❌ Nivel de servicio (KPI)

4. **Agrupaciones**:
   - ❌ Agrupaciones por rangos de stock
   - ❌ Agrupaciones por valor de inventario

---

## 7. Checklist de Revisión

### ✅ Verificación del Archivo Actual

#### Modelo de Datos
- [x] Tabla Productos existe
- [x] Tabla Clientes existe
- [x] Tabla Ventas existe
- [x] Tabla Detalle_Ventas existe
- [x] Relaciones entre tablas configuradas

#### Medidas DAX
- [x] -- Total de Productos Vendidos
- [x] -- Valor Total Inventario
- [x] -- Stock Total
- [x] -- Total de Ventas
- [x] -- Ingresos Totales
- [x] -- Rotación de Inventario
- [ ] Medidas de tiempo (MoM, YoY, YTD)
- [ ] Más medidas con diferentes funciones DAX

#### Visualizaciones
- [x] Tarjetas con métricas principales
- [x] Gráfico de barras por categoría
- [x] Gráfico de columnas (Top 10)
- [x] Gráfico de anillo
- [x] Tabla con filtros
- [x] Medidor (Gauge)
- [ ] Visuales KPI completos
- [ ] Gráficos temporales

#### Jerarquías y Agrupaciones
- [ ] Jerarquía de Tiempo
- [ ] Jerarquía de Productos
- [ ] Agrupaciones por rangos

#### KPIs
- [ ] KPI 1: Rotación (con objetivo y estado)
- [ ] KPI 2: Margen de Utilidad
- [ ] KPI 3: Nivel de Servicio

---

## 🎓 Cómo Usar Esta Información

### Para Entender el Archivo:
1. **Abre Power BI Desktop** con el archivo
2. **Ve a Vista de Modelo** para ver las tablas y relaciones
3. **Ve a Vista de Informes** para ver las visualizaciones
4. **Expande las tablas** en el panel de campos para ver medidas

### Para Completar los Requisitos:
1. **Revisa** `Guia_Paso_a_Paso_Medidas_DAX.md` para crear medidas faltantes
2. **Revisa** `Codigo_DAX_Listo_Copiar.md` para código listo
3. **Revisa** `Documentacion_Sprint4.md` para crear jerarquías y KPIs

### Para Presentar:
1. **Usa Vista de Informes** para mostrar el dashboard
2. **Explica cada visualización** siguiendo esta guía
3. **Destaca las métricas clave** mostradas en las tarjetas

---

## 📌 Resumen Ejecutivo

### ✅ Lo que TIENES:
- ✅ Modelo de datos completo (4 tablas relacionadas)
- ✅ 6 medidas DAX básicas creadas
- ✅ 7 visualizaciones funcionando
- ✅ Tema personalizado medieval
- ✅ Dashboard funcional con métricas clave

### ❌ Lo que FALTA:
- ❌ Jerarquías (Tiempo, Productos)
- ❌ Medidas avanzadas (análisis temporal)
- ❌ KPIs completos (objetivos y estados)
- ❌ Agrupaciones por rangos
- ❌ Más medidas con diferentes funciones DAX

### 🎯 Próximos Pasos Recomendados:

1. **Crear medidas faltantes** (usar guías proporcionadas)
2. **Crear jerarquías** en el modelo
3. **Completar KPIs** con objetivos y estados
4. **Agregar visualizaciones temporales**
5. **Probar y validar** todas las medidas

---

## 🔍 Comandos Útiles en Power BI

### Ver Medidas:
- Panel de campos → Expandir tabla → Buscar ícono 🧮

### Editar Medida:
- Click derecho en medida → "Editar medida"

### Ver Datos:
- Vista de Datos → Seleccionar tabla

### Ver Modelo:
- Vista de Modelo → Ver relaciones

### Probar Medida:
- Arrastrar medida a una tabla nueva
- Verificar que muestre valores

---

## 📞 Referencias Rápidas

- **Guía Paso a Paso**: `Guia_Paso_a_Paso_Medidas_DAX.md`
- **Código DAX Listo**: `Codigo_DAX_Listo_Copiar.md`
- **Documentación Completa**: `Documentacion_Sprint4.md`
- **Ejemplos DAX**: `Notebook_DAX_Ejemplos.md`

---

**Fecha de Creación**: Diciembre 2025  
**Versión**: 1.0  
**Proyecto**: Tienda Aurelion - Sprint 4

---

## ✨ Conclusión

Tu archivo Power BI tiene una **base sólida** con:
- Modelo de datos bien estructurado
- Visualizaciones funcionales
- Medidas básicas creadas

Ahora necesitas **completar los requisitos** agregando:
- Más medidas DAX avanzadas
- Jerarquías y agrupaciones
- KPIs completos

¡Sigue las guías proporcionadas para completar tu proyecto! 🚀



