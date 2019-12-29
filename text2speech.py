import os 
from gtts import gTTS 

# Sample text 
sample_text = " Phaneroo Make Manifest"

print("Please wait...processing")
tts = gTTS(text=sample_text, lang="en-uk")

# save the mp3 to the current directory
tts.save("sample_voice.mp3")

# play the audio using the default audio player on your system
os.system("start sample_voice.mp3")

