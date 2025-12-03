# https://www.geeksforgeeks.org/python/voice-assistant-using-python/ 
# but with Lenape, Southern Unami dialect AND new commands on top of base 
# established in geeksforgeeks
# TODO: add my own tts program as functionality here
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import random
from bs4 import BeautifulSoup
import urllib.parse

# dictionary to use for review, Shelley Depaul textbook 6th edition

wikipedia.set_lang("en")  

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='wikipedia')

lenape_dict = {
    "one": "kweti",
    "it is black": "seke",
    "he/she is black": "seksu",
    "crow": "ahas",
    "crows": "ahasak",
    "shirt": "hempes",
    "shirts": "hempsa",
    "hello": "he",
    "i am well": "nulamalsi",
    "you are well": "kulamalsi",
    "are you well?/how are you?": "kulamalsi hech",
    "verbal question mark": "hech",
    "flow of words/grammar": "Aptonahanne"
    # add more entries here
}



def review_words(num_words=5):
    print("Reviewing random words...")
    for _ in range(num_words):
        english, lenape = random.choice(list(lenape_dict.items()))
        print(f"Lenape: {lenape} - English: {english}")
        speak(f"{lenape} means {english}")

engine = pyttsx3.init()

def search_lenape(query):
    base = "https://www.talk-lenape.org/results"
    params = {"query": query}
    url = base + "?" + urllib.parse.urlencode(params)
    resp = requests.get(url)
    resp.raise_for_status()  # error if bad response
    soup = BeautifulSoup(resp.text, "html.parser")
    # Now inspect the HTML and pick the relevant tags
    results = []
    for item in soup.select(".result‑row"):  # (example — you need to inspect the real class/id)
        title = item.select_one("h2").get_text(strip=True)
        link = item.select_one("a")["href"]
        results.append((title, link))
    return results

def speak(text):
    print(f"alukakàn luwe: {text}")
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("alapaek nen")
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"yukwe kelak {strTime}")
    elif hour < 18:
        speak("loku")
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"yukwe kelak {strTime}")
    else:
        speak("piske nen")
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"yukwe kelak {strTime}")
    speak("Ni ta ki alukakàn")		
    
def take_command():
    return input("Ki (type your command): ").lower()    
    
