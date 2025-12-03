# CLI-Lenape-Assistant
This is a command line Lenape assistant to help you do various tasks from the command line in English and Lenape. 

Original Tutorial this is Built and Expanded from: [![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-0F9D58?style=flat&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/python/voice-assistant-using-python/)

## Introduction 
A Python-based voice assistant focused on supporting the Lenape language and general productivity.
Built on top of a base Python voice assistant tutorial from GeeksforGeeks, with additional functionality for the Southern Unami dialect and custom commands.

## Features
- Fully command-line driven; accepts typed commands
- Review random Lenape vocabulary from a built-in dictionary
- Open websites like YouTube, Google, Tumblr, and the Lenape Talking Dictionary
- Open local applications: Obsidian, Anki
- Tell the current time
- Tell jokes using pyjokes

## Commands
| Command Keywords    | Action                                                        |
| ------------------- | ------------------------------------------------------------- |
| `wikipedia`         | Search Wikipedia and read a short summary                     |
| `Wikipedia a`       | Open [Wikipedia](https://www.wikipedia.org/)                  |
| `Nta Wikipedia`     | Open [Wikipedia](https://www.wikipedia.org/)                  |
| `Kta Wikipedia`     | Open [Wikipedia](https://www.wikipedia.org/)                  |
| `kta youtube`       | Open [YouTube](https://www.youtube.com/)                      |
| `nta youtube`       | Open [YouTube](https://www.youtube.com/)                      |
| `youtube a`         | Open [YouTube](https://www.youtube.com/)                      |
| `kta google`        | Open [Google](https://www.google.com/)                        |
| `nta google`        | Open [Google](https://www.google.com/)                        |
| `google a`          | Open [Google](https://www.google.com/)                        |
| `dictionary`        | Open [Lenape Talking Dictionary](https://www.talk-lenape.org) |
| `LTD`               | Open [Lenape Talking Dictionary](https://www.talk-lenape.org) |
| `kta LTD`           | Open [Lenape Talking Dictionary](https://www.talk-lenape.org) |
| `kta dictionary`    | Open [Lenape Talking Dictionary](https://www.talk-lenape.org) |
| `nta LTD`           | Open [Lenape Talking Dictionary](https://www.talk-lenape.org) |
| `nta dictionary`    | Open [Lenape Talking Dictionary](https://www.talk-lenape.org) |
| `LTD a`             | Open [Lenape Talking Dictionary](https://www.talk-lenape.org) |
| `dictionary a`      | Open [Lenape Talking Dictionary](https://www.talk-lenape.org) |
| `search LTD`        | Search the Lenape Talking Dictionary                          |
| `search dictionary` | Search the Lenape Talking Dictionary                          |
| `Tumblr a`          | Open [Tumblr](https://www.tumblr.com/)                        |
| `Nta Tumblr`        | Open [Tumblr](https://www.tumblr.com/)                        |
| `Kta Tumblr`        | Open [Tumblr](https://www.tumblr.com/)                        |
| `obsidian`          | Open Obsidian.md application                                  |
| `nta obsidian`      | Open Obsidian.md application                                  |
| `kta obsidian`      | Open Obsidian.md application                                  |
| `obsidian a`        | Open Obsidian.md application                                  |
| `Kta anki`          | Open Anki application                                         |
| `anki a`            | Open Anki application                                         |
| `nta anki`          | Open Anki application                                         |
| `review`            | Review random words from the built-in Lenape dictionary       |
| `time`              | Speak the current time                                        |
| `joke`              | Speak a random joke using pyjokes                             |
| `exit`              | Exit the assistant                                            |
| `bye`               | Exit the assistant                                            |
| `knewlech`          | Exit the assistant                                            |
| `Knewlech`          | Exit the assistant                                            |
| `Lapich Knewel`     | Exit the assistant                                            |
| `Lapi Knewlech`     | Exit the assistant                                            |


## Installation 
1. Clone this repository (or install from Github):
```
git clone https://github.com/moorelanguage/CLI-Lenape-Assistant.git
cd CLI-Lenape-Assistant
```
2. Install required Python packages:
```
pip install pyttsx3 wikipedia pyjokes beautifulsoup4
```
3. Run the assistant, which is assistant.py
```
python assistant.py
```
Note: If you downloaded the ZIP file from GitHub, unzip it first and navigate to the folder containing assistant.py in your command line. 

## Roadmap 
- Fully implement searching Wikipedia and providing short summaries
- Add similar searching of sources like Wikipedia, think encyclopedia britannica 
- Add more websites, currently planning to add Linkedin and Github.

## Contributing
1. Fork the repository
2. Create your branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push to your branch: `git push origin feature-name`
5. Open a Pull Request

## Technology used 
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
