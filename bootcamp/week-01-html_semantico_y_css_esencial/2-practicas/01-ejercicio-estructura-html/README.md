# Ejercicio 01: Estructura HTML Semántica

## 🎯 Objetivo

Transformar una página estructurada con `div`s genéricos en una página con HTML5 semántico correcto, mejorando accesibilidad y claridad del código.

---

## 🛠️ Configuración

No necesitas ninguna instalación. Solo un browser y VS Code.

1. Abre `starter/index.html` en VS Code
2. Abre también el archivo en tu browser (arrastra el archivo al browser o usa Live Server)
3. Sigue los pasos del ejercicio

---

## 📋 Instrucciones

### Paso 1: Estructura Base del Documento

Toda página web válida comienza con esta estructura mínima:

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Título de la Página</title>
  </head>
  <body>
    <!-- Contenido aquí -->
  </body>
</html>
```

- `<!DOCTYPE html>` — Le dice al browser que este es HTML5
- `lang="es"` — El idioma del documento (crucial para lectores de pantalla y SEO)
- `charset="UTF-8"` — Soporta caracteres especiales (ñ, á, é, etc.)
- `viewport` — Necesario para responsive design

**Abre `starter/index.html`** y observa que la estructura base ya está configurada. Descomenta el **bloque 1** para agregar la meta description.

---

### Paso 2: Header y Navegación

El encabezado de página va dentro de `<header>`. La navegación principal va dentro de `<nav>`:

```html
<header>
  <a href="/" class="logo">Mi Sitio</a>
  <nav aria-label="Navegación principal">
    <ul>
      <li><a href="/" aria-current="page">Inicio</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/contacto">Contacto</a></li>
    </ul>
  </nav>
</header>
```

- `<header>` — Encabezado: puede estar en la página o dentro de `<article>`
- `<nav>` — Navegación: agrupa links de navegación
- `aria-label="Navegación principal"` — Identifica esta nav si hay varias en la página
- `aria-current="page"` — Indica el enlace activo a lectores de pantalla

**Descomenta el bloque 2** en el starter.

---

### Paso 3: Contenido Principal

El contenido principal va dentro de `<main>`. Solo debe haber **uno por página**:

```html
<main>
  <section aria-labelledby="noticias-titulo">
    <h2 id="noticias-titulo">Últimas Noticias</h2>

    <article>
      <h3><a href="/blog/post-1">Título del artículo</a></h3>
      <p>Resumen del artículo...</p>
      <a href="/blog/post-1">Leer más sobre Título del artículo</a>
    </article>

  </section>
</main>
```

- `<main>` — Contenido principal, único en la página
- `<section>` + `aria-labelledby` — Sección temática accesible
- `<article>` — Contenido autónomo: este post puede ir en RSS o newsletter
- El enlace "Leer más" es descriptivo (no solo "haz clic aquí")

**Descomenta el bloque 3** en el starter.

---

### Paso 4: Sidebar (Aside)

El contenido complementario (sidebar, advertencias, info relacionada) va en `<aside>`:

```html
<aside aria-label="Artículos relacionados">
  <h3>También te puede interesar</h3>
  <ul>
    <li><a href="/blog/post-2">Otro artículo interesante</a></li>
    <li><a href="/blog/post-3">Y otro más aquí</a></li>
  </ul>
</aside>
```

- `<aside>` es contenido _tangencialmente_ relacionado con el contenido principal
- Puede estar dentro de `<main>` o fuera (sidebar de toda la página)

**Descomenta el bloque 4** en el starter.

---

### Paso 5: Footer y Accesibilidad Final

El pie de página va en `<footer>`. Añade los toques finales de accesibilidad:

```html
<footer>
  <nav aria-label="Links de pie de página">
    <ul>
      <li><a href="/privacidad">Privacidad</a></li>
      <li><a href="/terminos">Términos</a></li>
    </ul>
  </nav>
  <address>
    <a href="mailto:hola@misitio.com">hola@misitio.com</a>
  </address>
  <p><small>&copy; 2026 Mi Sitio. Todos los derechos reservados.</small></p>
</footer>
```

**Descomenta el bloque 5** en el starter.

---

## ✅ Resultado Esperado

Al finalizar, tu página debe:

- Tener estructura semántica completa: `header > nav`, `main > section > article`, `aside`, `footer`
- Pasar la validación en [validator.w3.org](https://validator.w3.org/)
- Navegarse correctamente con solo el teclado (`Tab` para avanzar, `Shift+Tab` para retroceder)
- Al usar un lector de pantalla (o el modo de lectura del browser), la estructura debe ser coherente

---

## 💡 Para Reflexionar

- ¿Puedes navegar toda la página solo con `Tab` y `Enter`?
- Abre DevTools → Elements y verifica que la estructura semántica es correcta
- Intenta ejecutar [axe DevTools](https://www.deque.com/axe/devtools/) o [WAVE](https://wave.webaim.org/) para auditar accesibilidad
