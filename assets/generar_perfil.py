"""Genera los SVG del perfil con estética de API: hero, botones de contacto, stack y cabecera del garage.

Uso: python assets/generar_perfil.py   (escribe los archivos en assets/)
"""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parent

# ------------------------------------------------------------------ datos
USUARIO = "HerSamm"
ROL = "Desarrollador .NET"
UBICACION = "Mariano Roque Alonso, Paraguay"
ROLES_ROTATIVOS = ["Desarrollador .NET", "APIs con ASP.NET Core", "Minimal APIs + EF Core"]
EMAIL = "samulopez424@gmail.com"
LINKEDIN = "in/hermes-lópez-5b46b32a9"

JSON = [  # (sangría, [(clase, texto), ...])
    (0, [("p", "{")]),
    (1, [("k", '"usuario"'), ("p", ": "), ("s", f'"{USUARIO}"'), ("p", ",")]),
    (1, [("k", '"rol"'), ("p", ": "), ("s", f'"{ROL}"'), ("p", ",")]),
    (1, [("k", '"ubicacion"'), ("p", ": "), ("s", '"Mariano Roque Alonso, PY"'), ("p", ",")]),
    (1, [("k", '"enfoque"'), ("p", ": "), ("s", '"ASP.NET Core Minimal APIs"'), ("p", ",")]),
    (1, [("k", '"datos"'), ("p", ": ["), ("s", '"EF Core"'), ("p", ", "), ("s", '"SQL Server"'), ("p", ", "), ("s", '"MySQL"'), ("p", "]")]),
    (0, [("p", "}")]),
]

STACK = [  # (categoría, [(nombre, color, sigla, color de sigla)])
    ("Lenguajes", [("C#", "#9B4F96", "C#", "#fff"), ("JavaScript", "#F7DF1E", "JS", "#111"),
                   ("HTML5", "#E34F26", "5", "#fff"), ("CSS", "#1572B6", "3", "#fff")]),
    ("Backend", [(".NET", "#512BD4", ".N", "#fff"), ("ASP.NET Core", "#5C2D91", "AS", "#fff"),
                 ("Minimal APIs", "#512BD4", "MA", "#fff")]),
    ("Frontend", [("HTML", "#E34F26", "5", "#fff"), ("CSS", "#1572B6", "3", "#fff")]),
    ("Datos", [("Entity Framework Core", "#68217A", "EF", "#fff"), ("SQL Server", "#CC2927", "SQ", "#fff"),
               ("MySQL", "#00758F", "My", "#fff")]),
    ("Testing", [("Swagger", "#85EA2D", "Sw", "#111"), ("Postman", "#FF6C37", "Po", "#fff")]),
]

# ----------------------------------------------------------------- estilo
W = 880
BASE_CSS = """
  text { font-family: 'Segoe UI', -apple-system, 'Helvetica Neue', Arial, sans-serif; }
  :where(text:not([fill])) { fill: #9a9ab0; }
  :where(text:not([font-size])) { font-size: 13px; }
  .mono { font-family: Consolas, Menlo, 'Fira Code', 'Courier New', monospace; }
  .fg { fill: #e6e6f0; } .soft { fill: #c9c9d9; } .brand { fill: #a397f7; } .ok { fill: #10b981; } .cyan { fill: #00b4d8; }
  .k { fill: #a397f7; } .s { fill: #34d399; } .p { fill: #8b8ba3; }
  .j { animation: show .3s ease-out backwards; }
  @keyframes show { from { opacity: 0; } to { opacity: 1; } }
  @keyframes blink { 50% { opacity: 0; } }
  @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
"""

def svg(w, h, title, body, css=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t">\n'
            f'<title id="t">{escape(title)}</title>\n<style>{BASE_CSS}{css}</style>\n{body}\n</svg>\n')

def header_bar(path, titulo, y=0):
    """Barra 'GET /ruta  Título ----- 200 OK'."""
    tx = 68 + len(path) * 7.8 + 16
    return f'''<g transform="translate(0 {y})">
  <rect x=".5" y=".5" width="{W-1}" height="47" rx="10" fill="#0f1a22" stroke="#1e4a55"/>
  <rect x="16" y="14" width="40" height="20" rx="4" fill="#00b4d8"/>
  <text x="36" y="28" text-anchor="middle" class="mono" font-size="11" font-weight="700" fill="#06222b">GET</text>
  <text x="68" y="29" class="mono fg" font-size="13">{escape(path)}</text>
  <text x="{tx:.0f}" y="29" class="fg" font-size="15" font-weight="700">{escape(titulo)}</text>
  <line x1="{tx + len(titulo) * 8.6 + 16:.0f}" y1="24" x2="{W-80}" y2="24" stroke="#2a3a44" stroke-dasharray="4 4"/>
  <text x="{W-16}" y="29" text-anchor="end" class="mono ok" font-size="12">200 OK</text>
</g>'''

