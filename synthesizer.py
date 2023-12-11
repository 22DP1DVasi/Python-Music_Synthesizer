# Created by Danila
# Synthesizer

import keyboard
import pygame

def play_sound(file_path):
    pygame.mixer.init()
    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
    except pygame.error as error:
        print("Audio playback error:", error)

def synthesizer_pad():
    while True:
        if keyboard.is_pressed("q"):
            play_sound()
        #...

