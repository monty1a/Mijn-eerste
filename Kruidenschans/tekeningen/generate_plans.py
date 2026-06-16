#!/usr/bin/env python3
"""
Genereert schone plattegrond-schetsen van Kruidenschans 24, Voorhout
(woningtype M4, plan Oosthout B1, Noorlander Bouw 1986) op basis van de
originele bestektekeningen en de constructieberekeningen.

Output: SVG + PNG per blad in deze map.
Eenheid in de tekeningen = millimeter. Garden/achterzijde = boven, straat = onder.
"""
import cairosvg
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------- kleuren / stijl ----------
WALL = "#2b2b2b"
WALL_T = 240          # buitenmuur dik
PARTY_T = 300         # woningscheidende wand
INNER_T = 100         # binnenwand
ROOM = "#f7f4ee"
ROOM2 = "#eef3f5"
WET = "#e7f0f4"       # natte ruimte
OUT_GREEN = "#e8f0df"
PAVE = "#efece4"
GRAVEL = "#f0eee8"
INK = "#1b1b1b"
DIMC = "#7a6f5f"
ACCENT = "#c0532b"
GAINFILL = "#ffe2b0"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class SVG:
    def __init__(self, w, h, vb=None):
        self.w, self.h = w, h
        self.vb = vb or (0, 0, w, h)
        self.el = []

    def add(self, s):
        self.el.append(s)

    def rect(self, x, y, w, h, fill="none", stroke="none", sw=0, rx=0, dash=None, opacity=1):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" rx="{rx}" '
                 f'opacity="{opacity}"{d}/>')

    def line(self, x1, y1, x2, y2, stroke=WALL, sw=INNER_T, cap="square", dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>')

    def poly(self, pts, fill="none", stroke="none", sw=0, dash=None, closed=True, opacity=1):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        tag = "polygon" if closed else "polyline"
        self.add(f'<{tag} points="{p}" fill="{fill}" stroke="{stroke}" '
                 f'stroke-width="{sw}" stroke-linejoin="round" opacity="{opacity}"{d}/>')

    def circle(self, x, y, r, fill="none", stroke="none", sw=0):
        self.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{sw}"/>')

    def path(self, d, fill="none", stroke=WALL, sw=INNER_T, dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}/>')

    def text(self, x, y, s, size=180, fill=INK, anchor="middle", weight="400",
             italic=False, rotate=None, spacing=0):
        st = "italic" if italic else "normal"
        tr = f' transform="rotate({rotate} {x:.1f} {y:.1f})"' if rotate else ""
        ls = f' letter-spacing="{spacing}"' if spacing else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-family="Helvetica, Arial, sans-serif" '
                 f'font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
                 f'font-weight="{weight}" font-style="{st}"{ls}{tr}>{esc(s)}</text>')

    def render(self, name):
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
                f'viewBox="{self.vb[0]} {self.vb[1]} {self.vb[2]} {self.vb[3]}">')
        body = head + "\n".join(self.el) + "</svg>"
        with open(os.path.join(OUT, name + ".svg"), "w") as f:
            f.write(body)
        cairosvg.svg2png(bytestring=body.encode(), write_to=os.path.join(OUT, name + ".png"),
                         output_width=1600)
        print("->", name)


