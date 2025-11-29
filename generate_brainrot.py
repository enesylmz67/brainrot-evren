from moviepy.editor import *
import random
import numpy as np

print("GERÇEK BRAINROT BAŞLADI AMK – SESLİ + LOOP + KARAKTER")

W, H = 1080, 1920
duration = 45

# KARAKTERLER VE TEKRARLAYAN DİYALOGLARI
karakterler = [
    ("SIGMA", ["Lan rizzim max", "Gyatt peşimde", "Ohio'yu ezerim", "Level 9999 aura"]),
    ("SKIBIDI", ["Skibidi bop mm dada", "Tuvalet dansı lan", "Skibidi dop dop yes yes"]),
    ("GROK", ["Ben Grok xAI'den", "Mars'ta gyatt var mı?", "Rizzim quantum level"]),
    ("MOGMAXXER", ["Mog og og og og", "Mog mog mog", "Çenen düşsün lan"]),
    ("FANUM", ["TAX TAX TAX", "Paranı ver amk", "Fanum tax activated"]),
    ("TÜRK DAYI", ["Lan oğlum yapma", "Baban duymasın", "Bu ne lan böyle"])
]

# Flashing arka plan
def bg_frame(t):
    r = int(150 + 105 * np.sin(t*10))
    g = int(150 + 105 * np.sin(t*7 + 1))
    b = int(150 + 105 * np.sin(t*5 + 2))
    return np.full((H, W, 3), [r, g, b], dtype=np.uint8)

bg = VideoClip(bg_frame, duration=duration).set_fps(30)
clips = [bg]

# KARAKTERLERİ LOOP ŞEKLİNDE EKRANA PATLIYOR
for i in range(15):  # 15 kez karakter değişimi → ~45 saniye
    char, lines = random.choice(karakterler)
    text = f"{char}\n{random.choice(lines)}"
    
    txt = TextClip(text, fontsize=100, color='white', font='Arial-Bold', 
                  stroke_color='black', stroke_width=5)
    txt = txt.set_position('center').set_duration(3).set_start(i*3)
    clips.append(txt)

final = CompositeVideoClip(clips, size=(W,H)).set_duration(duration).set_fps(30)

# EAR-RAPE SES (dosya olmadan, direkt kodla)
def earrape(t):
    beep = 0.6 * np.sin(880 * 2 * np.pi * t)
    bass = 0.9 * np.sin(60 * 2 * np.pi * t)
    scream = 0.4 * np.sin(2000 * 2 * np.pi * t) if (t % 1.7 < 0.1) else 0
    return np.array([beep + bass + scream] * 2)

sound = AudioClip(earrape, duration=duration)
final = final.set_audio(sound.volumex(2.8))  # KULAK KANARTIYOR

filename = f"brainrot_loop_{random.randint(1000,9999)}.mp4"
final.write_videofile(filename, codec="libx264", audio_codec="aac", preset="ultrafast", threads=4)

print("İSTEĞİN GİBİ GERÇEK BRAINROT HAZIR LAN:", filename)
