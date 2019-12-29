import os 
from gtts import gTTS 

# Sample text 
sample_text = " Manifesting God through Technology"

print("Please wait...processing")
tts = gTTS(text=sample_text, lang="en-uk")

# save the mp3 to the current directory
tts.save("sample_voice.mp3")



