from synthesizer import Synthesizer, Waveform, player

def play(hz, duration):
    synthesizer = Synthesizer(Waveform.sine, 1.0, False)
    wave = synthesizer.generate_constant_wave(hz, duration)
    player_ = player.Player()
    player_.open_stream()
    player_.play_wave(wave)
