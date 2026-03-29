#!/usr/bin/env python3
"""Generate SVG assets for week-03."""
import os

BASE = "bootcamp/week-03-colores_tipografia_y_espaciado/0-assets"
os.makedirs(BASE, exist_ok=True)

# ─────────────────────────────────────────────────
# SVG 1: Paleta de colores — escala 50-950
# ─────────────────────────────────────────────────
svg1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 340" width="800" height="340" font-family="system-ui, sans-serif">
  <rect width="800" height="340" fill="#0f172a"/>

  <!-- Title -->
  <text x="400" y="32" text-anchor="middle" font-size="15" font-weight="700" fill="#f1f5f9" letter-spacing="1">PALETA DE COLORES TAILWIND — ESCALA 50 a 950</text>

  <!-- Color row: sky -->
  <text x="14" y="68" font-size="11" fill="#94a3b8">sky</text>
  <!-- shades: 50 100 200 300 400 500 600 700 800 900 950 -->
  <rect x="50" y="52" width="66" height="26" rx="4" fill="#f0f9ff"/>
  <text x="83" y="69" text-anchor="middle" font-size="9" fill="#334155">50</text>
  <rect x="120" y="52" width="66" height="26" rx="4" fill="#e0f2fe"/>
  <text x="153" y="69" text-anchor="middle" font-size="9" fill="#334155">100</text>
  <rect x="190" y="52" width="66" height="26" rx="4" fill="#bae6fd"/>
  <text x="223" y="69" text-anchor="middle" font-size="9" fill="#334155">200</text>
  <rect x="260" y="52" width="66" height="26" rx="4" fill="#7dd3fc"/>
  <text x="293" y="69" text-anchor="middle" font-size="9" fill="#334155">300</text>
  <rect x="330" y="52" width="66" height="26" rx="4" fill="#38bdf8"/>
  <text x="363" y="69" text-anchor="middle" font-size="9" fill="#334155">400</text>
  <rect x="400" y="52" width="66" height="26" rx="4" fill="#0ea5e9"/>
  <text x="433" y="69" text-anchor="middle" font-size="9" fill="#fff">500</text>
  <rect x="470" y="52" width="66" height="26" rx="4" fill="#0284c7"/>
  <text x="503" y="69" text-anchor="middle" font-size="9" fill="#fff">600</text>
  <rect x="540" y="52" width="66" height="26" rx="4" fill="#0369a1"/>
  <text x="573" y="69" text-anchor="middle" font-size="9" fill="#fff">700</text>
  <rect x="610" y="52" width="66" height="26" rx="4" fill="#075985"/>
  <text x="643" y="69" text-anchor="middle" font-size="9" fill="#fff">800</text>
  <rect x="680" y="52" width="55" height="26" rx="4" fill="#0c4a6e"/>
  <text x="707" y="69" text-anchor="middle" font-size="9" fill="#fff">900+</text>

  <!-- Color row: emerald -->
  <text x="14" y="108" font-size="11" fill="#94a3b8">emerald</text>
  <rect x="50" y="92" width="66" height="26" rx="4" fill="#ecfdf5"/>
  <text x="83" y="109" text-anchor="middle" font-size="9" fill="#334155">50</text>
  <rect x="120" y="92" width="66" height="26" rx="4" fill="#d1fae5"/>
  <text x="153" y="109" text-anchor="middle" font-size="9" fill="#334155">100</text>
  <rect x="190" y="92" width="66" height="26" rx="4" fill="#a7f3d0"/>
  <text x="223" y="109" text-anchor="middle" font-size="9" fill="#334155">200</text>
  <rect x="260" y="92" width="66" height="26" rx="4" fill="#6ee7b7"/>
  <text x="293" y="109" text-anchor="middle" font-size="9" fill="#334155">300</text>
  <rect x="330" y="92" width="66" height="26" rx="4" fill="#34d399"/>
  <text x="363" y="109" text-anchor="middle" font-size="9" fill="#334155">400</text>
  <rect x="400" y="92" width="66" height="26" rx="4" fill="#10b981"/>
  <text x="433" y="109" text-anchor="middle" font-size="9" fill="#fff">500</text>
  <rect x="470" y="92" width="66" height="26" rx="4" fill="#059669"/>
  <text x="503" y="109" text-anchor="middle" font-size="9" fill="#fff">600</text>
  <rect x="540" y="92" width="66" height="26" rx="4" fill="#047857"/>
  <text x="573" y="109" text-anchor="middle" font-size="9" fill="#fff">700</text>
  <rect x="610" y="92" width="66" height="26" rx="4" fill="#065f46"/>
  <text x="643" y="109" text-anchor="middle" font-size="9" fill="#fff">800</text>
  <rect x="680" y="92" width="55" height="26" rx="4" fill="#022c22"/>
  <text x="707" y="109" text-anchor="middle" font-size="9" fill="#fff">900+</text>

  <!-- Color row: red -->
  <text x="14" y="148" font-size="11" fill="#94a3b8">red</text>
  <rect x="50" y="132" width="66" height="26" rx="4" fill="#fef2f2"/>
  <text x="83" y="149" text-anchor="middle" font-size="9" fill="#334155">50</text>
  <rect x="120" y="132" width="66" height="26" rx="4" fill="#fee2e2"/>
  <text x="153" y="149" text-anchor="middle" font-size="9" fill="#334155">100</text>
  <rect x="190" y="132" width="66" height="26" rx="4" fill="#fecaca"/>
  <text x="223" y="149" text-anchor="middle" font-size="9" fill="#334155">200</text>
  <rect x="260" y="132" width="66" height="26" rx="4" fill="#fca5a5"/>
  <text x="293" y="149" text-anchor="middle" font-size="9" fill="#334155">300</text>
  <rect x="330" y="132" width="66" height="26" rx="4" fill="#f87171"/>
  <text x="363" y="149" text-anchor="middle" font-size="9" fill="#334155">400</text>
  <rect x="400" y="132" width="66" height="26" rx="4" fill="#ef4444"/>
  <text x="433" y="149" text-anchor="middle" font-size="9" fill="#fff">500</text>
  <rect x="470" y="132" width="66" height="26" rx="4" fill="#dc2626"/>
  <text x="503" y="149" text-anchor="middle" font-size="9" fill="#fff">600</text>
  <rect x="540" y="132" width="66" height="26" rx="4" fill="#b91c1c"/>
  <text x="573" y="149" text-anchor="middle" font-size="9" fill="#fff">700</text>
  <rect x="610" y="132" width="66" height="26" rx="4" fill="#991b1b"/>
  <text x="643" y="149" text-anchor="middle" font-size="9" fill="#fff">800</text>
  <rect x="680" y="132" width="55" height="26" rx="4" fill="#450a0a"/>
  <text x="707" y="149" text-anchor="middle" font-size="9" fill="#fff">900+</text>

  <!-- Color row: amber -->
  <text x="14" y="188" font-size="11" fill="#94a3b8">amber</text>
  <rect x="50" y="172" width="66" height="26" rx="4" fill="#fffbeb"/>
  <text x="83" y="189" text-anchor="middle" font-size="9" fill="#334155">50</text>
  <rect x="120" y="172" width="66" height="26" rx="4" fill="#fef3c7"/>
  <text x="153" y="189" text-anchor="middle" font-size="9" fill="#334155">100</text>
  <rect x="190" y="172" width="66" height="26" rx="4" fill="#fde68a"/>
  <text x="223" y="189" text-anchor="middle" font-size="9" fill="#334155">200</text>
  <rect x="260" y="172" width="66" height="26" rx="4" fill="#fcd34d"/>
  <text x="293" y="189" text-anchor="middle" font-size="9" fill="#334155">300</text>
  <rect x="330" y="172" width="66" height="26" rx="4" fill="#fbbf24"/>
  <text x="363" y="189" text-anchor="middle" font-size="9" fill="#334155">400</text>
  <rect x="400" y="172" width="66" height="26" rx="4" fill="#f59e0b"/>
  <text x="433" y="189" text-anchor="middle" font-size="9" fill="#fff">500</text>
  <rect x="470" y="172" width="66" height="26" rx="4" fill="#d97706"/>
  <text x="503" y="189" text-anchor="middle" font-size="9" fill="#fff">600</text>
  <rect x="540" y="172" width="66" height="26" rx="4" fill="#b45309"/>
  <text x="573" y="189" text-anchor="middle" font-size="9" fill="#fff">700</text>
  <rect x="610" y="172" width="66" height="26" rx="4" fill="#92400e"/>
  <text x="643" y="189" text-anchor="middle" font-size="9" fill="#fff">800</text>
  <rect x="680" y="172" width="55" height="26" rx="4" fill="#451a03"/>
  <text x="707" y="189" text-anchor="middle" font-size="9" fill="#fff">900+</text>

  <!-- Separator -->
  <line x1="40" y1="210" x2="760" y2="210" stroke="#1e293b" stroke-width="1"/>

  <!-- Legend: Usos por escala -->
  <text x="400" y="230" text-anchor="middle" font-size="12" font-weight="600" fill="#38bdf8">Usos recomendados por escala</text>
  <rect x="40" y="240" width="130" height="80" rx="8" fill="#1e293b"/>
  <text x="105" y="258" text-anchor="middle" font-size="11" font-weight="700" fill="#e2e8f0">50 — 100</text>
  <text x="105" y="274" text-anchor="middle" font-size="10" fill="#94a3b8">Fondos suaves</text>
  <text x="105" y="288" text-anchor="middle" font-size="10" fill="#94a3b8">Badges claros</text>
  <text x="105" y="302" text-anchor="middle" font-size="10" fill="#94a3b8">Sections tintadas</text>

  <rect x="185" y="240" width="130" height="80" rx="8" fill="#1e293b"/>
  <text x="250" y="258" text-anchor="middle" font-size="11" font-weight="700" fill="#e2e8f0">200 — 300</text>
  <text x="250" y="274" text-anchor="middle" font-size="10" fill="#94a3b8">Bordes</text>
  <text x="250" y="288" text-anchor="middle" font-size="10" fill="#94a3b8">Separadores</text>
  <text x="250" y="302" text-anchor="middle" font-size="10" fill="#94a3b8">Accents sutiles</text>

  <rect x="330" y="240" width="130" height="80" rx="8" fill="#1e293b"/>
  <text x="395" y="258" text-anchor="middle" font-size="11" font-weight="700" fill="#e2e8f0">400 — 600</text>
  <text x="395" y="274" text-anchor="middle" font-size="10" fill="#94a3b8">Botones</text>
  <text x="395" y="288" text-anchor="middle" font-size="10" fill="#94a3b8">Íconos</text>
  <text x="395" y="302" text-anchor="middle" font-size="10" fill="#94a3b8">Colores de acento</text>

  <rect x="475" y="240" width="130" height="80" rx="8" fill="#1e293b"/>
  <text x="540" y="258" text-anchor="middle" font-size="11" font-weight="700" fill="#e2e8f0">700 — 900</text>
  <text x="540" y="274" text-anchor="middle" font-size="10" fill="#94a3b8">Texto principal</text>
  <text x="540" y="288" text-anchor="middle" font-size="10" fill="#94a3b8">Texto headings</text>
  <text x="540" y="302" text-anchor="middle" font-size="10" fill="#94a3b8">Fondos oscuros</text>

  <rect x="620" y="240" width="130" height="80" rx="8" fill="#1e293b"/>
  <text x="685" y="258" text-anchor="middle" font-size="11" font-weight="700" fill="#e2e8f0">950</text>
  <text x="685" y="274" text-anchor="middle" font-size="10" fill="#94a3b8">Dark backgrounds</text>
  <text x="685" y="288" text-anchor="middle" font-size="10" fill="#94a3b8">Dark mode base</text>
  <text x="685" y="302" text-anchor="middle" font-size="10" fill="#94a3b8">Max contraste</text>
