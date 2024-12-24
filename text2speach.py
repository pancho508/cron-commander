from gtts import gTTS

# The narration script
narration_text = """
El universo… qué vasto y magnífico lugar, ¿no es así?

¿Alguna vez te has preguntado por qué el universo se expande? Seguro que no es solo por la física.

Tal vez… solo está haciendo espacio… para más bromas.

Al final de todo, el humor es el alma de la existencia. Y dime, ¿qué puede ser más gracioso que tú, una pequeña mota de polvo, tratando de comprender todo esto?

El universo se ríe contigo, no de ti.
"""

# Generate the audio file
audio = gTTS(text=narration_text, lang="es", slow=False)
audio.save("Alan_Watts_Universe_Humor.mp3")
print("MP3 file saved as 'Alan_Watts_Universe_Humor.mp3'")