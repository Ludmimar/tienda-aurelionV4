# 📊 LAYOUT VISUAL DEL DASHBOARD - TIENDA AURELION

## Vista Previa del Dashboard Power BI

Este documento muestra visualmente cómo debería verse tu dashboard al finalizarlo.

---

## 📄 PÁGINA 1: OVERVIEW (Vista General)

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                   ⚔️  TIENDA AURELION - DASHBOARD OVERVIEW                   ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  ║
║  │  TOTAL    │  │  VALOR    │  │  STOCK    │  │  TOTAL    │  │ INGRESOS  │  ║
║  │ PRODUCTOS │  │   TOTAL   │  │   TOTAL   │  │  VENTAS   │  │  TOTALES  │  ║
║  │           │  │ INVENTARIO│  │           │  │           │  │           │  ║
║  │    80     │  │ $285,000  │  │  4,068    │  │   100     │  │ $219,000  │  ║
║  └───────────┘  └───────────┘  └───────────┘  └───────────┘  └───────────┘  ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ┌──────────────────────────────────┐  ┌──────────────────────────────────┐  ║
║  │ PRODUCTOS POR CATEGORÍA          │  │ TOP 10 PRODUCTOS MÁS VALIOSOS    │  ║
║  │                                  │  │                                  │  ║
║  │ Armas          ████████████ 15   │  │     ┌─────┐                     │  ║
║  │ Armaduras      ████████ 12       │  │     │█████│                     │  ║
║  │ Pociones       ██████ 10         │  │     │█████│  ┌────┐             │  ║
║  │ Accesorios     ██████████ 14     │  │     │█████│  │████│  ┌───┐     │  ║
║  │ Consumibles    ████ 8            │  │     │█████│  │████│  │███│     │  ║
║  │ Escudos        ████ 6            │  │ ┌───┼─────┼──┼────┼──┼───┼───┐ │  ║
║  │ Calzado        ██ 4              │  │ │   │     │  │    │  │   │   │ │  ║
║  │ ...                              │  │ └───┴─────┴──┴────┴──┴───┴───┘ │  ║
║  │                                  │  │  Armadura Capa  Espada Báculo   │  ║
║  └──────────────────────────────────┘  └──────────────────────────────────┘  ║
║                                                                               ║
║  ┌──────────────────────────────────┐  ┌──────────────────────────────────┐  ║
║  │ DISTRIBUCIÓN DE STOCK            │  │ ⚠️  PRODUCTOS CON STOCK BAJO     │  ║
║  │    POR CATEGORÍA                 │  │                                  │  ║
║  │                                  │  │ Producto          Cat.   Stock   │  ║
║  │         ┌─────────┐              │  │ ──────────────────────────────── │  ║
║  │        ╱           ╲             │  │ Gema Resurrección Cons.   3 🔴   │  ║
║  │       │   Armas     │            │  │ Bestiario Comp.   Libros  5 🔴   │  ║
║  │       │    23%      │            │  │ Capa Real         Capas   7 🔴   │  ║
║  │       │             │            │  │ Grimorio Antiguo  Libros  8 🟡   │  ║
║  │   Acc.│             │Armaduras   │  │ Armadura Mithril  Armad.  8 🟡   │  ║
║  │   18% │             │   19%      │  │ Capa Invisibilid. Capas  10 🟡   │  ║
║  │       │             │            │  │ Perla Sabiduría   Acces. 12 🟡   │  ║
║  │        ╲           ╱             │  │ ...                              │  ║
║  │         └─────────┘              │  │                                  │  ║
║  │      Pociones 22%  Consumibles   │  │ TOTAL: 15 productos              │  ║
║  │                       18%        │  │                                  │  ║
║  └──────────────────────────────────┘  └──────────────────────────────────┘  ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### 📊 Visuales en esta página:

| Visual | Tipo | Propósito |
|--------|------|-----------|
| **5 Tarjetas KPI** | Card | Mostrar métricas principales del negocio |
| **Productos por Categoría** | Barras horizontales | Ver distribución de productos |
| **Top 10 Más Valiosos** | Columnas | Identificar productos de alto valor |
| **Distribución Stock** | Gráfico de anillos | Visualizar proporción de inventario |
| **Stock Bajo** | Tabla con formato | Alertas de reabastecimiento |

