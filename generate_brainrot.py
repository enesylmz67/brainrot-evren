from moviepy.editor import *
import random

print("GROK BRAINROT FABRİKASI V2 – IMAGEMAGICK’SIZ ÇALIŞIR")

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

# Renkli flashing arka plan
def flashing_bg(t):
    return [random.randint(100,255), random.randint(0,255), random.randint(0,255)]

bg = ColorClip(size=(W,H), color=(0,0,0), duration=duration).set_fps(30)

clips = [bg]

for i in range(6):
    char = random.choice(list(char