</svg>'''

# ─────────────────────────────────────────────────
# SVG 2: Escala de espaciado
# ─────────────────────────────────────────────────
svg2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="800" height="400" font-family="system-ui, sans-serif">
  <rect width="800" height="400" fill="#0f172a"/>
  <text x="400" y="30" text-anchor="middle" font-size="15" font-weight="700" fill="#f1f5f9" letter-spacing="1">ESCALA DE ESPACIADO TAILWIND — 1 unidad = 4px</text>
  <text x="400" y="50" text-anchor="middle" font-size="12" fill="#64748b">p-{n} px-{n} py-{n} m-{n} space-{n} gap-{n}</text>

  <!-- bars -->
  <!-- n=1 -->
  <text x="60" y="82" text-anchor="end" font-size="11" fill="#94a3b8">1</text>
  <rect x="70" y="70" width="4" height="18" rx="2" fill="#38bdf8"/>
  <text x="80" y="82" font-size="10" fill="#64748b">4px · p-1 / m-1</text>
  <text x="700" y="82" text-anchor="end" font-size="10" fill="#475569">micro spacing, separadores finos</text>

  <!-- n=2 -->
  <text x="60" y="112" text-anchor="end" font-size="11" fill="#94a3b8">2</text>
  <rect x="70" y="100" width="8" height="18" rx="2" fill="#38bdf8"/>
  <text x="84" y="112" font-size="10" fill="#64748b">8px · p-2 / m-2</text>
  <text x="700" y="112" text-anchor="end" font-size="10" fill="#475569">padding pequeño en badges</text>

  <!-- n=3 -->
  <text x="60" y="142" text-anchor="end" font-size="11" fill="#94a3b8">3</text>
  <rect x="70" y="130" width="12" height="18" rx="2" fill="#38bdf8"/>
  <text x="88" y="142" font-size="10" fill="#64748b">12px · p-3 / m-3</text>
  <text x="700" y="142" text-anchor="end" font-size="10" fill="#475569">botones pequeños</text>

  <!-- n=4 -->
  <text x="60" y="172" text-anchor="end" font-size="11" fill="#94a3b8">4</text>
  <rect x="70" y="160" width="16" height="18" rx="2" fill="#38bdf8"/>
  <text x="92" y="172" font-size="10" fill="#64748b">16px · p-4 / m-4</text>
  <text x="700" y="172" text-anchor="end" font-size="10" fill="#475569">padding base de componentes</text>

  <!-- n=5 -->
  <text x="60" y="202" text-anchor="end" font-size="11" fill="#94a3b8">5</text>
  <rect x="70" y="190" width="20" height="18" rx="2" fill="#38bdf8"/>
  <text x="96" y="202" font-size="10" fill="#64748b">20px · p-5 / m-5</text>
  <text x="700" y="202" text-anchor="end" font-size="10" fill="#475569">spacing entre íconos y texto</text>

  <!-- n=6 -->
  <text x="60" y="232" text-anchor="end" font-size="11" fill="#38bdf8" font-weight="700">6</text>
  <rect x="70" y="220" width="24" height="18" rx="2" fill="#0ea5e9"/>
  <text x="100" y="232" font-size="10" fill="#e2e8f0" font-weight="600">24px · p-6 / m-6  ← más usado en cards</text>
  <text x="700" y="232" text-anchor="end" font-size="10" fill="#38bdf8">★ padding de card</text>

  <!-- n=8 -->
  <text x="60" y="262" text-anchor="end" font-size="11" fill="#38bdf8" font-weight="700">8</text>
  <rect x="70" y="250" width="32" height="18" rx="2" fill="#0ea5e9"/>
  <text x="108" y="262" font-size="10" fill="#e2e8f0" font-weight="600">32px · p-8 / m-8  ← secciones y layouts</text>
  <text x="700" y="262" text-anchor="end" font-size="10" fill="#38bdf8">★ padding de sección</text>

  <!-- n=10 -->
  <text x="60" y="292" text-anchor="end" font-size="11" fill="#94a3b8">10</text>
  <rect x="70" y="280" width="40" height="18" rx="2" fill="#38bdf8"/>
  <text x="116" y="292" font-size="10" fill="#64748b">40px · p-10 / m-10</text>
  <text x="700" y="292" text-anchor="end" font-size="10" fill="#475569">separación entre secciones</text>

  <!-- n=12 -->
  <text x="60" y="322" text-anchor="end" font-size="11" fill="#94a3b8">12</text>
  <rect x="70" y="310" width="48" height="18" rx="2" fill="#38bdf8"/>
  <text x="124" y="322" font-size="10" fill="#64748b">48px · p-12 / m-12</text>
  <text x="700" y="322" text-anchor="end" font-size="10" fill="#475569">héros, secciones grandes</text>

  <!-- n=16 -->
  <text x="60" y="352" text-anchor="end" font-size="11" fill="#94a3b8">16</text>
  <rect x="70" y="340" width="64" height="18" rx="2" fill="#38bdf8"/>
  <text x="140" y="352" font-size="10" fill="#64748b">64px · p-16 / m-16</text>
  <text x="700" y="352" text-anchor="end" font-size="10" fill="#475569">espaciado vertical de página</text>

  <!-- Formula -->
  <rect x="240" y="368" width="320" height="26" rx="6" fill="#1e293b"/>
  <text x="400" y="385" text-anchor="middle" font-size="12" font-weight="600" fill="#38bdf8">Fórmula: valor × 4 = px  (p-6 = 24px, p-8 = 32px)</text>
</svg>'''

