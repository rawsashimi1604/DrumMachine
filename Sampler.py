import pygame as pg

class Sampler:
    def __init__(self, channels):
        self.channels = channels

        self.sounds = {} # Mapping of name : Sound objects
        self.channelMap = {} # Mapping of name : Channel objects
        self.soundCount = 0
    
    # Add sound to sound dictionary
    def addSound(self, name, sound):
        if self.soundCount <= self.channels:
            if name not in self.sounds:
                self.sounds[name] = pg.mixer.Sound(sound)
                self.mapChannel(name)
                self.soundCount += 1
            else:
                # If name already exists, do not add, raise error
                raise ValueError("Current name already exists.")

        else:
            raise ValueError("Number of sounds is already maximum.")
    
    # Maps sound to specific channel
    def mapChannel(self, name):
        self.channelMap[name] = pg.mixer.Channel(self.soundCount)

    # Play sound according to mapped channel
    def playSound(self, name):
        self.channelMap[name].play(self.sounds[name])

    # Change volume of sound
    def changeVolume(self, name, value):
        if value < 0 or value > 1:
            raise ValueError("Volume value must be between 0.0 and 1.0")
        else:
            channel = self.channelMap[name]
            channel.set_volume(value)
    
        

if __name__ == "__main__":
    drumkitSampler = Sampler(16) # Create drum kit sampler with 16 channels
    drumkitSampler.addSound("hh_close", "samples\kit_close\CYCdh_K1close_ClHat-01.wav") 
    drumkitSampler.addSound("hh_open", "samples\kit_close\CYCdh_K1close_OpHat-01.wav") 
    drumkitSampler.addSound("hh_clutch", "samples\kit_close\CYCdh_K1close_PdHat-01.wav") 
    drumkitSampler.addSound("kick", "samples\kit_close\CYCdh_K1close_Kick-01.wav") 
    drumkitSampler.addSound("snare", "samples\kit_close\CYCdh_K1close_Snr-01.wav") 


    

    

