import os
from gtts import gTTS

# Vocabulary for Week 01, Day 01
# Format: "filename_suffix": "Portuguese Text"
vocab = {
    "oi": "Oi",
    "ola": "Olá",
    "bom_dia": "Bom dia",
    "boa_tarde": "Boa tarde",
    "boa_noite": "Boa noite",
    "tudo_bem": "Tudo bem?",
    "como_voce_esta": "Como você está?",
    "tudo_joia": "Tudo joia?",
    "tchau": "Tchau",
    "ate_logo": "Até logo",
    "ate_amanha": "Até amanhã"
}

# Target directory: ../Week_01/audio relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "..", "Week_01", "Day_01")

if not os.path.exists(output_dir):
    print(f"Creating directory: {output_dir}")
    os.makedirs(output_dir)

print(f"Generating audio files in: {output_dir}...")

for filename, text in vocab.items():
    file_path = os.path.join(output_dir, f"{filename}.mp3")
    print(f"  Generating: '{text}' -> {filename}.mp3")
    try:
        tts = gTTS(text=text, lang='pt', slow=False)
        tts.save(file_path)
    except Exception as e:
        print(f"  ERROR generating {filename}: {e}")

print("Generation complete!")