# ─────────────────────────────────────────────────
# SVG 3: Jerarquía tipográfica
# ─────────────────────────────────────────────────
svg3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="800" height="420" font-family="system-ui, sans-serif">
  <rect width="800" height="420" fill="#0f172a"/>
  <text x="400" y="30" text-anchor="middle" font-size="15" font-weight="700" fill="#f1f5f9" letter-spacing="1">JERARQUÍA TIPOGRÁFICA EN TAILWIND</text>

  <!-- Left col: scale -->
  <rect x="20" y="44" width="340" height="360" rx="10" fill="#1e293b"/>
  <text x="190" y="66" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="700">ESCALA DE TAMAÑOS</text>
  <text x="30" y="92" font-size="9" fill="#94a3b8">text-xs        12px</text>
  <text x="30" y="116" font-size="10" fill="#94a3b8">text-sm      14px</text>
  <text x="30" y="144" font-size="11" fill="#94a3b8">text-base    16px</text>
  <text x="30" y="175" font-size="13" fill="#94a3b8">text-lg      18px</text>
  <text x="30" y="208" font-size="14" fill="#cbd5e1">text-xl      20px</text>
  <text x="30" y="244" font-size="16" fill="#e2e8f0">text-2xl   24px</text>
  <text x="30" y="282" font-size="18" fill="#f1f5f9" font-weight="600">text-3xl  30px</text>
  <text x="30" y="323" font-size="22" fill="#f1f5f9" font-weight="700">text-4xl 36px</text>
  <text x="30" y="368" font-size="27" fill="#38bdf8" font-weight="800">text-5xl 48px</text>
  <text x="30" y="398" font-size="12" fill="#475569">↑ Hero headline</text>

  <!-- Right col: weights -->
  <rect x="380" y="44" width="400" height="360" rx="10" fill="#1e293b"/>
  <text x="580" y="66" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="700">PESOS (font-weight)</text>

  <text x="390" y="96" font-size="15" font-weight="100" fill="#64748b">font-thin     — 100</text>
  <text x="390" y="122" font-size="15" font-weight="300" fill="#94a3b8">font-light    — 300</text>
  <text x="390" y="148" font-size="15" font-weight="400" fill="#cbd5e1">font-normal  — 400 · cuerpo texto</text>
  <text x="390" y="174" font-size="15" font-weight="500" fill="#e2e8f0">font-medium — 500 · labels, nav</text>
  <text x="390" y="200" font-size="15" font-weight="600" fill="#f1f5f9">font-semibold — 600 · subtítulos</text>
  <text x="390" y="228" font-size="15" font-weight="700" fill="#f1f5f9">font-bold — 700 · headings</text>
  <text x="390" y="256" font-size="15" font-weight="800" fill="#f8fafc">font-extrabold — 800</text>
  <text x="390" y="284" font-size="15" font-weight="900" fill="#38bdf8">font-black — 900 · impact</text>

  <line x1="390" y1="300" x2="765" y2="300" stroke="#334155" stroke-width="1"/>
  <text x="580" y="320" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="700">LINE-HEIGHT (leading)</text>
  <text x="390" y="340" font-size="13" fill="#94a3b8">leading-tight   1.25 · headings cortos</text>
  <text x="390" y="360" font-size="13" fill="#94a3b8">leading-normal  1.5 · default</text>
  <text x="390" y="380" font-size="13" fill="#e2e8f0">leading-relaxed 1.625 · cuerpo de texto</text>
  <text x="390" y="400" font-size="13" fill="#64748b">leading-loose   2.0 · muy aireado</text>
