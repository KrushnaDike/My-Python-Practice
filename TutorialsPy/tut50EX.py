# Healthy Programer
# 9am - 5am
# Water - water.mp3 (2 liter) - Stopper(Drank) - log - Every 40 min
# Eayes - eyes.mp3 - Stopper(EyDone) - log - Every 30 min
# Physical activity - pysical.mp3 - Stopper(ExDone) - log - Every 45 min
# Rules
#     use Pygame module to play audio


from pygame import mixer
from time import time
# # Starting the mixer
# mixer.init()
#
# # Loading the song
# mixer.music.load("Drank.mp3")
#
# # Setting the volume
# mixer.music.set_volume(0.7)
#
# # Start playing the song
# mixer.music.play()
#
# # infinite loop
# while True:
#
#     print("Press 'p' to pause, 'r' to resume")
#     print("Press 'e' to exit the program")
#     query = input("  ")
#
#     if query == 'p':
#
#         # Pausing the music
#         mixer.music.pause()
#     elif query == 'r':
#
#         # Resuming the music
#         mixer.music.unpause()
#     elif query == 'e':
#
#         # Stop the mixer
#         mixer.music.stop()
#         break


# This code is also Work

print("😍😍😍😍😍😍😍😍😍😍😍😍❤Healthy Programmer😍😍😍😍😍😍😍😍😍😍😍😍❤")
name = input("Enter Your Name :")
print(f"{name.capitalize()} Welcome to our office")
print("We will help to maintain your health...!")


def getdate():
    import datetime
    return datetime.datetime.now()

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {str([str(getdate())])}\n")

def water_func(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    a = input("pleas Drank water and type \'Drank\' to stop\n")
    if a == "Drank":
        log_now("Drank Water at")
        mixer.music.stop()

    while a != "Drank":
        print("Pleas Enter Correct input...!")
        a = input("pleas Drank water and type \'Drank\' to stop\n")
        if a == "Drank":
            log_now("Drank Water at")
            mixer.music.stop()

def eyes_func(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    a = input("pleas Done Exercise and type \'EyDone\' to stop\n")
    if a == "EyDone":
        log_now("Eyes Exercise done at")
        mixer.music.stop()

    while a != "EyDone":
        print("Pleas Enter Correct input...!")
        a = input("pleas Done Exercise and type \'EyDone\' to stop\n")
        if a == "EyDone":
            log_now("Eyes Exercise done at")
            mixer.music.stop()

def phy_func(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    a = input("pleas Done physical exercise and type \'ExDone\' to stop\n")
    if a == "ExDone":
        log_now("Physical Exercise done at")
        mixer.music.stop()

    while a != "ExDone":
        print("Pleas Enter Correct input...!")
        a = input("pleas Done physical exercise and type \'ExDone\' to stop\n")
        if a == "ExDone":
            log_now("Physical Exercise done at")
            mixer.music.stop()

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_phy = time()
    watersecs = 50
    eyessecs = 100
    physecs = 200
    while True:
        if time() - init_water > watersecs:
            water_func("Drank.mp3")
            init_water = time()

        if time() - init_eyes > eyessecs:
            eyes_func("Eyes.mp3")
            init_eyes = time()

        if time() - init_phy > physecs:
            phy_func("Excersise.mp3")
            init_phy = time()







# Main Program is here

# print("😍😍😍😍😍😍😍😍😍😍😍😍❤Healthy Programmer😍😍😍😍😍😍😍😍😍😍😍😍❤")
# name = input("Enter Your Name :")
# print(f"{name.capitalize()} Welcome to our office")
# print("We will help to maintain your health...!")
#
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
# def music_onloop(file, stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#     a = input()
#     while True:
#         if a == stopper:
#             mixer.music.stop()
#             break
#
# def log_now(msg):
#     with open("mylogs.txt", "a") as f:
#         f.write(f"{msg} {str([str(getdate())])}\n")
#
# if __name__ == "__main__":
#     init_water = time()
#     init_eyes = time()
#     init_phy = time()
#     watersecs = 5
#     eyessecs = 10
#     physecs = 20
#
#     while True:
#         if time() - init_water > watersecs:
#             print("Pleas Drank water and type \'Drank\' to stop:")
#             music_onloop("Drank.mp3", "Drank")
#             log_now("Drank water at ")
#             init_water = time()
#
#         if time() - init_eyes > eyessecs:
#             print("Plead Done Exercise and type \'EyDone\' to stop")
#             music_onloop("Eyes.mp3", "EyDone")
#             log_now("Eyes exercise done at ")
#             init_eyes = time()
#
#         if time() - init_phy > physecs:
#             print("Pleas Done Physical Exercise and type \'ExDone\'")
#             music_onloop("Excersise.mp3", "ExDone")
#             log_now("Exercise Done at ")
#             init_phy = time()