import speech_recognition as sr
from gtts import gTTS
import time
import playsound
from time import ctime
import webbrowser
import pyautogui
import random
import pyjokes
import os
import numpy as np


class person:
    name = ''

    def setName(self, name):
        self.name = name


def there_exists(terms, said):
    for term in terms:
        if term in said:
            return True


def hydrogen_speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'hydrogen.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    print(f'Hydrogen 2.0: {text}')
    os.remove(filename)


def hydrogen_respond(said, person_obj):
    if there_exists(['hey', 'hi', 'hello'], said) and 'remember' and 'this' and 'Delhi' not in said:
        greetings = [f"hey, how can I help you, {person_obj.name}", f"hey, what's up?, {person_obj.name}",
                     f"I'm listening, {person_obj.name}", f"how can I help you?, {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        hydrogen_speak(greet)

    elif there_exists(["your name", "what's your name", "tell me your name", "who are you"], said):
        if person_obj.name:
            hydrogen_speak("my name is Hydrogen and my version is 1.0")
        else:
            hydrogen_speak(
                "my name is Hydrogen and my version is 1.0. what's your name?")

    elif there_exists(["what are you doing"], said):
        replies = ["nothing, just chilling", "you know, just my thing",
                   "nothing, just scrolling through instagram"]
        reply = replies[random.randint(0, len(replies) - 1)]
        hydrogen_speak(reply)

    elif there_exists(["is my name"], said):
        if person_obj.name:
            hydrogen_speak(f"your name is {person_obj.name}")
        else:
            hydrogen_speak("I dont know your name. what is your name")

    elif there_exists(["my name is"], said):
        if "not" in said:
            hydrogen_speak("okay then what is your name?")
        else:
            person_name = said.split("is")[-1].strip()
            hydrogen_speak(f"okay, i will remember that {person_name}")
            person_obj.setName(person_name)

    elif there_exists(["how are you"], said):
        hydrogen_speak(f"I'm fine, thanks for asking, {person_obj.name}")

    elif there_exists(["what is the time", "tell me the time", "what time is it"], said):
        time_ = ctime().split(" ")[3].split(":")[0:2]
        if time_[0] == "00":
            hours = '12'
        else:
            hours = time_[0]
        minutes = time_[1]
        time_ = f'{hours}. {minutes}'
        hydrogen_speak(time_)

    elif there_exists(["play rock paper scissors"], said):
        hydrogen_speak("choose among rock paper or scissors")
        moves = ["rock", "paper", "scissor"]
        cmove = random.choice(moves)

        pmove = get_audio()
        # pmove = input("Your choice: ").lower()

        hydrogen_speak(f"I chose {cmove} and You chose {pmove}")
        if pmove == cmove:
            hydrogen_speak("the match is a draw")
        elif pmove == "rock" and cmove == "scissor":
            hydrogen_speak("you won")
        elif pmove == "rock" and cmove == "paper":
            hydrogen_speak("i won")
        elif pmove == "paper" and cmove == "rock":
            hydrogen_speak("you won")
        elif pmove == "paper" and cmove == "scissor":
            hydrogen_speak("i won")
        elif pmove == "scissor" and cmove == "paper":
            hydrogen_speak("you won")
        elif pmove == "scissor" and cmove == "rock":
            hydrogen_speak("i won")

    elif there_exists(["make a note", "take a note", "remember something", "remember this"], said):
        hydrogen_speak("ok, what do you want me to remember")

        said = get_audio()
        # said = input("Note: ")

        with open(f"your_notes.txt", "a") as file:
            file.write(said)
            file.write('\n')
        hydrogen_speak("Done")

    elif there_exists(["what did i ask you to note down", "show me my notes", "ask you to remember"], said):
        if os.path.exists("your_notes.txt"):
            hydrogen_speak("sure")
            with open("your_notes.txt", "r") as file:
                print('')
                print(file.read())
        else:
            hydrogen_speak("you did not ask me to make any note")

    elif there_exists(["forget what i told you to remember", "clear my notes", "delete my notes"], said):
        hydrogen_speak("consider it done")
        try:
            os.remove("your_notes.txt")
        except Exception:
            pass

    elif there_exists(["search for", "who is"], said) and 'youtube' not in said:
        if there_exists(["search for"], said):
            search_term = said.split("for")[-1].strip()
            hydrogen_speak(f'Here is what I found for {search_term} on google')
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
        if there_exists(["who is"], said):
            search_term = said.split("is")[-1].strip()
            hydrogen_speak(
                f'Here is what I found about {search_term} on google')
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)

    elif there_exists(["youtube for"], said):
        search_term = said.split("for")[-1].strip()
        hydrogen_speak(f'Here is what I found for {search_term} on youtube')
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)

    elif there_exists(["open"], said):
        search_term = said.split("open")[-1].strip()
        if search_term == "youtube":
            hydrogen_speak(f"opening {search_term}")
            url = "https://www.youtube.com/"
            webbrowser.get().open(url)
        elif search_term == "twitter":
            hydrogen_speak(f"opening {search_term}")
            url = "https://twitter.com/home"
            webbrowser.get().open(url)
        elif search_term == "whatsapp":
            hydrogen_speak(f"opening {search_term}")
            url = "https://web.whatsapp.com/"
            webbrowser.get().open(url)
        elif search_term == "mail":
            hydrogen_speak(f"opening {search_term}")
            url = "https://mail.google.com/mail/u/0/#inbox"
            webbrowser.get().open(url)
        elif search_term == "reddit":
            hydrogen_speak(f"opening {search_term}")
            url = "https://www.reddit.com/"
            webbrowser.get().open(url)
        else:
            hydrogen_speak("sorry i did not get that")

    elif there_exists(["latest news", "news"], said):
        hydrogen_speak("here's the latest news for you")
        url = "https://news.google.com/topstories?gl=IN&hl=en-IN&ceid=IN:en"
        webbrowser.get().open(url)

    elif there_exists(["capture", "my screen", "screenshot"], said):
        myScreenshot = pyautogui.screenshot()
        num = random.randint(0, 10000)
        myScreenshot.save(r"screen" + str(num) + ".png")
        hydrogen_speak("done")

    elif there_exists(["joke"], said):
        hydrogen_speak(pyjokes.get_joke())

    elif there_exists(["location of"], said):
        search_term = said.split("of")[-1].strip()
        hydrogen_speak(f"getting the location of {search_term}")
        url = f"https://www.google.com/maps/place/{search_term}"
        webbrowser.get().open(url)

    elif "close" and "browser" in said:
        hydrogen_speak("closing browser")
        os.system("taskkill /im chrome.exe /f")

    elif there_exists(["will you be my boyfriend", "wll you be my girlfriend"], said):
        hydrogen_speak(
            "haha, i am not sure about that, you should give me some time to think")

    elif there_exists(["i love you"], said):
        hydrogen_speak("of course, i love you too, you are my bestfriend")

    elif there_exists(["who made you", "your purpose"], said):
        hydrogen_speak(
            "i was created by Harin Kumar, as a general purpose voice assistant")

    elif there_exists(["solve sudoku"], said):
        hydrogen_speak("ok. processing the algorithms")
        solve_sudoku()

    elif there_exists(["i want to play some games"], said):
        hydrogen_speak("ok, which game do you want to play")

    elif there_exists(["start snake"], said):
        hydrogen_speak("opening snake game")
        hydrogen_speak("these are the controls")
        print("Controls:")
        print("w, a, s, d - movement keys")
        print("e - exit game")

        dir_ = os.getcwd()
        dir_ = dir_.split("\\")
        cd = dir_[-1]

        if cd == "Hydrogen_2.0":
            os.chdir("hydrogen_assets")
        elif cd == "hydrogen_assets":
            pass
        elif cd == "si":
            os.chdir('..')

        os.system("hs.exe")

    elif there_exists(["start ping pong"], said):
        hydrogen_speak("opening ping pong")
        hydrogen_speak("these are the controls")
        print("Controls: ")
        print("w,s - movement keys(player a)")
        print("up,down - movement keys(player b)")
        print("e - exit game")

        dir_ = os.getcwd()
        dir_ = dir_.split("\\")
        cd = dir_[-1]

        if cd == "Hydrogen_2.0":
            os.chdir("hydrogen_assets")
        elif cd == "hydrogen_assets":
            pass
        elif cd == "si":
            os.chdir('..')

        os.system("hp.exe")

    elif there_exists(["start space invaders"], said):
        hydrogen_speak("opening space invaders")
        hydrogen_speak("these are the controls")
        print("Controls: ")
        print("a, d - movement keys")
        print("w - shoot")
        print("e - exit game")

        dir_ = os.getcwd()
        dir_ = dir_.split("\\")
        cd = dir_[-1]

        if cd == "Hydrogen_2.0":
            os.chdir("hydrogen_assets\si")
        elif cd == "hydrogen_assets":
            os.chdir("si")
        elif cd == "si":
            pass

        os.system("hsi.exe")

    elif there_exists(["exit", "quit", "goodbye", "bye", "shutdown"], said):
        hydrogen_speak('bye. take care')
        hydrogen_speak("going offline")
        exit()