# ---------- bouwstenen ----------
def door(s, x, y, w, swing="dr", t=INNER_T):
    """Deuropening met draairichting. (x,y)=scharnier, w=breedte.
    swing: dr/dl = horizontale wand deur naar rechts/links;
           du/dd = verticale wand deur omhoog/omlaag."""
    s.line(x, y, x + (w if swing in ("dr", "dl") else 0),
           y + (w if swing in ("du", "dd") else 0), stroke="white", sw=t + 40)
    if swing == "dr":
        s.path(f"M {x} {y} A {w} {w} 0 0 1 {x+w} {y+w}", stroke="#9a9a9a", sw=18)
        s.line(x, y, x, y + w, stroke="#9a9a9a", sw=22)
    elif swing == "dl":
        s.path(f"M {x} {y} A {w} {w} 0 0 0 {x-w} {y+w}", stroke="#9a9a9a", sw=18)
        s.line(x, y, x, y + w, stroke="#9a9a9a", sw=22)
    elif swing == "du":
        s.path(f"M {x} {y} A {w} {w} 0 0 0 {x+w} {y-w}", stroke="#9a9a9a", sw=18)
        s.line(x, y, x + w, y, stroke="#9a9a9a", sw=22)
    elif swing == "dd":
        s.path(f"M {x} {y} A {w} {w} 0 0 1 {x+w} {y+w}", stroke="#9a9a9a", sw=18)
        s.line(x, y, x + w, y, stroke="#9a9a9a", sw=22)


def window(s, x1, y1, x2, y2, t=WALL_T):
    s.line(x1, y1, x2, y2, stroke="white", sw=t + 30)
    s.line(x1, y1, x2, y2, stroke="#7fa9c4", sw=60)
    s.line(x1, y1, x2, y2, stroke="white", sw=20)


def stair(s, x, y, w, h, steps=10, up=True, label="trap"):
    s.rect(x, y, w, h, fill="#faf7f0", stroke="#9a9a9a", sw=20)
    for i in range(1, steps):
        yy = y + h * i / steps
        s.line(x, yy, x + w, yy, stroke="#b3a892", sw=22)
    # looprichtingpijl
    cx = x + w / 2
    s.line(cx, y + h - 60, cx, y + 80, stroke=ACCENT, sw=30)
    s.poly([(cx - 80, y + 200), (cx + 80, y + 200), (cx, y + 60)], fill=ACCENT)
    s.text(cx, y + h - 130, label, size=130, fill="#6b6256")


def titleblock(s, x, y, w, blad, titel, schaal="1:100"):
    s.rect(x, y, w, 900, fill="white", stroke=INK, sw=18)
    s.line(x, y + 300, x + w, y + 300, stroke=INK, sw=12)
    s.line(x, y + 560, x + w, y + 560, stroke=INK, sw=12)
    s.text(x + 120, y + 200, "Kruidenschans 24, Voorhout", size=185, anchor="start", weight="700")
    s.text(x + 120, y + 460, titel, size=240, anchor="start", weight="700", fill=ACCENT)
    s.text(x + 120, y + 720, "woningtype M4 – plan Oosthout B1 – herget. uit bestektek. 1986",
           size=140, anchor="start", fill="#555")
    s.text(x + w - 120, y + 720, f"schaal {schaal} (indicatief)", size=140, anchor="end", fill="#555")
    s.text(x + w - 120, y + 200, blad, size=170, anchor="end", weight="700")


def northarrow(s, x, y, r=320, ang=0, note=None):
    s.circle(x, y, r, fill="white", stroke=INK, sw=18)
    s.poly([(x, y - r * 0.78), (x - r * 0.34, y + r * 0.4), (x, y + r * 0.12),
            (x + r * 0.34, y + r * 0.4)], fill=INK)
    s.text(x, y - r - 60, "N", size=210, weight="700")
    if note:
        s.text(x, y + r + 200, note, size=120, fill="#777")


def scalebar(s, x, y, total_m=5):
    seg = 1000
    for i in range(total_m):
        f = INK if i % 2 == 0 else "white"
        s.rect(x + i * seg, y, seg, 120, fill=f, stroke=INK, sw=12)
    s.text(x, y - 60, "0", size=120, anchor="middle")
    s.text(x + total_m * seg, y - 60, f"{total_m} m", size=120, anchor="middle")


def dim(s, x1, y1, x2, y2, txt, off=0):
    s.line(x1, y1, x2, y2, stroke=DIMC, sw=18)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    rot = 0 if abs(y2 - y1) < abs(x2 - x1) else -90
    s.text(mx, my - 60 + off, txt, size=150, fill=DIMC, rotate=rot)
    for (ex, ey) in ((x1, y1), (x2, y2)):
        s.line(ex - 40, ey - 40, ex + 40, ey + 40, stroke=DIMC, sw=14)


