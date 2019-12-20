from pathlib import Path

import numpy as np
import simpleaudio as sa
import wavio
from PIL import Image


class SpectroGraphic(object):
    """docstring for SpectroGraphic"""

    def __init__(
        self,
        path: Path = "./data/tao.png",
        height: int = 100,
        conversion_method: int = 0,
        duration: int = 20,
        min_freq: int = 1000,
        max_freq: int = 8000,
        sample_rate: int = 44100,
        num_tones: int = 3,
    ):
        super(SpectroGraphic, self).__init__()
        self.PATH = Path(path)
        self.image = Image.open(self.PATH)
        self.HEIGHT = height
        self.CONVERSION_METHOD = conversion_method
        self.DURATION = duration

        # Width after setting height to self.height
        # Preserving aspect ratio
        self.WIDTH = int(self.image.width * (self.HEIGHT / self.image.height))

        # duration per column
        self.DURATION_COL = self.DURATION / self.WIDTH

        self.wall_gen = SoundWall(
            duration=self.DURATION_COL,
            sample_rate=sample_rate,
            min_freq=min_freq,
            max_freq=max_freq,
            y_resolution=height,
            num_tones=num_tones,
        )

    def _resize(self):
        """[summary]
        We resize the image to be at most self.HEIGHT pixels tall.

        [description]
        The reason is to put a limit on the frequency resolution that
        we would need to draw it in on the spectrograph.
        """

        # resizing image
        self.image = self.image.resize(
            size=(self.WIDTH, self.HEIGHT), resample=Image.LANCZOS
        )

    def _get_columns(self):

        # resize image
        self._resize()

        # convert to gray scale
        self.image = self.image.convert(mode="L")

        self.image_array = np.array(self.image) / 255

        # transpose image to get list of columns
        self.columns = np.transpose(self.image_array)

    def _sound_array(self):
        self._resize()
        self._get_columns()

        result = np.hstack([self.wall_gen.gen_soundwall(col) for col in self.columns])
        return result


class SoundWall(object):
    """docstring for SoundWall"""

    def __init__(
        self,
        duration: int,
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

        self.duration = duration

    def _get_wave(self, freq: int, intensity: float = 1, duration: float = 1):

        # get timesteps, "duration" is note-duration in seconds
        t = np.linspace(start=0, stop=duration, num=duration * self.sample_rate)

        sine_wave = (intensity ** 5) * np.sin(freq * t * 2 * np.pi)

        return sine_wave

    def gen_sixel(self, y: int, intensity: float = 1):

        # pixel position (count) from the top
        if y < 0 or y > self.y_resolution:
            raise ValueError("y must be between 0 and 1.")

        # loudness of sixel
        if not (0 <= intensity <= 1):
            raise ValueError("Intensity must be between 0 and 1.")

        # length of sixel
        if self.duration < 0:
            raise ValueError("Duration must be positive.")

        # calculating base frequency for sixel
        base_freq = (self.max_freq - self.min_freq) / (self.y_resolution) * (
            self.y_resolution - y
        ) + self.min_freq

        # get base wave
        wave = self._get_wave(base_freq, intensity, self.duration)

        # add tones to fill sixel
        # first tone:
        tone_freq = base_freq
        for _ in range(self.num_tones):

            tone_freq += self.tone_delta
            wave += self._get_wave(tone_freq, intensity, self.duration)

        return wave

    def gen_soundwall(self, column: np.ndarray):

        # empty wave
        wave = self.gen_sixel(0, 0)

        for idx, intensity in enumerate(column):
            wave += self.gen_sixel(idx, intensity)

        return wave


if __name__ == "__main__":

    sg = SpectroGraphic(path="./data/papa.jpeg")
    audio = sg._sound_array()

    audio *= 32767 / np.max(np.abs(audio))

    # convert to 16-bit data
    audio = audio.astype(np.int16)

    # start playback
    wave_object = sa.WaveObject(audio, 1, 2, 44100)

    # wavit for playback to finish before exiting
    po = wave_object.play()
    po.wait_done()
    # wavio.write("test.wav", audio, sw.sample_rate)
