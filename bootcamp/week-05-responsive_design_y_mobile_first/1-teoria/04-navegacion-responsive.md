# 🗺️ Navegación Responsive

## 🎯 Objetivos

- Construir un navbar que se adapta de mobile a desktop
- Implementar el hamburger menu con el checkbox hack de CSS puro
- Entender las estrategias de menú mobile sin JavaScript

---

## 📋 Contenido

![Navbar responsive — mobile con hamburger vs desktop con links](../0-assets/04-navbar-responsive.svg)

### 1. Estructura Base del Navbar

```html
<header class="sticky top-0 z-50 border-b border-gray-100 bg-white/90 backdrop-blur-sm">
  <nav class="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6">

    <!-- Logo -->
    <a href="/" class="text-xl font-black text-gray-900">
      Brand
    </a>

    <!-- Links — ocultos en mobile -->
    <ul class="hidden md:flex items-center gap-8">
      <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Inicio</a></li>
      <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Servicios</a></li>
      <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Precios</a></li>
      <li><a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Blog</a></li>
    </ul>

    <!-- CTA — oculto en mobile pequeño -->
    <div class="hidden md:flex items-center gap-3">
      <a href="#" class="text-sm font-medium text-gray-600 hover:text-gray-900">Ingresar</a>
      <a href="#" class="rounded-lg bg-sky-500 px-4 py-2 text-sm font-semibold text-white hover:bg-sky-600 transition-colors">
        Comenzar gratis
      </a>
    </div>

    <!-- Hamburger — solo visible en mobile -->
    <button class="block md:hidden rounded-lg p-2 text-gray-600 hover:bg-gray-100 transition-colors"
            aria-label="Abrir menú">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
      </svg>
    </button>

  </nav>

  <!-- Mobile menu — requiere JS o checkbox hack para abrir/cerrar -->
  <div class="hidden border-t border-gray-100 px-4 pb-4 pt-2 md:hidden">
    <ul class="space-y-1">
      <li><a href="#" class="block rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Inicio</a></li>
      <li><a href="#" class="block rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Servicios</a></li>
      <li><a href="#" class="block rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Precios</a></li>
      <li><a href="#" class="block rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Blog</a></li>
    </ul>
    <div class="mt-3 border-t border-gray-100 pt-3">
      <a href="#" class="block w-full rounded-lg bg-sky-500 px-4 py-2.5 text-center text-sm font-semibold text-white">
        Comenzar gratis
      </a>
    </div>
  </div>
</header>
```

---

### 2. Checkbox Hack — Menú Mobile sin JavaScript

```html
<!-- El input checkbox es el "estado" del menú -->
<header>
  <!-- Checkbox invisible que guarda el estado abierto/cerrado -->
  <input type="checkbox" id="menu-toggle" class="peer sr-only" />

  <nav class="flex items-center justify-between px-4 py-4">
    <a href="/" class="font-black text-xl">Brand</a>

    <!-- Links desktop -->
    <ul class="hidden md:flex gap-8">
      <li><a href="#">Inicio</a></li>
      <li><a href="#">Servicios</a></li>
    </ul>

    <!-- Label que activa el checkbox (hamburger) -->
    <label for="menu-toggle"
           class="block md:hidden cursor-pointer rounded p-1"
           aria-label="Toggle menú">
      <!-- Icono hamburger -->
      <svg class="w-6 h-6 peer-checked:hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
      </svg>
    </label>
  </nav>

  <!-- Mobile menu — se muestra cuando peer (checkbox) está checked -->
  <!-- hidden por defecto, peer-checked:block cuando el checkbox está marcado -->
  <div class="hidden peer-checked:block md:hidden border-t px-4 pb-4">
    <ul class="space-y-1 pt-2">
      <li><a href="#" class="block py-2 text-gray-700">Inicio</a></li>
      <li><a href="#" class="block py-2 text-gray-700">Servicios</a></li>
    </ul>
  </div>
</header>
```

**Nota:** El `peer` necesita que el checkbox sea un hermano previo del elemento que reacciona. En proyectos con React/Next.js, se usa estado de componente.

---

## ✅ Checklist de Verificación

- [ ] El navbar tiene `sticky top-0 z-50` para que se mantenga visible al hacer scroll
- [ ] Los links usan `hidden md:flex` (ocultos en mobile)
- [ ] El hamburger usa `block md:hidden` (visible solo en mobile)
- [ ] El menú mobile funciona (checkbox hack o JS)
- [ ] Hay `aria-label` en el botón hamburger para accesibilidad