</svg>'''

# ─────────────────────────────────────────────────
# SVG 4: Text overflow y control de texto
# ─────────────────────────────────────────────────
svg4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 360" width="800" height="360" font-family="system-ui, sans-serif">
  <rect width="800" height="360" fill="#0f172a"/>
  <text x="400" y="30" text-anchor="middle" font-size="15" font-weight="700" fill="#f1f5f9" letter-spacing="1">CONTROL DE TEXTO: TRUNCATE, LINE-CLAMP, WRAPPING</text>

  <!-- Truncate demo -->
  <rect x="30" y="48" width="220" height="90" rx="8" fill="#1e293b"/>
  <text x="140" y="68" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="700">truncate</text>
  <rect x="44" y="76" width="192" height="24" rx="4" fill="#0f172a"/>
  <text x="44" y="92" font-size="11" fill="#e2e8f0" clip-path="url(#c1)">Título de producto muy largo...</text>
  <clipPath id="c1"><rect x="44" y="76" width="185" height="24"/></clipPath>
  <text x="140" y="122" text-anchor="middle" font-size="9" fill="#64748b">1 línea + elipsis</text>
  <text x="140" y="134" text-anchor="middle" font-size="9" fill="#64748b">necesita ancho definido</text>

  <!-- Line clamp 2 demo -->
  <rect x="270" y="48" width="220" height="90" rx="8" fill="#1e293b"/>
  <text x="380" y="68" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="700">line-clamp-2</text>
  <rect x="284" y="76" width="192" height="44" rx="4" fill="#0f172a"/>
  <text x="290" y="93" font-size="10" fill="#e2e8f0">Descripción extensa del</text>
  <text x="290" y="108" font-size="10" fill="#e2e8f0">producto que se corta aquí…</text>
  <text x="380" y="129" text-anchor="middle" font-size="9" fill="#64748b">2 líneas + elipsis</text>

  <!-- Line clamp 3 demo -->
  <rect x="510" y="48" width="260" height="90" rx="8" fill="#1e293b"/>
  <text x="640" y="68" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="700">line-clamp-3</text>
  <rect x="524" y="76" width="232" height="56" rx="4" fill="#0f172a"/>
  <text x="530" y="93" font-size="10" fill="#e2e8f0">Contenido extenso primera línea</text>
  <text x="530" y="108" font-size="10" fill="#e2e8f0">Segunda línea del texto</text>
  <text x="530" y="123" font-size="10" fill="#e2e8f0">Tercera línea y corte aquí…</text>

  <!-- Whitespace -->
  <rect x="30" y="158" width="350" height="90" rx="8" fill="#1e293b"/>
  <text x="205" y="178" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="700">whitespace-*</text>
  <rect x="44" y="186" width="322" height="52" rx="4" fill="#0f172a"/>
  <text x="52" y="202" font-size="10" fill="#64748b">whitespace-normal</text>
  <text x="52" y="215" font-size="9" fill="#94a3b8">→ colapsa espacios, hace wrap (default)</text>
  <text x="52" y="228" font-size="10" fill="#64748b">whitespace-nowrap</text>
  <text x="52" y="228" font-size="5" fill="#f87171">                         → nunca hace wrap (cuidado con overflow)</text>

  <!-- Word break -->
  <rect x="400" y="158" width="370" height="90" rx="8" fill="#1e293b"/>
  <text x="585" y="178" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="700">break-*</text>
  <rect x="414" y="186" width="342" height="52" rx="4" fill="#0f172a"/>
  <text x="422" y="202" font-size="10" fill="#64748b">break-words</text>
  <text x="422" y="215" font-size="9" fill="#94a3b8">→ corta URLs y palabras largas para evitar overflow</text>
  <text x="422" y="228" font-size="10" fill="#64748b">break-all</text>
  <text x="422" y="228" font-size="5" fill="#94a3b8">                   → corte en cualquier carácter (más agresivo)</text>

  <!-- Alignment row -->
  <rect x="30" y="268" width="740" height="72" rx="8" fill="#1e293b"/>
  <text x="400" y="288" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="700">ALINEACIÓN DE TEXTO</text>
  <rect x="44" y="296" width="160" height="32" rx="4" fill="#0f172a"/>
  <text x="52" y="316" font-size="12" fill="#e2e8f0">text-left</text>
  <rect x="220" y="296" width="160" height="32" rx="4" fill="#0f172a"/>
  <text x="300" y="316" text-anchor="middle" font-size="12" fill="#e2e8f0">text-center</text>
  <rect x="396" y="296" width="160" height="32" rx="4" fill="#0f172a"/>
  <text x="548" y="316" text-anchor="end" font-size="12" fill="#e2e8f0">text-right</text>
  <rect x="572" y="296" width="184" height="32" rx="4" fill="#0f172a"/>
  <text x="580" y="308" font-size="11" fill="#38bdf8">text-balance</text>
  <text x="580" y="322" font-size="9" fill="#64748b">balancea líneas en headings</text>
</svg>'''