# =================================================================
# BLAD 1 — SITUATIE / TUIN
# =================================================================
def situatie():
    s = SVG(1600, 2150, vb=(-2500, -3500, 16000, 21500))
    # perceel (lang, smal ~215 m2) – straat onder
    plot = [(-1200, -2800), (8600, -2800), (8600, 13800), (-1200, 13800)]
    s.poly(plot, fill="#fbfaf6", stroke="#9a9a9a", sw=40, dash="220,160")
    s.text(-900, -2400, "perceel VHT00-B-5008  ≈ 215 m²", size=210, anchor="start",
           italic=True, fill="#8a8170")

    # straat
    s.rect(-2500, 14000, 16000, 2400, fill="#ededed")
    s.text(3700, 15450, "K R U I D E N S C H A N S  (straat)", size=300, fill="#8a8a8a",
           weight="700", spacing=14)

    # achtertuin (boven, noord)
    s.rect(-1000, -2700, 9400, 8600, fill=OUT_GREEN, stroke="none")
    s.text(3700, -1300, "ACHTERTUIN", size=300, fill="#6f8a55", weight="700", spacing=10)
    # gazon-arcering
    for gx in range(0, 8000, 700):
        s.line(gx, 200, gx, 5600, stroke="#d6e4c4", sw=14)
    # boom achter
    s.circle(6900, 1400, 850, fill="#cfe0b6", stroke="#9bb578", sw=30)
    s.circle(900, 4600, 650, fill="#cfe0b6", stroke="#9bb578", sw=30)
    # tuinkast / berging in tuin
    s.rect(5700, 4400, 2400, 1400, fill="#e7ddc8", stroke="#9a8d72", sw=30)
    s.text(6900, 5250, "tuinkast", size=170, fill="#7a6f5a")
    # terras tegen huis
    s.rect(200, 5900, 3200, 1200, fill=PAVE, stroke="#cbc3b2", sw=20)
    for tx in range(300, 3400, 380):
        s.line(tx, 5950, tx, 7050, stroke="#d9d2c2", sw=12)
    s.text(1700, 6650, "terras", size=180, fill="#8a8170")

    # HUIS (footprint) – tegen straatzijde
    hx, hy, hw, hh = 200, 7100, 5200, 4900
    s.rect(hx, hy, hw, hh, fill="#dfe7ee", stroke=WALL, sw=WALL_T)
    s.text(hx + hw / 2, hy + 1400, "WONING", size=300, weight="700", fill="#3c5a72")
    s.text(hx + hw / 2, hy + 1800, "begane grond", size=180, fill="#5c6b78")
    s.text(hx + hw / 2, hy + 4500, "voorzijde / entree", size=170, fill="#5c6b78")
    # voordeur
    s.rect(hx + 1900, hy + hh - 120, 900, 200, fill=ACCENT)

    # oprit + carport naast/voor de woning (rechts)
    cx, cy, cw, ch = 5600, 7100, 2600, 6900
    s.rect(cx, cy, cw, ch, fill=PAVE, stroke="#cbc3b2", sw=30)
    for bx in range(int(cx) + 200, int(cx + cw), 360):
        for by in range(int(cy) + 200, int(cy + ch), 360):
            s.rect(bx, by, 300, 300, fill="none", stroke="#ddd5c4", sw=12)
    s.text(cx + cw / 2, cy + 600, "oprit /", size=200, fill="#8a8170")
    s.text(cx + cw / 2, cy + 900, "carport", size=200, fill="#8a8170")
    # carport dak (gestippeld)
    s.rect(cx, cy, cw, 3400, fill="none", stroke=ACCENT, sw=40, dash="180,140")
    # boom voortuin (linde, uit foto)
    s.circle(7200, 9600, 1000, fill="#cfe0b6", stroke="#9bb578", sw=30)
    s.text(7200, 9650, "boom", size=150, fill="#6f8a55")
    # haag / lage hekken voortuin
    s.line(-1000, 12400, 5400, 12400, stroke="#8fae6a", sw=70, dash="120,90")
    s.text(2200, 12250, "haag", size=150, fill="#6f8a55", anchor="start")
    # bankje bij voordeur (uit foto)
    s.rect(3050, hy + hh + 120, 900, 260, fill="#cdbd9c", stroke="#9a8d72", sw=18)

    northarrow(s, 9600, -1900, note="oriëntatie indicatief")
    scalebar(s, 9000, 12800, 5)
    dim(s, -1700, -2800, -1700, 13800, "perceel ≈ 40 m", )
    titleblock(s, -2400, 16900, 15800, "blad 1 / 5", "Situatie & tuin", "1:200")
    s.render("1_situatie_tuin")


