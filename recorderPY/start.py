import pygame
import sys
import keyboard
import pyautogui
from PIL import *
pygame.init()
Display = pygame.display.set_mode((800,600))
def start():
    try:
        img = pygame.image.load('./recorder/ss.png')
        IMG = pygame.transform.scale(img,(800,600))
        Display.blit(IMG,(0,0))
    except:
        pass
def record():
    ss = pyautogui.screenshot()
    ss.save('./recorder/ss.png')   
keyboard.press_and_release('windows + Alt + R')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    record()
    start()