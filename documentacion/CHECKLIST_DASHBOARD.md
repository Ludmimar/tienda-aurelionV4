# ✅ CHECKLIST DASHBOARD POWER BI - TIENDA AURELION

## 📋 Antes de Empezar

- [ ] Power BI Desktop instalado
- [ ] Carpeta `Sprint-2/datos/` con 4 archivos CSV
- [ ] Carpeta `Sprint-2/Power BI/` con queries M, medidas DAX y tema

---

## 🔄 FASE 1: Carga de Datos

- [ ] Tabla **Productos** cargada (80 filas)
- [ ] Tabla **Clientes** cargada (50 filas)
- [ ] Tabla **Ventas** cargada (100 filas)
- [ ] Tabla **Detalle_Ventas** cargada (273 filas)
- [ ] Relación: `Clientes[id]` → `Ventas[id_cliente]`
- [ ] Relación: `Ventas[id_venta]` → `Detalle_Ventas[id_venta]`
- [ ] Relación: `Productos[id]` → `Detalle_Ventas[id_producto]`
- [ ] Todas las relaciones están activas (líneas continuas)

---

## 🎨 FASE 2: Diseño Visual

- [ ] Tema `theme.json` importado
- [ ] Colores medievales aplicados (dorado, rojo oscuro, azul marino)

---

## 📊 FASE 3: Medidas DAX

### Medidas de Productos
- [ ] Valor Total Inventario
- [ ] Precio Promedio
- [ ] Stock Total
- [ ] Productos Stock Bajo
- [ ] % Stock Saludable

### Medidas de Ventas
- [ ] Total Ventas
- [ ] Ingresos Totales
- [ ] Promedio Venta
- [ ] Ticket Promedio
- [ ] Total Productos Vendidos

### Medidas de Clientes
- [ ] Total Clientes

---

## 📄 FASE 4: Página 1 - Overview

### Tarjetas KPI (fila superior)
- [ ] Total de Productos
- [ ] Valor Total Inventario
- [ ] Stock Total
- [ ] Total Ventas
- [ ] Ingresos Totales

### Gráficos Principales
- [ ] Gráfico de barras: Productos por Categoría
- [ ] Gráfico de columnas: Top 10 Productos Más Valiosos
- [ ] Gráfico de anillos: Distribución de Stock por Categoría
- [ ] Tabla: Productos con Stock Bajo (≤20 unidades)

### Formato
- [ ] Tabla de stock bajo tiene formato condicional (rojo/amarillo)
- [ ] Top 10 tiene filtro Top N aplicado
- [ ] Todos los gráficos tienen títulos descriptivos
- [ ] Elementos alineados correctamente

---

## 📄 FASE 5: Página 2 - Ventas y Clientes

### Tarjetas KPI (fila superior)
- [ ] Ticket Promedio
- [ ] Total Productos Vendidos
- [ ] Total Clientes
- [ ] Promedio Venta

### Gráficos de Ventas
- [ ] Gráfico de línea: Evolución de Ingresos por Fecha
- [ ] Gráfico de barras: Top 5 Productos Más Vendidos
- [ ] Tabla: Detalle de Ventas (con cliente y ciudad)

### Gráficos de Clientes
- [ ] Gráfico de columnas: Clientes por Ciudad

### Filtros (Slicers)
- [ ] Slicer de rango de fechas (Between style)

### Formato
- [ ] Top 5 tiene filtro Top N aplicado
- [ ] Tabla de ventas ordenada por fecha descendente
- [ ] Todos los gráficos tienen títulos descriptivos
- [ ] Elementos alineados correctamente

---

## 🎯 FASE 6: Verificación Final

### Funcionalidad
- [ ] Cross-filtering funciona (al hacer click en un gráfico, otros se filtran)
- [ ] Slicers filtran todos los visuales de la página
- [ ] No hay errores de visualización
- [ ] Tooltips muestran información correcta

### Diseño
- [ ] Título principal en cada página: "⚔️ TIENDA AURELION - DASHBOARD"
- [ ] Colores consistentes en todas las páginas
- [ ] Espaciado adecuado entre elementos
- [ ] Sin sobreposición de visuales
- [ ] Texto legible en todos los tamaños

### Datos
- [ ] Todos los números tienen sentido (no hay valores negativos extraños)
- [ ] Formatos de moneda aplicados correctamente
- [ ] Fechas se muestran correctamente
- [ ] Nombres de productos/clientes se visualizan completos

---

## 💾 FASE 7: Guardar y Exportar

- [ ] Archivo .pbix guardado: `Tienda_Aurelion_Dashboard_Sprint2.pbix`
- [ ] Archivo .pbit exportado (opcional): `Tienda_Aurelion_Template_Sprint2.pbit`
- [ ] Captura de pantalla de página Overview guardada
- [ ] Captura de pantalla de página Ventas y Clientes guardada

---

## 📊 KPIs Esperados (Aproximados)

Verifica que tus números sean similares a estos:

| KPI | Valor Esperado |
|-----|----------------|
| Total Productos | 80 |
| Stock Total | ~4,000 unidades |
| Valor Total Inventario | ~$280,000 |
| Total Ventas | 100 |
| Ingresos Totales | ~$219,000 |
| Ticket Promedio | ~$2,190 |
| Total Clientes | 50 |
| Productos Stock Bajo (≤20) | ~15 productos |

**Nota:** Los valores pueden variar ligeramente dependiendo de cálculos adicionales.

---

## ✨ BONUS: Mejoras Opcionales

- [ ] Agregar página 3: Análisis de Productos detallado
- [ ] Agregar página 4: Análisis de Proveedores
- [ ] Crear tooltips personalizados
- [ ] Agregar bookmarks para diferentes vistas
- [ ] Agregar botones de navegación entre páginas
- [ ] Agregar marca de última actualización (fecha actual)
- [ ] Agregar logos o imágenes temáticas medievales

---

## 🆘 Si algo no funciona...

Consulta la sección "SOLUCIÓN DE PROBLEMAS COMUNES" en:
`Sprint-2/GUIA_RAPIDA_DASHBOARD_POWERBI.md`

---

**¡Éxito con tu dashboard! ⚔️📊**

**Autor:** Martos Ludmila | **DNI:** 34811650 | **Sprint 3 - IBM 2025**