# =================================================================
# BLAD 2 — BEGANE GROND
# =================================================================
def shell(s, x0, y0, w, d):
    s.rect(x0, y0, w, d, fill="none", stroke=WALL, sw=WALL_T)


def begane_grond():
    s = SVG(1400, 1850, vb=(-1500, -3600, 9000, 17600))
    x0, y0 = 0, 0
    W = 5400
    Dbody = 9400
    # tuin/achterzijde label
    s.text(W / 2, -3050, "▲  ACHTERTUIN", size=200, fill="#6f8a55", weight="700")
    # terras + tuinkast buiten
    s.rect(200, -2600, 3200, 2300, fill=OUT_GREEN, stroke="#bcd1a3", sw=20)
    s.text(1700, -1400, "terras", size=170, fill="#6f8a55")
    s.rect(3600, -1500, 1600, 1200, fill="#e7ddc8", stroke="#9a8d72", sw=20)
    s.text(4400, -800, "tuinkast", size=150, fill="#7a6f5a")

    # casco
    s.rect(x0, y0, W, Dbody, fill=ROOM, stroke="none")
    # ruimtes (fills)
    s.rect(200, 200, 5000, 4500, fill=ROOM, stroke="none")            # woonkamer
    s.rect(200, 4900, 2400, 2400, fill=ROOM2, stroke="none")          # keuken
    s.rect(200, 7500, 1250, 900, fill=WET, stroke="none")             # toilet
    s.rect(200, 8500, 1250, 800, fill=ROOM2, stroke="none")           # meterkast
    s.rect(4000, 7500, 1200, 1800, fill=ROOM2, stroke="none")         # berging
    shell(s, x0, y0, W, Dbody)

    # binnenwanden
    s.line(200, 4800, 5200, 4800)                 # woonkamer/midden
    s.line(2600, 4800, 2600, 7300)                # keuken/hal
    s.line(3900, 4800, 3900, 9400)                # hal/rechterzone
    s.line(200, 7400, 2600, 7400)                 # boven keuken
    s.line(1450, 7400, 1450, 9400)               # toilet/mk - hal
    s.line(200, 8400, 1450, 8400)                # toilet/mk
    s.line(3900, 7400, 5200, 7400)               # boven berging

    # woningscheidende wanden accent
    s.line(0, 0, 0, Dbody, stroke=WALL, sw=PARTY_T)
    s.line(W, 0, W, Dbody, stroke=WALL, sw=PARTY_T)

    # ramen
    window(s, 700, 0, 3200, 0)                    # achtergevel pui woonkamer
    window(s, 700, 4900, 700, 6900)              # keuken zijraam (in party wand? -> raam achter)
    window(s, 200, 1200, 200, 3600)              # zijraam woonkamer (kopgevel)
    window(s, 4400, 0, 5000, 0)                  # raam bij tuinkast
    # voordeur + entree
    door(s, 3000, 9400, 1000, "du")
    s.text(3450, 9250, "entree", size=140, fill="#777")

    # binnendeuren
    door(s, 2600, 6400, 800, "du")               # keuken-hal
    door(s, 3050, 4800, 850, "dd")               # hal-woonkamer
    door(s, 1450, 7700, 700, "dr")               # hal-toilet
    door(s, 3900, 8400, 800, "dl")               # hal-berging
    # buitendeur berging->carport
    door(s, 4400, 9400, 800, "du")

    # trap
    stair(s, 2750, 5100, 1000, 2300, steps=11, label="")

    # labels
    s.text(2700, 2350, "woonkamer", size=260, weight="700")
    s.text(2700, 2700, "± 28 m²", size=160, fill="#777")
    s.text(1400, 6100, "keuken", size=220, weight="700")
    s.text(3300, 8100, "hal", size=200, weight="700")
    s.text(820, 7950, "toilet", size=150)
    s.text(820, 8950, "meterk.", size=140)
    s.text(4600, 8500, "berging", size=170)
    # carport
    s.rect(200, 9700, 5000, 4200, fill=PAVE, stroke="#cbc3b2", sw=20, dash="160,120")
    for (px, py) in [(350, 9850), (5050, 9850), (350, 13750), (5050, 13750), (2700, 13750)]:
        s.rect(px - 110, py - 110, 220, 220, fill=WALL)
    s.text(2700, 11900, "carport", size=240, weight="700", fill="#8a8170")

    # maatvoering
    dim(s, 0, -3300, W, -3300, "≈ 5,40 m")
    dim(s, 6100, 0, 6100, Dbody, "≈ 9,40 m")
    dim(s, 6100, 9700, 6100, 13900, "carport ≈ 4,2 m")

    northarrow(s, 7600, -2600, note="achtertuin = noord (ind.)")
    scalebar(s, 0, 14400, 5)
    titleblock(s, -1400, 15300, 8800, "blad 2 / 5", "Begane grond", "1:100")
    s.render("2_begane_grond")