# ------------------------------------------------------------------- hero
def hero():
    H = 262
    lines = []
    for i, (ind, toks) in enumerate(JSON):
        spans = "".join(f'<tspan class="{c}">{escape(t)}</tspan>' for c, t in toks)
        lines.append(f'<text x="{458 + ind * 18}" y="{108 + i * 19}" class="mono j" font-size="12.5" '
                     f'style="animation-delay:{1.5 + i * .12:.2f}s" xml:space="preserve">{spans}</text>')
    n = len(ROLES_ROTATIVOS)
    cyc = 4 * n
    roles = "".join(
        f'<text x="40" y="216" class="mono role" font-size="13" style="animation-delay:{i * 4 - (0 if i == 0 else 0)}s">{escape(r)}</text>'
        for i, r in enumerate(ROLES_ROTATIVOS))
    vis = 100 / n
    css = f"""
  .path {{ animation: type 1s steps(16) .3s backwards; }}
  .pending {{ opacity: 0; animation: pending 1.5s linear; }}
  .done {{ animation: show .3s ease-out 1.5s backwards; }}
  .role {{ fill: #00b4d8; opacity: 0; animation: role {cyc}s linear infinite backwards; }}
  .cursor {{ animation: blink 1.1s step-end infinite; }}
  @keyframes type {{ from {{ clip-path: inset(0 100% 0 0); }} to {{ clip-path: inset(0 0 0 0); }} }}
  @keyframes pending {{ from, to {{ opacity: 1; }} }}
  @keyframes role {{ 0% {{ opacity: 0; }} 2% {{ opacity: 1; }} {vis - 2:.1f}% {{ opacity: 1; }} {vis:.1f}%, 100% {{ opacity: 0; }} }}
"""
    body = f'''<defs>
  <pattern id="grid" width="22" height="22" patternUnits="userSpaceOnUse"><path d="M22 0H0V22" fill="none" stroke="#a397f7" stroke-opacity=".06"/></pattern>
  <radialGradient id="glow" cx=".15" cy=".3" r=".6"><stop offset="0" stop-color="#5b3fd6" stop-opacity=".28"/><stop offset="1" stop-color="#5b3fd6" stop-opacity="0"/></radialGradient>
</defs>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="12" fill="#0e0e17" stroke="#26263a"/>
<rect x="1" y="35" width="{W-2}" height="{H-36}" fill="url(#grid)"/>
<rect x="1" y="35" width="{W-2}" height="{H-36}" fill="url(#glow)"/>
<line x1="1" y1="34.5" x2="{W-1}" y2="34.5" stroke="#26263a"/>
<text x="18" y="22" class="mono" font-size="12"><tspan class="brand">{{ }}</tspan> <tspan class="fg" font-weight="700">{escape(USUARIO.lower())}</tspan><tspan class="p"> / API v1</tspan></text>
<g class="pending"><circle cx="{W-96}" cy="18" r="4" fill="#f59e0b"/><text x="{W-86}" y="22" class="mono" font-size="12" fill="#f59e0b">pendiente…</text></g>
<g class="done"><circle cx="{W-76}" cy="18" r="4" fill="#10b981"/><text x="{W-66}" y="22" class="mono ok" font-size="12">200 OK</text></g>

<rect x="24" y="54" width="40" height="20" rx="4" fill="#00b4d8"/>
<text x="44" y="68" text-anchor="middle" class="mono" font-size="11" font-weight="700" fill="#06222b">GET</text>
<text x="74" y="69" class="mono soft path" font-size="13">/api/v1/{escape(USUARIO.lower())}</text>
<text x="22" y="124" class="fg" font-size="44" font-weight="700">{escape(USUARIO)}</text>
<text x="24" y="154" class="soft" font-size="17" font-weight="600">{escape(ROL)} · C# / .NET</text>
<path d="M30 168c-3.9 0-7 3-7 6.8 0 5 7 11.2 7 11.2s7-6.2 7-11.2c0-3.8-3.1-6.8-7-6.8zm0 9.4a2.6 2.6 0 1 1 0-5.2 2.6 2.6 0 0 1 0 5.2z" fill="#00b4d8"/>
<text x="44" y="182" class="soft" font-size="13">{escape(UBICACION)}</text>
<text x="24" y="216" class="mono cyan" font-size="13">&gt;</text>
{roles}
<rect class="cursor" x="210" y="205" width="7" height="14" fill="#a397f7"/>

<rect x="440.5" y="52.5" width="415" height="187" rx="8" fill="#0a0a12" stroke="#26263a"/>
<text x="456" y="72" font-size="11">Respuesta</text>
<text x="840" y="72" text-anchor="end" class="mono" font-size="11"><tspan class="ok">200 OK</tspan><tspan class="p"> · application/json</tspan></text>
<line x1="441" y1="82.5" x2="855" y2="82.5" stroke="#26263a"/>
{"".join(lines)}
<rect class="cursor" x="458" y="{108 + len(JSON) * 19 - 11}" width="7" height="14" fill="#a397f7"/>'''
    title = f"GET /api/v1/{USUARIO.lower()} · 200 OK — {USUARIO}, {ROL} · C# / .NET · {UBICACION}"
    return svg(W, H, title, body, css)

