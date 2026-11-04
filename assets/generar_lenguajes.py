"""Genera assets/lenguajes.svg: autos estilo Rocket League haciendo acrobacias."""
import sys

OUT = sys.argv[1]
S = 0.88          # escala de los autos
GLOCAL = 60       # suelo en coordenadas locales del auto
W, H = 760, 336
ROW_GROUND = [146, 292]

# ---------------------------------------------------------------- autos
def wheel(cx, cy=47):
    spokes = " ".join(f"M{cx} {cy}L{cx+dx:.2f} {cy+dy:.2f}" for dx, dy in
                      [(0, -6.6), (6.28, -2.04), (3.88, 5.34), (-3.88, 5.34), (-6.28, -2.04)])
    return (f'<g class="wheel"><circle cx="{cx}" cy="{cy}" r="13" fill="#141619"/>'
            f'<circle cx="{cx}" cy="{cy}" r="11.6" fill="none" stroke="#2b3036" stroke-width="1.6" stroke-dasharray="2.2 1.6"/>'
            f'<circle cx="{cx}" cy="{cy}" r="7.6" fill="#aeb6bf"/>'
            f'<path d="{spokes}" stroke="#5b636c" stroke-width="2" stroke-linecap="round"/>'
            f'<circle cx="{cx}" cy="{cy}" r="2" fill="#2b3036"/></g>')

def boost(x, y):
    return (f'<g transform="translate({x} {y})">'
            f'<path class="flame" d="M0 -4Q-9 -5 -24 0Q-9 5 0 4Z" fill="#ff7a1a"/>'
            f'<path class="flame f2" d="M0 -2.2Q-5 -2.4 -13 0Q-5 2.4 0 2.2Z" fill="#ffe7a3"/>'
            f'<circle class="spark" cx="-16" cy="0" r="2" fill="#ffb347"/>'
            f'<circle class="spark s2" cx="-16" cy="-2" r="1.6" fill="#ffd27a"/>'
            f'<circle class="spark s3" cx="-16" cy="2" r="1.4" fill="#ff8c2a"/></g>')

CARS = {
    # Octane: compacto, trompa redondeada, cabina corta, alerón con soportes
    "octane": dict(
        center=62,
        body="M6 52L4 36Q4 30 10 29L30 27L40 14Q42 11 46 11L70 11Q74 11 77 14L88 26L108 30Q118 32 120 40L121 48Q121 52 116 52L112 52L111 47A15 15 0 0 0 81 47L80 52L42 52L41 47A15 15 0 0 0 11 47L10 52Z",
        wells=[(26, "c"), (96, "c")],
        glass="M43 25L49 15L69 15Q72 15 74 17L84 25Z", pillars=[(59, 15, 10)],
        extras='<path d="M1 19L25 16.5L25 19.5L2 22.5Z" fill="#1f2328"/><rect x="9" y="21" width="3" height="8" fill="#1f2328"/><rect x="18" y="20" width="3" height="8" fill="#1f2328"/>'
               '<path d="M100 52L122 52L122 54.5L100 54.5Z" fill="#111"/>'
               '<path d="M50 30L58 30L51 44L43 44Z" fill="#fff" opacity=".28"/>',
        head="M112 33L120 36L119.5 39L111 36Z", tail=(4, 31), wheels=[26, 96], exhaust=(4, 40)),
    # Dominus: largo y bajo, capó largo, techo fastback, cola con alerón integrado
    "dominus": dict(
        center=67,
        body="M4 52L3 36Q3 32 8 31L20 30L22 27L27 28L48 18Q51 16 55 16L74 16Q78 16 81 18L94 27L120 32Q130 34 131 41L131 48Q131 52 126 52L119 52L119 47A15 15 0 0 0 89 47L88 52L43 52L43 47A15 15 0 0 0 13 47L12 52Z",
        wells=[(28, "c"), (104, "c")],
        glass="M51 27L56 19L74 19Q77 19 79 21L88 27Z", pillars=[(66, 19, 8)],
        extras='<path d="M100 31L109 32.6M101 33.6L107 34.6" stroke="#000" stroke-opacity=".35" stroke-width="1.4" stroke-linecap="round"/>'
               '<path d="M108 52L132 52L132 54.5L108 54.5Z" fill="#111"/>'
               '<path d="M46 36L86 33L86 35.5L46 38.5Z" fill="#fff" opacity=".3"/>',
        head="M122 35L130 38L129.5 40.5L121 37.5Z", tail=(3, 33), wheels=[28, 104], exhaust=(3, 42)),
    # Fennec: caja alta, techo plano con alerón, pasos de rueda cuadrados
    "fennec": dict(
        center=62,
        body="M4 52L4 17Q4 12 9 12L21 10L25 9Q27 8 30 8L68 8Q72 8 74 10L88 25L112 28Q120 29 120 36L120 48Q120 52 116 52L112 52L111 47L107 33L85 33L81 47L80 52L41 52L41 47L37 33L15 33L11 47L10 52Z",
        wells=[(26, "s"), (96, "s")],
        glass="M27 22L30 11.5L67 11.5Q70 11.5 72 13.5L81.5 22Z", pillars=[(50, 11.5, 10.5)],
        extras='<path d="M2 9L27 6.5L27 9.5L4 12Z" fill="#1f2328"/>'
               '<path d="M98 52L121 52L121 54.5L98 54.5Z" fill="#111"/>'
               '<path d="M44 27L76 27L76 29.5L44 29.5Z" fill="#fff" opacity=".3"/>',
        head="M112 31L120 33L120 36.5L111 34.5Z", tail=(4, 22), wheels=[26, 96], exhaust=(4, 42)),
}

