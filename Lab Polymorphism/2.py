class Guitar:
    def play(self):
        print("playing the guitar")

class Piano:
    def play(self):
        print("playing the piano")

def play_instrument(instrument):
    if instrument:
        instrument.play()
    else:
        print("No instrument to play")

guitar = Guitar()
piano = Piano()

play_instrument(guitar)
play_instrument(piano)