# =================================================================
# BLAD 3 — VERDIEPING
# =================================================================
def verdieping():
    s = SVG(1400, 1700, vb=(-1500, -2400, 9000, 14600))
    W, D = 5400, 9400
    s.text(W / 2, -1900, "▲  achterzijde (tuin)", size=190, fill="#6f8a55", weight="700")

    s.rect(0, 0, W, D, fill=ROOM, stroke="none")
    # fills
    s.rect(200, 200, 2800, 4200, fill=ROOM, stroke="none")     # slk2
    s.rect(3000, 200, 2200, 4200, fill=ROOM, stroke="none")    # slk3
    s.rect(200, 4500, 2100, 2000, fill=WET, stroke="none")     # badkamer
    s.rect(200, 6700, 5000, 2500, fill=ROOM2, stroke="none")   # slk1
    shell(s, 0, 0, W, D)
    s.line(0, 0, 0, D, stroke=WALL, sw=PARTY_T)
    s.line(W, 0, W, D, stroke=WALL, sw=PARTY_T)

    # binnenwanden
    s.line(3000, 200, 3000, 4400)
    s.line(200, 4400, 5200, 4400)
    s.line(2300, 4400, 2300, 6600)
    s.line(3600, 4400, 3600, 6600)
    s.line(200, 6600, 5200, 6600)
    s.line(200, 6500, 2300, 6500)

    # dakkapellen-aanduiding op voor- en achtergevel (vergroten hoogte)
    s.rect(700, -240, 3000, 240, fill="#dfe7ee", stroke="#7a90a4", sw=24)
    s.text(2200, -90, "dakkapel", size=120, fill="#5c6b78")
    s.rect(900, D, 3200, 240, fill="#dfe7ee", stroke="#7a90a4", sw=24)
    s.text(2500, D + 170, "dakkapel", size=120, fill="#5c6b78")

    # ramen
    window(s, 600, 0, 2600, 0)
    window(s, 3200, 0, 5000, 0)
    window(s, 1000, D, 4000, D)
    window(s, 0, 1000, 0, 3200)

    # trap (omlaag) + overloop
    stair(s, 2400, 4600, 1100, 1900, steps=10, label="")
    s.text(2950, 4350, "overloop", size=150, fill="#777")

    # deuren
    door(s, 2300, 600, 800, "dd")        # overloop->slk2 (via gang) (indicatief)
    door(s, 3000, 700, 800, "dd")        # ->slk3
    door(s, 2300, 4800, 750, "dr")       # ->badkamer
    door(s, 2600, 6600, 850, "dd")       # ->slk1

    # labels
    s.text(1600, 2350, "slaapkamer 2", size=200, weight="700")
    s.text(1600, 2650, "± 12 m²", size=140, fill="#777")
    s.text(4100, 2350, "slaapkamer 3", size=190, weight="700")
    s.text(4100, 2650, "± 9 m²", size=140, fill="#777")
    s.text(1250, 5550, "badkamer", size=180, weight="700")
    s.text(2700, 8000, "slaapkamer 1", size=230, weight="700")
    s.text(2700, 8300, "± 15 m²", size=150, fill="#777")

    dim(s, 0, -1500, W, -1500, "≈ 5,40 m")
    dim(s, 6100, 0, 6100, D, "≈ 9,40 m")
    s.text(6700, D / 2, "vloer +2,70  /  plafond +5,40", size=140, fill=DIMC, rotate=-90)

    northarrow(s, 7600, -1400)
    scalebar(s, 0, 9900, 5)
    titleblock(s, -1400, 10900, 8800, "blad 3 / 5", "Verdieping (1e)", "1:100")
    s.render("3_verdieping")


