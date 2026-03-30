# Optimización de Tailwind en Producción

## 🎯 Objetivos

- Entender cómo funciona el purging automático de Tailwind en producción
- Identificar y evitar patrones que impiden el purging correcto
- Usar `tailwind-merge` para evitar conflictos de clases
- Analizar el bundle CSS generado y reducir su tamaño

---

## 1. Cómo funciona el purging en Tailwind v4

En Tailwind v4 el proceso es completamente automático:

```
Modo desarrollo (pnpm dev):  JIT — genera todas las clases bajo demanda → CSS grande
Producción (pnpm build):     Purging — elimina clases no usadas → CSS típico de 5-15KB
```

Tailwind escanea todos los archivos especificados en `content` y **solo incluye las clases que encuentra**:

```javascript
// tailwind.config.js — Tailwind escanea estos archivos
module.exports = {
  content: [
    './index.html',
    './src/**/*.{html,js,jsx,ts,tsx}',
    './components/**/*.{js,jsx,ts,tsx}',
    // Si usas daisyUI también:
    './node_modules/daisyui/dist/**/*.js',
  ],
  // ...
}
```

---

## 2. El error más común: clases dinámicas no purgeables

Tailwind **no puede detectar** clases creadas por concatenación de strings:

```jsx
// ❌ PELIGROSO — Tailwind no puede leer estas clases al hacer el build
// El resultado depende de runtime, no del scan de archivos

const color = 'sky'
const size = 'lg'

<div className={`bg-${color}-500`}>       {/* ← bg-sky-500 NO se detecta */}
<div className={`text-${size}`}>          {/* ← text-lg NO se detecta */}
<button className={`btn-${variant}`}>     {/* ← btn-primary NO detectado */}
```

```jsx
// ✅ CORRECTO — Clases completas en el código fuente

// Opción 1: Mapa de variantes completo
const colors = {
  sky:    'bg-sky-500',    // ← clase completa: detectable
  red:    'bg-red-500',
  green:  'bg-green-500',
}
<div className={colors[color]}>

// Opción 2: Clsx con clases completas
<div className={clsx({
  'bg-sky-500':   color === 'sky',    // ← clase completa: detectable
  'bg-red-500':   color === 'red',
  'bg-green-500': color === 'green',
})}>

// Opción 3: Objecto de variantes (patrón de shadcn/ui)
const variants = {
  primary:   'bg-sky-500 text-white hover:bg-sky-600',
  secondary: 'bg-gray-100 text-gray-700 hover:bg-gray-200',
}
<button className={variants[variant]}>
```

**Regla de oro**: Si la clase Tailwind aparece completa en el código fuente, se incluirá en el build.

---

## 3. `tailwind-merge` — Resolver conflictos en runtime

Cuando tienes componentes que aceptan `className` del exterior, pueden surgir conflictos:

```jsx
// Componente base con p-4
function Card({ className, children }) {
  return (
    <div className={`p-4 rounded-lg bg-white ${className}`}>
      {children}
    </div>
  )
}

// Consumidor quiere p-8 — resultado con template literal:
<Card className="p-8">...</Card>
// className generado: "p-4 rounded-lg bg-white p-8"
// CSS: ambas se aplican — p-4 y p-8 — p-4 gana porque está primero
// 🐛 BUG: el override no funciona
```

```jsx
// Con tailwind-merge solventado
import { twMerge } from 'tailwind-merge'

function Card({ className, children }) {
  return (
    <div className={twMerge('p-4 rounded-lg bg-white', className)}>
      {children}
    </div>
  )
}

// Ahora:
<Card className="p-8">...</Card>
// className generado: "rounded-lg bg-white p-8"
// ✅ p-4 eliminado — p-8 gana correctamente
```

### Casos que resuelve `tailwind-merge`

