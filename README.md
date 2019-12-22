# SpectroGraphic
_Turn any image into a sound whose spectrogram looks like the image!_

![result](banner.png)

<hr>

#### What is this?

Most sounds are intricate combinations of many acoustic waves each having different frequencies and intensities. A spectrogram is a way to represent sound by plotting time on the horizontal axis and the frequency spectrum on the vertical axis. Sort of like sheet music on steroids.

What this tool does is, taking an image and simply interpreting it as a spectrogram. Therefore, by generating the corresponding sound, we have embedded our image in a spectrogram.

The game DOOM used a similar technique to [hide satanic figures inside its soundtrack](https://www.theverge.com/2016/5/31/11825606/doom-2016-soundtrack-satan-666-inverted-pentagram). Now everyone can do the same! 😊

#### Set-up

Get the command-line tool `spectrographic` via `pip` by running `pip install spectrographic`. You can also simply use `spectrographic.py` from `stand-alone\` as a command-line tool directly.
Furthermore, make sure you meet all the dependencies inside the `requirements.txt`. Install them with `pip install requirements.txt`.

After installation with `pip` one simply needs to run `spectrographic [...]` in the console and with the stand-alone script you have to use `python spectrographic.py [...]` inside the folder containing `spectrographic.py`.

You could also simply import the `SpectroGraphic` class from `spectrographic`. Check the doc-strings for detailed explanations and more features.

#### Command-line tool usage
```
usage: spectrographic [-h] [--version] -i PATH_TO_IMAGE [-d DURATION] [-m MIN_FREQ] [-M MAX_FREQ] [-r RESOLUTION] [-c CONTRAST] [-p] [-s SAVE_FILE]

Turn any image into sound.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -i PATH_TO_IMAGE, --image PATH_TO_IMAGE
                        Path of image that we want to embed in a spectrogram.
  -d DURATION, --duration DURATION
                        Duration of generated sound.
  -m MIN_FREQ, --min_freq MIN_FREQ
                        Smallest frequency used for drawing the image.
  -M MAX_FREQ, --max_freq MAX_FREQ
                        Largest frequency used for drawing the image.
  -r RESOLUTION, --resolution RESOLUTION
                        Vertical resolution of the image in the spectrogram.
  -c CONTRAST, --contrast CONTRAST
                        Contrast of the image in the spectrogram.
  -p, --play            Directly play the resulting sound.
  -s SAVE_FILE, --save SAVE_FILE
                        Path to .wav file in which to save the resulting sound.
```
Thus, if you have the source image at `./source.png` and you want to generate a 10s long sound in the frequency range of 10kHz to 20kHz. You also want to save the resulting .wav-file as `sound.wav` and also play the resulting sound. Then you need to run:

`spectrographic --image ./source.png --min_freq 10000 --max_freq 20000 --duration 10 --save sound.wav --play`

or if you are using the stand-alone script:

`python spectrographic.py --image ./source.png --min_freq 10000 --max_freq 20000 --duration 10 --save sound.wav --play`

#### Contribute

Bug reports, fixes and additional features are always welcome! Make sure to run the tests with `python setup.py test` and write your own for new features. Thanks.
