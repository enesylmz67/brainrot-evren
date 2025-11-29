from moviepy.editor import *
import random
import numpy as np

print("GROK BRAINROT V7 – KARAKTER + SENARYO + KESİN ÇALIŞIR")

W, H = 1080, 1920
duration = 35

# Karakterler ve diyaloglar (senaryo random)
characters = {
    "SIGMA": ["Lan rizzim max", "Gyatt peşimde", "Ohio'yu ezerim"],
    "SKIBIDI": ["Skibidi bop mm dada", "Tuvalet dansı lan"],
    "GROK": ["Ben Grok xAI'den", "Mars'ta gyatt var mı?"],
    "MOGMAXXER": ["Mog mog mog", "Çenen düşsün"],
    "FANUM": ["TAX TAX", "Paranı ver"],
    "TÜRK DAYI": ["Lan oğlum yapma", "Baban duymasın"]
}

# Rastgele senaryo (3-5 karakter seç, diyalog zinciri)
selected_chars = random.sample(list(characters.keys()), random.randint(3, 5))
print("Bugün senaryo: " + " vs ".join(selected_chars) + " rizz savaşı")

bg = ColorClip(size=(W,H), color=(0,0,0), duration=duration)

clips = [bg]

for i, char in enumerate(selected_chars):
    line = random.choice(characters[char])
    text = f"{char}\n{line}"
    txt = TextClip(text, fontsize=80, color='white', font='Arial-Bold', stroke_color='black', stroke_width=2)
    txt = txt.set_pos('center').set_duration(5).set_start(i*5)
    txt = txt.fx(vfx.fadein, 0.5).fx(vfx.fadeout, 0.5)
    clips.append(txt)

final = CompositeVideoClip(clips, size=(W,H)).set_fps(30)

# Earrape ses
beep = AudioClip(lambda t: [0.4*np.sin(440*2*np.pi*t)]*2, duration=duration).volumex(2.5)
bass = AudioClip(lambda t: [0.6*np.sin(80*2*np.pi*t)]*2, duration=duration).volumex(4)
final = final.set_audio(CompositeAudioClip([beep, bass]))

filename = f"brainrot_bolum_{random.randint(1,999)}.mp4"
final.write_videofile(filename, codec="libx264", audio_codec="aac", preset="ultrafast", threads=4, logger=None)

print(f"BÖLÜM HAZIR: {filename}")
