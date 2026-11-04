"""Genera los SVG del perfil con estética de HUD/menú de Rocket League.

Uso: python assets/generar_perfil.py   (escribe los archivos en assets/)
"""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parent

# ------------------------------------------------------------------ datos
USUARIO = "HerSamm"
TITULO = "Desarrollador .NET"
SUBTITULO = "C# · .NET · ASP.NET Core Minimal APIs"
UBICACION = "Mariano Roque Alonso, Paraguay"
EMAIL = "samulopez424@gmail.com"
LINKEDIN = "in/hermes-lópez-5b46b32a9"

# Loadout: (ranura del garage, categoría real, [(tecnología, color)])
LOADOUT = [
    ("Cuerpo",           "Lenguajes", [("C#", "#9B4F96"), ("JavaScript", "#F7DF1E"), ("HTML5", "#E34F26"), ("CSS", "#1572B6")]),
    ("Boost",            "Backend",   [(".NET", "#512BD4"), ("ASP.NET Core", "#7B4FD8"), ("Minimal APIs", "#512BD4")]),
    ("Calcomanía",       "Frontend",  [("HTML", "#E34F26"), ("CSS", "#1572B6")]),
    ("Ruedas",           "Datos",     [("Entity Framework Core", "#8E44AD"), ("SQL Server", "#CC2927"), ("MySQL", "#00758F")]),
    ("Explosión de gol", "Testing",   [("Swagger", "#85EA2D"), ("Postman", "#FF6C37")]),
]

# ----------------------------------------------------------------- estilo
W = 880
BLUE, ORANGE = "#1f8fff", "#ff7a1a"
CSS = f"""
  text {{ font-family: Bahnschrift, 'DIN Alternate', 'Arial Narrow', 'Segoe UI', Arial, sans-serif; font-style: italic; }}
  :where(text:not([fill])) {{ fill: #ffffff; }}
  :where(text:not([font-size])) {{ font-size: 13px; }}
  :where(text:not([font-weight])) {{ font-weight: 700; }}
  .in {{ animation: slide .45s cubic-bezier(.2,.8,.3,1) backwards; }}
  .fade {{ animation: fade .4s ease-out backwards; }}
  @keyframes slide {{ from {{ transform: translateX(-26px); opacity: 0; }} to {{ transform: none; opacity: 1; }} }}
  @keyframes fade {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} .ring {{ stroke-dashoffset: 0 !important; }} }}
"""

DEFS = f"""
  <linearGradient id="navy" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1838"/><stop offset="1" stop-color="#070d22"/></linearGradient>
  <radialGradient id="gb" cx="0" cy="0" r="1"><stop offset="0" stop-color="{BLUE}" stop-opacity=".35"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
  <radialGradient id="go" cx="1" cy="1" r="1"><stop offset="0" stop-color="{ORANGE}" stop-opacity=".3"/><stop offset="1" stop-color="{ORANGE}" stop-opacity="0"/></radialGradient>
  <pattern id="hex" width="28" height="48.5" patternUnits="userSpaceOnUse"><path d="M14 0L28 8.08V24.25L14 32.33L0 24.25V8.08Z M14 32.33V48.5" fill="none" stroke="#fff" stroke-opacity=".045"/></pattern>
"""

def svg(w, h, title, body, css="", defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t">\n'
            f'<title id="t">{escape(title)}</title>\n<style>{CSS}{css}</style>\n<defs>{DEFS}{defs}</defs>\n{body}\n</svg>\n')

def para(x, y, w, h, k=10):
    """Paralelogramo inclinado (la forma típica de los menús de RL)."""
    return f"{x + k},{y} {x + w},{y} {x + w - k},{y + h} {x},{y + h}"