def well(cx, kind):
    if kind == "c":
        return f'<circle cx="{cx}" cy="47" r="15" fill="#0b0d10"/>'
    return f'<path d="M{cx-15} 52L{cx-15} 47L{cx-11} 33L{cx+11} 33L{cx+15} 47L{cx+15} 52Z" fill="#0b0d10"/>'

def car_def(name, c):
    pillars = "".join(f'<rect x="{x}" y="{y}" width="3" height="{h}" fill="currentColor"/>' for x, y, h in c["pillars"])
    return f'''
    <clipPath id="clip-{name}"><path d="{c["body"]}"/></clipPath>
    <g id="{name}">
      {boost(*c["exhaust"])}
      <path d="{c["body"]}" fill="currentColor"/>
      <g clip-path="url(#clip-{name})">
        <rect x="0" y="0" width="140" height="31" fill="#fff" opacity=".14"/>
        <rect x="0" y="41" width="140" height="15" fill="#000" opacity=".28"/>
      </g>
      <path d="{c["glass"]}" fill="#16202c"/>
      <path d="{c["glass"]}" fill="url(#glass)" opacity=".55"/>
      {pillars}
      {c["extras"]}
      <path d="{c["head"]}" fill="#fff6c9"/>
      <rect x="{c["tail"][0]}" y="{c["tail"][1]}" width="3" height="5" rx="1" fill="#ff2d2d"/>
      {"".join(well(x, k) for x, k in c["wells"])}
      {"".join(wheel(x) for x in c["wheels"])}
    </g>'''

# ---------------------------------------------------------- acrobacias
# Cada fotograma: (porcentajes, dict de valores, timing)
# valores: ty, tx, r, sx, sy, op
def kf(*frames):
    return frames

