import pygame as pg
import time

pg.mixer.init()
pg.init()


# Sounds
hhClose = pg.mixer.Sound("./samples/kit_close/CYCdh_K1close_ClHat-01.wav")
hhOpen = pg.mixer.Sound("./samples/kit_close/CYCdh_K1close_OpHat-01.wav")
kick = pg.mixer.Sound("./samples/kit_close/CYCdh_K1close_Kick-01.wav")
snare = pg.mixer.Sound("./samples/kit_close/CYCdh_K1close_Snr-01.wav")

pg.mixer.set_num_channels(50)

for i in range(25):
    pg.mixer.Channel(1).play(hhClose)
    pg.mixer.Channel(0).play(kick)
    
    time.sleep(0.3)

    pg.mixer.Channel(1).play(hhClose)

    time.sleep(0.3)

    pg.mixer.Channel(1).play(hhClose)
    pg.mixer.Channel(0).play(snare)

    time.sleep(0.3)

    pg.mixer.Channel(1).play(hhClose)

    time.sleep(0.15)

    pg.mixer.Channel(1).play(hhClose)

    time.sleep(0.15)

    
