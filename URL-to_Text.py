import requests
from bs4 import BeautifulSoup
import subprocess

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


url = "https://timesofindia.indiatimes.com/india/air-pollution-level-increases-in-delhi-eight-stations-in-red-zone/articleshow/114761531.cms"


scraped_text = scrape_website(url)
if scraped_text:
    print(scraped_text)
    print(type(scraped_text))


# For good voice uncomment below code but voice complete voice is not coming 
# from bark import SAMPLE_RATE, generate_audio, preload_models
# from scipy.io.wavfile import write as write_wav
# from IPython.display import Audio

# # download and load all models
# preload_models()

# # generate audio from text
# text_prompt = scraped_text
# audio_array = generate_audio(text_prompt)

# # save audio to disk
# write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
  
# # play text in notebook
# Audio(audio_array, rate=SAMPLE_RATE)



# this code is giving full voice but voice quality is not good 
def text_to_speech(text):
    # Use subprocess to call espeak
    subprocess.run(['espeak', text])

if __name__ == "__main__":
    text = scraped_text
    text_to_speech(text)

print("Sucess")