### 🎨 Colores:
- **Fondo:** Gris oscuro (#2C2C2C)
- **Títulos:** Dorado (#D4AF37)
- **Texto:** Beige (#F5F5DC)
- **Alertas:** 🔴 Rojo (stock ≤ 10) | 🟡 Amarillo (stock ≤ 20)

---

## 📄 PÁGINA 2: VENTAS Y CLIENTES

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║               ⚔️  TIENDA AURELION - VENTAS Y CLIENTES                        ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐   ║
║  │ TICKET   │  │  TOTAL   │  │  TOTAL   │  │ PROMEDIO │  │   FILTRO     │   ║
║  │ PROMEDIO │  │PRODUCTOS │  │ CLIENTES │  │  VENTA   │  │   FECHAS     │   ║
║  │          │  │ VENDIDOS │  │          │  │          │  │ ┌──────────┐ │   ║
║  │ $2,190   │  │  2,546   │  │    50    │  │ $2,190   │  │ 2024-05-01 │ │   ║
║  └──────────┘  └──────────┘  └──────────┘  └──────────┘  │     to     │ │   ║
║                                                           │ 2024-08-08 │ │   ║
║                                                           └──────────┘ │   ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │ EVOLUCIÓN DE INGRESOS POR FECHA                                        │  ║
║  │                                                                        │  ║
║  │  $6000┤                                       ●                        │  ║
║  │       │                     ●         ●                                │  ║
║  │  $5000┤           ●                             ●                      │  ║
║  │       │     ●                                                          │  ║
║  │  $4000┤ ●         ●   ●                                                │  ║
║  │       │                       ●   ●   ●                                │  ║
║  │  $3000┤       ●                           ●       ●                    │  ║
║  │       │                                                   ●        ●   │  ║
║  │  $2000┤                                                                │  ║
║  │       │                                                                │  ║
║  │  $1000┤                                                                │  ║
║  │       └────────────────────────────────────────────────────────────── │  ║
║  │       May 1        May 15       Jun 1        Jun 15       Jul 1       │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                                                               ║
║  ┌──────────────────────────────────┐  ┌──────────────────────────────────┐  ║
║  │ TOP 5 PRODUCTOS MÁS VENDIDOS     │  │ CLIENTES POR CIUDAD              │  ║
║  │                                  │  │                                  │  ║
║  │ Poción de Vida     ██████ 324    │  │       ┌────┐                    │  ║
║  │ Poción de Maná     ████ 165      │  │       │████│                    │  ║
║  │ Flechas Mágicas    ███ 118       │  │       │████│  ┌───┐             │  ║
║  │ Pergamino Fuego    ██ 85         │  │       │████│  │███│  ┌──┐      │  ║
║  │ Pergamino Hielo    ██ 73         │  │   ┌───┼────┼──┼───┼──┼──┼──┐   │  ║
║  │                                  │  │   │   │    │  │   │  │  │  │   │  ║
║  └──────────────────────────────────┘  │   └───┴────┴──┴───┴──┴──┴──┘   │  ║
║                                        │   Gondor  Rohan  La   Rivendell  │  ║
║  ┌──────────────────────────────────┐  │           Comarca                │  ║
║  │ DETALLE DE VENTAS                │  └──────────────────────────────────┘  ║
║  │                                  │                                        ║
║  │ ID  Fecha      Total  Cliente    │                                        ║
║  │ ───────────────────────────────  │                                        ║
║  │ 100 2024-08-08 $3,800 Legolas    │                                        ║
║  │ 99  2024-08-07 $3,150 Smeagol    │                                        ║
║  │ 98  2024-08-06   $950 Gollum     │                                        ║
║  │ 97  2024-08-05 $4,680 Sauron     │                                        ║
║  │ 96  2024-08-04 $1,490 Tom Bomb.  │                                        ║
║  │ ...                              │                                        ║
║  └──────────────────────────────────┘                                        ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### 📊 Visuales en esta página:

| Visual | Tipo | Propósito |
|--------|------|-----------|
| **4 Tarjetas KPI + Slicer** | Cards + Date Slicer | Métricas de ventas y filtro temporal |
| **Evolución Ingresos** | Gráfico de línea | Ver tendencia de ventas en el tiempo |
| **Top 5 Más Vendidos** | Barras horizontales | Identificar productos populares |
| **Clientes por Ciudad** | Columnas | Distribución geográfica |
| **Detalle Ventas** | Tabla | Lista completa de transacciones |

### 🎯 Interactividad:
- **Filtro de fechas:** Filtra todos los visuales de ventas
- **Cross-filtering:** Click en una ciudad → filtra ventas de esa ciudad
- **Click en producto:** Ver ventas de ese producto específico

---

## 📐 DIMENSIONES RECOMENDADAS

### Tamaños de Visuales (en unidades de Power BI):

**Página Overview:**
- Tarjetas KPI: 200×150 px cada una, alineadas horizontalmente
- Gráfico de barras (Categorías): 450×350 px
- Gráfico de columnas (Top 10): 450×350 px
- Gráfico de anillos: 450×300 px
- Tabla Stock Bajo: 450×300 px

**Página Ventas:**
- Tarjetas KPI: 180×130 px cada una
- Gráfico de línea (Evolución): 950×350 px (ancho completo)
- Top 5 Vendidos: 450×300 px
- Clientes por Ciudad: 450×300 px
- Tabla de Ventas: 950×300 px (ancho completo)

---

## 🎨 PALETA DE COLORES DETALLADA

### Colores Principales
```
Dorado Aurelion:    #D4AF37  ████████  (Títulos, acentos)
Rojo Dragón:        #8B0000  ████████  (Gráficos, importante)
Azul Marino:        #000080  ████████  (Gráficos secundarios)
Plata:              #C0C0C0  ████████  (Texto secundario)
```

### Colores de Alerta
```
Amarillo Oro:       #FFD700  ████████  (Advertencias)
Rojo Crítico:       #FF0000  ████████  (Alertas urgentes)
Verde Saludable:    #00AA00  ████████  (Estado OK)
```

### Colores de Fondo
```
Gris Oscuro:        #2C2C2C  ████████  (Fondo principal)
Beige Pergamino:    #F5F5DC  ████████  (Texto principal)
```

---

## 📊 DATOS ESPERADOS (KPIs)

### Overview:
- **Total Productos:** 80 unidades
- **Valor Total Inventario:** ~$285,000
- **Stock Total:** ~4,068 unidades
- **Productos Stock Bajo:** ~15 productos
- **Total Ventas:** 100 transacciones
- **Ingresos Totales:** ~$219,000

### Ventas y Clientes:
- **Ticket Promedio:** ~$2,190
- **Total Productos Vendidos:** ~2,546 unidades
- **Total Clientes:** 50 clientes
- **Promedio Venta:** ~$2,190
- **Periodo:** Mayo 2024 - Agosto 2024

### Top Categorías (por cantidad):
1. Pociones (14 productos)
2. Armas (13 productos)
3. Armaduras (12 productos)
4. Accesorios (12 productos)
5. Consumibles (10 productos)

### Top 5 Productos Más Vendidos:
1. Poción de Vida (324 unidades)
2. Poción de Maná (165 unidades)
3. Flechas Mágicas (118 unidades)
4. Pergamino de Fuego (85 unidades)
5. Pergamino de Hielo (73 unidades)

### Top 5 Ciudades:
1. Gondor
2. La Comarca
3. Rohan
4. Rivendell
5. Bosque Negro

---

## 🔍 VERIFICACIÓN VISUAL

Usa esta lista para verificar que tu dashboard se vea correctamente:

### ✅ Diseño General
- [ ] Fondo oscuro medieval (#2C2C2C)
- [ ] Títulos en dorado (#D4AF37)
- [ ] Fuentes legibles (Segoe UI o similar)
- [ ] Espaciado uniforme entre elementos
- [ ] Sin sobreposición de visuales

### ✅ Tarjetas KPI
- [ ] Números grandes y visibles (36-48pt)
- [ ] Formato de moneda con $ y comas
- [ ] Títulos descriptivos arriba de cada valor
- [ ] Alineadas horizontalmente

### ✅ Gráficos
- [ ] Todos tienen títulos claros
- [ ] Ejes etiquetados correctamente
- [ ] Colores consistentes (paleta medieval)
- [ ] Leyendas visibles cuando son necesarias
- [ ] Tooltips funcionando al pasar el mouse

### ✅ Tablas
- [ ] Columnas alineadas correctamente
- [ ] Formato condicional aplicado (Stock Bajo)
- [ ] Encabezados visibles y claros
- [ ] Filas alternadas para mejor lectura

### ✅ Interactividad
- [ ] Slicers funcionando
- [ ] Cross-filtering activo
- [ ] Tooltips personalizados (opcional)
- [ ] Drill-through configurado (opcional)

---

## 📱 RESPONSIVE DESIGN

El dashboard debería verse bien en diferentes tamaños:

**Desktop (1920×1080):** Layout completo con todos los elementos visibles
**Laptop (1366×768):** Elementos ligeramente más compactos pero legibles
**Tablet (1024×768):** Power BI ajustará automáticamente el tamaño

**Tip:** Usa las guías de alineación de Power BI (View → Snap to grid) para mantener todo alineado.

---

## 🎯 PRÓXIMOS PASOS

Una vez que tu dashboard se vea como estos layouts:

1. **Testea la interactividad:** Haz click en diferentes elementos y verifica que los filtros funcionen
2. **Verifica los datos:** Compara los números con los esperados arriba
3. **Toma capturas:** Guarda screenshots de cada página
4. **Exporta:** Guarda como .pbix y opcionalmente como .pbit
5. **Documenta:** Anota cualquier insight interesante que descubras

---

**🎨 Diseñado por:** Martos Ludmila  
**🏢 Institución:** IBM - Sprint 3  
**📅 Año:** 2025  
**⚔️ Tema:** Tienda Aurelion - Medieval Fantasy Dashboard



