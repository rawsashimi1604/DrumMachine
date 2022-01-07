import pygame as pg
from Sampler import Sampler
from Grid import Grid
from Player import Player
import time

pg.init()

# Initialize Drum Kit Sampler
drumkitSampler = Sampler(16) # Create drum kit sampler with 16 channels
drumkitSampler.addSound("hh_close", "samples\kit_close\CYCdh_K1close_ClHat-02.wav") 
drumkitSampler.addSound("hh_open", "samples\kit_close\CYCdh_K1close_OpHat-01.wav") 
drumkitSampler.addSound("hh_clutch", "samples\kit_close\CYCdh_K1close_PdHat-01.wav") 
drumkitSampler.addSound("kick", "samples\kit_close\CYCdh_K1close_Kick-04.wav") 
drumkitSampler.addSound("snare", "samples\kit_close\CYCdh_K1close_Snr-03.wav")
drumkitSampler.addSound("metronome", "samples\click\High Seiko SQ50.wav")

# Initialize Player
player = Player(80, drumkitSampler)
player.init()

# Initialize Grid Object for each drum sound
hh_close_grid = Grid(16, [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
hh_open_grid = Grid(16, [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
hh_clutch_grid = Grid(16, [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
kick_grid = Grid(16, [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])
snare_grid = Grid(16, [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
metronome_grid = Grid(16, [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])

# Import Grid Objects into Player
player.importSoundGrid("hh_close", hh_close_grid)
player.importSoundGrid("hh_open", hh_open_grid)
player.importSoundGrid("hh_clutch", hh_clutch_grid)
player.importSoundGrid("kick", kick_grid)
player.importSoundGrid("snare", snare_grid)
player.importSoundGrid("metronome", metronome_grid)

# Mix volume
player.changeVolume("hh_close", 0.30)
player.changeVolume("hh_open", 0.30)
player.changeVolume("hh_clutch", 0.30)
player.changeVolume("snare", 0.9)
player.changeVolume("kick", 0.8)
player.changeVolume("metronome", 0.50)

# Start player
player.start()