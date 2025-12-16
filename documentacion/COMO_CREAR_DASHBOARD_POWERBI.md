# 🚀 CÓMO CREAR EL DASHBOARD EN POWER BI - GUÍA MAESTRA

## ⚔️ Tienda Aurelion - Sprint 3

Esta es la **guía maestra** que te dirigirá a todos los recursos necesarios para crear tu dashboard de Power BI en 30 minutos.

---

## 📋 ÍNDICE RÁPIDO

| Recurso | Descripción | Archivo |
|---------|-------------|---------|
| 🏁 **Guía Paso a Paso** | Instrucciones detalladas para crear el dashboard | [`GUIA_RAPIDA_DASHBOARD_POWERBI.md`](./GUIA_RAPIDA_DASHBOARD_POWERBI.md) |
| ✅ **Checklist** | Lista de verificación para no olvidar nada | [`CHECKLIST_DASHBOARD.md`](./CHECKLIST_DASHBOARD.md) |
| 🎨 **Layout Visual** | Cómo debe verse el dashboard terminado | [`LAYOUT_VISUAL_DASHBOARD.md`](./LAYOUT_VISUAL_DASHBOARD.md) |
| 🔍 **Validador de Datos** | Script Python para verificar que los datos estén correctos | [`programas/validar_datos_powerbi.py`](./programas/validar_datos_powerbi.py) |
| 📊 **Guía Completa Power BI** | Documentación exhaustiva con teoría y mejores prácticas | [`documentacion/GUIA_POWER_BI.md`](./documentacion/GUIA_POWER_BI.md) |

---

## 🎯 FLUJO DE TRABAJO RECOMENDADO

### ANTES DE ABRIR POWER BI (5 minutos)

#### 1️⃣ Verificar que tengas todo