def arena_bg(w, h, rx=14):
    return (f'<clipPath id="c"><rect width="{w}" height="{h}" rx="{rx}"/></clipPath>'
            f'<g clip-path="url(#c)"><rect width="{w}" height="{h}" fill="url(#navy)"/><rect width="{w}" height="{h}" fill="url(#hex)"/>'
            f'<rect width="{w}" height="{h}" fill="url(#gb)"/><rect width="{w}" height="{h}" fill="url(#go)"/></g>'
            f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="{rx}" fill="none" stroke="#24345f"/>')

def tw(s, px=8.6):
    return len(s) * px

# ------------------------------------------------------------------- hero
def hero():
    H = 262
    cx, cy, r = 770, 150, 60
    circ = 2 * 3.14159 * r
    css = f"""
  .flash {{ opacity: 0; animation: flash .55s ease-out; transform-box: fill-box; transform-origin: center; }}
  .ring {{ stroke-dasharray: {circ:.1f}; stroke-dashoffset: {circ:.1f}; animation: fill 1.4s cubic-bezier(.3,.6,.3,1) 2.3s forwards; }}
  .pulse {{ animation: pulse 1.6s ease-in-out 3.7s infinite alternate; }}
  @keyframes flash {{ 0% {{ opacity: 0; transform: scale(1.8); }} 25% {{ opacity: 1; transform: scale(1); }} 80% {{ opacity: 1; }} 100% {{ opacity: 0; transform: scale(.9); }} }}
  @keyframes fill {{ to {{ stroke-dashoffset: 0; }} }}
  @keyframes pulse {{ from {{ opacity: .35; }} to {{ opacity: .9; }} }}
"""
    defs = f'<linearGradient id="boost" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#ffb347"/><stop offset="1" stop-color="{ORANGE}"/></linearGradient>'
    count = "".join(
        f'<text class="flash" x="{cx}" y="{cy + 16}" text-anchor="middle" font-size="{46 if t != "GO!" else 40}" font-weight="900" '
        f'fill="{"#ffffff" if t != "GO!" else ORANGE}" style="animation-delay:{.3 + i * .55:.2f}s">{t}</text>'
        for i, t in enumerate(["3", "2", "1", "GO!"]))
    ticks = "".join(
        f'<line x1="{cx}" y1="{cy - r - 13}" x2="{cx}" y2="{cy - r - 8}" stroke="#4a5d8f" stroke-width="2" transform="rotate({a} {cx} {cy})"/>'
        for a in range(0, 360, 30))
    body = f'''{arena_bg(W, H)}
<!-- Marcador -->
<polygon points="{para(262, 0, 150, 38, -12)}" fill="{BLUE}"/>
<polygon points="{para(404, 0, 72, 38, 0)}" fill="#0a1330" stroke="#24345f"/>
<polygon points="{para(468, 0, 150, 38, 12)}" fill="{ORANGE}"/>
<text x="292" y="25" font-size="14" font-weight="800">{escape(USUARIO.upper())}</text>
<text x="392" y="27" text-anchor="end" font-size="20" font-weight="900">3</text>
<text x="440" y="26" text-anchor="middle" font-size="18" font-weight="800">5:00</text>
<text x="488" y="27" font-size="20" font-weight="900">0</text>
<text x="590" y="25" text-anchor="end" font-size="14" font-weight="800">BUGS</text>

<!-- Banner de jugador -->
<g class="in" style="animation-delay:.2s">
  <polygon points="{para(24, 62, 560, 176, 18)}" fill="#0c1a3f" fill-opacity=".9" stroke="#24345f"/>
  <polygon points="{para(24, 62, 26, 176, 18)}" fill="{BLUE}"/>
  <polygon points="{para(560, 62, 24, 10, 4)}" fill="{ORANGE}"/>
</g>
<g class="in" style="animation-delay:.45s">
  <text x="69" y="133" font-size="58" font-weight="900" fill="{BLUE}" fill-opacity=".55">{escape(USUARIO.upper())}</text>
  <text x="66" y="130" font-size="58" font-weight="900">{escape(USUARIO.upper())}</text>
</g>
<text class="in" x="66" y="164" font-size="20" font-weight="800" fill="{ORANGE}" style="animation-delay:.65s">{escape(TITULO.upper())}</text>
<text class="in" x="64" y="192" font-size="14" font-weight="600" fill="#c7d3f2" style="animation-delay:.8s">{escape(SUBTITULO)}</text>
<g class="in" style="animation-delay:.95s">
  <path d="M68 206c-3.6 0-6.5 2.8-6.5 6.3 0 4.7 6.5 10.4 6.5 10.4s6.5-5.7 6.5-10.4c0-3.5-2.9-6.3-6.5-6.3zm0 8.7a2.4 2.4 0 1 1 0-4.8 2.4 2.4 0 0 1 0 4.8z" fill="{BLUE}"/>
  <text x="80" y="219" font-size="13" font-weight="600" fill="#c7d3f2">{escape(UBICACION)}</text>
</g>

<!-- Medidor de boost con cuenta regresiva de kickoff -->
<circle class="pulse" cx="{cx}" cy="{cy}" r="{r + 18}" fill="{ORANGE}" fill-opacity=".12"/>
{ticks}
<circle cx="{cx}" cy="{cy}" r="{r}" fill="#081029" stroke="#1a2a55" stroke-width="12"/>
<circle class="ring" cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="url(#boost)" stroke-width="12" stroke-linecap="round" transform="rotate(-90 {cx} {cy})"/>
{count}
<g class="fade" style="animation-delay:3.4s">
  <text x="{cx}" y="{cy + 12}" text-anchor="middle" font-size="40" font-weight="900">100</text>
  <text x="{cx}" y="{cy + 32}" text-anchor="middle" font-size="12" font-weight="800" fill="{ORANGE}" letter-spacing="2">BOOST</text>
</g>'''
    title = f"{USUARIO} — {TITULO} · {SUBTITULO} · {UBICACION}"
    return svg(W, H, title, body, css, defs)

# ---------------------------------------------------------------- botones
ICONS = {
    "linkedin": '<text x="40" y="40" text-anchor="middle" font-size="18" font-weight="900" font-style="normal">in</text>',
    "email": '<path d="M29 23h22a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H29a2 2 0 0 1-2-2V25a2 2 0 0 1 2-2zm0 2v.6l11 6.8 11-6.8V25H29zm22 3.3-11 6.7-11-6.7V39h22z" fill="#fff"/>',
}

def boton(icono, accion, titulo, sub, color):
    w, h = 440, 64
    css = """
  .shine { animation: shine 4s ease-in-out infinite; }
  @keyframes shine { 0%, 70% { transform: translateX(-120px); } 100% { transform: translateX(560px); } }
"""
    defs = '<linearGradient id="sh" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".18"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
    body = f'''<clipPath id="b"><polygon points="{para(6, 4, w - 12, h - 8, 14)}"/></clipPath>
<polygon points="{para(6, 4, w - 12, h - 8, 14)}" fill="#0c1a3f" stroke="{color}" stroke-width="1.5"/>
<g clip-path="url(#b)">
  <polygon points="{para(6, 4, 66, h - 8, 14)}" fill="{color}"/>
  <rect class="shine" x="0" y="0" width="80" height="{h}" fill="url(#sh)" transform="skewX(-20)"/>
</g>
{ICONS[icono]}
<text x="84" y="25" font-size="10.5" font-weight="700" fill="{color}" letter-spacing="1.5">{escape(accion.upper())}</text>
<text x="84" y="44" font-size="17" font-weight="900">{escape(titulo.upper())}</text>
<text x="{84 + tw(titulo, 11.5) + 8:.0f}" y="44" font-size="12" font-weight="500" fill="#c7d3f2">{escape(sub)}</text>
<polygon points="{w - 44},26 {w - 30},32 {w - 44},38" fill="{color}"/>'''
    return svg(w, h, f"{titulo}: {sub}", body, css, defs)

# ---------------------------------------------------------------- loadout
def loadout():
    top, row_h = 66, 52
    H = top + len(LOADOUT) * row_h + 16
    parts = [arena_bg(W, H),
             f'<polygon points="{para(0, 0, 170, 40, -16)}" fill="{BLUE}"/>',
             '<text x="22" y="27" font-size="18" font-weight="900" letter-spacing="1">LOADOUT</text>',
             '<text x="186" y="27" font-size="14" font-weight="600" fill="#c7d3f2">Stack tecnológico</text>',
             f'<polygon points="{para(W - 150, 14, 60, 8, 4)}" fill="{BLUE}"/><polygon points="{para(W - 84, 14, 60, 8, 4)}" fill="{ORANGE}"/>',
             f'<line x1="16" y1="50.5" x2="{W - 16}" y2="50.5" stroke="#24345f"/>']
    d = .15
    for i, (slot, cat, items) in enumerate(LOADOUT):
        y = top + i * row_h
        parts.append(f'<g class="in" style="animation-delay:{d:.2f}s">'
                     f'<text x="26" y="{y + 15}" font-size="10.5" font-weight="700" fill="{ORANGE}" letter-spacing="1.5">{escape(slot.upper())}</text>'
                     f'<text x="26" y="{y + 35}" font-size="17" font-weight="900">{escape(cat.upper())}</text></g>')
        x = 200
        for name, color in items:
            w = tw(name.upper(), 8.4) + 42
            d += .07
            parts.append(
                f'<g class="in" style="animation-delay:{d:.2f}s">'
                f'<polygon points="{para(x, y + 4, w, 34, 9)}" fill="#13224d" stroke="#2a3d73"/>'
                f'<polygon points="{para(x, y + 4, 18, 34, 9)}" fill="{color}"/>'
                f'<text x="{x + 24}" y="{y + 26}" font-size="13.5" font-weight="800">{escape(name.upper())}</text></g>')
            x += w + 6
        if i < len(LOADOUT) - 1:
            parts.append(f'<line x1="26" y1="{y + row_h - 3}" x2="{W - 26}" y2="{y + row_h - 3}" stroke="#18264d" stroke-dasharray="2 5"/>')
    alt = "Loadout / stack tecnológico — " + ". ".join(f"{c}: {', '.join(n for n, _ in it)}" for _, c, it in LOADOUT)
    return svg(W, H, alt, "\n".join(parts))

def h_arena():
    h = 50
    body = f'''<polygon points="{para(0, 6, 190, 38, -16)}" fill="{ORANGE}"/>
<text x="22" y="32" font-size="18" font-weight="900" letter-spacing="1">FREE PLAY</text>
<text x="206" y="32" font-size="14" font-weight="600" fill="#c7d3f2">Garage · cada tecnología con su auto</text>
<polygon points="{para(W - 150, 21, 60, 8, 4)}" fill="{BLUE}"/><polygon points="{para(W - 84, 21, 60, 8, 4)}" fill="{ORANGE}"/>'''
    return svg(W, h, "Free play — Garage", body)

FILES = {
    "hero.svg": hero(),
    "btn-linkedin.svg": boton("linkedin", "Agregar amigo", "LinkedIn", LINKEDIN, BLUE),
    "btn-email.svg": boton("email", "Enviar mensaje", "Email", EMAIL, ORANGE),
    "stack.svg": loadout(),
    "h-arena.svg": h_arena(),
}
for name, content in FILES.items():
    (OUT / name).write_text(content, encoding="utf-8")
    print("escrito", name)
