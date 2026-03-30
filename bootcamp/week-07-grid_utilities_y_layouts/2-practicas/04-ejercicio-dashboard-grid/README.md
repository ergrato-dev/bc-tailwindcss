# Ejercicio 04: Dashboard con Grid

## 🎯 Objetivo

Construir un dashboard de métricas donde los widgets tienen diferentes tamaños usando `col-span-*` y `row-span-*` en un grid de 6 columnas, demostrando el poder de Grid para layouts complejos.

---

## 📋 Instrucciones

### Paso 1: Grid de stat widgets iguales

Descomenta el **bloque 1** para ver 4 widgets de estadísticas (`col-span-3` cada uno en un grid de 6, equivalente a 2 columnas) con el patrón interno Flex para icono + número + label.

### Paso 2: Widgets de diferentes tamaños

Descomenta el **bloque 2** para ver widgets con tamaños variados: un gráfico principal que ocupa `col-span-4` y otros widgets en `col-span-2`. Este es el layout clásico de dashboards de analytics.

### Paso 3: Widget con `row-span-2` (tabla lateral)

Descomenta el **bloque 3** para ver cómo `row-span-2` permite que una tabla de actividad reciente ocupe 2 filas, mientras que a su izquierda hay 2 widgets apilados verticalmente.

### Paso 4: Dashboard completo responsive

Descomenta el **bloque 4** para ver el dashboard completo: `grid-cols-1` en mobile (todos apilados), `md:grid-cols-4` en tablet, `lg:grid-cols-6` en desktop con todos los `col-span-*` y `row-span-*` activados.

---

## ✅ Verificación

- El bloque 1 muestra 4 stat widgets en 2 columnas
- El bloque 2 muestra el gráfico principal más grande que los widgets secundarios
- El bloque 3 muestra la tabla de actividad ocupando 2 filas verticalmente
- El bloque 4 es completamente responsive y en desktop muestra el layout complejo de 6 columnas