# ---------------------------------------------------------------- botones
ICONS = {
    "linkedin": '<text x="34" y="38" text-anchor="middle" fill="#fff" font-size="17" font-weight="800">in</text>',
    "email": '<path d="M24 22h20a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H24a2 2 0 0 1-2-2V24a2 2 0 0 1 2-2zm0 2v.5l10 6.5 10-6.5V24H24zm20 3.2-10 6.4-10-6.4V38h20z" fill="#fff"/>',
}

def boton(icono, titulo, sub, flecha):
    w, h = 440, 64
    body = f'''<rect x="4.5" y="4.5" width="{w-9}" height="{h-9}" rx="10" fill="#13131f" stroke="#26263a"/>
<rect x="16" y="13" width="36" height="36" rx="8" fill="#5b3fd6"/>
<g transform="translate(0 -0)">{ICONS[icono]}</g>
<text x="66" y="30" class="fg" font-size="15" font-weight="700">{escape(titulo)}</text>
<text x="66" y="47" class="mono" font-size="11.5">{escape(sub)}</text>
<text x="{w-24}" y="38" text-anchor="end" class="soft" font-size="18">{flecha}</text>'''
    return svg(w, h, f"{titulo}: {sub}", body)

# ------------------------------------------------------------------ stack
def stack():
    row_h, top = 46, 64
    H = top + len(STACK) * row_h + 14
    parts = [header_bar("/stack", "Stack tecnológico"),
             f'<rect x=".5" y="56.5" width="{W-1}" height="{H-57}" rx="10" fill="#0e0e17" stroke="#26263a"/>',
             f'<line x1="28" y1="{top + 20}" x2="28" y2="{top + (len(STACK) - 1) * row_h + 20}" stroke="#5b3fd6" stroke-width="2"/>']
    delay = .2
    for r, (cat, items) in enumerate(STACK):
        y = top + r * row_h
        cy = y + 20
        fill = "#10b981" if r == 0 else "#0e0e17"
        parts.append(f'<circle cx="28" cy="{cy}" r="6" fill="{fill}" stroke="#a397f7" stroke-width="2"/>')
        parts.append(f'<text x="48" y="{cy + 5}" class="fg" font-size="14" font-weight="700">{escape(cat)}</text>')
        x = 180
        for name, color, sig, sc in items:
            w = 38 + len(name) * 7.1
            parts.append(
                f'<g class="j" style="animation-delay:{delay:.2f}s">'
                f'<rect x="{x}" y="{cy - 13}" width="{w:.0f}" height="26" rx="6" fill="#161624" stroke="#2a2a3d"/>'
                f'<rect x="{x + 6}" y="{cy - 8}" width="16" height="16" rx="3" fill="{color}"/>'
                f'<text x="{x + 14}" y="{cy + 3.5}" text-anchor="middle" font-size="8.5" font-weight="800" fill="{sc}">{escape(sig)}</text>'
                f'<text x="{x + 30}" y="{cy + 4.5}" class="soft" font-size="12.5">{escape(name)}</text></g>')
            x += w + 10
            delay += .06
        if r < len(STACK) - 1:
            parts.append(f'<line x1="48" y1="{y + row_h - 2}" x2="{W-20}" y2="{y + row_h - 2}" stroke="#1d1d2c" stroke-dasharray="3 4"/>')
    alt = "GET /stack — " + ". ".join(f"{c}: {', '.join(i[0] for i in items)}" for c, items in STACK)
    return svg(W, H, alt, "\n".join(parts))

def h_garage():
    return svg(W, 56, "GET /garage — Garage", header_bar("/garage", "Garage"))

FILES = {
    "hero.svg": hero(),
    "btn-linkedin.svg": boton("linkedin", "LinkedIn", LINKEDIN, "↗"),
    "btn-email.svg": boton("email", "Email", EMAIL, "→"),
    "stack.svg": stack(),
    "h-garage.svg": h_garage(),
}
for name, content in FILES.items():
    (OUT / name).write_text(content, encoding="utf-8")
    print("escrito", name)