```javascript
// Padding / margin
twMerge('p-4', 'p-8')          // → 'p-8'
twMerge('px-4 py-2', 'p-8')    // → 'p-8'

// Colores
twMerge('bg-red-500', 'bg-sky-500')  // → 'bg-sky-500'
twMerge('text-sm text-gray-700', 'text-lg')  // → 'text-gray-700 text-lg'

// Flexbox
twMerge('flex flex-col', 'flex-row')  // → 'flex flex-row'
```

---

## 4. Analizar el bundle en producción

```bash
# Generar el build de producción
pnpm build

# Ver el tamaño del CSS generado
ls -lh dist/assets/*.css

# Resultado esperado  con purging correcto:
# index-BxYzK2Aw.css  8.7kB   ← ✅ menos de 15KB es excelente
```

### Con Vite: analizar con `rollup-plugin-visualizer`

```bash
pnpm add -D rollup-plugin-visualizer
```

```javascript
// vite.config.js
import { visualizer } from 'rollup-plugin-visualizer'

export default defineConfig({
  plugins: [
    tailwindcss(),
    visualizer({ open: true, gzipSize: true }),
  ],
})
```

---

## 5. Problemas comunes y soluciones

### El CSS de producción es muy grande (>100KB)

```javascript
// ✅ Verificar que content apunta a los archivos correctos
content: [
  './index.html',
  './src/**/*.{js,jsx,ts,tsx}',  // ← extensiones correctas
  // ❌ No olvidar: si hay archivos HTML extra fuera de src
]
```

### Clases que funcionan en dev pero no en prod

```jsx
// ❌ Este patrón hace que las clases no sean detectadas por Tailwind
const getClass = (type) => `text-${type}-600`  // → 'text-blue-600' no se detecta

// ✅ Mapa de clases completas
const classMap = {
  blue:   'text-blue-600',
  red:    'text-red-600',
  green:  'text-green-600',
}
const getClass = (type) => classMap[type]
```

### CSS variables de Tailwind no funcionan en prod

```css
/* ✅ Asegúrate de que globals.css importa correctamente */
@import "tailwindcss";   /* ← Tailwind v4 */

/* ❌ Sintaxis antigua de v3 — no funciona en v4 */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

## 6. Lazy loading y rendimiento de página completa

```html
<!-- Lazy loading de imágenes — nativo del browser -->
<img src="proyecto.jpg" alt="Proyecto portfolio" loading="lazy" />

<!-- Imágenes con Tailwind: preservar aspecto -->
<div class="aspect-video overflow-hidden rounded-xl">
  <img
    src="cover.jpg"
    alt="Portada del proyecto"
    loading="lazy"
    class="w-full h-full object-cover transition-transform duration-500 hover:scale-105"
  />
</div>
```

```html
<!-- Fuentes: preconnect para Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

---

## 7. Deploy en Vercel (proyecto Next.js)

```bash
# Instalar Vercel CLI
pnpm add -g vercel

# Primer deploy (sigue el wizard)
vercel

# Deploy en producción
vercel --prod
```

### Variables de entorno en Vercel

```bash
# Configurar una variable de entorno de producción
vercel env add NEXT_PUBLIC_API_URL production
```

### Deploy automático desde GitHub

1. Conecta tu repo en **vercel.com/dashboard**
2. Cada push a `main` hace deployment automático
3. Pull requests generan **Preview Deployments** con URL única

---

## ✅ Checklist de Verificación

- [ ] `pnpm build` ejecuta sin errores
- [ ] CSS de producción es menor de 30KB (idealmente <15KB)
- [ ] No hay clases generadas con concatenación de strings
- [ ] Componentes con `className` prop usan `cn()` (tailwind-merge incluido)
- [ ] Imágenes con `loading="lazy"`
- [ ] Proyecto desplegado en Vercel o Netlify

---

## 📚 Recursos

- [TailwindCSS — Content Configuration](https://tailwindcss.com/docs/content-configuration)
- [tailwind-merge en npm](https://www.npmjs.com/package/tailwind-merge)
- [Vercel Deployment Documentation](https://vercel.com/docs)
- [Netlify Deploy Docs](https://docs.netlify.com/site-deploys/overview/)
