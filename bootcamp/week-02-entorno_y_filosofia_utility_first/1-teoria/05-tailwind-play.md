# ▶️ Tailwind Play — El Sandbox Online

## 🎯 Objetivos

- Usar Tailwind Play para experimentar sin instalar nada
- Compartir código con compañeros mediante links
- Usar Play como herramienta de debugging y prototipado rápido

---

## 📋 Contenido

### 1. ¿Qué es Tailwind Play?

**Tailwind Play** (`play.tailwindcss.com`) es un editor online que:
- Corre Tailwind completo en el browser en tiempo real
- Permite compartir código con una URL única
- Actualiza el preview al escribir (igual que un editor local)
- Soporta Tailwind v4 y todas sus variantes

Es perfecto para:
- Probar una idea rápido antes de escribirla en tu proyecto
- Reportar bugs o mostrar ejemplos a otros
- Experimentar con clases sin configurar nada

---

### 2. La Interfaz

```
┌─────────────────────────────────────────────────────────┐
│  [HTML]  [Config]                    [Share] [Copy CSS] │
├────────────────────────────┬────────────────────────────┤
│                            │                            │
│   Editor HTML              │   Preview en tiempo real   │
│                            │                            │
│   <div class="...">        │   ┌─────────────────────┐  │
│     ...                    │   │ Tu componente aquí  │  │
│   </div>                   │   └─────────────────────┘  │
│                            │                            │
└────────────────────────────┴────────────────────────────┘
```

- **Panel HTML**: Donde escribes tu HTML con clases Tailwind
- **Panel Config**: Para agregar configuración custom (colores, fuentes)
- **Preview**: Se actualiza en tiempo real
- **Share**: Genera una URL única para compartir tu código

---

### 3. Tu Primer Experimento

Abre [play.tailwindcss.com](https://play.tailwindcss.com) y reemplaza el contenido con:

```html
<div class="min-h-screen bg-slate-900 flex items-center justify-center p-8">
  <div class="bg-white rounded-2xl shadow-xl overflow-hidden max-w-md w-full">

    <!-- Header de la card -->
    <div class="bg-sky-500 px-6 py-8 text-center">
      <div class="mx-auto h-20 w-20 rounded-full bg-white/20 ring-4 ring-white/30"></div>
      <h2 class="mt-4 text-2xl font-bold text-white">Tu Nombre</h2>
      <p class="mt-1 text-sky-100">Desarrollador Frontend</p>
    </div>

    <!-- Cuerpo de la card -->
    <div class="p-6 space-y-4">

      <!-- Estadísticas -->
      <div class="grid grid-cols-3 gap-4 text-center">
        <div>
          <p class="text-2xl font-bold text-gray-900">42</p>
          <p class="text-xs text-gray-500">Proyectos</p>
        </div>
        <div>
          <p class="text-2xl font-bold text-gray-900">1.2k</p>
          <p class="text-xs text-gray-500">Seguidores</p>
        </div>
        <div>
          <p class="text-2xl font-bold text-gray-900">348</p>
          <p class="text-xs text-gray-500">Siguiendo</p>
        </div>
      </div>

      <!-- Botón -->
      <button class="w-full rounded-lg bg-sky-500 py-2.5 text-sm font-semibold text-white hover:bg-sky-600 transition-colors">
        Seguir
      </button>

    </div>
  </div>
</div>
```

Observa cómo el preview se actualiza con cada cambio.

---

### 4. Experimentar con Variantes

En Play es seguro experimentar. Prueba cambiar:
- `bg-slate-900` por `bg-gray-100` — tema claro
- `bg-sky-500` por `bg-violet-500` — color diferente
- `rounded-2xl` por `rounded-none` — sin bordes redondeados
- Agregar `dark:bg-gray-800` y activar dark mode desde Config

---

### 5. Compartir Código

1. Haz clic en **Share** (esquina superior derecha)
2. Copia la URL generada: `https://play.tailwindcss.com/aBcDeFgH`
3. Comparte en Discord, Slack o con tu instructor

Cada URL preserva exactamente tu código HTML y config.

---

### 6. Limitaciones de Play

Play es estupendo para prototipos rápidos, pero:
- ❌ No tiene IntelliSense completo como VS Code
- ❌ No puedes dividir en múltiples archivos
- ❌ No está disponible offline
- ❌ No se integra con frameworks (React, Vue, etc.)

Para proyectos reales, siempre usa el entorno local con Vite.

---

## ✅ Checklist de Verificación

- [ ] He abierto Tailwind Play y creado un componente básico
- [ ] Experimenté cambiando colores y variantes en tiempo real
- [ ] Compartí un enlace de Play con alguien
- [ ] Entiendo cuándo usar Play vs el entorno local
