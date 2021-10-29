import colorama as clrama
from winsound import Beep
import time
import os
from gtts import gTTS
from code import english_to_morse


def eng_to_morse():
    eng_to_morse_message = []
    for char in english_message:
        eng_to_morse_message.append(english_to_morse[char])
    return ' '.join(eng_to_morse_message)


def morse_to_english():
    morse_to_english_message = []
    english_keys = list(english_to_morse.keys())
    morse_values = list(english_to_morse.values())
    for char in morse_message.split(" "):
        index = morse_values.index(char)
        english_letter = english_keys[index]
        morse_to_english_message.append(english_letter)
    return ''.join(morse_to_english_message)


def play_again_choice():
    choice_input = input("\nWould you like to make another message? Please type 'yes' or 'no': ").lower()
    if choice_input == 'yes':
        choice = True
    else:
        choice = False
    return choice


def play_morse_sound():
    for char in encoded_message:
        if char == ".":
            Beep(500, 100)
            time.sleep(.05)
        elif char == "-":
            Beep(500, 300)
            time.sleep(.05)
        elif char == " ":
            time.sleep(.5)


def play_eng_sound():
    text_to_speak = gTTS(encoded_message)
    text_to_speak.save(savefile='eng_message.mp3')
    os.system('eng_message.mp3')


clrama.init()
first_play = True
play_again = False
while first_play or play_again:
    if first_play:
        welcome = "\nWelcome to the English-Morse code converter. This converter can convert messages both ways!"
        print(welcome)
    user_input = input("\nWhat language will you be typing? Please write 'English', 'Morse', or 'Exit': ").lower()

    if user_input == 'english':
        english_message = input(
            "\nWhat English message would you like to convert into Morse code? Write it here: ").upper()
        encoded_message = eng_to_morse()
        print(f"\n {clrama.Fore.CYAN}{encoded_message}{clrama.Fore.RESET}")
        sound_prompt = input("\nWould you like to hear the encoded message? Please type 'yes' or 'no': ").lower()
        if sound_prompt == "yes":
            play_morse_sound()
        play_again = play_again_choice()

    elif user_input == 'morse':
        morse_message = input("\nWhat Morse coded message would you like to convert into English? Write it here: ")
        encoded_message = morse_to_english()
        print(f"\n {clrama.Fore.CYAN}{encoded_message}{clrama.Fore.RESET}")
        sound_prompt = input("\nWould you like to hear the encoded message? Please type 'yes' or 'no': ").lower()
        if sound_prompt == "yes":
            play_eng_sound()
        play_again = play_again_choice()

    elif user_input == 'exit':
        play_again = False

    else:
        print(f"{clrama.Fore.RED}\nOops. You must have typed an invalid command. Please try again.{clrama.Fore.RESET}")
        play_again = True

    first_play = False

