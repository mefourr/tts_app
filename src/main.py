import os
from speechpro.cloud.speech import synthesis

сlient = synthesis.SynthesisClient()

text = 'ПИДОРАСЫ!!!'
audio = сlient.synthesize(synthesis.enums.Voice.JULIA, synthesis.enums.PlaybackProfile.SPEAKER, text)
    
with open('output.wav', 'wb') as f:
    f.write(audio)