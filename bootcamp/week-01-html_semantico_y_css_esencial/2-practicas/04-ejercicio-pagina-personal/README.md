# Ejercicio 04: Página Personal

## 🎯 Objetivo

Integrar todos los conceptos de la semana — HTML semántico, box model, cascade, especificidad y unidades — en una página personal completa.

---

## 🛠️ Configuración

1. Abre `starter/index.html` en VS Code y en el browser
2. Sigue los pasos descomentando los bloques
3. Personaliza el contenido con tu nombre, descripción y skills

---

## 📋 Instrucciones

### Paso 1: Header con Perfil

El header de una página personal típica tiene: nombre, título profesional y navegación:

```html
<header>
  <div class="container">
    <div class="profile">
      <img src="..." alt="Foto de perfil de [Tu Nombre]" class="avatar" />
      <div>
        <h1>Tu Nombre</h1>
        <p>Frontend Developer</p>
      </div>
    </div>
    <nav>...</nav>
  </div>
</header>
```

**Descomenta el bloque 1** y personaliza con tu nombre y título.

---

### Paso 2: Sección About

Usa `<section>` con `aria-labelledby` para la sección "Sobre mí":

```html
<section aria-labelledby="about-title">
  <h2 id="about-title">Sobre Mí</h2>
  <p>
    Soy desarrollador frontend con pasión por...
  </p>
</section>
```

**Descomenta el bloque 2** y escribe tu descripción personal.

---

### Paso 3: Sección Skills/Skills

Una sección de habilidades con una lista descriptiva:

```html
<section>
  <h2>Habilidades</h2>
  <ul>
    <li>
      <strong>HTML/CSS</strong>
      <span>Semántico, accesible, responsive</span>
    </li>
  </ul>
</section>
```

**Descomenta el bloque 3** y ajusta tus skills.

---

### Paso 4: Sección Proyectos con Cards

Los proyectos se muestran como `<article>` dentro de una `<section>`:

```html
<section>
  <h2>Proyectos</h2>

  <article class="project-card">
    <h3><a href="#">Nombre del Proyecto</a></h3>
    <p>Descripción breve del proyecto...</p>
    <footer>
      <ul>
        <li>HTML</li>
        <li>CSS</li>
      </ul>
    </footer>
  </article>
</section>
```

**Descomenta el bloque 4** y escribe tus proyectos (pueden ser inventados o reales).

---

### Paso 5: Footer con Contacto

El pie de página con información de contacto:

```html
<footer>
  <address>
    <a href="mailto:tu@email.com">tu@email.com</a>
    <a href="https://github.com/tu-usuario">GitHub</a>
    <a href="https://linkedin.com/in/tu-perfil">LinkedIn</a>
  </address>
</footer>
```

**Descomenta el bloque 5** y añade tus links reales (o inventados para el ejercicio).

---

## ✅ Lista de Verificación Final

Antes de dar el ejercicio por terminado:

- [ ] HTML completamente semántico: `header`, `nav`, `main`, `section`, `article`, `footer`
- [ ] `lang="es"` en el `<html>`
- [ ] La imagen de avatar tiene `alt` descriptivo
- [ ] Los enlaces de contacto son descriptivos (no "haz clic aquí")
- [ ] CSS usando `rem` para tipografía y `box-sizing: border-box` global
- [ ] El diseño no tiene overflow no intencionado
- [ ] La página es navegable con solo el teclado

---

## 💡 Desafío Extra

Si terminas antes de tiempo:

1. Agrega una `<time>` con la fecha de "última actualización" en el footer
2. Agrega `aria-current="page"` al enlace activo en la navegación
3. Asegúrate de que el contraste de colores sea WCAG AA (ratio 4.5:1) usando [coolors contrast checker](https://coolors.co/contrast-checker)
