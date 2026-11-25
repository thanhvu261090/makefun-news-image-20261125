#!/usr/bin/env python3
"""Draw 'The World Today' front page for Wednesday 25 November 2026.

A single deterministic program: fixed text, fixed DejaVu fonts, no
network, no clock, no randomness. Two runs write byte-identical PNGs.
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (248, 243, 232)
INK = (20, 20, 20)
RED = (150, 24, 24)
GREY = (100, 94, 84)
RULE_LIGHT = (188, 180, 166)
NAVY = (28, 44, 66)
GOLD = (176, 128, 32)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def fnt(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, font, max_w):
    """Greedy word wrap; returns the lines that fit inside max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if not cur or d.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, max_w, text, font, leading, fill=INK):
    for line in wrap(d, text, font, max_w):
        d.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def hline(d, x0, y, x1, width=2, fill=INK):
    d.line([(x0, y), (x1, y)], fill=fill, width=width)


def headline_block(d, x, y, w, kicker, head, head_size, body,
                   body_size=15):
    """Kicker in red caps, bold serif headline, serif body. Returns y."""
    d.text((x, y), kicker, font=fnt(SANS_B, 13), fill=RED)
    y += 21
    y = para(d, x, y, w, head, fnt(SERIF_B, head_size), head_size + 7)
    y += 5
    y = para(d, x, y, w, body, fnt(SERIF, body_size), body_size + 6)
    return y


