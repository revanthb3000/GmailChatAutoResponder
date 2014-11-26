"""
I'm gonna put in the general purpose functions I use over here.
"""
import pygame
import time

"""
Plays an alert sound.
"""
def playAlert():
    pygame.init()
    pygame.mixer.init()
    sounda= pygame.mixer.Sound("../alert.wav")
    
    sounda.play()
    time.sleep(23)