ACTIONS = {
    "jump": (3.2, kf(
        ("0%, 28%", {}, "cubic-bezier(.2,.8,.3,1)"),
        ("50%", {"ty": -42}, "cubic-bezier(.7,0,.9,.4)"),
        ("68%", {"sx": 1.07, "sy": .88}, "ease-out"),
        ("78%, 100%", {}, None))),
    "frontflip": (3.8, kf(
        ("0%, 22%", {}, "ease-out"),
        ("40%", {"ty": -46, "r": 180}, "ease-in"),
        ("58%", {"r": 360, "sx": 1.05, "sy": .9}, "ease-out"),
        ("64%, 100%", {"r": 360}, None))),
    "dash": (4.2, kf(
        ("0%, 18%", {}, "cubic-bezier(.1,.9,.2,1)"),
        ("32%", {"tx": 95}, "ease-in"),
        ("38%", {"tx": 130, "op": 0}, None),
        ("39%", {"tx": -110, "op": 0}, "cubic-bezier(.1,.8,.3,1)"),
        ("62%, 100%", {}, None))),
    "backflip": (3.6, kf(
        ("0%, 22%", {}, "ease-out"),
        ("40%", {"ty": -46, "r": -180}, "ease-in"),
        ("58%", {"r": -360, "sx": 1.05, "sy": .9}, "ease-out"),
        ("64%, 100%", {"r": -360}, None))),
    "wheelie": (3.6, kf(
        ("0%, 18%", {}, "ease-out"),
        ("32%, 58%", {"r": -24}, "ease-in"),
        ("70%", {"r": 3}, None),
        ("78%, 100%", {}, None))),
    "doublejump": (3.4, kf(
        ("0%, 14%", {}, "ease-out"),
        ("28%", {"ty": -28}, "ease-in-out"),
        ("36%", {"ty": -22}, "ease-out"),
        ("52%", {"ty": -60}, "cubic-bezier(.7,0,.9,.4)"),
        ("70%", {"sx": 1.07, "sy": .88}, "ease-out"),
        ("78%, 100%", {}, None))),
    "sideflip": (4.2, kf(
        ("0%, 20%", {}, "ease-out"),
        ("38%", {"ty": -46, "sy": -1}, "ease-in"),
        ("56%, 100%", {}, None))),
    "bumps": (2.4, kf(
        ("0%, 100%", {}, "ease-out"),
        ("15%", {"ty": -12}, "ease-in"),
        ("30%", {"sx": 1.04, "sy": .93}, "ease-out"),
        ("45%", {"ty": -12}, "ease-in"),
        ("60%", {"sx": 1.04, "sy": .93}, "ease-out"),
        ("70%", {}, None))),
    "rock": (3.0, kf(
        ("0%, 18%", {}, "ease-out"),
        ("36%", {"ty": -28, "r": -16}, "ease-in-out"),
        ("54%", {"ty": -32, "r": 14}, "ease-in"),
        ("72%, 100%", {}, None))),
}

def car_tf(v):
    return (f'translate({v.get("tx", 0)}px,{v.get("ty", 0)}px) rotate({v.get("r", 0)}deg) '
            f'scale({v.get("sx", 1)},{v.get("sy", 1)})')

def shadow_tf(v):
    k = max(.35, 1 + v.get("ty", 0) / 80)
    return f'translateX({v.get("tx", 0)}px) scale({k:.2f})', k * v.get("op", 1)

def keyframes():
    out = []
    for name, (_, frames) in ACTIONS.items():
        car, sh = [], []
        for pct, v, timing in frames:
            t = f" animation-timing-function: {timing};" if timing else ""
            op = f" opacity: {v['op']};" if "op" in v else (" opacity: 1;" if name == "dash" else "")
            car.append(f"{pct} {{ transform: {car_tf(v)};{op}{t} }}")
            stf, sop = shadow_tf(v)
            sh.append(f"{pct} {{ transform: {stf}; opacity: {sop:.2f};{t} }}")
        out.append(f"@keyframes {name} {{ {' '.join(car)} }}")
        out.append(f"@keyframes sh-{name} {{ {' '.join(sh)} }}")
    return "\n    ".join(out)

# ---------------------------------------------------------------- escena
ITEMS = [  # (texto, color, auto, acción, fila, centro x, retraso)
    ("C#",         "#9B4F96", "octane",  "jump",       0, 80,  0.0),
    (".NET",       "#512BD4", "dominus", "frontflip",  0, 230, 0.4),
    ("JavaScript", "#F7DF1E", "fennec",  "dash",       0, 380, 0.8),
    ("HTML5",      "#E34F26", "octane",  "backflip",   0, 530, 1.2),
    ("CSS3",       "#1572B6", "dominus", "wheelie",    0, 680, 1.6),
    ("MySQL",      "#00758F", "fennec",  "doublejump", 1, 165, 0.2),
    ("SQL Server", "#CC2927", "octane",  "sideflip",   1, 315, 0.6),
    ("Swagger",    "#85EA2D", "dominus", "bumps",      1, 465, 1.0),
    ("Postman",    "#FF6C37", "fennec",  "rock",       1, 615, 1.4),
]

