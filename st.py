from synthesizer import Synthesizer, Waveform, player

def play(hz, volume):
    synthesizer = Synthesizer(Waveform.sine, volume, False)
    wave = synthesizer.generate_constant_wave(hz, 5)
    player_ = player.Player()
    player_.open_stream()
    player_.play_wave(wave)
