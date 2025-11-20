# Assignment: Text Adventure Game using Pygame with minimum of 10 user prompts
#Player is a novice bard navigating through a dungeon
#Player learns different songs to help with their dangerous journey
#Player encounters various obstacles that require specific songs to overcome
#Player starts with no songs and must find them throughout the dungeon
#The game ends when the player reaches the final destination or fails to overcome an obstacle
#Use Pygame for graphics and user input

import pygame
from time import sleep
import sys
Gameover = False


# ------------ Global Dictionaries and Lists ------------
songs = {
    "Healing Song": "Restores health",
    "Fireball Song": "Casts a fireball to defeat enemies",
    "Invisibility Song": "Makes the player invisible to enemies",
    "Speed Song": "Increases movement speed",
    "Shield Song": "Creates a protective shield around the player"
}

PlayerStats={
    "Health": 100,
    "Inventory": [],
    "Location": "Dungeon Entrance"
}

verblist={"languageHurt:[]


#Initialize Pygame
pygame.init()

#Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text Adventure Game")


#Main Game Loop
while not Gameover:
    
    #Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Drawing
    #Fill screen with black
    screen.fill((0, 0, 0))

    #Update the display
    pygame.display.flip()