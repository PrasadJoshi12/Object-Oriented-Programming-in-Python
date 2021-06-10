class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid File")
        self.filename = filename
class MP3file(AudioFile):
    ext = 'mp3'
    def play(self):
        print("Playing mp3: {}".format(self.filename))
class WAVfile(AudioFile):
    ext = 'wav'
    def play(self):
        print("Playing wav: {}".format(self.filename))
        
    
m = MP3file('sample.mp3')
m.play()

w = WAVfile('test.wav')
w.play()

#Output: 
Playing mp3: sample.mp3
Playing wav: test.wav


# We have defined class variable in derived class still parent class 
# is able to access the class variable 'ext' that's Polymorphism.
