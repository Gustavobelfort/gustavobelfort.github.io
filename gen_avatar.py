#!/usr/bin/env python3
"""
Generate a clean pixel art avatar in amber/retro terminal style.
3/4 profile: short dark hair, glasses, stubble beard, dark shirt, cross earring.
Hand-placed pixel map approach for clean results.
"""
from PIL import Image

# 48x48 logical pixels, 8x scale = 384x384
W, H = 48, 48
SCALE = 8

# Color palette indices
_ = 0   # bg
B = 1   # bg2
D = 2   # bg3/code dim
A = 3   # amber accent
G = 4   # gold
S = 5   # skin
L = 6   # skin light
K = 7   # skin dark
X = 8   # skin shadow
H_ = 9  # hair
HL = 10 # hair light
HD = 11 # hair dark
F = 12  # glasses frame
FL = 13 # frame light
FD = 14 # frame dark
LN = 15 # lens
LH = 16 # lens highlight
E = 17  # eye dark
EW = 18 # eye white
BR = 19 # beard
BL = 20 # beard light
BD = 21 # beard dark
SH = 22 # shirt
SL = 23 # shirt light
SD = 24 # shirt dark
N = 25  # nose
ND = 26 # nose dark
M = 27  # mouth
T = 28  # teeth
ER = 29 # earring
ES = 30 # earring shadow
CD = 31 # code dim
CM = 32 # code medium
CB = 33 # code bright
XS = 34 # extra skin highlight
EA = 35 # ear

PALETTE = {
    0:  (13, 10, 6),
    1:  (20, 16, 10),
    2:  (30, 24, 14),
    3:  (240, 160, 48),
    4:  (255, 209, 102),
    5:  (195, 138, 80),
    6:  (218, 165, 108),
    7:  (165, 112, 62),
    8:  (128, 82, 42),
    9:  (26, 18, 10),
    10: (52, 36, 20),
    11: (14, 10, 5),
    12: (175, 82, 32),
    13: (210, 110, 48),
    14: (120, 55, 22),
    15: (32, 44, 52),
    16: (52, 68, 76),
    17: (16, 10, 5),
    18: (195, 172, 140),
    19: (72, 50, 28),
    20: (92, 66, 38),
    21: (48, 32, 16),
    22: (22, 20, 34),
    23: (34, 32, 50),
    24: (14, 12, 22),
    25: (175, 122, 70),
    26: (140, 95, 50),
    27: (120, 62, 32),
    28: (190, 170, 145),
    29: (185, 175, 160),
    30: (135, 125, 110),
    31: (40, 30, 14),
    32: (65, 48, 22),
    33: (100, 75, 30),
    34: (228, 180, 125),
    35: (175, 120, 68),
}

