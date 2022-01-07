import pygame as pg
from Sampler import Sampler
import time

pg.mixer.init()
pg.init()

# Create sampler
drumkitSampler = Sampler(16) # Create drum kit sampler with 16 channels
drumkitSampler.addSound("hh_close", "samples\kit_close\CYCdh_K1close_ClHat-01.wav") 
drumkitSampler.addSound("hh_open", "samples\kit_close\CYCdh_K1close_OpHat-01.wav") 
drumkitSampler.addSound("hh_clutch", "samples\kit_close\CYCdh_K1close_PdHat-01.wav") 
drumkitSampler.addSound("kick", "samples\kit_close\CYCdh_K1close_Kick-01.wav") 
drumkitSampler.addSound("snare", "samples\kit_close\CYCdh_K1close_Snr-01.wav")

for i in range(100):
    drumkitSampler.playSound("kick")
    drumkitSampler.playSound("hh_close")

    time.sleep(0.3)

    drumkitSampler.playSound("hh_close")

    time.sleep(0.3)

    drumkitSampler.playSound("snare")
    drumkitSampler.playSound("hh_close")

    time.sleep(0.3)

    drumkitSampler.playSound("hh_close")

    time.sleep(0.3)