# =================================================================
# BLAD 4 — ZOLDER
# =================================================================
def zolder():
    s = SVG(1400, 1700, vb=(-1500, -2400, 9000, 14600))
    W, D = 5400, 9400
    s.text(W / 2, -1900, "▲  achterzijde (tuin)", size=190, fill="#6f8a55", weight="700")

    # volledige verdiepingsomtrek (gestippeld) = footprint
    s.rect(0, 0, W, D, fill="#faf8f2", stroke="#b6ab94", sw=60, dash="200,150")
    # bruikbaar deel binnen knieschotten
    kne = 1240  # afstand gevel waar dak = zoldervloer
    s.rect(0, kne, W, D - 2 * kne, fill=ROOM, stroke="none")
    # knieschotten (waar vrije hoogte ~1,0 m)
    ks = 2330
    s.line(0, ks, W, ks, stroke=WALL, sw=INNER_T, dash="40,40")
    s.line(0, D - ks, W, D - ks, stroke=WALL, sw=INNER_T, dash="40,40")
    s.text(W / 2 + 1500, ks - 120, "knieschot", size=130, anchor="middle", fill="#777")
    s.text(W / 2 + 1500, D - ks + 230, "knieschot", size=130, anchor="middle", fill="#777")
    # nok (ridge) – loopt in breedterichting, halverwege diepte
    s.line(0, D / 2, W, D / 2, stroke=ACCENT, sw=60)
    s.text(W / 2 - 1300, D / 2 - 120, "nok +9,20", size=150, anchor="middle", fill=ACCENT, weight="700")
    # buitenmuren laag deel
    s.line(0, 0, 0, D, stroke=WALL, sw=PARTY_T)
    s.line(W, 0, W, D, stroke=WALL, sw=PARTY_T)

    # trapgat
    s.rect(2400, 5400, 1100, 1900, fill="white", stroke=WALL, sw=80)
    s.line(2400, 5400, 3500, 7300, stroke="#b3a892", sw=24)
    s.line(3500, 5400, 2400, 7300, stroke="#b3a892", sw=24)
    s.text(2950, 5250, "trapgat", size=150, fill="#777")

    # dakraam / velux aanduiding
    for (dx, dy) in [(1100, 1700), (4000, 1700)]:
        s.rect(dx, dy, 900, 700, fill="#dfeaf2", stroke="#7a90a4", sw=30)
        s.text(dx + 450, dy + 420, "dakraam", size=120, fill="#5c6b78")
    # CV-opstelling
    s.rect(4300, 4900, 800, 700, fill="#eee", stroke="#999", sw=24)
    s.text(4700, 5300, "CV", size=140, fill="#666")

    s.text(W / 2, 3650, "ZOLDER", size=280, weight="700", fill="#7a6f5a")
    s.text(W / 2, 4000, "open bergzolder onder steil dak", size=160, fill="#8a8170")

    dim(s, 0, -1500, W, -1500, "≈ 5,40 m")
    dim(s, 6100, 0, 6100, D, "≈ 9,40 m")
    dim(s, -800, kne, -800, D - kne, "bruikbaar ≈ 6,9 m")

    northarrow(s, 7600, -1400)
    scalebar(s, 0, 9900, 5)
    titleblock(s, -1400, 10900, 8800, "blad 4 / 5", "Zolder", "1:100")
    s.render("4_zolder")


