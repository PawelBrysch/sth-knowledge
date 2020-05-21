import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\_auth\nataly_auth.json"

from google.cloud import texttospeech



# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
# synthesis_input = texttospeech.types.SynthesisInput(text="das Ferkelchen")
# synthesis_input = texttospeech.types.SynthesisInput(text="Ein Kastenstand ist ein Bestandteil eines Schweinestalls, welcher in der Schweineproduktion genutzt wird, um Zuchtsauen während der Trächtigkeit und Säugezeit zu halten.")
synthesis_input = texttospeech.types.SynthesisInput(text="Rote Rüben Suppe")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
# voice = texttospeech.types.VoiceSelectionParams(
#     language_code='de-DE',
#     ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

voice = texttospeech.types.VoiceSelectionParams(
    language_code='de-DE-Wavenet-E',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3,
    speaking_rate=0.7)

response = client.synthesize_speech(synthesis_input, voice, audio_config)

with open('output_M_E.mp3', 'wb') as out:
    out.write(response.audio_content)