# Define the 48x48 grid row by row
# Using the palette indices above
grid = [
    # Row 0-3: top background with code hints
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,CD,CD,CM,CD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,CD,CM,CD,CD,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,CD,CD,CM,CB,CM,CD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,CD,CM,CD,_,_,_],
    # Row 4-5: top of head starts
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,HD,HD,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,HD,HD,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 6-7
    [_,_,CD,CM,CD,_,_,_,_,_,_,_,_,HD,H_,H_,H_,H_,HL,H_,H_,H_,HL,H_,H_,H_,H_,H_,H_,H_,H_,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,HD,H_,H_,H_,HL,H_,H_,H_,HL,H_,H_,H_,H_,HL,H_,H_,H_,H_,H_,H_,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 8-9: forehead appears
    [_,_,_,_,_,_,_,_,_,_,_,_,H_,H_,H_,HL,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,HD,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,H_,HD,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 10-11: forehead
    [_,_,_,_,_,_,_,_,_,_,_,HD,H_,H_,H_,X, S, S, L, L, L, S, S, S, S, S, K, H_,H_,H_,H_,H_,H_,H_,HD,_,_,_,_,_,_,_,CD,CM,CD,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,HD,H_,H_,X, S, S, L, L,34, L, L, S, S, S, S, K, K, H_,H_,H_,H_,H_,H_,H_,HD,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 12-13: upper face
    [_,_,_,_,_,_,_,_,_,_,_,HD,H_,X, S, S, L, L,34,34, L, L, S, S, S, S, S, K, K, H_,H_,H_,H_,H_,H_,HD,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,CD,CM,CB,CD,_,_,_,_,_,_,HD,H_,X, S, S, L, L, L, L, L, S, S, S, S, S, S, K, K, H_,H_,H_,H_,H_,HD,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 14: eyebrow line
    [_,_,_,_,_,_,_,_,_,_,_,HD,H_,X, S, S,HD,HD,HD,HD,HD, S, S,HD,HD,HD,HD,HD, K, K, H_,H_,H_,H_,HD,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 15: above glasses
    [_,_,_,_,_,_,_,_,_,_,_,HD,H_,X, S, S, H_,H_,H_,H_, S, S, S, H_,H_,H_,H_, S, K, K, H_,H_,H_,H_,HD,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 16-17: glasses top
    [_,_,_,_,_,_,_,_,_,_,_,HD,H_,X, S,FL,FL,FL,FL,FL,FL, S,FL,FL,FL,FL,FL,FL, K, K, H_,H_,H_,H_,HD,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,HD,H_,X, F,LH,LN,LN,LN,LN, F, F, F,LH,LN,LN,LN, F, F,FD,FD,FD,FD,35,HD,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 18-19: glasses middle (eyes visible)
    [_,_,_,_,_,_,_,_,_,_,_,HD,H_,X, F,LH,LN,EW,EW,E, E,LN, F,LH,LN,EW,E, E,LN, F,FD, K,35,35,HD,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,CD,CM,CD,_,_,_,_,_,_,HD,H_,X, F,LN,LN,EW,E, E,LN,LN, F,LN,LN,EW,E,LN,LN, F, K, K,35,35,HD,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 20-21: glasses bottom
    [_,_,_,_,_,_,_,_,_,_,_,HD,H_,X, F,LN,LN,LN,LN,LN, F, S, F,LN,LN,LN,LN, F, K, K, K,35,35,HD,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,HD,H_,X, S,FD,FD, F, F,FD,FD, S, S,FD, F, F,FD,FD, K, K, K,35,35,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 22-23: cheeks / nose
    [_,_,_,_,_,_,_,_,_,_,_,_,HD,X, S, S, S, S, S, S, S, S, S, S, S, S, K, K, K, K,35,35,35,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,HD,X, S, S, S, S, S,25,25,ND, S, S, S, S, K, K, K,35,35,35,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 24-25: nose / upper lip
    [_,CD,CM,CD,_,_,_,_,_,_,_,_,HD,X, S, S, K, S,25,25,ND,ND, S, S, S, K, K, K, K,35,35,ER,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,HD,X,BR, K, K, S, S,ND,ND, S, S, S, K, K, K, K,35,ES,ER,ES,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 26-27: mouth area with beard
    [_,_,_,_,_,_,_,_,_,_,_,_,_,HD,BR,BD,BR, K, K, S, S, S, K, K, K, K, K,BR,ES,ER,ES,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,HD,BD,BR,BD,BR,27, T, T, T,27,BR, K,BR,BD,BR,HD,ER,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 28-29: chin beard
    [_,_,_,_,_,_,_,_,_,_,_,_,_,HD,BD,BR,BD,BR,27, M, M,27,BR,BR,BR,BD,BR,BD,HD,_,_,_,_,_,_,_,_,_,_,_,_,CD,CM,CD,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,HD,BD,BR,BD,BR,BD,BD,BR,BD,BR,BD,BR,BD,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 30-31: chin / jawline
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,HD,BD,BR,BD,BD,BR,BR,BD,BD,BR,BD,BR,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,HD,BD,BD,BD,BD,BD,BD,BD,BD,BD,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 32-33: neck
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,HD,X, K, K, K, K, K, K,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,CD,CM,CB,CM,CD,_,_,_,_,_,_,_,_,_,HD,X, K, K, K, K, K,HD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 34-35: collar / shirt start
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,SL,SD,SD,SL, K, K,SL,SD,SD,SL,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,_,_,SL,SH,SD,SD,SD,SL,SL,SD,SD,SD,SH,SL,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 36-39: shirt body
    [_,_,_,_,_,_,_,_,_,_,_,_,_,SL,SH,SH,SH,SD,SD,SD,SD,SD,SD,SH,SH,SH,SL,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,_,SL,SH,SH,SH,SH,SH,SD,SD,SD,SD,SH,SH,SH,SH,SH,SL,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,_,SL,SH,SH,SH,SH,SH,SH,SH,SD,SD,SH,SH,SH,SH,SH,SH,SH,SL,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,_,_,SL,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SL,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 40-43: wider shirt / shoulders
    [_,_,_,_,_,_,_,_,_,SL,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SL,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,_,_,SL,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SL,_,_,_,_,_,_,_,_,CD,CM,CD,_,_,_,_,_],
    [_,_,CD,CM,CD,_,_,SD,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SD,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,_,_,SD,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SD,_,_,_,_,_,_,_,_,_,_,_,_,_,_],
    # Row 44-47: bottom
    [_,_,_,_,_,SD,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SD,_,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,_,SD,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SD,_,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,_,SD,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SD,_,_,_,_,_,_,_,_,_,_,_],
    [_,_,SD,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SH,SD,_,_,_,_,_,_,_,_,_,_],
]

img = Image.new('RGB', (W, H), PALETTE[0])
px = img.load()

for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val in PALETTE and x < W and y < H:
            px[x, y] = PALETTE[val]

# Scale up with nearest-neighbor for crisp pixels
final = img.resize((W * SCALE, H * SCALE), Image.NEAREST)
final.save('/home/user/gustavobelfort.github.io/public/images/pixel-avatar.png')
print(f"Avatar saved: {W*SCALE}x{H*SCALE}px")