def solve_sudoku():
    def empty_pos(b):
        for i in range(len(b)):
            for j in range(len(b[0])):
                if b[i][j] == 0:
                    return (i, j)

        return None

    def is_valid(b, num, pos):
        for i in range(len(b[0])):
            if b[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(b)):
            if b[i][pos[1]] == num and pos[0] != i:
                return False

        x = pos[1] // 3
        y = pos[0] // 3

        for i in range(y*3, y*3 + 3):
            for j in range(x*3, x*3 + 3):
                if b[i][j] == num and (i, j) != pos:
                    return False

        return True

    def backtrack(b):
        empty = empty_pos(b)
        if not empty:
            return True
        else:
            r, c = empty

        for i in range(1, 10):
            if is_valid(b, i, (r, c)):
                b[r][c] = i

                if backtrack(b):
                    return True

                b[r][c] = 0

        return False

    def print_board(b):
        for i in range(len(b)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(b[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end=" ")

                if j == 8:
                    print(b[i][j])
                else:
                    print(str(b[i][j]) + " ", end="")

    def user_input():
        hydrogen_speak("type in the board entries")
        print("")
        print("enter the entries in a single line(separated by space, enter 0 if empty): ")
        entries = list(map(int, input().split()))
        matrix = np.array(entries).reshape(9, 9)
        return matrix

    board = user_input()
    print("")
    hydrogen_speak("setting up the board")

    print("")
    print_board(board)
    print("")

    hydrogen_speak("processing the board")
    start = time.time()
    backtrack(board)
    end = time.time()
    time_taken = end - start
    time_taken_ = "{:.4f}".format(time_taken)
    sent = f"time taken to solve is, {time_taken_} seconds"
    hydrogen_speak(sent)
    hydrogen_speak("displaying the output")

    print("")
    print_board(board)
    print("")


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio)
            print(f'You: {said}')
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            hydrogen_speak('Sorry, the service is down')
    return said.lower()


def hydrogen_start():
    hydrogen_speak('Hydrogen, 2.0. at your service, how can i help you')
    person_obj = person()
    while True:
        said = get_audio()
        # said = input("You: ").lower()
        hydrogen_respond(said, person_obj)


hydrogen_start()
