# 🌐 APLICACIÓN WEB CON STREAMLIT - TIENDA AURELION

## 🚀 Inicio Rápido

### Instalación

```bash
# Instalar las dependencias necesarias
pip install streamlit pandas numpy matplotlib seaborn scipy
```

O usando el archivo requirements.txt:

```bash
pip install -r requirements.txt
```

### Ejecución

```bash
streamlit run app_streamlit.py
```

La aplicación se abrirá automáticamente en tu navegador en: `http://localhost:8501`

---

## 📱 Características de la Aplicación Web

### 🏠 Página de Inicio
- **Dashboard completo** con métricas principales
- **Gráficos interactivos**:
  - Productos por categoría
  - Distribución de precios
  - Productos por proveedor
  - Top 5 más valiosos
- **Alertas automáticas** de productos con stock bajo

### 🔍 Explorar Productos
- **Filtros avanzados**:
  - Por categoría
  - Por proveedor
  - Por rango de precios (slider interactivo)
  - Por estado de stock
- **Búsqueda por nombre** (búsqueda parcial)
- **Tabla interactiva** con todos los detalles
- **Estadísticas de resultados** filtrados

### 📊 Estadísticas
- **Análisis completo por categoría**:
  - Cantidad de productos
  - Stock total
  - Precio promedio
  - Valor total
- **Análisis por proveedor**:
  - Productos por proveedor
  - Diversificación
  - Valor generado
- **Productos destacados**:
  - Más caro
  - Más económico
  - Mayor valor en inventario

### 💰 Gestión de Ventas ⭐ NUEVO
- **Ver todas las ventas**: Historial completo con filtros
- **Ver detalle de venta**: Información detallada por transacción
- **Estadísticas de ventas**: Análisis de ingresos y tendencias

### 👥 Gestión de Clientes ⭐ NUEVO
- **Listar clientes**: Vista completa con información de contacto
- **Estadísticas de clientes**: Análisis de base de clientes
- **Agregar nuevos productos**:
  - Formulario interactivo
  - Validación de datos
  - ID automático
- **Actualizar stock**:
  - Agregar stock (recepción de mercancía)
  - Reducir stock (ventas)
  - Establecer stock nuevo (inventario)
  - Alertas de stock bajo

---

## 🎨 Características Visuales

- ✨ **Interfaz moderna y profesional**
- 🎨 **Tema medieval/fantasía** con colores personalizados
- 📱 **Diseño responsive** (funciona en móviles)
- ⚡ **Interactividad en tiempo real**
- 📊 **Gráficos dinámicos**
- 🔔 **Alertas visuales** para stock bajo

---

## 💡 Ventajas sobre la Versión de Consola

| Aspecto | Consola Python | Streamlit Web |
|---------|----------------|---------------|
| **Interfaz** | Texto | Visual interactiva |
| **Gráficos** | Texto/ASCII | Gráficos reales |
| **Filtros** | Manual | Sliders y selectores |
| **Acceso** | Local | Web (compartible) |
| **Actualización** | Reinicio | Tiempo real |
| **Experiencia** | Básica | Profesional |

---

## 📊 Capturas de la Interfaz

### Dashboard Principal
```
╔══════════════════════════════════════════════════╗
║      ⚔️ TIENDA AURELION ⚔️                      ║
║    Sistema de Gestión de Inventario              ║
╠══════════════════════════════════════════════════╣
║  [📦 20]  [📊 1,468]  [💰 85,075]  [🏷️ 10]  [⚠️ 3] ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  📈 Gráficos Interactivos                        ║
║  - Productos por Categoría (barras)              ║
║  - Distribución de Precios (barras)              ║
║  - Productos por Proveedor (barras)              ║
║  - Top 5 Más Valiosos (barras)                   ║
║                                                  ║
║  ⚠️ ALERTA: 3 productos con stock bajo           ║
║                                                  ║
╚══════════════════════════════════════════════════╝
```

### Explorar Productos
```
🎛️ Filtros (Barra Lateral)
├── Categoría: [Dropdown]
├── Proveedor: [Dropdown]
├── Precio: [Slider] 25 ━━●━━━━━ 5000
├── Stock: [Radio] Todos / Bajo / Saludable
└── Buscar: [Text Input]

📦 Resultados: 5 productos
┌────────────────────────────────────────────────┐
│ ID │ Nombre  │ Cat.  │ Precio │ Stock │ Estado │
├────┼─────────┼───────┼────────┼───────┼────────┤
│  1 │ Espada  │ Armas │  1500  │  25   │ ✅ OK  │
│  2 │ Armadura│ Armor │  3000  │  15   │ ✅ OK  │
└────────────────────────────────────────────────┘

Stock Total: 1,468  |  Valor: 85,075 💰  |  Promedio: 932 💰
```

---

## 🔧 Solución de Problemas

### Error: "streamlit: comando no encontrado"

**Solución:**
```bash
# Verificar que está instalado
pip list | grep streamlit

# Reinstalar si es necesario
pip install --upgrade streamlit
```

### Error: "No module named 'pandas'"

**Solución:**
```bash
pip install pandas
```

### El navegador no se abre automáticamente

**Solución:**
Abre manualmente en tu navegador: `http://localhost:8501`

### Cambios en el CSV no se reflejan

**Solución:**
- Presiona `C` en la terminal para limpiar cache
- O usa el menú "Clear cache" en la app (esquina superior derecha)

---

## 📦 Estructura de Archivos

