"""
Created on Fri Sep  15 12:30:16 2023

@author: M.Nasir
"""


''' Task 1 : Music Player in Python 
'''


import pygame

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()

# Load a music file
music_file = "abc.mp3"
pygame.mixer.music.load(music_file)

while True:
    print("Music Player Menu:")
    print("1. Play")
    print("2. Stop")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        pygame.mixer.music.play()
    elif choice == '2':
        pygame.mixer.music.stop()
    elif choice == '3':
        pygame.mixer.music.stop()
        pygame.quit()
        break
    else:
        print("Invalid choice. Please enter a valid option.")
