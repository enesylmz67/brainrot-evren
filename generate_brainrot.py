from moviepy.editor import *
import random
import os

print("GROK BRAINROT FABRİKASI BAŞLADI AMK")

W, H = 1080, 1920
duration = random.uniform(25, 45)

characters = {
    "sigma": ["Lan rizzim max", "Gyatt peşimde", "Ohio'yu ezerim"],
    "skibidi": ["Skibidi bop mm dada", "Tuvalet dansı yap lan"],
    "grok": ["Ben Grok, xAI'den", "Mars'ta gyatt var mı lan?"],
    "mogmaxxer": ["Mog mog mog", "Çenen düşsün lan"],
    "fanum": ["TAX! TAX!", "Paranı ver amk"],
    "turkdayi": ["Lan oğlum dans etme", "Baban duymasın"]
}

bg = ColorClip(size=(W,H), color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)), duration=duration)

clips = [bg]
for i in range(6):
    char = random.choice(list(characters.keys()))
    lines = characters[char]
    txt = TextClip(f"{char.upper()}\n{random.choice(lines)}", fontsize=80, color='white', font='Arial-Bold', stroke_color='black', stroke_width=5)
    txt = txt.set_pos('center').set_duration(4).set_start(i*4)
    clips.append(txt.on_color(size=(W,H), color=(0,0,0), col_opacity=0.6))

final = CompositeVideoClip(clips).set_fps(30)
audio_files = [f"audio/{f}" for f in os.listdir("audio") if f.endswith(('.mp3','.wav'))] if os.path.exists("audio") else []
if audio_files:
    audio = CompositeAudioClip([AudioFileClip(random.choice(audio_files)).volumex(2.5) for _ in range(3)])
    final = final.set_audio(audio.audio_loop(duration=duration))

episode = len([f for f in os.listdir('.') if f.startswith('brainrot_')]) + 1
filename = f"brainrot_bolum_{episode}.mp4"
final.write_videofile(filename, codec="libx264", audio_codec="aac", threads=4, preset="ultrafast")

print(f"BÖLÜM {episode} HAZIR: {filename}")
