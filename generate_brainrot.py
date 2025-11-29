from moviepy.editor import *
import random

print("GROK BRAINROT FABRİKASI V3 – KESİN ÇALIŞIR")

W, H = 1080, 1920
duration = random.uniform(25, 45)

characters = {
    "SIGMA": ["Lan rizzim max", "Gyatt peşimde", "Ohio'yu ezerim"],
    "SKIBIDI": ["Skibidi bop mm dada", "Tuvalet dansı lan"],
    "GROK": ["Ben Grok xAI'den", "Mars'ta gyatt var mı?"],
    "MOGMAXXER": ["Mog mog mog", "Çenen düşsün"],
    "FANUM": ["TAX! TAX!", "Paranı ver"],
    "TÜRK DAYI": ["Lan oğlum yapma", "Baban duymasın"]
}

def flashing_bg(t):
    return [random.randint(100,255), random.randint(0,255), random.randint(0,255)]

bg = ColorClip(size=(W,H), color=(0,0,0), duration=duration).set_fps(30)

clips = [bg]

for i in range(7):
    char = random.choice(list(characters.keys()))
    text = f"{char}\n{random.choice(characters[char])}"
    txt = TextClip(text, fontsize=100, color='white', font='Impact', stroke_color='black', stroke_width=6, size=(W-100, None))
    txt = txt.set_position('center').set_duration(4).set_start(i*4)
    txt = txt.on_color(size=(W, txt.h+80), color=(random.randint(0,50),0,random.randint(0,50)), pos='center', col_opacity=0.9)
    clips.append(txt)

final = CompositeVideoClip(clips, size=(W,H)).set_fps(30)

beep = AudioClip(lambda t: 0.3*np.sin(440*np.pi*t), duration=duration)
bass = AudioClip(lambda t: 0.6*np.sin(60*np.pi*t), duration=duration)
audio = CompositeAudioClip([beep.volumex(2.5), bass.volumex(4)])

final = final.set_audio(audio)

filename = f"brainrot_{random.randint(1,9999)}.mp4"
final.write_videofile(filename, codec="libx264", audio_codec="aac", threads=4, preset="ultrafast", bitrate="18000k", logger=None)

print(f"LAN BÖLÜM HAZIR: {filename}")
