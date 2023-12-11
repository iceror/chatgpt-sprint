import os
from dotenv import load_dotenv
from openai import OpenAI
import openai

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def tonality_menu():
  print("In wich tonality you'd like to work?")
  print("1. C")
  print("2. D")
  print("3. E")
  print("4. F")
  print("5. G")
  print("6. A")
  print("7. B")

def get_key():
  while True:
    tonality_menu()
    choice = input("Use numbers 1-7 ")

    if choice == "q":
      return None

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 7:
                keys = ["C", "D", "E", "F", "G", "A", "B"]
                key = keys[choice - 1]
                return key
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
    # else:
    #     print("Invalid input. Please enter a valid number (1-7) or 'q' to quit.")

def is_alterated(user_key):
    sharp_or_flat = input("Sharp or flat?")
    if sharp_or_flat.lower() == "sharp":
      return user_key + "# "
    elif sharp_or_flat.lower() == "flat":
      return user_key + "b "

def mode_menu():
  print("Choose a mode:")
  print("1. Ionian")
  print("2. Dorian")
  print("3. Frigian")
  print("4. Lydian")
  print("5. Mixolydian")
  print("6. Aeolian")
  print("7. Locrian")

def get_mode():
  while True:
    mode_menu()
    choice = input("Use numbers 1-7 ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 7:
                modes = ["Ionian", "Dorian", "Frigian", "Lydian", "Mixolydian", "Aeolian", "Locrian"]
                mode = modes[choice - 1]
                return mode
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

def scenario_menu():
  print("Choose a scenario")
  print("1. Village theme")
  print("2. Mini-boss battle")
  print("3. Boss battle")
  print("4. Exploring")
  print("5. Puzzle")
  print("6. Race")
  print("7. Minigame")

def get_scenario():
  while True:
    scenario_menu()
    choice = input("Use numbers 1-7 ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 7:
                scenarios = ["Village theme", "Mini-boss battle", "Boss battle", "Exploring", "Puzzle", "Race", "Minigame"]
                scenario = scenarios[choice - 1]
                return scenario
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

def duration_menu():
  print("Choose a duration:")
  print("1. 10 seconds")
  print("2. 20 seconds")
  print("3. 30 seconds")
  print("4. 40 seconds")
  print("5. 50 seconds")
  print("6. 60 seconds")

def get_duration():
  while True:
    duration_menu()
    choice = input("Use numbers 1-6 ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 7:
                durations = ["10 seconds", "20 seconds", "30 seconds", "40 seconds", "50 seconds", "60 seconds"]
                duration = durations[choice - 1]
                return duration
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def generate_videogame_track():
  print("Hi, I'm a videogame music composer, I can help you create your own tracks!")
  videogame_name = input("What's the name of the videogame? ")
  user_key = get_key()
  key_alteration = input("Would you like your tonality to be # of b? (Yes/No) ")
  if key_alteration.lower() == "yes":
    user_key = is_alterated(user_key)

  mode = get_mode()
  #print(user_key + mode)

  scenario = get_scenario()
  #print(scenario)
  duration = get_duration()
  modulation_bool = input("Would you like the track to have a modulation? (Yes/No)")
  if modulation_bool.lower() == "yes":
    modulation_key = get_key()

  modulation_alteration = input("Would you like your tonality to be # of b? (Yes/No) ")
  if modulation_alteration.lower() == "yes":
    modulation_key = is_alterated(modulation_key)

    modulation_mode = get_mode()
    modulation_bars = input("For how many bars? ")
    user_prompt = f"The videogame is called {videogame_name}. Generate a chord chart in {user_key} {mode} for the {scenario} that has a total duration of {duration}. The track will modulate to {modulation_key}{modulation_mode} for {modulation_bars} bars and come back to the original key. The track must me loopable and have and ending to the tonal center of the original key."
  elif modulation_bool == False:
    user_prompt = f"Generate a chord chart in {user_key} {mode} for the {scenario} that has a duration of {duration}. The videogame is called {videogame_name}. The track must me loopable and have and ending to the tonal center of the key"

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
