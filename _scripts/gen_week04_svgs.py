#!/usr/bin/env python3
"""Generate 5 SVGs for week-04: Borders, Shadows, Sizing y Estados."""
import os

BASE = "bootcamp/week-04-borders_shadows_sizing_y_estados/0-assets"
os.makedirs(BASE, exist_ok=True)

svgs = {}

# ─── SVG 01: Borders y Rounded ───────────────────────────────────────────────
svgs["01-borders-rounded.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="800" height="420">
  <rect width="800" height="420" fill="#0f172a"/>
  <text x="400" y="36" text-anchor="middle" font-family="system-ui, sans-serif" font-size="18" font-weight="700" fill="#f8fafc">Borders, Rounded y Ring</text>

  <!-- Border Width Scale -->
  <text x="30" y="68" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Border Width</text>
  <rect x="30" y="78" width="80" height="44" rx="6" ry="6" fill="none" stroke="#38bdf8" stroke-width="1"/>
  <text x="70" y="106" text-anchor="middle" font-family="monospace" font-size="10" fill="#7dd3fc">border</text>
  <rect x="130" y="78" width="80" height="44" rx="6" ry="6" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <text x="170" y="106" text-anchor="middle" font-family="monospace" font-size="10" fill="#7dd3fc">border-2</text>
  <rect x="230" y="78" width="80" height="44" rx="6" ry="6" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <text x="270" y="106" text-anchor="middle" font-family="monospace" font-size="10" fill="#7dd3fc">border-4</text>
  <rect x="330" y="78" width="80" height="44" rx="6" ry="6" fill="none" stroke="#38bdf8" stroke-width="8"/>
  <text x="370" y="106" text-anchor="middle" font-family="monospace" font-size="10" fill="#7dd3fc">border-8</text>

  <!-- Rounded Scale -->
  <text x="30" y="152" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Border Radius Scale</text>
  <rect x="30"  y="162" width="52" height="44" rx="0" ry="0" fill="#0ea5e9" opacity="0.15" stroke="#38bdf8" stroke-width="1"/>
  <text x="56"  y="190" text-anchor="middle" font-family="monospace" font-size="9" fill="#7dd3fc">none</text>
  <rect x="96"  y="162" width="52" height="44" rx="2" ry="2" fill="#0ea5e9" opacity="0.15" stroke="#38bdf8" stroke-width="1"/>
  <text x="122" y="190" text-anchor="middle" font-family="monospace" font-size="9" fill="#7dd3fc">sm</text>
  <rect x="162" y="162" width="52" height="44" rx="4" ry="4" fill="#0ea5e9" opacity="0.15" stroke="#38bdf8" stroke-width="1"/>
  <text x="188" y="190" text-anchor="middle" font-family="monospace" font-size="9" fill="#7dd3fc">base</text>
  <rect x="228" y="162" width="52" height="44" rx="6" ry="6" fill="#0ea5e9" opacity="0.15" stroke="#38bdf8" stroke-width="1"/>
  <text x="254" y="190" text-anchor="middle" font-family="monospace" font-size="9" fill="#7dd3fc">md</text>
  <rect x="294" y="162" width="52" height="44" rx="8" ry="8" fill="#0ea5e9" opacity="0.15" stroke="#38bdf8" stroke-width="1"/>
  <text x="320" y="190" text-anchor="middle" font-family="monospace" font-size="9" fill="#7dd3fc">lg</text>
  <rect x="360" y="162" width="52" height="44" rx="12" ry="12" fill="#0ea5e9" opacity="0.15" stroke="#38bdf8" stroke-width="1"/>
  <text x="386" y="190" text-anchor="middle" font-family="monospace" font-size="9" fill="#7dd3fc">xl</text>
  <rect x="426" y="162" width="52" height="44" rx="16" ry="16" fill="#0ea5e9" opacity="0.15" stroke="#38bdf8" stroke-width="1"/>
  <text x="452" y="190" text-anchor="middle" font-family="monospace" font-size="9" fill="#7dd3fc">2xl</text>
  <rect x="492" y="162" width="52" height="44" rx="22" ry="22" fill="#0ea5e9" opacity="0.15" stroke="#38bdf8" stroke-width="1"/>
  <text x="518" y="190" text-anchor="middle" font-family="monospace" font-size="9" fill="#7dd3fc">full</text>

  <!-- Ring vs Border vs Outline -->
  <text x="30" y="238" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Ring vs Border vs Outline</text>
  <!-- Border — ocupa espacio -->
  <rect x="30" y="250" width="160" height="52" rx="8" ry="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="271" text-anchor="middle" font-family="monospace" font-size="11" fill="#38bdf8">border-2</text>
  <text x="110" y="287" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">ocupa espacio en layout</text>
  <!-- Ring — no ocupa espacio -->
  <rect x="210" y="254" width="160" height="52" rx="8" ry="8" fill="#1e293b"/>
  <rect x="206" y="250" width="168" height="60" rx="10" ry="10" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2"/>
  <text x="290" y="275" text-anchor="middle" font-family="monospace" font-size="11" fill="#38bdf8">ring-2</text>
  <text x="290" y="291" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">no ocupa espacio (box-shadow)</text>
  <!-- foco label -->
  <rect x="390" y="258" width="100" height="36" rx="8" ry="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="440" y="282" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#94a3b8">focus-visible:ring</text>

  <!-- Overflow hidden diagram -->
  <text x="30" y="340" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">overflow-hidden + rounded-xl (necesario para imágenes)</text>
  <!-- sin overflow hidden -->
  <rect x="30" y="354" width="120" height="48" rx="12" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
  <rect x="30" y="354" width="120" height="24" fill="#ef4444" opacity="0.5"/>
  <text x="90" y="415" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#ef4444">sin overflow-hidden ✗</text>
  <!-- con overflow hidden -->
  <clipPath id="w4-clip">
    <rect x="170" y="354" width="120" height="48" rx="12"/>
  </clipPath>
  <rect x="170" y="354" width="120" height="48" rx="12" fill="#0f172a" stroke="#22c55e" stroke-width="1"/>
  <rect x="170" y="354" width="120" height="24" fill="#22c55e" opacity="0.5" clip-path="url(#w4-clip)"/>
  <text x="230" y="415" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#22c55e">overflow-hidden ✓</text>
</svg>'''

# ─── SVG 02: Shadow Scale ─────────────────────────────────────────────────────
svgs["02-shadow-scale.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" width="800" height="380">
  <defs>
    <filter id="sh-sm"><feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="#00000040"/></filter>
    <filter id="sh-md"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#00000050"/></filter>
    <filter id="sh-lg"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#00000060"/></filter>
    <filter id="sh-xl"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#00000070"/></filter>
    <filter id="sh-2xl"><feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#00000080"/></filter>
    <filter id="sh-colored"><feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#38bdf880"/></filter>
  </defs>
  <rect width="800" height="380" fill="#0f172a"/>
  <text x="400" y="34" text-anchor="middle" font-family="system-ui, sans-serif" font-size="18" font-weight="700" fill="#f8fafc">Escala de Shadows — Elevación Visual</text>

  <!-- Cards con sombra creciente -->
  <g transform="translate(30, 60)">
    <!-- shadow-none -->
    <rect x="0" y="10" width="96" height="80" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <text x="48" y="56" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">shadow-none</text>
    <text x="48" y="104" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#475569">sin sombra</text>

    <!-- shadow-sm -->
    <rect x="116" y="10" width="96" height="80" rx="10" fill="#1e293b" filter="url(#sh-sm)"/>
    <text x="164" y="56" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">shadow-sm</text>
    <text x="164" y="104" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#475569">inputs, base</text>

    <!-- shadow-md -->
    <rect x="232" y="8" width="96" height="80" rx="10" fill="#1e293b" filter="url(#sh-md)"/>
    <text x="280" y="54" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">shadow-md</text>
    <text x="280" y="104" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#475569">cards hover</text>

    <!-- shadow-lg -->
    <rect x="348" y="5" width="96" height="80" rx="10" fill="#1e293b" filter="url(#sh-lg)"/>
    <text x="396" y="51" text-anchor="middle" font-family="monospace" font-size="10" fill="#94a3b8">shadow-lg</text>
    <text x="396" y="104" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#475569">dropdowns</text>

    <!-- shadow-xl -->
    <rect x="464" y="2" width="96" height="80" rx="10" fill="#1e293b" filter="url(#sh-xl)"/>
    <text x="512" y="48" text-anchor="middle" font-family="monospace" font-size="10" fill="#38bdf8">shadow-xl</text>
    <text x="512" y="104" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#475569">modals</text>

    <!-- shadow-2xl -->
    <rect x="580" y="0" width="96" height="80" rx="10" fill="#1e293b" filter="url(#sh-2xl)"/>
    <text x="628" y="46" text-anchor="middle" font-family="monospace" font-size="10" fill="#38bdf8">shadow-2xl</text>
    <text x="628" y="104" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" fill="#475569">máxima elevación</text>
  </g>

  <!-- Colored shadows -->
  <text x="30" y="210" font-family="system-ui, sans-serif" font-size="13" font-weight="600" fill="#cbd5e1">Sombras de color — shadow-{color}/{opacidad}</text>
  <rect x="30" y="225" width="140" height="48" rx="8" fill="#0ea5e9" filter="url(#sh-colored)"/>
  <text x="100" y="255" text-anchor="middle" font-family="monospace" font-size="11" fill="white">shadow-sky-500/50</text>

  <defs>
    <filter id="sh-violet"><feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#7c3aed80"/></filter>
    <filter id="sh-green"><feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#10b98180"/></filter>
  </defs>
  <rect x="190" y="225" width="140" height="48" rx="8" fill="#7c3aed" filter="url(#sh-violet)"/>
  <text x="260" y="255" text-anchor="middle" font-family="monospace" font-size="11" fill="white">shadow-violet/50</text>
  <rect x="350" y="225" width="140" height="48" rx="8" fill="#10b981" filter="url(#sh-green)"/>
  <text x="420" y="255" text-anchor="middle" font-family="monospace" font-size="11" fill="white">shadow-emerald/50</text>

  <!-- Elevación con hover pattern -->
  <text x="30" y="310" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Patrón de elevación: shadow-sm → shadow-xl + -translate-y en hover</text>
  <line x1="30" y1="330" x2="700" y2="330" stroke="#334155" stroke-width="1" stroke-dasharray="4,4"/>
  <rect x="50" y="340" width="80" height="28" rx="6" fill="#1e293b" filter="url(#sh-sm)"/>
  <text x="90" y="359" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">reposo</text>
  <text x="180" y="358" font-family="system-ui, sans-serif" font-size="16" fill="#475569">→</text>
  <rect x="210" y="332" width="80" height="28" rx="6" fill="#1e293b" filter="url(#sh-xl)"/>
  <text x="250" y="351" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="#38bdf8">hover</text>
  <text x="320" y="352" font-family="system-ui, sans-serif" font-size="10" fill="#64748b">hover:shadow-xl hover:-translate-y-1 transition-all duration-200</text>
</svg>'''

# ─── SVG 03: Sizing ───────────────────────────────────────────────────────────
svgs["03-sizing.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="800" height="420">
  <rect width="800" height="420" fill="#0f172a"/>
  <text x="400" y="34" text-anchor="middle" font-family="system-ui, sans-serif" font-size="18" font-weight="700" fill="#f8fafc">Sizing — Width, Height, Min/Max y Aspect Ratio</text>

  <!-- Width scale bars -->
  <text x="30" y="62" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Width Scale (% del contenedor)</text>
  <rect x="30" y="72" width="190" height="18" rx="3" fill="#38bdf8" opacity="0.5"/>
  <text x="226" y="85" font-family="monospace" font-size="10" fill="#7dd3fc">w-1/4 — 25%</text>
  <rect x="30" y="96" width="380" height="18" rx="3" fill="#38bdf8" opacity="0.6"/>
  <text x="416" y="109" font-family="monospace" font-size="10" fill="#7dd3fc">w-1/2 — 50%</text>
  <rect x="30" y="120" width="570" height="18" rx="3" fill="#38bdf8" opacity="0.75"/>
  <text x="606" y="133" font-family="monospace" font-size="10" fill="#7dd3fc">w-3/4 — 75%</text>
  <rect x="30" y="144" width="740" height="18" rx="3" fill="#38bdf8" opacity="0.9"/>
  <text x="30" y="177" font-family="monospace" font-size="10" fill="#7dd3fc">w-full — 100%</text>

  <!-- Max-width containers -->
  <text x="30" y="205" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">max-w Containers (centrados con mx-auto)</text>
  <!-- max-w-sm -->
  <rect x="30" y="215" width="200" height="20" rx="4" fill="#0ea5e9" opacity="0.2" stroke="#38bdf8" stroke-width="1"/>
  <text x="130" y="229" text-anchor="middle" font-family="monospace" font-size="9" fill="#38bdf8">max-w-sm · 384px</text>
  <!-- max-w-xl -->
  <rect x="30" y="240" width="300" height="20" rx="4" fill="#0ea5e9" opacity="0.3" stroke="#38bdf8" stroke-width="1"/>
  <text x="180" y="254" text-anchor="middle" font-family="monospace" font-size="9" fill="#38bdf8">max-w-xl · 576px</text>
  <!-- max-w-2xl -->
  <rect x="30" y="265" width="350" height="20" rx="4" fill="#0ea5e9" opacity="0.4" stroke="#38bdf8" stroke-width="1"/>
  <text x="205" y="279" text-anchor="middle" font-family="monospace" font-size="9" fill="#38bdf8">max-w-2xl · 672px</text>
  <!-- max-w-4xl -->
  <rect x="30" y="290" width="468" height="20" rx="4" fill="#0ea5e9" opacity="0.5" stroke="#38bdf8" stroke-width="1"/>
  <text x="264" y="304" text-anchor="middle" font-family="monospace" font-size="9" fill="#38bdf8">max-w-4xl · 896px</text>
  <!-- max-w-7xl -->
  <rect x="30" y="315" width="667" height="20" rx="4" fill="#0ea5e9" opacity="0.65" stroke="#38bdf8" stroke-width="1"/>
  <text x="363" y="329" text-anchor="middle" font-family="monospace" font-size="9" fill="#0f172a" font-weight="700">max-w-7xl · 1280px — layout de página</text>

  <!-- Aspect Ratio -->
  <text x="30" y="360" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Aspect Ratio</text>
  <!-- square -->
  <rect x="30" y="372" width="40" height="40" rx="4" fill="#0ea5e9" opacity="0.4" stroke="#38bdf8" stroke-width="1"/>
  <text x="50" y="424" text-anchor="middle" font-family="monospace" font-size="9" fill="#7dd3fc">square</text>
  <!-- video -->
  <rect x="90" y="378" width="88" height="49.5" rx="4" fill="#7c3aed" opacity="0.4" stroke="#a78bfa" stroke-width="1"/>
  <text x="134" y="424" text-anchor="middle" font-family="monospace" font-size="9" fill="#c4b5fd">video 16:9</text>
  <!-- 4:3 -->
  <rect x="200" y="376" width="80" height="60" rx="4" fill="#10b981" opacity="0.3" stroke="#34d399" stroke-width="1"/>
  <text x="240" y="424" text-anchor="middle" font-family="monospace" font-size="9" fill="#6ee7b7">4:3</text>
  <!-- object-cover label -->
  <text x="350" y="385" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">object-cover: rellena y recorta</text>
  <text x="350" y="400" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">object-contain: encuadra sin recortar</text>
  <text x="350" y="415" font-family="monospace" font-size="10" fill="#38bdf8">h-48 w-full object-cover → imagen responsive</text>
</svg>'''

# ─── SVG 04: Estados Interactivos ─────────────────────────────────────────────
svgs["04-estados-interactivos.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="800" height="400">
  <rect width="800" height="400" fill="#0f172a"/>
  <text x="400" y="34" text-anchor="middle" font-family="system-ui, sans-serif" font-size="18" font-weight="700" fill="#f8fafc">Estados Interactivos — Pseudo-class Variants</text>

  <!-- Estado diagram: estado normal -->
  <text x="30" y="64" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">Estado base</text>
  <rect x="30" y="74" width="120" height="40" rx="8" fill="#0ea5e9"/>
  <text x="90" y="99" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="600" fill="white">Botón</text>

  <!-- hover -->
  <text x="175" y="64" font-family="monospace" font-size="10" fill="#94a3b8">hover:</text>
  <rect x="175" y="74" width="120" height="40" rx="8" fill="#0284c7"/>
  <text x="235" y="99" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="600" fill="white">Botón</text>

  <!-- focus-visible -->
  <text x="320" y="64" font-family="monospace" font-size="10" fill="#94a3b8">focus-visible:</text>
  <rect x="320" y="74" width="120" height="40" rx="8" fill="#0ea5e9"/>
  <rect x="316" y="70" width="128" height="48" rx="10" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="380" y="99" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="600" fill="white">Botón</text>

  <!-- active -->
  <text x="468" y="64" font-family="monospace" font-size="10" fill="#94a3b8">active:</text>
  <rect x="471" y="76" width="112" height="38" rx="8" fill="#075985" transform="scale(0.97)" transform-origin="468 94"/>
  <text x="527" y="99" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="600" fill="#93c5fd">Botón</text>

  <!-- disabled -->
  <text x="610" y="64" font-family="monospace" font-size="10" fill="#94a3b8">disabled:</text>
  <rect x="610" y="74" width="120" height="40" rx="8" fill="#0ea5e9" opacity="0.4"/>
  <text x="670" y="99" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="600" fill="white" opacity="0.5">Botón</text>
  <line x1="610" y1="74" x2="730" y2="114" stroke="#ef4444" stroke-width="1.5" opacity="0.5"/>

  <!-- focus vs focus-visible explanation -->
  <rect x="30" y="140" width="740" height="80" rx="8" fill="#1e293b"/>
  <text x="50" y="165" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#f1f5f9">focus: vs focus-visible:</text>
  <text x="50" y="184" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">• focus: — Activa con click del mouse Y con teclado. Usar en inputs.</text>
  <text x="50" y="200" font-family="system-ui, sans-serif" font-size="11" fill="#94a3b8">• focus-visible: — Solo activa con teclado (Tab). Ideal para botones. No molesta al usuario de mouse.</text>

  <!-- group -->
  <text x="30" y="252" font-family="system-ui, sans-serif" font-size="13" font-weight="600" fill="#cbd5e1">group — reacción del hijo al estado del padre</text>
  <rect x="30" y="262" width="300" height="90" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="40" y="280" font-family="monospace" font-size="10" fill="#64748b">group</text>
  <rect x="50" y="286" width="260" height="24" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="180" y="302" text-anchor="middle" font-family="monospace" font-size="10" fill="#38bdf8">group-hover:text-sky-600</text>
  <rect x="50" y="316" width="120" height="24" rx="6" fill="#0f172a"/>
  <text x="110" y="332" text-anchor="middle" font-family="monospace" font-size="10" fill="#64748b">group-hover:opacity-100</text>
  <line x1="40" y1="275" x2="310" y2="275" stroke="#334155" stroke-width="1"/>

  <!-- peer -->
  <text x="360" y="252" font-family="system-ui, sans-serif" font-size="13" font-weight="600" fill="#cbd5e1">peer — sibling reactivo</text>
  <rect x="360" y="262" width="380" height="90" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <!-- checkbox peer -->
  <rect x="380" y="280" width="24" height="24" rx="4" fill="#38bdf8" stroke="#38bdf8" stroke-width="1"/>
  <text x="392" y="296" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" fill="white">✓</text>
  <text x="415" y="296" font-family="monospace" font-size="9" fill="#64748b">peer (input checkbox)</text>
  <!-- sibling reactivo -->
  <rect x="380" y="314" width="340" height="24" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="550" y="330" text-anchor="middle" font-family="monospace" font-size="10" fill="#38bdf8">peer-checked:bg-sky-500 / peer-checked:translate-x-5</text>

  <!-- Transition hint -->
  <text x="30" y="378" font-family="monospace" font-size="11" fill="#38bdf8">transition-colors duration-200</text>
  <text x="230" y="378" font-family="system-ui, sans-serif" font-size="11" fill="#64748b">→ siempre añadir a elementos con estados hover/focus para suavizar cambios</text>
</svg>'''

# ─── SVG 05: Group, Peer y Transiciones ───────────────────────────────────────
svgs["05-group-peer-transiciones.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="800" height="420">
  <rect width="800" height="420" fill="#0f172a"/>
  <text x="400" y="34" text-anchor="middle" font-family="system-ui, sans-serif" font-size="18" font-weight="700" fill="#f8fafc">Group, Peer y Transiciones — Interacciones Avanzadas</text>

  <!-- Card interactiva con group -->
  <text x="30" y="62" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#cbd5e1">Card con group (estado hover activo)</text>

  <!-- card shell -->
  <rect x="30" y="72" width="220" height="200" rx="16" fill="#1e293b"/>
  <!-- imagen con zoom simulado -->
  <rect x="30" y="72" width="220" height="100" rx="0" fill="#0ea5e9" opacity="0.6" clip-path="url(#card-clip)"/>
  <clipPath id="card-clip">
    <rect x="30" y="72" width="220" height="100" rx="0"/>
  </clipPath>
  <!-- top rounded clip -->
  <rect x="30" y="72" width="220" height="100" rx="16" fill="none"/>
  <text x="140" y="128" text-anchor="middle" font-family="system-ui, sans-serif" font-size="10" fill="white" opacity="0.8">group-hover:scale-110 → zoom</text>
  <!-- content -->
  <text x="50" y="190" font-family="monospace" font-size="10" fill="#38bdf8">group-hover:text-sky-600 ✓</text>
  <text x="50" y="208" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#f1f5f9">Título del artículo</text>
  <text x="50" y="252" font-family="monospace" font-size="10" fill="#38bdf8">group-hover:opacity-100 ✓</text>
  <text x="50" y="268" font-family="system-ui, sans-serif" font-size="11" fill="#38bdf8">Leer más →</text>

  <!-- Annotations -->
  <line x1="260" y1="108" x2="310" y2="108" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="315" y="112" font-family="monospace" font-size="10" fill="#38bdf8">group-hover:scale-110</text>
  <line x1="260" y1="208" x2="310" y2="208" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="315" y="212" font-family="monospace" font-size="10" fill="#38bdf8">group-hover:text-sky-600</text>
  <line x1="260" y1="268" x2="310" y2="268" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="315" y="272" font-family="monospace" font-size="10" fill="#38bdf8">group-hover:opacity-100 translate-x-1</text>

  <!-- Peer toggle diagram -->
  <text x="30" y="302" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#cbd5e1">Peer — custom toggle</text>
  <!-- unchecked state -->
  <rect x="30" y="316" width="44" height="24" rx="12" fill="#475569"/>
  <circle cx="42" cy="328" r="9" fill="white"/>
  <text x="85" y="332" font-family="monospace" font-size="10" fill="#64748b">peer (unchecked)</text>
  <!-- checked state -->
  <rect x="30" y="355" width="44" height="24" rx="12" fill="#38bdf8"/>
  <circle cx="62" cy="367" r="9" fill="white"/>
  <text x="85" y="371" font-family="monospace" font-size="10" fill="#38bdf8">peer-checked: → bg-sky-500 + translate-x-5</text>

  <!-- Transitions guide -->
  <rect x="490" y="60" width="290" height="340" rx="12" fill="#1e293b"/>
  <text x="634" y="86" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#f1f5f9">Guía de Transiciones</text>

  <!-- rows -->
  <text x="510" y="112" font-family="monospace" font-size="10" fill="#38bdf8">transition-colors</text>
  <text x="510" y="126" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">background-color, color, border-color</text>

  <line x1="510" y1="136" x2="766" y2="136" stroke="#334155" stroke-width="1"/>
  <text x="510" y="152" font-family="monospace" font-size="10" fill="#38bdf8">transition-shadow</text>
  <text x="510" y="166" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">box-shadow únicamente</text>

  <line x1="510" y1="176" x2="766" y2="176" stroke="#334155" stroke-width="1"/>
  <text x="510" y="192" font-family="monospace" font-size="10" fill="#38bdf8">transition-transform</text>
  <text x="510" y="206" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">scale, translate, rotate</text>

  <line x1="510" y1="216" x2="766" y2="216" stroke="#334155" stroke-width="1"/>
  <text x="510" y="232" font-family="monospace" font-size="10" fill="#38bdf8">transition-opacity</text>
  <text x="510" y="246" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">opacity</text>

  <line x1="510" y1="256" x2="766" y2="256" stroke="#334155" stroke-width="1"/>
  <text x="510" y="272" font-family="monospace" font-size="10" fill="#ef4444">transition-all</text>
  <text x="510" y="286" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">todo (evitar en producción)</text>

  <line x1="510" y1="296" x2="766" y2="296" stroke="#334155" stroke-width="1"/>
  <text x="634" y="316" text-anchor="middle" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Duración recomendada</text>
  <text x="510" y="336" font-family="monospace" font-size="10" fill="#38bdf8">duration-150</text>
  <text x="620" y="336" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">active:scale-95 (muy rápido)</text>
  <text x="510" y="352" font-family="monospace" font-size="10" fill="#38bdf8">duration-200</text>
  <text x="620" y="352" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">hover colors, shadows</text>
  <text x="510" y="368" font-family="monospace" font-size="10" fill="#38bdf8">duration-300</text>
  <text x="620" y="368" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">scale, translate, opacity</text>
  <text x="510" y="384" font-family="monospace" font-size="10" fill="#ef4444">duration-500+</text>
  <text x="620" y="384" font-family="system-ui, sans-serif" font-size="9" fill="#64748b">solo para efectos especiales</text>
</svg>'''

# Write all SVGs
for fname, content in svgs.items():
    path = os.path.join(BASE, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ {path}")

print(f"\n✅ Week 04 SVGs: {len(svgs)} files created.")
