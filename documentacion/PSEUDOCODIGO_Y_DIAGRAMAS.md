# 📐 PSEUDOCÓDIGO Y DIAGRAMAS - TIENDA AURELION

## 📋 Índice
1. [Algoritmo Principal](#algoritmo-principal)
2. [Funciones de Carga y Guardado](#funciones-de-carga-y-guardado)
3. [Funciones de Búsqueda](#funciones-de-búsqueda)
4. [Funciones de Gestión](#funciones-de-gestión)
5. [Diagramas de Flujo](#diagramas-de-flujo)

---

## 🔄 Algoritmo Principal

### PSEUDOCÓDIGO DEL PROGRAMA COMPLETO

```
PROGRAMA TiendaAurelion

// ========== CONSTANTES ==========
CONSTANTE ARCHIVO_PRODUCTOS = "datos/productos.csv"
CONSTANTE ARCHIVO_CLIENTES = "datos/clientes.csv"
CONSTANTE ARCHIVO_VENTAS = "datos/ventas.csv"
CONSTANTE ARCHIVO_DETALLE_VENTAS = "datos/detalle_ventas.csv"
CONSTANTE UMBRAL_STOCK_BAJO = 20

// ========== FUNCIÓN PRINCIPAL ==========
FUNCIÓN main()
    INICIO
        limpiar_pantalla()
        mostrar_banner()
        
        ESCRIBIR "Cargando datos del inventario..."
        productos = cargar_datos()
        
        SI productos está vacío ENTONCES
            ESCRIBIR "❌ No se pudieron cargar los productos"
            TERMINAR
        FIN SI
        
        pausar()
        
        // Bucle principal del menú
        MIENTRAS verdadero HACER
            limpiar_pantalla()
            mostrar_banner()
            mostrar_menu()
            
            opcion = validar_entrada_numerica("Selecciona una opción: ", 0, 10)
            
            SEGÚN opcion SEA:
                CASO 0:
                    ESCRIBIR "¡Gracias por usar Tienda Aurelion!"
                    SALIR del bucle
                CASO 1:
                    listar_todos_productos(productos)
                CASO 2:
                    buscar_por_categoria(productos)
                CASO 3:
                    buscar_por_id(productos)
                CASO 4:
                    buscar_por_nombre(productos)
                CASO 5:
                    buscar_por_rango_precios(productos)
                CASO 6:
                    productos_bajo_stock(productos)
                CASO 7:
                    estadisticas_inventario(productos)
                CASO 8:
                    buscar_por_proveedor(productos)
                CASO 9:
                    agregar_producto(productos)
                CASO 10:
                    actualizar_stock(productos)
            FIN SEGÚN
            
            pausar()
        FIN MIENTRAS
    FIN
FIN FUNCIÓN

// ========== FUNCIONES DE CARGA Y GUARDADO ==========

FUNCIÓN cargar_datos() RETORNA lista_de_diccionarios
    INICIO
        productos = []
        
        INTENTAR
            ABRIR ARCHIVO_CSV PARA LECTURA COMO archivo
                lector_csv = crear_lector_diccionarios(archivo)
                
                PARA cada fila EN lector_csv HACER
                    INTENTAR
                        // Convertir campos numéricos
                        fila['id'] = convertir_a_entero(fila['id'])
                        fila['precio'] = convertir_a_entero(fila['precio'])
                        fila['stock'] = convertir_a_entero(fila['stock'])
                        
                        AGREGAR fila A productos
                    CAPTURAR error_conversion:
                        ESCRIBIR "⚠️ Error al procesar fila"
                        CONTINUAR
                    FIN INTENTAR
                FIN PARA
            CERRAR archivo
            
            ESCRIBIR "✅ Se cargaron", longitud(productos), "productos"
            RETORNAR productos
            
        CAPTURAR archivo_no_encontrado:
            ESCRIBIR "❌ No se encontró el archivo"
            RETORNAR []
        CAPTURAR error_general:
            ESCRIBIR "❌ Error inesperado:", error_general
            RETORNAR []
        FIN INTENTAR
    FIN
FIN FUNCIÓN

FUNCIÓN guardar_datos(productos) RETORNA booleano
    INICIO
        INTENTAR
            SI productos está vacío ENTONCES
                ESCRIBIR "⚠️ No hay productos para guardar"
                RETORNAR falso
            FIN SI
            
            columnas = obtener_claves(productos[0])
            
            ABRIR ARCHIVO_CSV PARA ESCRITURA COMO archivo
                escritor_csv = crear_escritor_diccionarios(archivo, columnas)
                escribir_encabezado()
                
                PARA cada producto EN productos HACER
                    escribir_fila(producto)
                FIN PARA
            CERRAR archivo
            
            ESCRIBIR "✅ Datos guardados correctamente"
            RETORNAR verdadero
            
        CAPTURAR error:
            ESCRIBIR "❌ Error al guardar:", error
            RETORNAR falso
        FIN INTENTAR
    FIN
FIN FUNCIÓN

// ========== FUNCIONES DE VALIDACIÓN ==========

FUNCIÓN validar_entrada_numerica(mensaje, minimo, maximo) RETORNA entero
    INICIO
        MIENTRAS verdadero HACER
            INTENTAR
                valor = convertir_a_entero(LEER_ENTRADA(mensaje))
                
                SI valor < minimo ENTONCES
                    ESCRIBIR "⚠️ El valor debe ser >=", minimo
                    CONTINUAR
                FIN SI
                
                SI maximo NO es nulo Y valor > maximo ENTONCES
                    ESCRIBIR "⚠️ El valor debe ser <=", maximo
                    CONTINUAR
                FIN SI
                
                RETORNAR valor
                
            CAPTURAR error_conversion:
                ESCRIBIR "⚠️ Ingresa un número válido"
            FIN INTENTAR
        FIN MIENTRAS
    FIN
FIN FUNCIÓN

// ========== FUNCIONES DE BÚSQUEDA ==========

FUNCIÓN buscar_por_categoria(productos)
    INICIO
        limpiar_pantalla()
        mostrar_banner()
        ESCRIBIR "🏷️ BUSCAR POR CATEGORÍA"
        
        // Obtener categorías únicas
        categorias = conjunto_vacío()
        PARA cada producto EN productos HACER
            AGREGAR producto['categoria'] A categorias
        FIN PARA
        categorias = ordenar(categorias)
        
        // Mostrar categorías disponibles
        ESCRIBIR "Categorías disponibles:"
        PARA cada categoria EN categorias HACER
            ESCRIBIR "  •", categoria
        FIN PARA
        
        categoria_buscar = LEER_ENTRADA("Ingresa categoría: ")
        categoria_buscar = quitar_espacios(categoria_buscar)
        
        // Buscar productos
        resultados = []
        PARA cada producto EN productos HACER
            SI minusculas(producto['categoria']) == minusculas(categoria_buscar) ENTONCES
                AGREGAR producto A resultados
            FIN SI
        FIN PARA
        
        // Mostrar resultados
        SI resultados NO está vacío ENTONCES
            ESCRIBIR "✅ Se encontraron", longitud(resultados), "productos"
            PARA cada producto EN resultados HACER
                mostrar_producto(producto)
            FIN PARA
        SINO
            ESCRIBIR "❌ No se encontraron productos"
        FIN SI
    FIN
FIN FUNCIÓN

FUNCIÓN buscar_por_id(productos)
    INICIO
        limpiar_pantalla()
        mostrar_banner()
        ESCRIBIR "🆔 BUSCAR POR ID"
        
        id_buscar = validar_entrada_numerica("Ingresa ID: ", 1, nulo)
        
        // Buscar producto
        PARA cada producto EN productos HACER
            SI producto['id'] == id_buscar ENTONCES
                ESCRIBIR "✅ Producto encontrado:"
                mostrar_producto(producto)
                RETORNAR
            FIN SI
        FIN PARA
        
        ESCRIBIR "❌ No se encontró producto con ID", id_buscar
    FIN
FIN FUNCIÓN

FUNCIÓN buscar_por_nombre(productos)
    INICIO
        limpiar_pantalla()
        mostrar_banner()
        ESCRIBIR "📦 BUSCAR POR NOMBRE"
        
        nombre = LEER_ENTRADA("Ingresa nombre a buscar: ")
        nombre = quitar_espacios(minusculas(nombre))
        
        SI nombre está vacío ENTONCES
            ESCRIBIR "⚠️ Debes ingresar un nombre"
            RETORNAR
        FIN SI
        
        // Búsqueda parcial (contiene)
        resultados = []
        PARA cada producto EN productos HACER
            SI nombre ESTÁ_EN minusculas(producto['nombre']) ENTONCES
                AGREGAR producto A resultados
            FIN SI
        FIN PARA
        
        // Mostrar resultados
        SI resultados NO está vacío ENTONCES
            ESCRIBIR "✅ Se encontraron", longitud(resultados), "productos"
            PARA cada producto EN resultados HACER
                mostrar_producto(producto)
            FIN PARA
        SINO
            ESCRIBIR "❌ No se encontraron productos"
        FIN SI
    FIN
FIN FUNCIÓN

FUNCIÓN buscar_por_rango_precios(productos)
    INICIO
        limpiar_pantalla()
        mostrar_banner()
        ESCRIBIR "💰 BUSCAR POR RANGO DE PRECIOS"
        
        precio_min = validar_entrada_numerica("Precio mínimo: ", 0, nulo)
        precio_max = validar_entrada_numerica("Precio máximo: ", precio_min, nulo)
        
        // Filtrar por rango
        resultados = []
        PARA cada producto EN productos HACER
            SI precio_min <= producto['precio'] <= precio_max ENTONCES
                AGREGAR producto A resultados
            FIN SI
        FIN PARA
        
        // Mostrar resultados
        SI resultados NO está vacío ENTONCES
            ESCRIBIR "✅ Se encontraron", longitud(resultados), "productos"
            PARA cada producto EN resultados HACER
                mostrar_producto(producto)
            FIN PARA
        SINO
            ESCRIBIR "❌ No se encontraron productos en ese rango"
        FIN SI
    FIN
FIN FUNCIÓN

FUNCIÓN buscar_por_proveedor(productos)
    INICIO
        limpiar_pantalla()
        mostrar_banner()
        ESCRIBIR "🏪 BUSCAR POR PROVEEDOR"
        
        // Obtener proveedores únicos
        proveedores = conjunto_vacío()
        PARA cada producto EN productos HACER
            AGREGAR producto['proveedor'] A proveedores
        FIN PARA
        proveedores = ordenar(proveedores)
        
        // Mostrar proveedores disponibles
        ESCRIBIR "Proveedores disponibles:"
        PARA cada proveedor EN proveedores HACER
            ESCRIBIR "  •", proveedor
        FIN PARA
        
        proveedor_buscar = LEER_ENTRADA("Ingresa proveedor: ")
        proveedor_buscar = quitar_espacios(proveedor_buscar)
        
        // Buscar productos
        resultados = []
        PARA cada producto EN productos HACER
            SI minusculas(producto['proveedor']) == minusculas(proveedor_buscar) ENTONCES
                AGREGAR producto A resultados
            FIN SI
        FIN PARA
        
        // Mostrar resultados con estadísticas
        SI resultados NO está vacío ENTONCES
            ESCRIBIR "✅ Se encontraron", longitud(resultados), "productos"
            PARA cada producto EN resultados HACER
                mostrar_producto(producto)
            FIN PARA
            
            // Calcular estadísticas del proveedor
            stock_total = 0
            valor_total = 0
            PARA cada producto EN resultados HACER
                stock_total = stock_total + producto['stock']
                valor_total = valor_total + (producto['precio'] * producto['stock'])
            FIN PARA
            
            ESCRIBIR "📊 Estadísticas del proveedor:"
            ESCRIBIR "  • Total productos:", longitud(resultados)
            ESCRIBIR "  • Stock total:", stock_total, "unidades"
            ESCRIBIR "  • Valor total:", valor_total, "monedas"
        SINO
            ESCRIBIR "❌ No se encontraron productos del proveedor"
        FIN SI
    FIN
FIN FUNCIÓN

// ========== FUNCIONES DE ANÁLISIS ==========

FUNCIÓN productos_bajo_stock(productos)
    INICIO
        limpiar_pantalla()
        mostrar_banner()
        ESCRIBIR "⚠️ PRODUCTOS CON BAJO STOCK"
        ESCRIBIR "Umbral:", UMBRAL_STOCK_BAJO, "unidades"
        
        // Filtrar productos con stock bajo
        resultados = []
        PARA cada producto EN productos HACER
            SI producto['stock'] <= UMBRAL_STOCK_BAJO ENTONCES
                AGREGAR producto A resultados
            FIN SI
        FIN PARA
        
        // Ordenar por stock (menor a mayor)
        resultados = ordenar(resultados, POR: 'stock', ASCENDENTE)
        
        // Mostrar resultados
        SI resultados NO está vacío ENTONCES
            ESCRIBIR "⚠️ Se encontraron", longitud(resultados), "productos con stock bajo"
            PARA cada producto EN resultados HACER
                mostrar_producto(producto)
            FIN PARA
            ESCRIBIR "💡 Sugerencia: Contacta proveedores para reabastecer"
        SINO
            ESCRIBIR "✅ ¡Todos los productos tienen stock adecuado!"
        FIN SI
    FIN
FIN FUNCIÓN

FUNCIÓN estadisticas_inventario(productos)
    INICIO
        limpiar_pantalla()
        mostrar_banner()
        ESCRIBIR "📊 ESTADÍSTICAS DEL INVENTARIO"
        
        SI productos está vacío ENTONCES
            ESCRIBIR "⚠️ No hay productos para analizar"
            RETORNAR
        FIN SI
        
        // Variables para estadísticas
        total_productos = longitud(productos)
        stock_total = 0
        valor_total = 0
        suma_precios = 0
        
        categorias = conjunto_vacío()
        proveedores = conjunto_vacío()
        productos_por_categoria = diccionario_vacío()
        
        producto_mas_caro = productos[0]
        producto_mas_barato = productos[0]
        
        // Calcular estadísticas
        PARA cada producto EN productos HACER
            // Sumas
            stock_total = stock_total + producto['stock']
            valor_total = valor_total + (producto['precio'] * producto['stock'])
            suma_precios = suma_precios + producto['precio']
            
            // Conjuntos únicos
            AGREGAR producto['categoria'] A categorias
            AGREGAR producto['proveedor'] A proveedores
            
            // Contar por categoría
            cat = producto['categoria']
            SI cat NO está EN productos_por_categoria ENTONCES
                productos_por_categoria[cat] = 0
            FIN SI
            productos_por_categoria[cat] = productos_por_categoria[cat] + 1
            
            // Producto más caro
            SI producto['precio'] > producto_mas_caro['precio'] ENTONCES
                producto_mas_caro = producto
            FIN SI
            
            // Producto más barato
            SI producto['precio'] < producto_mas_barato['precio'] ENTONCES
                producto_mas_barato = producto
            FIN SI
        FIN PARA
        
        // Calcular promedios
        precio_promedio = suma_precios / total_productos
        stock_promedio = stock_total / total_productos
        
        // Mostrar estadísticas generales
        ESCRIBIR "═══ ESTADÍSTICAS GENERALES ═══"
        ESCRIBIR "📦 Total productos:", total_productos
        ESCRIBIR "🏷️ Categorías únicas:", longitud(categorias)
        ESCRIBIR "🏪 Proveedores únicos:", longitud(proveedores)
        ESCRIBIR "📊 Stock total:", stock_total, "unidades"
        ESCRIBIR "💰 Valor total:", valor_total, "monedas"
        ESCRIBIR "💵 Precio promedio:", precio_promedio, "monedas"
        ESCRIBIR "📈 Stock promedio:", stock_promedio, "unidades"
        
        // Mostrar productos destacados
        ESCRIBIR "═══ PRODUCTOS DESTACADOS ═══"
        ESCRIBIR "💎 Más caro:", producto_mas_caro['nombre']
        ESCRIBIR "   Precio:", producto_mas_caro['precio'], "monedas"
        ESCRIBIR "🎯 Más económico:", producto_mas_barato['nombre']
        ESCRIBIR "   Precio:", producto_mas_barato['precio'], "monedas"
        
        // Mostrar distribución por categoría
        ESCRIBIR "═══ PRODUCTOS POR CATEGORÍA ═══"
        items = ordenar(productos_por_categoria.items(), POR: valor, DESCENDENTE)
        PARA cada (categoria, cantidad) EN items HACER
            barra = repetir("█", cantidad * 3)
            ESCRIBIR categoria, "│", barra, cantidad
        FIN PARA
    FIN
FIN FUNCIÓN

// ========== FUNCIONES DE GESTIÓN ==========

FUNCIÓN agregar_producto(productos)
    INICIO
        limpiar_pantalla()
        mostrar_banner()
        ESCRIBIR "➕ AGREGAR NUEVO PRODUCTO"
        
        // Generar nuevo ID
        SI productos NO está vacío ENTONCES
            nuevo_id = maximo(producto['id'] PARA producto EN productos) + 1
        SINO
            nuevo_id = 1
        FIN SI
        
        ESCRIBIR "🆔 ID asignado:", nuevo_id
        
        // Solicitar datos
        nombre = quitar_espacios(LEER_ENTRADA("📦 Nombre: "))
        SI nombre está vacío ENTONCES
            ESCRIBIR "❌ El nombre no puede estar vacío"
            RETORNAR
        FIN SI
        
        // Mostrar categorías existentes
        categorias = conjunto_vacío()
        PARA cada producto EN productos HACER
            AGREGAR producto['categoria'] A categorias
        FIN PARA
        ESCRIBIR "🏷️ Categorías existentes:"
        PARA cada cat EN ordenar(categorias) HACER
            ESCRIBIR "  •", cat
        FIN PARA
        
        categoria = quitar_espacios(LEER_ENTRADA("🏷️ Categoría: "))
        SI categoria está vacío ENTONCES
            ESCRIBIR "❌ La categoría no puede estar vacía"
            RETORNAR
        FIN SI
        
        precio = validar_entrada_numerica("💰 Precio: ", 1, nulo)
        stock = validar_entrada_numerica("📊 Stock: ", 0, nulo)
        
        descripcion = quitar_espacios(LEER_ENTRADA("📝 Descripción: "))
        SI descripcion está vacío ENTONCES
            ESCRIBIR "❌ La descripción no puede estar vacía"
            RETORNAR
        FIN SI
        
        // Mostrar proveedores existentes
        proveedores = conjunto_vacío()
        PARA cada producto EN productos HACER
            AGREGAR producto['proveedor'] A proveedores
        FIN PARA
        ESCRIBIR "🏪 Proveedores existentes:"
        PARA cada prov EN ordenar(proveedores) HACER
            ESCRIBIR "  •", prov
        FIN PARA
        
        proveedor = quitar_espacios(LEER_ENTRADA("🏪 Proveedor: "))
        SI proveedor está vacío ENTONCES
            ESCRIBIR "❌ El proveedor no puede estar vacío"
            RETORNAR
        FIN SI
        
        // Crear nuevo producto
        nuevo_producto = {
            'id': nuevo_id,
            'nombre': nombre,
            'categoria': categoria,
            'precio': precio,
            'stock': stock,
            'descripcion': descripcion,
            'proveedor': proveedor
        }
        
        // Mostrar confirmación
        ESCRIBIR "═══ CONFIRMAR NUEVO PRODUCTO ═══"
        mostrar_producto(nuevo_producto)
        
        confirmacion = minusculas(LEER_ENTRADA("¿Agregar? (s/n): "))
        
        SI confirmacion == 's' ENTONCES
            AGREGAR nuevo_producto A productos
            SI guardar_datos(productos) ENTONCES
                ESCRIBIR "✅ Producto agregado exitosamente"
            FIN SI
        SINO
            ESCRIBIR "❌ Operación cancelada"
        FIN SI
    FIN
FIN FUNCIÓN

FUNCIÓN actualizar_stock(productos)
    INICIO
        limpiar_pantalla()
        mostrar_banner()
        ESCRIBIR "🔄 ACTUALIZAR STOCK"
        
        id_buscar = validar_entrada_numerica("Ingresa ID: ", 1, nulo)
        
        // Buscar producto
        producto_encontrado = nulo
        PARA cada producto EN productos HACER
            SI producto['id'] == id_buscar ENTONCES
                producto_encontrado = producto
                SALIR del bucle
            FIN SI
        FIN PARA
        
        SI producto_encontrado es nulo ENTONCES
            ESCRIBIR "❌ No se encontró producto con ID", id_buscar
            RETORNAR
        FIN SI
        
        // Mostrar producto actual
        ESCRIBIR "📦 Producto encontrado:"
        mostrar_producto(producto_encontrado)
        
        ESCRIBIR "Stock actual:", producto_encontrado['stock'], "unidades"
        ESCRIBIR "Opciones:"
        ESCRIBIR "  1. Agregar stock (recibir mercancía)"
        ESCRIBIR "  2. Reducir stock (venta)"
        ESCRIBIR "  3. Establecer stock nuevo (inventario)"
        ESCRIBIR "  4. Cancelar"
        
        opcion = validar_entrada_numerica("Opción: ", 1, 4)
        
        SI opcion == 4 ENTONCES
            ESCRIBIR "❌ Operación cancelada"
            RETORNAR
        FIN SI
        
        SEGÚN opcion SEA:
            CASO 1:
                cantidad = validar_entrada_numerica("Cantidad a agregar: ", 1, nulo)
                nuevo_stock = producto_encontrado['stock'] + cantidad
                accion = "agregaron " + cantidad + " unidades"
            CASO 2:
                cantidad = validar_entrada_numerica("Cantidad a reducir: ", 1, producto_encontrado['stock'])
                nuevo_stock = producto_encontrado['stock'] - cantidad
                accion = "redujeron " + cantidad + " unidades"
            CASO 3:
                nuevo_stock = validar_entrada_numerica("Nuevo stock: ", 0, nulo)
                accion = "estableció en " + nuevo_stock + " unidades"
        FIN SEGÚN
        
        // Mostrar confirmación
        ESCRIBIR "═══ CONFIRMAR ACTUALIZACIÓN ═══"
        ESCRIBIR "Stock actual:", producto_encontrado['stock'], "unidades"
        ESCRIBIR "Stock nuevo:", nuevo_stock, "unidades"
        SI nuevo_stock <= UMBRAL_STOCK_BAJO ENTONCES
            ESCRIBIR "⚠️ ADVERTENCIA: Stock bajo"
        FIN SI
        
        confirmacion = minusculas(LEER_ENTRADA("¿Confirmar? (s/n): "))
        
        SI confirmacion == 's' ENTONCES
            producto_encontrado['stock'] = nuevo_stock
            SI guardar_datos(productos) ENTONCES
                ESCRIBIR "✅ Stock actualizado. Se", accion
            FIN SI
        SINO
            ESCRIBIR "❌ Operación cancelada"
        FIN SI
    FIN
FIN FUNCIÓN

// ========== FUNCIONES DE INTERFAZ ==========

FUNCIÓN mostrar_producto(producto, mostrar_indice, indice)
    INICIO
        SI mostrar_indice ENTONCES
            ESCRIBIR "─────────────────"
            ESCRIBIR "Producto #", indice + 1
        FIN SI
        
        ESCRIBIR "─────────────────"
        ESCRIBIR "🆔 ID:", producto['id']
        ESCRIBIR "📦 Nombre:", producto['nombre']
        ESCRIBIR "🏷️ Categoría:", producto['categoria']
        ESCRIBIR "💰 Precio:", producto['precio'], "monedas"
        ESCRIBIR "📊 Stock:", producto['stock'], "unidades", FIN_LÍNEA
        
        SI producto['stock'] <= UMBRAL_STOCK_BAJO ENTONCES
            ESCRIBIR "⚠️ ¡STOCK BAJO!"
        SINO
            ESCRIBIR ""
        FIN SI
        
        ESCRIBIR "📝 Descripción:", producto['descripcion']
        ESCRIBIR "🏪 Proveedor:", producto['proveedor']
        ESCRIBIR "─────────────────"
    FIN
FIN FUNCIÓN

FUNCIÓN mostrar_menu()
    INICIO
        ESCRIBIR "╔══════════════════════════════════════╗"
        ESCRIBIR "║         MENÚ PRINCIPAL               ║"
        ESCRIBIR "╠══════════════════════════════════════╣"
        ESCRIBIR "║ 🔍 CONSULTAS Y BÚSQUEDAS             ║"
        ESCRIBIR "║  1. Listar todos los productos       ║"
        ESCRIBIR "║  2. Buscar por categoría             ║"
        ESCRIBIR "║  3. Buscar por ID                    ║"
        ESCRIBIR "║  4. Buscar por nombre                ║"
        ESCRIBIR "║  5. Buscar por rango de precios      ║"
        ESCRIBIR "║  6. Ver productos con bajo stock     ║"
        ESCRIBIR "║  7. Ver estadísticas del inventario  ║"
        ESCRIBIR "║  8. Buscar por proveedor             ║"
        ESCRIBIR "╠══════════════════════════════════════╣"
        ESCRIBIR "║ ✏️ GESTIÓN DE INVENTARIO             ║"
        ESCRIBIR "║  9. Agregar nuevo producto           ║"
        ESCRIBIR "║ 10. Actualizar stock de producto     ║"
        ESCRIBIR "╠══════════════════════════════════════╣"
        ESCRIBIR "║  0. Salir del sistema                ║"
        ESCRIBIR "╚══════════════════════════════════════╝"
    FIN
FIN FUNCIÓN

FIN PROGRAMA
```

---

## 📊 DIAGRAMAS DE FLUJO

### Diagrama de Flujo Principal

```
                    ┌─────────────────┐
                    │     INICIO      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Limpiar pantalla│
                    │ Mostrar banner  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Cargar datos    │
                    │ desde CSV       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  ¿Cargó datos?  │
                    └────┬────────┬───┘
                      NO │        │ SÍ
                         │        │
                         ▼        ▼
                  ┌──────────┐  ┌──────────────┐
                  │  Error   │  │ Pausar para  │
                  │  Salir   │  │   continuar  │
                  └──────────┘  └──────┬───────┘
                                       │
                    ┌──────────────────┘
                    │
                    ▼
        ┌───────────────────────────┐
        │    Limpiar pantalla       │
        │    Mostrar banner         │
        │    Mostrar menú           │
        └───────────┬───────────────┘
                    │
                    ▼
        ┌───────────────────────────┐
        │  Leer opción (0-10)       │
        └───────────┬───────────────┘
                    │
                    ▼
        ┌───────────────────────────┐
        │    ¿Opción == 0?          │
        └────┬──────────────────┬───┘
          SÍ │                  │ NO
             │                  │
             ▼                  ▼
      ┌──────────┐    ┌─────────────────────┐
      │ Mensaje  │    │ Ejecutar función    │
      │ despedida│    │ según opción:       │
      └────┬─────┘    │ 1-10                │
           │          └──────────┬──────────┘
           │                     │
           │                     ▼
           │          ┌─────────────────────┐
           │          │ Pausar para         │
           │          │ continuar           │
           │          └──────────┬──────────┘
           │                     │
           │                     │
           │          ┌──────────┘
           │          │
           │          └─────┐
           │                │
           ▼                ▼
        ┌──────────────────────┐
        │        FIN           │
        └──────────────────────┘
```

### Diagrama de Flujo: Cargar Datos

```
      ┌─────────────────┐
      │  cargar_datos() │
      └────────┬────────┘
               │
               ▼
      ┌─────────────────┐
      │ productos = []  │
      └────────┬────────┘
               │
               ▼
      ┌─────────────────┐
      │ Intentar abrir  │
      │   archivo CSV   │
      └────┬───────┬────┘
     ERROR │       │ OK
           │       │
           ▼       ▼
      ┌────────┐ ┌────────────────┐
      │Archivo │ │Crear lector    │
      │no      │ │DictReader      │
      │existe  │ └────────┬───────┘
      └───┬────┘          │
          │               ▼
          │      ┌────────────────┐
          │      │ Para cada fila │
          │      │   en archivo   │
          │      └────────┬───────┘
          │               │
          │               ▼
          │      ┌────────────────┐
          │      │ Intentar       │
          │      │ convertir id,  │
          │      │ precio, stock  │
          │      │ a entero       │
          │      └────┬─────┬─────┘
          │     ERROR │     │ OK
          │           │     │
          │           ▼     ▼
          │      ┌────────┐ ┌────────┐
          │      │Continuar│ │Agregar │
          │      │siguiente│ │a lista │
          │      └────────┘ └───┬────┘
          │                     │
          │      ┌──────────────┘
          │      │
          │      ▼
          │  ┌────────────────┐
          │  │ ¿Más filas?    │
          │  └───┬────────┬───┘
          │   NO │        │ SÍ
          │      │        │
          │      │        └──────┐
          │      │               │
          │      ▼               │
          │  ┌────────────┐     │
          │  │Cerrar      │     │
          │  │archivo     │     │
          │  └─────┬──────┘     │
          │        │             │
          ├────────┘             │
          │                      │
          ▼                      │
      ┌────────────┐             │
      │  Mostrar   │◄────────────┘
      │  mensaje   │
      └─────┬──────┘
            │
            ▼
      ┌────────────┐
      │  Retornar  │
      │  productos │
      └────────────┘
```

### Diagrama de Flujo: Buscar por Categoría

```
   ┌────────────────────────┐
   │ buscar_por_categoria() │
   └───────────┬────────────┘
               │
               ▼
   ┌────────────────────────┐
   │ Limpiar pantalla       │
   │ Mostrar banner         │
   └───────────┬────────────┘
               │
               ▼
   ┌────────────────────────┐
   │ Obtener categorías     │
   │ únicas de productos    │
   └───────────┬────────────┘
               │
               ▼
   ┌────────────────────────┐
   │ Ordenar categorías     │
   └───────────┬────────────┘
               │
               ▼
   ┌────────────────────────┐
   │ Mostrar lista de       │
   │ categorías disponibles │
   └───────────┬────────────┘
               │
               ▼
   ┌────────────────────────┐
   │ Leer categoría a       │
   │ buscar del usuario     │
   └───────────┬────────────┘
               │
               ▼
   ┌────────────────────────┐
   │ resultados = []        │
   └───────────┬────────────┘
               │
               ▼
   ┌────────────────────────┐
   │ Para cada producto     │
   └───────────┬────────────┘
               │
               ▼
   ┌────────────────────────┐
   │ ¿Categoría coincide?   │
   │ (ignora mayúsculas)    │
   └────┬───────────────┬───┘
     NO │               │ SÍ
        │               │
        │               ▼
        │      ┌────────────────┐
        │      │ Agregar a      │
        │      │ resultados     │
        │      └────────┬───────┘
        │               │
        └───────┬───────┘
                │
                ▼
   ┌────────────────────────┐
   │ ¿Más productos?        │
   └───┬────────────────┬───┘
    NO │                │ SÍ
       │                │
       │                └──────┐
       │                       │
       ▼                       │
   ┌────────────────────┐     │
   │ ¿resultados vacío? │     │
   └───┬────────────┬───┘     │
    NO │            │ SÍ      │
       │            │          │
       ▼            ▼          │
┌──────────┐ ┌──────────┐     │
│ Mostrar  │ │ Mostrar  │     │
│resultados│ │  error   │     │
└──────────┘ └──────────┘     │
       │            │          │
       └─────┬──────┘          │
             │                 │
             ▼                 │
      ┌──────────┐             │
      │    FIN   │◄────────────┘
      └──────────┘
```

### Diagrama de Flujo: Agregar Producto

```
   ┌────────────────────┐
   │ agregar_producto() │
   └─────────┬──────────┘
             │
             ▼
   ┌────────────────────┐
   │ Limpiar pantalla   │
   │ Mostrar banner     │
   └─────────┬──────────┘
             │
             ▼
   ┌────────────────────┐
   │ Generar nuevo ID   │
   │ (máximo ID + 1)    │
   └─────────┬──────────┘
             │
             ▼
   ┌────────────────────┐
   │ Mostrar ID asignado│
   └─────────┬──────────┘
             │
             ▼
   ┌────────────────────┐
   │ Leer nombre        │
   └─────────┬──────────┘
             │
             ▼
   ┌────────────────────┐
   │ ¿Nombre vacío?     │
   └───┬────────────┬───┘
    SÍ │            │ NO
       │            │
       ▼            ▼
   ┌───────┐  ┌──────────────┐
   │ Error │  │ Mostrar      │
   │Salir  │  │ categorías   │
   └───────┘  │ existentes   │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │ Leer         │
              │ categoría    │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │ ¿Vacío?      │
              └──┬─────────┬─┘
             SÍ │         │ NO
                │         │
                ▼         ▼
           ┌───────┐ ┌─────────┐
           │ Error │ │ Validar │
           │Salir  │ │ precio  │
           └───────┘ └────┬────┘
                          │
                          ▼
                     ┌─────────┐
                     │ Validar │
                     │ stock   │
                     └────┬────┘
                          │
                          ▼
                     ┌─────────┐
                     │  Leer   │
                     │descrip. │
                     └────┬────┘
                          │
                          ▼
                     ┌─────────┐
                     │¿Vacío?  │
                     └──┬────┬─┘
                    SÍ │    │ NO
                       │    │
                       ▼    ▼
                  ┌──────┐ ┌──────────┐
                  │Error │ │ Mostrar  │
                  │Salir │ │proveedores│
                  └──────┘ └─────┬────┘
                                 │
                                 ▼
                            ┌─────────┐
                            │  Leer   │
                            │proveedor│
                            └────┬────┘
                                 │
                                 ▼
                            ┌─────────┐
                            │ ¿Vacío? │
                            └──┬────┬─┘
                           SÍ │    │ NO
                              │    │
                              ▼    ▼
                         ┌──────┐ ┌──────────┐
                         │Error │ │  Crear   │
                         │Salir │ │diccionario│
                         └──────┘ │  nuevo   │
                                  │ producto │
                                  └─────┬────┘
                                        │
                                        ▼
                                  ┌──────────┐
                                  │ Mostrar  │
                                  │ producto │
                                  │confirmar │
                                  └─────┬────┘
                                        │
                                        ▼
                                  ┌──────────┐
                                  │¿Confirma?│
                                  │  (s/n)   │
                                  └──┬────┬──┘
                                 NO │    │ SÍ
                                    │    │
                                    │    ▼
                                    │ ┌──────────┐
                                    │ │ Agregar a│
                                    │ │  lista   │
                                    │ └────┬─────┘
                                    │      │
                                    │      ▼
                                    │ ┌──────────┐
                                    │ │ Guardar  │
                                    │ │   CSV    │
                                    │ └────┬─────┘
                                    │      │
                                    │      ▼
                                    │ ┌──────────┐
                                    │ │ Mensaje  │
                                    │ │  éxito   │
                                    │ └────┬─────┘
                                    │      │
                                    ▼      ▼
                              ┌──────────────┐
                              │ Mensaje      │
                              │ cancelación  │
                              └──────┬───────┘
                                     │
                                     ▼
                              ┌──────────┐
                              │   FIN    │
                              └──────────┘
```

### Diagrama de Flujo: Estadísticas

```
   ┌───────────────────────┐
   │estadisticas_inventario│
   └──────────┬────────────┘
              │
              ▼
   ┌──────────────────────┐
   │ Limpiar pantalla     │
   │ Mostrar banner       │
   └──────────┬───────────┘
              │
              ▼
   ┌──────────────────────┐
   │ ¿productos vacío?    │
   └───┬──────────────┬───┘
    SÍ │              │ NO
       │              │
       ▼              ▼
   ┌───────┐  ┌──────────────────┐
   │Error  │  │ Inicializar      │
   │Salir  │  │ variables:       │
   └───────┘  │ • total = 0      │
              │ • stock_tot = 0  │
              │ • valor_tot = 0  │
              │ • suma_prec = 0  │
              │ • categorias = {}│
              │ • proveedores={}│
              └────────┬─────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Para cada       │
              │ producto        │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Acumular sumas: │
              │ • stock_total   │
              │ • valor_total   │
              │ • suma_precios  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Agregar a sets: │
              │ • categorías    │
              │ • proveedores   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Contar productos│
              │ por categoría   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Identificar:    │
              │ • más caro      │
              │ • más barato    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ ¿Más productos? │
              └───┬─────────┬───┘
               NO │         │ SÍ
                  │         │
                  │         └────┐
                  │              │
                  ▼              │
          ┌────────────────┐    │
          │ Calcular       │    │
          │ promedios:     │    │
          │ • precio       │    │
          │ • stock        │    │
          └────────┬───────┘    │
                   │             │
                   ▼             │
          ┌────────────────┐    │
          │ Mostrar:       │    │
          │ • Generales    │    │
          │ • Destacados   │    │
          │ • Por categoría│    │
          └────────┬───────┘    │
                   │             │
                   ▼             │
            ┌──────────┐         │
            │   FIN    │◄────────┘
            └──────────┘
```

---

## 🔑 Conceptos Clave del Algoritmo

### 1. **Estructuras de Datos Utilizadas**
- **Lista (Array)**: Para almacenar la colección de productos
- **Diccionario (Hash Map)**: Para representar cada producto con sus atributos
- **Conjunto (Set)**: Para obtener valores únicos (categorías, proveedores)

### 2. **Algoritmos de Búsqueda**
- **Búsqueda lineal**: Recorre toda la lista para encontrar coincidencias
- **Filtrado**: Crea sublistas según criterios específicos
- **Búsqueda parcial**: Usa operador `in` para coincidencias de substring

### 3. **Algoritmos de Ordenamiento**
- **Ordenamiento por clave**: Ordena productos según un campo específico
- **Ordenamiento ascendente/descendente**: Para stock, precios, etc.

### 4. **Complejidad Temporal**
- Carga de datos: **O(n)** donde n = número de productos
- Búsqueda lineal: **O(n)**
- Estadísticas: **O(n)**
- Ordenamiento: **O(n log n)**

### 5. **Validaciones Implementadas**
- ✅ Validación de tipos de datos (enteros, strings)
- ✅ Validación de rangos (precio mínimo/máximo)
- ✅ Validación de campos vacíos
- ✅ Validación de existencia de archivos
- ✅ Manejo de excepciones (try-except)

### 6. **Persistencia de Datos**
- Lectura desde CSV al iniciar
- Escritura a CSV después de modificaciones
- Formato CSV para portabilidad

---

## 📈 Flujo de Datos

```
┌──────────────┐
│ Archivo CSV  │
│tienda_aurelion│
└──────┬───────┘
       │
       │ cargar_datos()
       ▼
┌─────────────────┐
│ Lista Python    │
│ [producto1,     │
│  producto2, ... │
│  productoN]     │
└────────┬────────┘
         │
         ├──────────────┬──────────────┬──────────────┐
         │              │              │              │
         ▼              ▼              ▼              ▼
    ┌────────┐    ┌────────┐    ┌────────┐    ┌────────┐
    │Buscar  │    │Agregar │    │Analizar│    │Actualizar│
    └────┬───┘    └───┬────┘    └───┬────┘    └───┬────┘
         │            │              │             │
         └────────────┴──────────────┴─────────────┘
                      │
                      │ guardar_datos()
                      ▼
              ┌──────────────┐
              │ Archivo CSV  │
              │ actualizado  │
              └──────────────┘
```

---

Este documento proporciona el pseudocódigo completo y los diagramas de flujo necesarios para entender la lógica del programa Tienda Aurelion.

---

**👨‍💻 Autor:** Martos Ludmila  
**📋 DNI:** 34811650  
**🏢 Institución:** IBM  
**📅 Sprint:** 1 - Introducción a la Inteligencia Artificial  
**📆 Año:** 2025

