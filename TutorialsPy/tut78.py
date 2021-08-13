from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def mylogs_1(msg):
    with open("mylogs_1.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_phy = time()
    watersecs = 40*60
    eyessecs = 30*60
    physecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print(f"Please drink water and enter 'drank' to stop alarm.")
            musiconloop("Drank.mp3", "drank")
            mylogs_1("Drink water at")
            init_water = time()

        if time() - init_eyes > eyessecs:
            print(f"Please do eyes exersice and enter 'eydone' to stop alarm.")
            musiconloop("Eyes.mp3", "eydone")
            mylogs_1("Eyes exercise done at")
            init_eyes = time()

        if time() - init_phy > physecs:
            print(f"Please do physical exersice and enter 'pydone' to stop alarm.")
            musiconloop("Excersise.mp3", "pydone")
            mylogs_1("Physical exercise done at")
            init_phy = time()