# =================================================================
# BLAD 5 — DOORSNEDE: BESTAAND vs ACHTERGEVEL OPTREKKEN
# =================================================================
def doorsnede():
    s = SVG(1700, 1500, vb=(-1500, -1500, 14500, 12800))
    # x = diepte (0 achtergevel/tuin .. 8000 voorgevel/straat), y omlaag = hoogte invers
    def Y(h_mm):       # hoogte -> svg y (peil onder)
        return 9200 - h_mm
    span = 8000
    ridge_x = 4000
    goot, nok, vdv, zv = 3700, 9200, 2700, 5400

    # maaiveld
    s.line(-1200, Y(0), span + 1200, Y(0), stroke="#8a8170", sw=40)
    s.rect(-1200, Y(0), span + 2400, 700, fill="#efe9dc")

    # ---------- BESTAAND (links referentie, dun/grijs) ----------
    # vloeren
    for (yy, lab) in [(0, "begane grond  vloer  ±0,00"),
                      (vdv, "verdiepingsvloer  +2,70"),
                      (zv, "zoldervloer  +5,40")]:
        s.line(0, Y(yy), span, Y(yy), stroke=WALL, sw=120)
    # buitenmuren tot goot
    s.line(0, Y(0), 0, Y(goot), stroke=WALL, sw=WALL_T)
    s.line(span, Y(0), span, Y(goot), stroke=WALL, sw=WALL_T)
    # bestaand dak (gestippeld grijs)
    s.poly([(0, Y(goot)), (ridge_x, Y(nok)), (span, Y(goot))],
           fill="none", stroke="#9a9a9a", sw=70, dash="200,140", closed=False)

    # ---------- NIEUW: achtergevel optrekken (links = tuinzijde, x=0) ----------
    new_rear_top = nok          # achtergevel optrekken tot nokhoogte
    # nieuwe achtergevel (vol) van goot tot nok
    s.line(0, Y(goot), 0, Y(new_rear_top), stroke=ACCENT, sw=WALL_T)
    # nieuw dakvlak: van nieuwe achtergevel-top naar bestaande nok
    s.line(0, Y(new_rear_top), ridge_x, Y(nok), stroke=ACCENT, sw=70)
    # voorste dakvlak blijft (teken vol)
    s.line(ridge_x, Y(nok), span, Y(goot), stroke=WALL, sw=70)

    # dakkapel op voorste dakvlak (2e dakkapel op achterdak na optrekken niet meer nodig)
    dk_x = 6000
    dk_h = 1500
    s.rect(dk_x - 700, Y(goot + 1700) - dk_h, 1400, dk_h, fill="#dfe7ee",
           stroke="#3c5a72", sw=50)
    s.line(dk_x - 700, Y(goot + 1700) - dk_h, dk_x + 700, Y(goot + 1700) - dk_h - 250,
           stroke="#3c5a72", sw=50)
    s.text(dk_x, Y(goot + 1700) - dk_h / 2, "dakkapel", size=140, fill="#3c5a72")
    # nieuwe dakisolatie aanduiding (dikkere lijn langs dakvlakken)
    s.line(0, Y(new_rear_top) + 130, ridge_x, Y(nok) + 130, stroke="#6f8a55", sw=40, dash="120,90")
    s.line(ridge_x, Y(nok) + 130, span, Y(goot) + 130, stroke="#6f8a55", sw=40, dash="120,90")
    s.text(ridge_x + 1500, Y(nok) + 700, "nieuwe dakisolatie Rc≥6,3", size=150,
           fill="#6f8a55", weight="700")

    # gewonnen ruimte arceren (driehoek/zone achterzijde boven bestaand dak)
    s.poly([(0, Y(goot)), (0, Y(new_rear_top)), (ridge_x, Y(nok))],
           fill=GAINFILL, stroke="none", opacity=0.75)
    # extra op verdieping/zolder achter (rechthoekje volle hoogte achterzijde)
    s.poly([(0, Y(goot)), (ridge_x, Y(nok)),
            (ridge_x, Y(nok)), (0, Y(goot))], fill="none")

    # niveaulijnen tekst
    for (yy, lab) in [(0, "±0,00 peil"), (vdv, "+2,70 verdieping"),
                      (goot, "+3,70 goot"), (zv, "+5,40 zolder"), (nok, "+9,20 nok")]:
        s.line(span + 200, Y(yy), span + 600, Y(yy), stroke=DIMC, sw=16)
        s.text(span + 700, Y(yy) + 60, lab, size=170, anchor="start", fill=DIMC)

    # labels ruimtes
    s.text(ridge_x, Y(1.0 * 1000 + 300), "begane grond", size=200, fill="#888")
    s.text(ridge_x, Y(vdv + 900), "verdieping", size=200, fill="#888")
    s.text(1500, Y(zv + 1300), "winst", size=230, weight="700", fill=ACCENT)
    s.text(1500, Y(zv + 950), "zolder → volwaardig", size=150, fill=ACCENT)

    # zijde-aanduiding
    s.text(0, Y(0) + 520, "ACHTERGEVEL (tuin)", size=180, anchor="middle", weight="700", fill=ACCENT)
    s.text(span, Y(0) + 520, "VOORGEVEL (straat)", size=180, anchor="middle", weight="700", fill="#666")

    # legenda
    lx, ly = 9300, 1100
    s.rect(lx, ly, 4600, 2300, fill="white", stroke=INK, sw=16)
    s.text(lx + 200, ly + 320, "Doorsnede over de diepte", size=200, anchor="start", weight="700")
    s.line(lx + 240, ly + 620, lx + 700, ly + 620, stroke="#9a9a9a", sw=60, dash="160,110")
    s.text(lx + 800, ly + 680, "bestaand dak", size=170, anchor="start")
    s.line(lx + 240, ly + 940, lx + 700, ly + 940, stroke=ACCENT, sw=60)
    s.text(lx + 800, ly + 1000, "nieuw: achtergevel opgetrokken", size=170, anchor="start")
    s.rect(lx + 240, ly + 1180, 460, 240, fill=GAINFILL)
    s.text(lx + 800, ly + 1370, "oppervlakte-/ruimtewinst", size=170, anchor="start")
    s.text(lx + 200, ly + 1750, "Geschatte winst volwaardige", size=165, anchor="start", fill=INK)
    s.text(lx + 200, ly + 1960, "vloer (≥2,3 m): ≈ +15 à +22 m²", size=185,
           anchor="start", weight="700", fill=ACCENT)

    titleblock(s, -1400, 10500, 14200, "blad 5 / 5",
               "Doorsnede – voorstel achtergevel optrekken", "1:100")
    s.render("5_doorsnede_voorstel")


if __name__ == "__main__":
    situatie()
    begane_grond()
    verdieping()
    zolder()
    doorsnede()
    print("klaar")
