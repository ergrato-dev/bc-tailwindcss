# Ejercicio 01: Setup del Entorno — Vite + TailwindCSS v4

## 🎯 Objetivo

Crear un proyecto Vite + TailwindCSS v4 desde cero, verificar que funciona y entender qué hace cada archivo de configuración.

---

## 🛠️ Configuración

No necesitas clonar nada. Vas a crear el proyecto desde cero.

---

## 📋 Instrucciones

### Paso 1: Crear el Proyecto Vite

Crea un proyecto JavaScript vanilla con Vite:

```bash
pnpm create vite@latest perfil-card -- --template vanilla
cd perfil-card
pnpm install
```

**¿Qué creó Vite?** Observa la estructura:
```
perfil-card/
├── index.html
├── package.json
├── vite.config.js
├── src/
│   ├── counter.js
│   ├── main.js
│   ├── style.css
│   └── javascript.svg
└── public/
    └── vite.svg
```

**Abre `starter/index.html`** — el ejercicio empieza aquí. Descomenta el **bloque 1** para ver la estructura base.

---

### Paso 2: Instalar Tailwind

Sigue las instrucciones comentadas en `starter/index.html` bloque 2.

El comando es:
```bash
pnpm add -D tailwindcss @tailwindcss/vite
```

---

### Paso 3: Configurar vite.config.js

Descomenta el **bloque 3**. Muestra la configuración correcta de `vite.config.js`.

---

### Paso 4: Actualizar el CSS

Descomenta el **bloque 4**. Muestra cómo actualizar `src/style.css` con `@import "tailwindcss"`.

---

### Paso 5: Primera Clase Tailwind

Descomenta el **bloque 5**. Agrega un texto simple con clases Tailwind para verificar que funciona.

Ejecuta `pnpm dev` y verifica en el browser.

---

## ✅ Verificación

El ejercicio está completo cuando:
- `pnpm dev` inicia sin errores en la consola
- El browser muestra el texto con estilos Tailwind aplicados
- IntelliSense autocompleta clases en VS Code al escribir `class="`
- `pnpm build` genera la carpeta `dist/` sin errores