def scene():
    out = []
    for text, color, car, action, row, cx, d in ITEMS:
        g = ROW_GROUND[row]
        c = CARS[car]
        x = cx - c["center"] * S
        y = g - GLOCAL * S
        oy = g - 26 * S
        ox = cx
        if action == "wheelie":
            ox, oy = x + c["wheels"][0] * S, g
        dur = ACTIONS[action][0]
        anim = f"animation: {action} {dur}s {d}s infinite"
        out.append(
            f'<ellipse cx="{cx}" cy="{g + 1}" rx="{58 * S:.0f}" ry="4" fill="#000" opacity=".35" '
            f'style="transform-box: fill-box; transform-origin: center; animation: sh-{action} {dur}s {d}s infinite"/>')
        out.append(
            f'<g class="a" style="--ox:{ox:.1f}px; --oy:{oy:.1f}px; {anim}">'
            f'<use href="#{car}" transform="translate({x:.1f} {y:.1f}) scale({S})" color="{color}"/></g>')
        out.append(f'<text x="{cx}" y="{g + 26}">{text}</text>')
    return "\n  ".join(out)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Tecnologías representadas como autos estilo Rocket League (Octane, Dominus y Fennec) haciendo acrobacias en un estadio">
  <style>
    text {{ font-family: Bahnschrift, 'DIN Alternate', 'Arial Narrow', 'Segoe UI', Arial, sans-serif; font-size: 15px; font-weight: 700; font-style: italic; letter-spacing: .4px; text-anchor: middle; fill: #e6edf3; }}
    .a {{ transform-box: view-box; transform-origin: var(--ox) var(--oy); }}
    .line {{ stroke: #fff; stroke-opacity: .22; stroke-width: 2; stroke-dasharray: 16 10; animation: road .45s linear infinite; }}
    .wheel {{ transform-box: fill-box; transform-origin: center; animation: spin .4s linear infinite; }}
    .flame {{ transform-box: fill-box; transform-origin: right center; animation: flicker .16s ease-in-out infinite alternate; }}
    .f2 {{ animation-duration: .11s; }}
    .spark {{ transform-box: fill-box; transform-origin: center; animation: spark .5s linear infinite; }}
    .s2 {{ animation-delay: .17s; }} .s3 {{ animation-delay: .34s; }}
    .ball {{ transform-box: fill-box; transform-origin: center bottom; animation: ball 1.6s infinite; }}
    .ballspin {{ transform-box: fill-box; transform-origin: center; animation: spin 1.6s linear infinite; }}
    .orb {{ transform-box: fill-box; transform-origin: center; animation: orb 1.8s ease-in-out infinite alternate; }}
    .pad {{ animation: pad 1.8s ease-in-out infinite alternate; }}

    @keyframes road {{ to {{ stroke-dashoffset: 26; }} }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    @keyframes flicker {{ from {{ transform: scaleX(.6); opacity: .75; }} to {{ transform: scaleX(1.35); opacity: 1; }} }}
    @keyframes spark {{ from {{ transform: translateX(0) scale(1); opacity: 1; }} to {{ transform: translateX(-16px) scale(.2); opacity: 0; }} }}
    @keyframes ball {{
      0%   {{ transform: translateY(0) scale(1.15,.82); animation-timing-function: cubic-bezier(.2,.7,.4,1); }}
      8%   {{ transform: translateY(-4px) scale(1,1); animation-timing-function: cubic-bezier(.2,.7,.4,1); }}
      50%  {{ transform: translateY(-62px); animation-timing-function: cubic-bezier(.6,0,.8,.3); }}
      96%  {{ transform: translateY(0) scale(1,1); }}
      100% {{ transform: translateY(0) scale(1.15,.82); }}
    }}
    @keyframes orb {{ from {{ transform: translateY(0); }} to {{ transform: translateY(-6px); }} }}
    @keyframes pad {{ from {{ opacity: .45; }} to {{ opacity: 1; }} }}
    {keyframes()}

    @media (prefers-reduced-motion: reduce) {{
      *, .a, ellipse {{ animation: none !important; }}
    }}
  </style>

  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a1022"/><stop offset="1" stop-color="#121a33"/></linearGradient>
    <radialGradient id="blue" cx="0" cy="0" r="1"><stop offset="0" stop-color="#2d7cff" stop-opacity=".35"/><stop offset="1" stop-color="#2d7cff" stop-opacity="0"/></radialGradient>
    <radialGradient id="orange" cx="1" cy="1" r="1"><stop offset="0" stop-color="#ff7a1a" stop-opacity=".3"/><stop offset="1" stop-color="#ff7a1a" stop-opacity="0"/></radialGradient>
    <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9fc4ff"/><stop offset=".45" stop-color="#9fc4ff" stop-opacity="0"/><stop offset=".6" stop-color="#fff" stop-opacity=".5"/><stop offset=".7" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <radialGradient id="ballg" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#f4f6f8"/><stop offset="1" stop-color="#8f99a5"/></radialGradient>
    <radialGradient id="orbg" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="#fff1c2"/><stop offset=".5" stop-color="#ffa23a"/><stop offset="1" stop-color="#ff6a00"/></radialGradient>
    <pattern id="hex" width="28" height="48.5" patternUnits="userSpaceOnUse"><path d="M14 0L28 8.08V24.25L14 32.33L0 24.25V8.08Z M14 32.33V48.5" fill="none" stroke="#fff" stroke-opacity=".05"/></pattern>
    <clipPath id="panel"><rect width="{W}" height="{H}" rx="12"/></clipPath>
    {"".join(car_def(n, c) for n, c in CARS.items())}
  </defs>

  <g clip-path="url(#panel)">
    <!-- Estadio -->
    <rect width="{W}" height="{H}" fill="url(#bg)"/>
    <rect width="{W}" height="{H}" fill="url(#hex)"/>
    <rect width="{W}" height="{H}" fill="url(#blue)"/>
    <rect width="{W}" height="{H}" fill="url(#orange)"/>
    <line class="line" x1="0" y1="{ROW_GROUND[0] + 1}" x2="{W}" y2="{ROW_GROUND[0] + 1}"/>
    <line class="line" x1="0" y1="{ROW_GROUND[1] + 1}" x2="{W}" y2="{ROW_GROUND[1] + 1}"/>

    <!-- Pad de boost grande -->
    <g transform="translate(58 {ROW_GROUND[1]})">
      <ellipse class="pad" cx="0" cy="0" rx="22" ry="5" fill="#ff7a1a" opacity=".8"/>
      <ellipse cx="0" cy="0" rx="14" ry="3" fill="#ffd27a"/>
      <circle class="orb" cx="0" cy="-22" r="9" fill="url(#orbg)"/>
    </g>

    <!-- Pelota -->
    <ellipse cx="712" cy="{ROW_GROUND[1] + 1}" rx="14" ry="3.5" fill="#000" opacity=".45"/>
    <g class="ball">
      <g class="ballspin">
        <circle cx="712" cy="{ROW_GROUND[1] - 16}" r="16" fill="url(#ballg)" stroke="#5d6672" stroke-width="1.2"/>
        <path d="M712 {ROW_GROUND[1] - 22}l5.2 3v6l-5.2 3l-5.2 -3v-6z M712 {ROW_GROUND[1] - 22}v-10 M717.2 {ROW_GROUND[1] - 19}l8.6 -5 M717.2 {ROW_GROUND[1] - 13}l8.6 5 M712 {ROW_GROUND[1] - 10}v10 M706.8 {ROW_GROUND[1] - 13}l-8.6 5 M706.8 {ROW_GROUND[1] - 19}l-8.6 -5"
              fill="#c7ced6" stroke="#5d6672" stroke-width="1.1" stroke-linejoin="round"/>
      </g>
    </g>

    <!-- Autos -->
  {scene()}
  </g>
</svg>
'''

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("ok", len(svg))
