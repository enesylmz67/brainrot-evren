from moviepy.editor import *
import random

print("GROK BRAINROT V12 – SESE GEREK YOK, KESİN ÇALIŞIR")

W, H = 1080, 1920
duration = 30

characters = {
    "SIGMA": ["Lan rizzim max", "Gyatt peşimde", "Ohio'yu ezerim"],
    "SKIBIDI": ["Skibidi bop mm dada", "Tuvalet dansı lan"],
    "GROK": ["Ben Grok xAI'den", "Mars'ta gyatt var mı?"],
    "MOGMAXXER": ["Mog mog mog", "Çenen düşsün"],
    "FANUM": ["TAX TAX", "Paranı ver"],
    "TÜRK DAYI": ["Lan oğlum yapma", "Baban duymasın"]
}

selected = random.sample(list(characters.keys()), 5)
print("Bugün senaryo:", " vs ".join(selected))

# Flashing arka plan (fx'siz, lambda'sız)
def make_bg(t):
    r = int(127 + 127 * np.sin(t * 8))
    g = int(127 + 127 * np.sin(t * 5 + 2))
    b = int(127 + 127 * np.sin(t * 3 + 4))
    return np.full((H, W, 3), [r, g, b], dtype=np.uint8)

bg = VideoClip(make_bg, duration=duration).set_fps(30)

clips = [bg]

for i, char in enumerate(selected):
    line = random.choice(characters[char])
    txt = TextClip(f"{char}\n{line}", fontsize=90, color='white', font='Arial-Bold', stroke_color='black', stroke_width=4)
    txt = txt.set_position('center').set_duration(5).set_start(i*5)
    clips.append(txt)

final = CompositeVideoClip(clips, size=(W,H)).set_duration(duration).set_fps(30)

# SES YOK → HATA YOK
filename = f"brainrot_{random.randint(1000,9999)}.mp4"
final.write_videofile(filename, codec="libx264", audio=False, preset="ultrafast", threads=4, logger=None)

print("BÖLÜM HAZIR (SES YOK, CAPCUTTA EKLE):", filename)