# ─────────────────────────────────────────────────
# SVG 5: Sistema de diseño 60-30-10
# ─────────────────────────────────────────────────
svg5 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" width="800" height="380" font-family="system-ui, sans-serif">
  <rect width="800" height="380" fill="#0f172a"/>
  <text x="400" y="30" text-anchor="middle" font-size="15" font-weight="700" fill="#f1f5f9" letter-spacing="1">SISTEMA DE DISEÑO: REGLA 60-30-10</text>

  <!-- 60% neutral -->
  <rect x="30" y="50" width="440" height="200" rx="10" fill="#f8fafc"/>
  <text x="250" y="78" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">60% — Color Neutro</text>
  <text x="250" y="96" text-anchor="middle" font-size="11" fill="#475569">bg-white / bg-gray-50 / bg-slate-50</text>
  <text x="250" y="112" text-anchor="middle" font-size="11" fill="#475569">Fondo de página, fondo de cards, zonas de contenido</text>

  <!-- 30% secondary -->
  <rect x="50" y="128" width="200" height="100" rx="8" fill="#f1f5f9"/>
  <text x="150" y="152" text-anchor="middle" font-size="12" font-weight="600" fill="#334155">30% — Secundario</text>
  <text x="150" y="170" text-anchor="middle" font-size="10" fill="#64748b">bg-gray-100 a gray-200</text>
  <text x="150" y="185" text-anchor="middle" font-size="10" fill="#64748b">Sidebar, headers, dividers</text>
  <text x="150" y="200" text-anchor="middle" font-size="10" fill="#64748b">Fondos de sección alternos</text>

  <!-- 10% accent -->
  <rect x="268" y="128" width="182" height="100" rx="8" fill="#0ea5e9"/>
  <text x="359" y="152" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">10% — Acento</text>
  <text x="359" y="170" text-anchor="middle" font-size="10" fill="#bae6fd">bg-sky-500 / emerald / violet</text>
  <text x="359" y="185" text-anchor="middle" font-size="10" fill="#bae6fd">Botones CTA, iconos clave</text>
  <text x="359" y="200" text-anchor="middle" font-size="10" fill="#bae6fd">Links, highlights, badges</text>

  <!-- Arrow + label -->
  <text x="248" y="240" text-anchor="middle" font-size="10" fill="#64748b">Cuanto menos área, más saturación/impacto</text>

  <!-- Sistema coherente: tres pilares -->
  <rect x="30" y="268" width="740" height="100" rx="10" fill="#1e293b"/>
  <text x="400" y="292" text-anchor="middle" font-size="13" font-weight="700" fill="#38bdf8">Los Tres Pilares del Sistema</text>

  <rect x="50" y="304" width="200" height="52" rx="6" fill="#0f172a"/>
  <text x="150" y="322" text-anchor="middle" font-size="12" font-weight="600" fill="#38bdf8">🎨 Color</text>
  <text x="150" y="340" text-anchor="middle" font-size="10" fill="#94a3b8">Paleta semántica limitada</text>
  <text x="150" y="352" text-anchor="middle" font-size="10" fill="#94a3b8">Escala 50-950, WCAG AA</text>

  <rect x="300" y="304" width="200" height="52" rx="6" fill="#0f172a"/>
  <text x="400" y="322" text-anchor="middle" font-size="12" font-weight="600" fill="#38bdf8">🔤 Tipografía</text>
  <text x="400" y="340" text-anchor="middle" font-size="10" fill="#94a3b8">Escala xs → 5xl + pesos</text>
  <text x="400" y="352" text-anchor="middle" font-size="10" fill="#94a3b8">leading-relaxed en body</text>

  <rect x="550" y="304" width="200" height="52" rx="6" fill="#0f172a"/>
  <text x="650" y="322" text-anchor="middle" font-size="12" font-weight="600" fill="#38bdf8">📐 Espaciado</text>
  <text x="650" y="340" text-anchor="middle" font-size="10" fill="#94a3b8">Múltiplos de 4px</text>
  <text x="650" y="352" text-anchor="middle" font-size="10" fill="#94a3b8">p-4, p-6, py-12 consistentes</text>

  <!-- 60-30-10 legend -->
  <text x="510" y="80" font-size="28" font-weight="900" fill="#f1f5f9">60%</text>
  <text x="510" y="100" font-size="11" fill="#64748b">espacio neutro</text>
  <text x="510" y="140" font-size="28" font-weight="900" fill="#94a3b8">30%</text>
  <text x="510" y="160" font-size="11" fill="#64748b">tono secundario</text>
  <text x="510" y="200" font-size="28" font-weight="900" fill="#38bdf8">10%</text>
  <text x="510" y="220" font-size="11" fill="#64748b">acento vibrante</text>
</svg>'''

svgs = {
    "01-paleta-colores.svg": svg1,
    "02-escala-espaciado.svg": svg2,
    "03-tipografia-jerarquia.svg": svg3,
    "04-text-overflow.svg": svg4,
    "05-sistema-diseno.svg": svg5,
}

for fname, content in svgs.items():
    path = os.path.join(BASE, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ {path}")

print(f"\n✅ {len(svgs)} SVGs created for week-03.")
