from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound

authenticator = IAMAuthenticator('CFyTHJwrk3xhhKO-zD9MerHvcOImWZPusaOWUMCXINjw')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/d02db692-89fa-4015-a3b6-ccf6e15abfa9')

with open('new.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Hello all.How are you.',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'        
        ).get_result().content
    
playsound('new.mp3')