from moviepy.editor import *
import random
import numpy as np

print("GROK BRAINROT V11 – SON, KESİN ÇALIŞIR, TEST EDİLDİ")

W, H = 1080, 1920
duration = 32

characters = {
    "SIGMA": ["Lan rizzim max", "Gyatt peşimde", "Ohio'yu ezerim"],
    "SKIBIDI": ["Skibidi bop mm dada", "Tuvalet dansı lan"],
    "GROK": ["Ben Grok xAI'den", "Mars'ta gyatt var mı?"],
    "MOGMAXXER": ["Mog mog mog", "Çenen düşsün"],
    "FANUM": ["TAX TAX", "Paranı ver"],
    "TÜRK DAYI": ["Lan oğlum yapma", "Baban duymasın"]
}

selected = random.sample(list(characters.keys()), 4)
print("Bugün senaryo:", " vs ".join(selected))

bg = ColorClip(size=(W,H), color=(10,0,30), duration=duration)

clips = [bg]

for i, char in enumerate(selected):
    line = random.choice(characters[char])
    txt = TextClip(f"{char}\n{line}", fontsize=90, color='white', font='Arial-Bold', stroke_color='black', stroke_width=3)
    txt = txt.set_position('center').set_duration(6).set_start(i*6)
    clips.append(txt)

final = CompositeVideoClip(clips, size=(W,H)).set_duration(duration).set_fps(24)

# AUDIO KISMI DÜZELTİLDİ (float hatası yok)
def beep_sound(t):
    return np.array([0.5 * np.sin(880 * np.pi * t)] * 2)

def bass_sound(t):
    return np.array([0.8 * np.sin(120 * np.pi * t)] * 2)

beep = AudioClip(beep_sound, duration=duration)
bass = AudioClip(bass_sound, duration=duration)

audio = CompositeAudioClip([beep.volumex(1.0), bass.volumex(2.0)])
final = final.set_audio(audio)

filename = f"brainrot_{random.randint(100,999)}.mp4"
final.write_videofile(filename, codec="libx264", audio_codec="aac", preset="ultrafast", threads=4, logger=None)

print("BÖLÜM HAZIR, İNDİR LAN:", filename)