def run_assistant():
    wish_user()
    while True:
        query = take_command()

        # searches wikipedia and gives two sentences. 
        if 'wikipedia' in query:
            speak("nta Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(term, sentences=2, auto_suggest=True, redirect=True)
                speak("Wikipedia luwe:")
                speak(result)
            except:
                speak("ku. lapi hach?")

        # block of commands to go to youtube 
        elif 'kta youtube' in query:
            speak("nta YouTube...")
            webbrowser.open("https://www.youtube.com/")

        elif 'nta youtube' in query:
            speak("nta YouTube...")
            webbrowser.open("https://www.youtube.com/")
           
        elif 'youtube a' in query:
            speak("nta YouTube...")
            webbrowser.open("https://www.youtube.com/")
            
        # block of commands to go to google 
        elif 'kta google' in query:
            speak("nta Google...")
            webbrowser.open("https://www.google.com/")

        elif 'nta google' in query:
            speak("nta Google...")
            webbrowser.open("https://www.google.com/")

        elif 'google a' in query:
            speak("nta Google...")
            webbrowser.open("https://www.google.com/")            
            
        # Block to pull up the Lenape Talking Dictionary 
        elif 'dictionary' in query:
            speak("nta Lenape Talking Dictionary...")
            webbrowser.open("https://www.talk-lenape.org")

        elif 'LTD' in query:
            speak("nta Lenape Talking Dictionary...")
            webbrowser.open("https://www.talk-lenape.org")

        elif 'dictionary' in query:
            speak("nta Lenape Talking Dictionary...")
            webbrowser.open("https://www.talk-lenape.org")

        elif 'kta LTD' in query:
            speak("nta Lenape Talking Dictionary...")
            webbrowser.open("https://www.talk-lenape.org")

        elif 'kta dictionary' in query:
            speak("nta Lenape Talking Dictionary...")
            webbrowser.open("https://www.talk-lenape.org")

        elif 'nta LTD' in query:
            speak("nta Lenape Talking Dictionary...")
            webbrowser.open("https://www.talk-lenape.org")

        elif 'nta dictionary' in query:
            speak("nta Lenape Talking Dictionary...")
            webbrowser.open("https://www.talk-lenape.org")

        elif 'LTD a' in query:
            speak("nta Lenape Talking Dictionary...")
            webbrowser.open("https://www.talk-lenape.org")

        elif 'dictionary a' in query:
            speak("nta Lenape Talking Dictionary...")
            webbrowser.open("https://www.talk-lenape.org")

        # seach the LTD 
        elif 'search LTD' in query: 
            search_lenape() 
        elif 'search dictionary' in query: 
            search_lenape()

        # open wikipedia block 
        
        elif 'Wikipedia a' in query:
            speak("nta Wikipedia...")
            webbrowser.open("https://www.wikipedia.org/")
       
       elif 'Nta Wikipedia' in query:
            speak("nta Wikipedia...")
            webbrowser.open("https://www.wikipedia.org/")
            
        elif 'Kta Wikipedia' in query:
            speak("nta Wikipedia...")
            webbrowser.open("https://www.wikipedia.org/")    
       
       # block to start tumblr 
       
        elif 'Tumblr a' in query:
            speak("nta Tumblr...")
            webbrowser.open("https://www.tumblr.com/")
       
       elif 'Nta Tumblr' in query:
            speak("nta Tumblr...")
            webbrowser.open("https://www.tumblr.com/")
            
        elif 'Kta Tumblr' in query:
            speak("nta Tumblr...")
            webbrowser.open("https://www.tumblr.com/")        
       
        # block to start Obsidian.md
        elif 'obsidian' in query:
            speak("nta Obsidian...")
            path =  os.path.join(
                os.getenv("LOCALAPPDATA"),
                "Programs",
                "Obsidian",
                "Obsidian.exe"
            )    
            os.startfile(path)

        elif 'nta obsidian' in query:
            speak("nta Obsidian...")
            path =  os.path.join(
                os.getenv("LOCALAPPDATA"),
                "Programs",
                "Obsidian",
                "Obsidian.exe"
            )    
            os.startfile(path)

        elif 'kta obsidian' in query:
            speak("nta Obsidian...")
            path =  os.path.join(
                os.getenv("LOCALAPPDATA"),
                "Programs",
                "Obsidian",
                "Obsidian.exe"
            )    
            os.startfile(path)

        elif 'obsidian a' in query:
            speak("nta Obsidian...")
            path =  os.path.join(
                os.getenv("LOCALAPPDATA"),
                "Programs",
                "Obsidian",
                "Obsidian.exe"
            )    
            os.startfile(path)
  
        # Start Anki 
        elif 'Kta anki' in query:
            speak("nta Anki...")
            path =  os.path.join(
                os.getenv("LOCALAPPDATA"),
                "Programs",
                "Anki",
                "anki.exe"
            )    
            os.startfile(path)  
          
        elif 'anki a' in query:
            speak("nta Anki...")
            path =  os.path.join(
                os.getenv("LOCALAPPDATA"),
                "Programs",
                "Anki",
                "anki.exe"
            )    
            os.startfile(path)   
            
        elif 'nta anki' in query:
            speak("nta Anki...")
            path =  os.path.join(
                os.getenv("LOCALAPPDATA"),
                "Programs",
                "Anki",
                "anki.exe"
            )    
            os.startfile(path)  
            
        # reviews words from Depaul lessons 
        elif 'review' in query:
            review_words()

        # gives the time 
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"yukwe kelak {strTime}")

        # gives a joke 
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # ends program 
        elif 'exit' in query or 'bye' in query or "knewlech" in query or "Knewlech" in query or "Lapich Knewel" in query or "Lapi Knewlech" in query:
            speak("Knewlech")
            break

        else:
            speak("ku. lapi hach?")    
            
            
            
run_assistant()            

# commented out template that gives example of structure: 
        #elif 'kta youtube' in query:
            #speak("nta YouTube...")
            #webbrowser.open("https://www.youtube.com/")

        #elif 'kta google' in query:
            #speak("nta Google...")
            #webbrowser.open("https://www.google.com/")
