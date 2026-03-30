# Ejercicio 04 — shadcn/ui: Composición de Componentes

## 🎯 Objetivo

Usar los patrones de shadcn/ui con HTML y Tailwind puro (sin la CLI por ahora), entendiendo el sistema de CSS variables de temas, el helper `cn()`, y la composición de componentes accesibles.

---

## 🛠️ Qué vas a construir

Una página de dashboard de portfolio con cuatro bloques replicando los patrones de shadcn/ui:
1. CSS variables del sistema de temas (light/dark) como lo hace shadcn
2. Componente Button con variantes usando `cn()` (replicando `button.tsx` de shadcn)
3. Composición de Card con sub-componentes: `CardHeader`, `CardContent`, `CardFooter`
4. Dialog/Modal accesible con overlay, focus trap simulado y teclado Escape

> 💡 Este ejercicio replica los patrones de shadcn/ui con HTML puro. En un proyecto real usarías la CLI y los componentes serían React+TypeScript. Los patrones son idénticos.

---

## 📁 Estructura

```
04-ejercicio-shadcn/
├── README.md
└── starter/
    └── index.html       ← Abre este archivo
```

---

## 📋 Instrucciones por Bloque

---

### 🔵 BLOQUE 1 — Sistema de CSS variables de shadcn

**Concepto**: shadcn/ui usa CSS variables semánticas (`--background`, `--foreground`, `--primary`, etc.) en lugar de clases de color directas. Al cambiar `dark`, las variables cambian automáticamente.

```css
/* Variables del tema light */
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
  --muted: 210 40% 96.1%;
  --border: 214.3 31.8% 91.4%;
  --ring: 222.2 84% 4.9%;
}

/* Dark mode: solo redefinimos las variables */
.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  --primary: 210 40% 98%;
}
```

```html
<!-- Uso en Tailwind con clases arbitrarias que referencian las vars -->
<div class="bg-[hsl(var(--background))] text-[hsl(var(--foreground))]">
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 1.

---

### 🔵 BLOQUE 2 — Componente Button con variantes (patrón shadcn)

**Concepto**: shadcn/ui usa `cva` (class-variance-authority) para variantes. Aquí lo replicamos con un mapa de variantes y `cn()`.

```javascript
// Replica del buttonVariants de shadcn/ui
const base = [
  'inline-flex items-center justify-center whitespace-nowrap',
  'rounded-md text-sm font-medium',
  'transition-colors duration-200',
  'outline-none focus-visible:ring-2 focus-visible:ring-offset-2',
  'disabled:pointer-events-none disabled:opacity-50',
].join(' ')

const variants = {
  default:     'bg-primary text-primary-foreground hover:bg-primary/90',
  destructive: 'bg-destructive text-destructive-foreground hover:bg-destructive/90',
  outline:     'border border-input bg-background hover:bg-accent hover:text-accent-foreground',
  secondary:   'bg-secondary text-secondary-foreground hover:bg-secondary/80',
  ghost:       'hover:bg-accent hover:text-accent-foreground',
  link:        'text-primary underline-offset-4 hover:underline',
}
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 2.

---

### 🔵 BLOQUE 3 — Card compuesto (CardHeader, CardContent, CardFooter)

**Concepto**: shadcn/ui usa sub-componentes para Cards. Cada sub-componente tiene sus clases base y acepta `className` para override usando `cn()`.

```html
<!-- Estructura de Card de shadcn/ui -->
<div class="rounded-xl border border-border bg-card text-card-foreground shadow-sm">
  <!-- CardHeader -->
  <div class="flex flex-col space-y-1.5 p-6">
    <h3 class="font-semibold leading-none tracking-tight">Título</h3>
    <p class="text-sm text-muted-foreground">Descripción</p>
  </div>
  <!-- CardContent -->
  <div class="p-6 pt-0">
    Contenido principal
  </div>
  <!-- CardFooter -->
  <div class="flex items-center p-6 pt-0 gap-2">
    <button>Acción</button>
  </div>
</div>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 3.

---

### 🔵 BLOQUE 4 — Dialog/Modal accesible

**Concepto**: shadcn/ui usa Radix UI para accesibilidad en modales (ARIA, foco, Escape). Aquí replicamos los estilos y el comportamiento básico con el elemento `<dialog>` nativo que ya incluye accesibilidad del browser.

```html
<!-- Dialog nativo — accesible out of the box -->
<dialog id="project-dialog" class="
  fixed inset-0 z-50 m-auto
  w-full max-w-lg rounded-xl border border-border
  bg-background text-foreground shadow-xl p-0
  backdrop:bg-black/60 backdrop:backdrop-blur-sm
">
  <div class="p-6">
    <!-- DialogHeader -->
    <div class="mb-4">
      <h2 class="text-lg font-semibold">Detalles del proyecto</h2>
      <p class="text-sm text-muted-foreground mt-1">Portfolio personal con Next.js</p>
    </div>
    <!-- DialogContent -->
    <div class="space-y-3 text-sm text-muted-foreground">
      Descripción detallada del proyecto...
    </div>
    <!-- DialogFooter -->
    <div class="flex justify-end gap-3 mt-6">
      <button onclick="document.getElementById('project-dialog').close()"
              class="btn-outline-style">Cancelar</button>
      <button class="btn-primary-style">Ver en GitHub</button>
    </div>
  </div>
</dialog>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 4.

---

## ✅ Checklist de Verificación

- [ ] BLOQUE 1: Las CSS variables cambian todos los colores al activar dark mode
- [ ] BLOQUE 2: Cada variante de Button tiene estilo visualmente distinto y correcto
- [ ] BLOQUE 3: Grid de 3 Cards con header, contenido y footer alineados consistentemente
- [ ] BLOQUE 4: Modal abre con botón, cierra con Escape o botón Cancelar, overlay oscuro visible
