# Ejercicio 01 — React + Tailwind con clases condicionales

## 🎯 Objetivo

Aprender a usar TailwindCSS dentro de un proyecto React con el CDN, manejar `className` en JSX, implementar clases condicionales y construir un componente `Button` reutilizable con variantes usando el helper `cn()`.

---

## 🛠️ Qué vas a construir

Una página de demostración interactiva en React (via CDN) con cuatro bloques:
1. El uso correcto de `className` vs `class` en JSX
2. Clases condicionales con ternarios y `clsx`
3. Componente `Button` con variantes `primary/secondary/danger/ghost` y tamaños `sm/md/lg`
4. Dark mode funcional con estado de React

---

## 📁 Estructura

```
01-ejercicio-react-tailwind/
├── README.md
└── starter/
    └── index.html       ← Abre este archivo
```

---

## 📋 Instrucciones por Bloque

Abre `starter/index.html` y descomenta cada bloque siguiendo los pasos.

> 💡 En este ejercicio usamos React via CDN con Babel para no requerir un bundler. Los conceptos aplican igual en un proyecto real con Vite.

---

### 🔵 BLOQUE 1 — `className` en JSX

**Concepto**: JSX requiere `className` en lugar de `class`. Es el error más común al empezar con React y Tailwind.

```jsx
// ❌ Incorrecto en JSX — genera un warning de React
<div class="flex items-center gap-4">

// ✅ Correcto en JSX
<div className="flex items-center gap-4">
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 1.

---

### 🔵 BLOQUE 2 — Clases condicionales

**Concepto**: En React necesitamos construir `className` dinámicamente según el estado del componente. El helper `cn()` (o `clsx`) es la solución estándar.

```jsx
// Patrón con ternario básico
const isActive = true
<div className={`px-4 py-2 rounded ${isActive ? 'bg-sky-500 text-white' : 'bg-gray-100 text-gray-700'}`} />

// Patrón con cn() (lo implementamos simple aquí sin tailwind-merge)
function cn(...classes) {
  return classes.filter(Boolean).join(' ')
}

<div className={cn(
  'px-4 py-2 rounded font-medium',
  isActive && 'bg-sky-500 text-white',
  !isActive && 'bg-gray-100 text-gray-700',
)} />
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 2.

---

### 🔵 BLOQUE 3 — Componente Button con variantes

**Concepto**: El patrón más común en React+Tailwind — un componente que acepta una prop `variant` y `size` para controlar sus clases.

```jsx
// Mapa de variantes: SIEMPRE clases completas (purging)
const variants = {
  primary:   'bg-sky-500 text-white hover:bg-sky-600',
  secondary: 'bg-gray-100 text-gray-700 hover:bg-gray-200',
  danger:    'bg-red-500 text-white hover:bg-red-600',
  ghost:     'text-gray-600 hover:bg-gray-100',
}

function Button({ variant = 'primary', size = 'md', className, children, ...props }) {
  return (
    <button className={cn(baseClasses, variants[variant], sizes[size], className)} {...props}>
      {children}
    </button>
  )
}

// Uso:
<Button>Primary</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="danger" size="sm">Eliminar</Button>
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 3.

---

### 🔵 BLOQUE 4 — Dark mode con estado React

**Concepto**: En React el dark mode se maneja con `useState` + `useEffect` para sincronizar con `localStorage` y la clase `dark` del `<html>`.

```jsx
function App() {
  const [isDark, setIsDark] = React.useState(false)

  React.useEffect(() => {
    document.documentElement.classList.toggle('dark', isDark)
    localStorage.setItem('theme', isDark ? 'dark' : 'light')
  }, [isDark])

  return (
    <div className="min-h-screen bg-white dark:bg-gray-950 transition-colors">
      <Button onClick={() => setIsDark(d => !d)}>
        {isDark ? '☀️ Modo claro' : '🌙 Modo oscuro'}
      </Button>
    </div>
  )
}
```

**Abre `starter/index.html`** y descomenta la sección del BLOQUE 4.

---

## ✅ Checklist de Verificación

- [ ] BLOQUE 1: Todos los atributos de clase usan `className`
- [ ] BLOQUE 2: Las clases cambian visualmente al hacer click (estado activo/inactivo)
- [ ] BLOQUE 3: Cada combinación variant+size muestra estilos distintos
- [ ] BLOQUE 4: Toggle cambia todo el fondo de la página + persiste al recargar
