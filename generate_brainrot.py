from moviepy.editor import *
import random, numpy as np

print("GROK BRAINROT V5 – BU SEFER KESİN ÇALIŞIR AMK")

W, H = 1080, 1920
duration = 35

# Flashing arka plan
bg = ColorClip(size=(W,H), color=(0,0,0), duration=duration)
bg = bg.fx(vfx.colorx, lambda t: 1 + 0.5*abs(np.sin(t*8)))

# Rastgele yazılar
words = ["SIGMA", "RIZZ", "GYATT", "OHIO", "SKIBIDI", "MOG", "TAX", "LAN", "GROK", "xAI", "MARS", "TÜRK DAYI", "
