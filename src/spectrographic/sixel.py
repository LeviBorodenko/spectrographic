import numpy as np
import simpleaudio as sa


class SoundWall(object):
    """docstring for Sixel"""

    def __init__(
        self,
        sample_rate: int = 44100,
        min_freq: int = 10000,
        max_freq: int = 17000,
        y_resolution: int = 1000,
        num_tones: int = 3,
    ):
        super(SoundWall, self).__init__()

        # Test and save parameters

        # height of image in pixels
        self.y_resolution = y_resolution

        # sample rate; 44100 is a good default
        self.sample_rate = sample_rate

        # region in which to draw the sixel
        self.min_freq = min_freq
        self.max_freq = max_freq

        # Number of tones used to fill the sixel
        self.num_tones = num_tones

        # height of each sixel
        self.height = (max_freq - min_freq) / (y_resolution)

        # delta height between each tone
        self.tone_delta = self.height / num_tones

    def _get_wave(self, freq: int, intensity: float = 1, duration: float = 1):

        # get timesteps, "duration" is note duration in seconds
        t = np.linspace(start=0, stop=duration, num=duration * self.sample_rate)

        sine_wave = intensity * np.sin(freq * t * 2 * np.pi)

        return sine_wave

    def _gen_sixel(self, y: int, intensity: float = 1, duration: float = 1):

        # pixel position (count) from the top
        if y < 0 or y > self.y_resolution:
            raise ValueError("y must be between 0 and 1.")

        # loudness of sixel
        if not (0 <= intensity <= 1):
            raise ValueError("Intensity must be between 0 and 1.")

        # length of sixel
        if duration < 0:
            raise ValueError("Duration must be positive.")

        # calculating base frequency for sixel
        base_freq = (self.max_freq - self.min_freq) / (self.y_resolution) * (
            self.y_resolution - y
        ) + self.min_freq

        # get base wave
        wave = self._get_wave(base_freq, intensity, duration)

        # add tones to fill sixel
        # first tone:
        tone_freq = base_freq
        for _ in range(self.num_tones):

            tone_freq += self.tone_delta
            wave += self._get_wave(tone_freq, intensity, duration)

        return wave


if __name__ == "__main__":

    sw = SoundWall(y_resolution=10, num_tones=10)

    audio = np.hstack(
        [
            sw._gen_sixel(1) + sw._gen_sixel(7),
            sw._gen_sixel(2),
            sw._gen_sixel(3, intensity=0.3, duration=3),
            sw._gen_sixel(4),
            sw._gen_sixel(7),
        ]
    )
    audio *= 32767 / np.max(np.abs(audio))

    # convert to 16-bit data
    audio = audio.astype(np.int16)

    # start playback
    play_obj = sa.play_buffer(audio, 1, 2, sw.sample_rate)

    # wavit for playback to finish before exiting
    play_obj.wait_done()
