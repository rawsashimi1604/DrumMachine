# Each grid represents a bar in music
# Each grid contains 16 notes (16 semiquavers)
# Each grid layout will be an array, 1 => play, -1 => off, 0 => rest

# 3 parameters, on off rest
# To be added, tuple velocity

class Grid:
    def __init__(self, notes, layout=None):
        self.notes = notes
        self.layout = layout
        if not self.layout:
            self.layout = [0 for i in range(notes)]

    def changeLayout(self, beat, beat_division, state):
        gridPlacement = ((beat - 1) * 4) + beat_division
        if gridPlacement > self.notes - 1 or gridPlacement < 0:
            raise ValueError("Grid placement is out of bounds.")
        else:
            self.layout[gridPlacement] = state