def tower_scene(d, x, y, w, h):
    """Stylised night skyline: a tall tower struck, smoke curling up."""
    d.rectangle([x, y, x + w, y + h], fill=NAVY)
    # stars
    for sx, sy in [(28, 18), (90, 42), (150, 14), (210, 36), (260, 20),
                   (330, 44), (60, 70), (300, 66), (180, 58)]:
        d.ellipse([x + sx - 2, y + sy - 2, x + sx + 2, y + sy + 2],
                  fill=(230, 225, 200))
    # low buildings
    for bx, bw, bh in [(0, 52, 46), (56, 40, 66), (100, 58, 38),
                       (300, 48, 58), (352, 44, 40)]:
        d.rectangle([x + bx, y + h - bh, x + bx + bw, y + h],
                    fill=(16, 26, 40))
        for wy in range(y + h - bh + 8, y + h - 6, 14):
            for wx in range(x + bx + 7, x + bx + bw - 6, 13):
                d.rectangle([wx, wy, wx + 4, wy + 6], fill=GOLD)
    # the tower: tapered, lit windows, a dark gash near the top
    tx = x + w // 2
    top = y + 12
    base = y + h
    d.polygon([(tx - 46, base), (tx - 22, top), (tx + 22, top),
               (tx + 46, base)], fill=(52, 70, 96))
    d.polygon([(tx - 22, top), (tx + 22, top), (tx + 13, top - 10),
               (tx - 13, top - 10)], fill=(52, 70, 96))
    for row in range(5):
        yy = top + 14 + row * 15
        half = 20 - row * 2
        for wx in range(tx - half, tx + half + 1, 10):
            d.rectangle([wx, yy, wx + 4, yy + 7], fill=GOLD)
    # impact flash + smoke
    d.ellipse([tx - 32, top + 28, tx + 32, top + 56], fill=(214, 96, 32))
    d.ellipse([tx - 17, top + 34, tx + 17, top + 52], fill=(240, 180, 90))
    for cx, cy, r in [(tx - 40, top - 4, 12), (tx - 10, top - 14, 15),
                      (tx + 24, top - 8, 11), (tx + 44, top + 6, 8)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(200, 196, 188))
    cap = fnt(SANS, 13)
    caption = "A tower in Riyadh's financial district, hit for the second time in a week."
    tw = d.textlength(caption, font=cap)
    cx0 = x + (w - tw) / 2
    d.rectangle([cx0 - 8, y + h - 26, cx0 + tw + 8, y + h - 6], fill=NAVY)
    d.text((cx0, y + h - 24), caption, font=cap, fill=(215, 210, 198))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 46
    R = W - M

    # ---- masthead ----
    hline(d, M, 26, R, 4)
    hline(d, M, 34, R, 1)
    mast = fnt(SERIF_B, 60)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=mast)
    d.text(((W - tw) / 2, 44), title, font=mast, fill=INK)
    hline(d, M, 122, R, 1)
    meta = fnt(SANS_B, 16)
    d.text((M, 132), "WEDNESDAY 25 NOVEMBER 2026", font=meta, fill=INK)
    right = "ONE WORLD  •  ONE PAGE  •  FREE"
    tw = d.textlength(right, font=meta)
    d.text((R - tw, 132), right, font=meta, fill=INK)
    hline(d, M, 158, R, 3)

    # ---- lead story: Riyadh ----
    y = headline_block(
        d, M, 176, R - M, "MIDDLE EAST  •  RIYADH",
        "Tower in Riyadh hit again as Houthi attacks reach the capital",
        30,
        "Eleven people were hurt when a tower in the King Abdullah "
        "Financial District was struck on Tuesday, the second attack on "
        "the district in a week. Saudi civil defence said the injured "
        "were taken to hospital, and the United Arab Emirates condemned "
        "the strike on the tower that houses the kingdom's sovereign "
        "wealth fund.",
        15)
    tower_scene(d, M, y + 6, R - M, 120)
    y = y + 6 + 120 + 10
    hline(d, M, y, R, 1, fill=RULE_LIGHT)
    y += 10

    # ---- two columns ----
    col_w = (R - M - 28) // 2
    x2 = M + col_w + 28
    y_left = headline_block(
        d, M, y, col_w, "IRAN  •  THE STRAIT OF HORMUZ",
        "Rial hits record low as US sanctions bite",
        22,
        "Iran's currency plunged on the black market after Washington "
        "announced fresh sanctions on its shadow banking network. "
        "Tehran warned ships in the strait and ruled out talks with "
        "the US unless seven conditions are met, while a tanker was "
        "reported struck by an unknown projectile in the strait.",
        14)
    y_right = headline_block(
        d, x2, y, col_w, "SPACE  •  CHINA",
        "Shenzhou-24 lifts off with a first for Pakistan",
        22,
        "China launched its Shenzhou-24 crew on Wednesday morning. "
        "The three astronauts include a Pakistani national, the first "
        "foreigner to board the Tiangong space station. The mission "
        "comes as Shanghai's party chief, a Politburo member, faces "
        "investigation in Beijing.",
        14)
    y = max(y_left, y_right) + 8
    hline(d, M, y, R, 1, fill=RULE_LIGHT)
    y += 10

    # ---- second row: markets + law ----
    y_left = headline_block(
        d, M, y, col_w, "TECHNOLOGY  •  MARKETS",
        "Huang in therapy as Nvidia's comeback rally fades",
        20,
        "Jensen Huang told staff he made \"some terrible mistakes\" a "
        "day after being reinstated as chief executive, and shares "
        "gave back some of Monday's 31.5% surge. A US jury also "
        "convicted Huawei of stealing trade secrets.",
        13)
    y_right = headline_block(
        d, x2, y, col_w, "WASHINGTON  •  THANKSGIVING",
        "Trump pardons the turkeys; Shein to pay $100m",
        20,
        "The president pardoned the Thanksgiving turkeys at the White "
        "House. Shein agreed to pay $100 million to settle US claims "
        "of deceptive practices, and the administration paused joint "
        "military operations with Ecuador.",
        13)
    y = max(y_left, y_right) + 8
    hline(d, M, y, R, 3)

    # ---- in brief ----
    y += 10
    d.text((M, y), "IN BRIEF", font=fnt(SANS_B, 14), fill=RED)
    y += 22
    briefs = [
        "Australia apologises to LGBTQ veterans for decades of military discrimination.",
        "Australia and Solomon Islands sign a security pact with Canberra as defence partner.",
        "Gunmen take 25 hostage at a supermarket in Colombia.",
        "A blast at a Hanoi hot-pot restaurant kills six and injures more than a dozen.",
        "Five women are killed every hour by relatives, the UN says.",
        "COP31 in Antalya ends without a deal as oil producers block a fossil-fuel phase-out.",
    ]
    for b in briefs:
        y = para(d, M + 16, y, R - M - 16, "•  " + b, fnt(SERIF, 13), 17)
        y += 1
    y += 3
    hline(d, M, y, R, 1, fill=RULE_LIGHT)
    y += 8
    foot = fnt(SANS, 11)
    note = ("Sources: Reuters, AP, SCMP, Gulf News, Manila Times — "
            "25 November 2026.  •  THE WORLD TODAY is a one-page summary.")
    tw = d.textlength(note, font=foot)
    d.text(((W - tw) / 2, y), note, font=foot, fill=GREY)

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