- [ ] Power BI Desktop instalado → [Descargar aquí](https://powerbi.microsoft.com/desktop/)
- [ ] Todos los archivos CSV en `Sprint-2/datos/`:
  - `productos.csv` (80 productos)
  - `clientes.csv` (50 clientes)
  - `ventas.csv` (100 ventas)
  - `detalle_ventas.csv` (273 detalles)

#### 2️⃣ Validar los datos (OPCIONAL pero recomendado)

```bash
# Ejecuta desde la carpeta Sprint-2/programas/
cd Sprint-2/programas
python validar_datos_powerbi.py
```

Este script verificará que:
- ✓ Todos los archivos existan
- ✓ Las columnas sean correctas
- ✓ No haya valores nulos problemáticos
- ✓ Las relaciones entre tablas sean válidas
- ✓ Los datos sean consistentes

**Si todo está ✅ VERDE**, puedes continuar con confianza.

#### 3️⃣ Leer el Layout Visual (3 minutos)

Abre [`LAYOUT_VISUAL_DASHBOARD.md`](./LAYOUT_VISUAL_DASHBOARD.md) para ver cómo se verá el dashboard terminado. Esto te dará una visión clara del objetivo final.

---

### MIENTRAS CREAS EL DASHBOARD (25 minutos)

#### 4️⃣ Seguir la Guía Paso a Paso

Abre [`GUIA_RAPIDA_DASHBOARD_POWERBI.md`](./GUIA_RAPIDA_DASHBOARD_POWERBI.md) y sigue las instrucciones:

**Tiempo estimado por sección:**
- ⏱️ **Paso 2 - Cargar 4 tablas:** 5 minutos
- ⏱️ **Paso 3 - Relaciones:** 2 minutos
- ⏱️ **Paso 4 - Tema:** 1 minuto
- ⏱️ **Paso 5 - Medidas DAX:** 3 minutos
- ⏱️ **Paso 6 - Página Overview:** 8 minutos
- ⏱️ **Paso 7 - Página Ventas:** 7 minutos
- ⏱️ **Paso 8 - Formateo:** 3 minutos
- ⏱️ **Paso 9 - Guardar:** 2 minutos

**TOTAL: ~30 minutos**

#### 5️⃣ Usar el Checklist

Mientras trabajas, marca los items en [`CHECKLIST_DASHBOARD.md`](./CHECKLIST_DASHBOARD.md) para asegurarte de que no olvides nada.

---

### DESPUÉS DE CREAR EL DASHBOARD (5 minutos)

#### 6️⃣ Verificación Final

Usa el checklist final en [`CHECKLIST_DASHBOARD.md`](./CHECKLIST_DASHBOARD.md#-fase-6-verificación-final) para verificar:

- ✓ Funcionalidad (cross-filtering, slicers)
- ✓ Diseño (colores, alineación, títulos)
- ✓ Datos (números correctos, formatos)

#### 7️⃣ Guardar y Documentar

- Guardar como `.pbix`: `Tienda_Aurelion_Dashboard_Sprint2.pbix`
- Exportar como `.pbit` (opcional): `Tienda_Aurelion_Template_Sprint2.pbit`
- Tomar capturas de pantalla de cada página
- Guardar las capturas en `Sprint-2/capturas/`

---

## 📁 ESTRUCTURA DE ARCHIVOS

```
Sprint-2/
├── 📄 COMO_CREAR_DASHBOARD_POWERBI.md ← ESTÁS AQUÍ (Guía Maestra)
├── 🚀 GUIA_RAPIDA_DASHBOARD_POWERBI.md (Instrucciones detalladas)
├── ✅ CHECKLIST_DASHBOARD.md (Lista de verificación)
├── 🎨 LAYOUT_VISUAL_DASHBOARD.md (Vista previa visual)
│
├── datos/ ← DATOS CSV
│   ├── productos.csv (80 productos)
│   ├── clientes.csv (50 clientes)
│   ├── ventas.csv (100 ventas)
│   └── detalle_ventas.csv (273 detalles)
│
├── Power BI/ ← RECURSOS POWER BI
│   ├── query_productos.m (Query M para tabla Productos)
│   ├── query_clientes.m (Query M para tabla Clientes)
│   ├── query_ventas.m (Query M para tabla Ventas)
│   ├── query_detalle_ventas.m (Query M para tabla Detalle_Ventas)
│   ├── measures.dax (Todas las medidas DAX)
│   ├── theme.json (Tema visual medieval)
│   ├── layout_instructions.md (Instrucciones de layout)
│   └── README.md (Explicación de los recursos)
│
├── programas/ ← SCRIPTS
│   ├── validar_datos_powerbi.py (Validador de datos)
│   ├── app_streamlit.py (App web alternativa)
│   └── analisis_estadistico.py (Análisis de datos)
│
├── documentacion/ ← DOCUMENTACIÓN COMPLETA
│   ├── GUIA_POWER_BI.md (Guía exhaustiva con teoría)
│   ├── INDICE_PROYECTO.md (Índice general)
│   └── ... (otros documentos)
│
└── capturas/ ← CAPTURAS DEL DASHBOARD (guardar aquí)
    ├── dashboard_overview.png (← crear después)
    └── dashboard_ventas_clientes.png (← crear después)
```

---

## 🎯 RUTAS RÁPIDAS SEGÚN TU OBJETIVO

### "Quiero crear el dashboard YA, sin leer teoría"
➡️ Ve directo a [`GUIA_RAPIDA_DASHBOARD_POWERBI.md`](./GUIA_RAPIDA_DASHBOARD_POWERBI.md)

### "Quiero ver cómo debe verse el dashboard antes de empezar"
➡️ Abre [`LAYOUT_VISUAL_DASHBOARD.md`](./LAYOUT_VISUAL_DASHBOARD.md)

### "Quiero verificar que mis datos estén correctos primero"
➡️ Ejecuta `python programas/validar_datos_powerbi.py`

### "Quiero entender Power BI en profundidad"
➡️ Lee [`documentacion/GUIA_POWER_BI.md`](./documentacion/GUIA_POWER_BI.md)

### "Necesito una lista de verificación para no olvidar nada"
➡️ Usa [`CHECKLIST_DASHBOARD.md`](./CHECKLIST_DASHBOARD.md)

### "Quiero copiar las queries M y medidas DAX"
➡️ Ve a la carpeta [`Power BI/`](./Power%20BI/)

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### ❌ "No puedo cargar los archivos CSV"

**Problema:** Power BI no encuentra `datos/productos.csv`

**Solución:**
1. Asegúrate de abrir Power BI Desktop desde la carpeta `Sprint-2/`
2. O modifica las queries M con rutas absolutas:
```m
File.Contents("D:/IBM/IBM-Inteligencia-Artificial/Sprint-2/datos/productos.csv")
```

---

### ❌ "Las medidas DAX dan error"

**Problema:** Power BI muestra error al crear medidas

**Solución:**
1. Verifica que los nombres de tablas sean EXACTOS:
   - `Productos` (no "productos" ni "Producto")
   - `Clientes` (no "clientes" ni "Cliente")
   - `Ventas` (no "ventas" ni "Venta")
   - `Detalle_Ventas` (no "detalle_ventas" ni "DetalleVentas")
2. Verifica que las columnas existan (ej: `Productos[precio]`)

---

### ❌ "Las relaciones no funcionan"

**Problema:** Cross-filtering no filtra los visuales

**Solución:**
1. Ve a **Model View**
2. Verifica que las líneas entre tablas sean **continuas** (no punteadas)
3. Verifica que las relaciones sean **"One to many"** (1 a muchos)
4. Si están punteadas (inactivas), click derecho → "Make this relationship active"

---

### ❌ "El tema visual no se aplica"

**Problema:** Los colores no cambian después de importar `theme.json`

**Solución:**
1. Verifica que hayas seleccionado el archivo correcto: `Sprint-2/Power BI/theme.json`
2. Los colores se aplican principalmente a nuevos gráficos
3. Para aplicar a gráficos existentes: Format visual → Colors → selecciona del tema
4. Si persiste, reinicia Power BI Desktop

---

### ❌ "Los números no coinciden con los esperados"

**Problema:** Los KPIs muestran valores muy diferentes a los documentados

**Solución:**
1. Ejecuta el script de validación: `python programas/validar_datos_powerbi.py`
2. Verifica que las 4 tablas se hayan cargado correctamente
3. Verifica que las medidas DAX estén bien escritas
4. Consulta los valores esperados en [`LAYOUT_VISUAL_DASHBOARD.md`](./LAYOUT_VISUAL_DASHBOARD.md#-datos-esperados-kpis)

---

## 💡 CONSEJOS PRO

### 🚀 Acelera el proceso

1. **Copia-pega múltiples medidas:** En lugar de crear medidas DAX una por una, copia varias a la vez si Power BI lo permite
2. **Usa Ctrl+C / Ctrl+V:** Duplica visuales similares y solo cambia los campos
3. **Snap to grid:** Activa **View → Snap to grid** para alinear elementos rápidamente
4. **Formato de pintor:** Usa **Format Painter** para copiar formato entre visuales

### 🎨 Mejora el diseño

1. **Usa las guías:** Arrastra desde las reglas para crear guías de alineación
2. **Agrupa elementos:** Selecciona varios visuales → Click derecho → Group
3. **Espacio uniforme:** Usa **Format → Align → Distribute horizontally/vertically**
4. **Colores consistentes:** Define la paleta al principio y úsala en todos los gráficos

### 📊 Mejora la interactividad

1. **Tooltips personalizados:** Crea una página de tooltip con detalles adicionales
2. **Bookmarks:** Guarda diferentes vistas del dashboard (View → Bookmarks)
3. **Botones de navegación:** Agrega botones para cambiar entre páginas
4. **Drill-through:** Configura drill-through para análisis detallados

---

## 📊 KPIs OBJETIVO

Al finalizar, tu dashboard debería mostrar aproximadamente:

| Métrica | Valor Esperado |
|---------|----------------|
| Total Productos | 80 |
| Valor Total Inventario | ~$285,000 |
| Stock Total | ~4,068 unidades |
| Total Ventas | 100 |
| Ingresos Totales | ~$219,000 |
| Ticket Promedio | ~$2,190 |
| Total Clientes | 50 |
| Productos Stock Bajo | ~15 |
| Total Productos Vendidos | ~2,546 unidades |

**Nota:** Ligeras variaciones son normales dependiendo de cálculos y filtros.

---

## 📚 RECURSOS ADICIONALES

### Documentación Oficial
- [Power BI Documentation (Microsoft)](https://docs.microsoft.com/power-bi/)
- [DAX Guide](https://dax.guide/)
- [Power Query M Reference](https://docs.microsoft.com/powerquery-m/)

### Tutoriales en Español
- [Curso Power BI (YouTube)](https://www.youtube.com/results?search_query=power+bi+tutorial+español)
- [Power BI Tips (Blog)](https://www.powerbitesp.com/)

### Comunidad
- [Power BI Community](https://community.powerbi.com/)
- [Power BI Ideas](https://ideas.powerbi.com/)

---

## ✅ CHECKLIST FINAL

Antes de dar por terminado el dashboard:

- [ ] Ejecuté el validador de datos y todo está ✅ verde
- [ ] Seguí la guía paso a paso completa
- [ ] Marqué todos los items del checklist
- [ ] Verifiqué que el layout coincida con el visual
- [ ] Testé la interactividad (cross-filtering, slicers)
- [ ] Guardé el archivo .pbix
- [ ] Tomé capturas de pantalla de cada página
- [ ] Exporté el .pbit (opcional)

---

## 🎓 CRÉDITOS

**Autora:** Martos Ludmila  
**DNI:** 34811650  
**Institución:** IBM - Introducción a la Inteligencia Artificial  
**Sprint:** 2 - Base de Datos Normalizada  
**Año:** 2025  
**Tema:** Tienda Aurelion - Sistema de Gestión de Inventario, Ventas y Clientes

---

## 🎯 SIGUIENTE PASO

**➡️ Abre Power BI Desktop y comienza con [`GUIA_RAPIDA_DASHBOARD_POWERBI.md`](./GUIA_RAPIDA_DASHBOARD_POWERBI.md)**

**¡Éxitos con tu dashboard! ⚔️📊**

---

**Última actualización:** Noviembre 2025