```
Entregable/
├── programas/
│   └── app_streamlit.py              ← Aplicación web principal
├── datos/
│   ├── productos.csv                 ← Base de datos de productos
│   ├── clientes.csv                  ← Base de datos de clientes
│   ├── ventas.csv                    ← Base de datos de ventas
│   └── detalle_ventas.csv            ← Detalles de ventas
├── requirements.txt                  ← Dependencias
├── documentacion/
│   └── INSTRUCCIONES_STREAMLIT.md    ← Este archivo
└── ... (otros archivos del proyecto)
```

---

## 🎯 Comandos Útiles

### Desarrollo

```bash
# Ejecutar con auto-reload (recarga automática al guardar)
streamlit run app_streamlit.py

# Ejecutar en puerto específico
streamlit run app_streamlit.py --server.port 8080

# Ejecutar sin abrir navegador
streamlit run app_streamlit.py --server.headless true
```

### Producción

```bash
# Compartir en la red local
streamlit run app_streamlit.py --server.address 0.0.0.0
```

---

## 🌐 Desplegar en la Nube (Opcional)

### Streamlit Community Cloud (Gratis)

1. Sube tu proyecto a GitHub
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu repositorio
4. ¡Tu app estará online en minutos!

### Otras opciones:
- Heroku
- Google Cloud Run
- AWS Elastic Beanstalk
- Azure App Service

---

## 💡 Funcionalidades Avanzadas

### Cache de Datos
La aplicación usa `@st.cache_data` para:
- ✅ Cargar datos una sola vez
- ✅ Mejorar rendimiento
- ✅ Reducir operaciones de I/O

### Actualización en Tiempo Real
- Cuando agregas o actualizas productos, la app recarga automáticamente
- Los gráficos se actualizan dinámicamente

### Persistencia de Datos
- Todos los cambios se guardan en el CSV
- Los datos persisten entre sesiones

---

## 🎓 Comparación: Consola vs Jupyter vs Streamlit

| Característica | Python Consola | Jupyter Notebook | Streamlit Web |
|----------------|----------------|------------------|---------------|
| **Instalación** | ✅ Simple | ⚠️ Media | ⚠️ Media |
| **Interfaz** | Texto | Notebook | Web profesional |
| **Gráficos** | ❌ ASCII | ✅ Matplotlib | ✅ Interactivos |
| **Filtros** | ❌ Manual | ⚠️ Widgets | ✅ Nativos |
| **Compartir** | ❌ Script | ⚠️ Archivo | ✅ URL |
| **Actualización** | ❌ Reinicio | ⚠️ Re-ejecutar | ✅ Automática |
| **Para Presentar** | ❌ No ideal | ✅ Bueno | ✅ Excelente |
| **Usuarios No Técnicos** | ❌ No | ❌ No | ✅ Sí |

---

## 📝 Notas Importantes

1. **Primera ejecución**: La primera vez puede tardar un poco mientras Streamlit descarga recursos

2. **Rendimiento**: Con 20 productos es instantáneo. Para 1000+ productos considera optimizaciones

3. **Seguridad**: Esta versión NO incluye autenticación. Para producción, considera agregar login

4. **Base de datos**: Actualmente usa CSV. Para producción, considera migrar a SQL

5. **Concurrent users**: Streamlit Community Cloud soporta múltiples usuarios simultáneos

---

## 🎤 Para tu Presentación

### Ventajas de Mostrar la App Web:

1. ✅ **Impresiona visualmente** - Más profesional que consola
2. ✅ **Demuestra habilidades modernas** - Web > Terminal
3. ✅ **Interactividad en vivo** - Puedes filtrar en tiempo real
4. ✅ **Gráficos profesionales** - Visualización de datos
5. ✅ **Fácil de usar** - Cualquiera puede usarla

### Cómo Presentarla:

1. Ejecuta `streamlit run app_streamlit.py` antes de presentar
2. Comparte tu pantalla mostrando el navegador
3. Navega por las diferentes secciones
4. Demuestra los filtros interactivos
5. Agrega un producto en vivo
6. Muestra las estadísticas actualizadas

---

## 🚀 Próximos Pasos (Extensiones Posibles)

- 📊 **Más gráficos**: Añadir Plotly para gráficos 3D
- 📈 **Tendencias**: Análisis temporal si agregas fechas
- 🤖 **ML**: Predicción de demanda
- 👥 **Multi-usuario**: Sistema de autenticación
- 📱 **App móvil**: Versión PWA
- 🔔 **Notificaciones**: Emails cuando stock bajo
- 📄 **Reportes**: Generar PDFs automáticos
- 🌐 **API**: Backend REST separado

---

## 📚 Recursos de Aprendizaje

- [Documentación oficial de Streamlit](https://docs.streamlit.io/)
- [Galería de apps de Streamlit](https://streamlit.io/gallery)
- [Cheat sheet de Streamlit](https://docs.streamlit.io/library/cheatsheet)
- [Pandas documentation](https://pandas.pydata.org/docs/)

---

## ✅ Checklist Pre-Presentación

- [ ] Streamlit instalado (`pip list | grep streamlit`)
- [ ] Pandas instalado (`pip list | grep pandas`)
- [ ] CSV en la misma carpeta que app_streamlit.py
- [ ] App ejecutándose sin errores
- [ ] Navegador abierto en localhost:8501
- [ ] Has probado todas las páginas
- [ ] Has probado agregar un producto
- [ ] Has probado actualizar stock
- [ ] Internet conectado (Streamlit descarga recursos)

---

**🎉 ¡Tu aplicación web está lista para impresionar! ⚔️**

**Ejecuta:** `streamlit run app_streamlit.py` **y explora tu tienda en el navegador.**

---

**Proyecto:** Tienda Aurelion - Sistema de Gestión  
**Autor:** Martos Ludmila  
**DNI:** 34811650  
**Sprint:** 1 - Introducción a la IA  
**Institución:** IBM  
**Versión:** 1.0 (Web Edition)

