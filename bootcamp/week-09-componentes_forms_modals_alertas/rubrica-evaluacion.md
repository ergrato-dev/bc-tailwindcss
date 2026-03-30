# 📊 Rúbrica de Evaluación — Semana 9

**Bootcamp TailwindCSS Zero to Hero** | Semana 9: Componentes UI — Forms, Modals y Alertas

---

## 🧠 Conocimiento (30%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Estilizado de inputs** | Conoce la anatomía completa de un input estilizado: `block w-full rounded-lg border bg-gray-800 px-4 py-2.5 text-white placeholder:text-gray-500 focus:outline-none focus:ring-2`; diferencia placeholder de label | Aplica estilos básicos al input; olvida `placeholder:text-gray-500` o `focus:outline-none` | Solo aplica `border` y colores básicos; no controla el estado focus ni placeholder |
| **Validación con `peer`** | Sabe colocar `peer` en el input y usar `peer-invalid:block` / `peer-placeholder-shown:hidden` en el mensaje de error; entiende que el hermano sibling must come after el peer en el DOM | Entiende la técnica `peer` básica; no combina `peer-invalid:` con `peer-placeholder-shown:hidden` para ocultar mensaje hasta el primer foco | No conoce la validación CSS/HTML; solo piensa en JavaScript para mostrar errores |
| **Modals: `fixed inset-0`** | Explica por qué se usa `fixed inset-0` (cubre 100vw × 100vh); entiende la pila `z-*`: contenido `z-0` → navbar `z-50` → modal overlay `z-50` → modal content `z-50`; sabe agregar `overflow-hidden` al body para bloquear scroll | Sabe construir el overlay con `fixed inset-0 bg-black/50`; no gestiona el z-index ni el scroll del body | Usa `position: absolute` en lugar de `fixed`; el overlay no cubre toda la pantalla |
| **`backdrop-blur`** | Aplica `backdrop-blur-sm` con `bg-gray-950/80` en el overlay; sabe que requiere `background-color` con opacidad para ser visible; entiende el impacto en GPU y performance | Aplica backdrop-blur; no lo combina con background semitransparente; no lo activa correctamente | No conoce `backdrop-blur`; usa `background: rgba()` solamente |
| **Alertas semánticas** | Diferencia las 4 variantes (success/error/warning/info) por color, ícono y mensaje; usa `bg-COLOR-500/10 border border-COLOR-500/20 text-COLOR-300`; agrega `role="alert"` y `aria-live="polite"` para accessibility | Usa los 4 colores semánticos; no agrega roles ARIA; sin icono | Usa un solo color o colores no semánticos para todas las alertas |

---

## 💪 Desempeño (40%)

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Ejercicio Formulario Login** | Login completo con email + password + remember me; todos los estados: default, focus (ring), error (borde rojo + mensaje), disabled; labels vinculados con `for/id`; botón submit estilizado | Login funcional con 2 estados (default/error); labels presentes; sin disabled | Solo inputs sin labels; un solo estado visual |
| **Ejercicio Formulario Complejo** | Formulario de registro con: name, email, password+confirm, select, checkbox group, radio y textarea; validación visual por campo; botones cancel/submit; responsive | Formulario con 5+ tipos de input; validación en 3+ campos; sin textarea o sin radio | Formulario con 2-3 inputs básicos; un solo estado |
| **Ejercicio Modal** | Modal con overlay `fixed inset-0 bg-gray-950/80 backdrop-blur-sm`; contenido centrado con `flex items-center justify-center`; botón cerrar accesible con `aria-label`; se activa con `peer` o similar | Modal visible con overlay básico; abre/cierra; sin backdrop-blur ni accesibilidad | Modal sin overlay real; no cubre la pantalla completa |
| **Ejercicio Notificaciones** | 4 tipos de alerta con sus 4 iconos; 2 variantes de toast (posición fija `bottom-4 right-4`); 1 banner full-width; dismiss con ×; `role="alert"` presente | 3 tipos de alerta con colores correctos; sin toast o sin dismiss | Solo 1-2 alertas con colores no semánticos |

---

## 📦 Producto (30%)

**Proyecto: Página de Contacto y Sistema de Notificaciones**

| Criterio | Excelente (100%) | Satisfactorio (70%) | Insuficiente (<70%) |
|----------|-----------------|---------------------|---------------------|
| **Formulario completo** | Todos los tipos: text, email, tel, select, checkbox, radio, textarea; `label` vinculado con `for/id`; placeholder descriptivo; `required` en campos obligatorios | 5+ tipos de input con labels; sin radio o sin textarea | 3 tipos de input; algunos sin label |
| **Estados de validación** | Borde + ícono + mensaje por campo para estado error; borde + ícono para estado success; `aria-describedby` apuntando al mensaje; transición de color | Borde de color en error + mensaje de texto; sin icono; sin aria | Solo cambio de color del borde; sin mensaje de error |
| **Modal de confirmación** | Modal al enviar con overlay blur, animación de entrada (`transition translate`), título + mensaje + botones; se cierra con botón o clic en overlay | Modal funcional que muestra/oculta; overlay sin blur o sin animación | Alerta nativa del browser (`alert()`) o sin modal |
| **Alertas y banner** | Banner dismissable al tope del contenido (success), alerta de error inline, toast `fixed bottom-4`; todos con `role="alert"`; botón dismiss con `aria-label` | Banner + 2 alertas; colores correctos; sin toast o sin dismiss | Solo 1 alerta sin dismiss ni rol ARIA |
| **Accesibilidad** | `label+for/id` en todos; `aria-describedby` en campos con error; `role="alert"` en notificaciones; `aria-label` en icon-buttons; contraste WCAG AA | La mayoría de labels; `role="alert"` en alertas; algunos aria | Labels ausentes en 3+ campos; sin roles ARIA |
| **Calidad de código** | HTML semántico (`<form>`, `<fieldset>`, `<legend>`, `<label>`); clases en orden consistente; separación visual de secciones | `<form>` y `<label>` presentes; orden de clases mayormente consistente | Solo `<div>` y `<input>` sin estructura semántica |
