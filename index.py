import os
from dotenv import load_dotenv
from openai import OpenAI
import openai

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def generate_videogame_track():
#variables 
  print("Hi, I'm a videogame music composer, I can help you create your own tracks!")
  videogame_name = input("What's the name of the videogame?")
  key = input("Please enter the tonality (whithout # or b) in which you'd like to work: ")
  key_alteration = input("Would you like your tonality to be # of b?")
  if key_alteration.lower() == "yes":
    sharp_or_flat = input("Sharp or flat?")
    if sharp_or_flat.lower() == "sharp":
      key = key + "sharp"
    elif sharp_or_flat.lower() == "flat":
      key = key + "flat"
  else:
    key = key

  mode = input("Enter the mode: ")
  scenario = input("For what game scenario you'd like your track: ")
  duration = input("Indicate the duration of the track in seconds: ")
  modulation_bool = input("Would you like the track to have a modulation?")

  if modulation_bool.lower() == "yes":
    modulation_bool = True
  elif modulation_bool.lower() == "no":
    modulation_bool = False

  if modulation_bool == True:
    modulation_key= input("To which key would you like the modulation to be?")
    modulation_mode= input("To which mode would you like the modulation to be?")
    modulation_bars = input("For how many bars?")
    user_prompt = f"The videogame is called {videogame_name}. Generate a chord chart in {key} {mode} for the {scenario} that has a duration of {duration}. The track will modulate to {modulation_key}{modulation_mode} for {modulation_bars} and come back to the original key. The track must me loopable and have and ending to the tonal center of the original key."
  elif modulation_bool == False:
    user_prompt = f"Generate a chord chart in {key} {mode} for the {scenario} that has a duration of {duration}. The videogame is called {videogame_name}. The track must me loopable and have and ending to the tonal center of the key"

  chat_completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=1.3,
    #temperature from 0 to 2 defines the creativity of the response
    #maxtokens maximum amount of tokens from the prompt and the response
    messages=[{
      "role": "system",
      "content": "You are a video-game music composer"
    },
    {
      "role": "user",
      "content": user_prompt
    }]
  )

  print(chat_completion.model_dump()['choices'][0]['message']['content'])

generate_videogame_track()
