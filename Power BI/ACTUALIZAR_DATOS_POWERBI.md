# 🔄 Cómo Actualizar Datos en Power BI Desktop

## 📋 Pasos para Actualizar los Datos

### Opción 1: Actualizar Datos (Refresh) - RECOMENDADO

1. **Abre Power BI Desktop**
   - Abre el archivo `Sprint4.pbix`

2. **Actualizar Datos**
   - Método 1: Presiona **F5** en tu teclado
   - Método 2: Ve a **Inicio** → Click en **Actualizar** (icono de flechas circulares)
   - Método 3: Click derecho en el nombre de la tabla en el panel de campos → **Actualizar datos**

3. **Espera a que termine**
   - Verás un mensaje "Actualizando..." en la parte inferior
   - Espera hasta que aparezca "Actualización completada"

### Opción 2: Transformar Datos y Recargar

1. **Ve a Transformar datos**
   - Click en **Inicio** → **Transformar datos** → **Transformar datos**

2. **Verifica la fuente**
   - En el Editor de Power Query, verifica que las tablas apunten a los CSV correctos
   - Deberías ver la ruta: `tienda-aurelionV4/datos/ventas.csv`

3. **Actualizar Todo**
   - Click en **Inicio** → **Cerrar y aplicar**
   - Esto recargará todos los datos desde los CSV

### Opción 3: Cambiar Origen y Recargar

Si los datos siguen sin actualizarse:

1. **Transformar datos**
   - **Inicio** → **Transformar datos** → **Transformar datos**

2. **Cambiar origen**
   - Selecciona la consulta "Ventas" en el panel izquierdo
   - Click derecho → **Configuración avanzada**
   - O ve a **Inicio** → **Origen de datos** → **Cambiar origen**

3. **Seleccionar nuevo archivo**
   - Navega hasta `tienda-aurelionV4/datos/ventas.csv`
   - Selecciona el archivo actualizado
   - Click en **Abrir**

4. **Aplicar cambios**
   - **Inicio** → **Cerrar y aplicar**

### Opción 4: Reimportar Tablas (Si nada funciona)

1. **Eliminar y recrear**
   - En Power Query, elimina las consultas de Ventas y Detalle_Ventas
   - Ve a **Inicio** → **Nueva consulta** → **Otras fuentes** → **Archivo CSV**
   - Selecciona `ventas.csv` y repite para `detalle_ventas.csv`

2. **Recrear relaciones**
   - Ve a **Vista de modelo** (icono de diagramas en el panel izquierdo)
   - Arrastra `id_venta` de Ventas a `id_venta` de Detalle_Ventas para crear la relación

## 🔍 Verificación

### Cómo verificar que los datos se actualizaron:

1. **Revisa el número de filas**
   - En Power BI, ve a **Vista de datos** (icono de tabla)
   - Selecciona la tabla "Ventas"
   - Deberías ver **1,296 filas** (o el número actualizado)

2. **Revisa el rango de fechas**
   - Crea un visual temporal con `Ventas[fecha]`
   - Deberías ver datos desde 2023 hasta 2025

3. **Verifica años disponibles**
   - Crea un gráfico con `Ventas[fecha]` agrupado por Año
   - Deberías ver: 2023, 2024, 2025

## 📊 Datos Esperados

Después de actualizar, deberías tener:

- **Total ventas**: 1,296 registros
- **Rango de fechas**: 2023-05-01 a 2025-12-16
- **Años**: 2023 (372), 2024 (372), 2025 (552)
- **Total detalles**: 3,322 registros

## ⚠️ Problemas Comunes

### "No se puede encontrar el archivo"
- **Solución**: Verifica que la ruta del CSV sea correcta
- Las rutas pueden cambiar si moviste la carpeta

### "Los datos no cambian después de actualizar"
- **Solución**: Cierra y vuelve a abrir Power BI Desktop
- O elimina la caché: Archivo → Opciones y configuración → Opciones → Actualización global → Limpiar caché

### "Error al cargar datos"
- **Solución**: Verifica que los CSV no estén abiertos en Excel u otro programa
- Verifica que los CSV tengan el formato correcto (UTF-8)

## ✅ Solución Rápida

**El método más rápido es:**
1. Abre Power BI Desktop con `Sprint4.pbix`
2. Presiona **F5**
3. Espera a que termine la actualización
4. Verifica que el número de filas sea 1,296

¡Listo! Los datos deberían estar actualizados.

