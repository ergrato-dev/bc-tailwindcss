# Ejercicio 01: Navbar Responsive

## 🎯 Objetivo

Construir un navbar completamente funcional con logo, links, CTA y menú hamburger que se abre y cierra sin usar JavaScript, usando la técnica `peer` de Tailwind.

---

## 📋 Instrucciones

### Paso 1: Navbar básico con Flex

Descomenta el **bloque 1** para ver la estructura base de un navbar: `flex justify-between` para separar logo, links y CTA en los extremos. Comprueba que en pantallas pequeñas el contenido se ve comprimido.

### Paso 2: Links con estado activo y hover suave

Descomenta el **bloque 2** para ver cómo diferenciar el link de la página actual con `aria-current="page"`, un subrayado decorativo con `after:` y color blanco. Compara con los links inactivos en `text-gray-400`.

### Paso 3: Hamburger con `peer` (sin JS)

Descomenta el **bloque 3** para ver la técnica del checkbox oculto: el `<input class="peer hidden">` controla la visibilidad del menú móvil a través de `peer-checked:flex`. El `<label>` actúa como botón visible.

### Paso 4: Navbar completo responsive

Descomenta el **bloque 4** que combina todo: sticky, backdrop-blur, links desktop ocultos en mobile (`hidden md:flex`), hamburger solo en mobile (`md:hidden`) y menú dropdown responsive.

---

## ✅ Verificación

- El bloque 1 muestra logo + links + CTA en una fila horizontal
- El bloque 2 muestra el link activo resaltado con subrayado sky
- El bloque 3: al hacer clic en el ≡, el menú vertical aparece y desaparece
- El bloque 4: completo y funcional — en desktop se ven los links, en mobile solo el hamburger
