# SpectroGraphic
_Turn any image into a sound whose spectrogram looks like the image_

![result](https://i.imgur.com/UoMYkVS.png)
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## What is this?

Most sounds are intricate combinations of many accustic waves each having different frequencies and intensities. A spectrogram is a way to represent sound by plotting time on the horizontal axis and the frequency spectrum on the vertical axis. Sort of like sheet music on steriods.

What this tool does is, taking an image and simply interpreting it as a spectrogram. Therefore, by generating the corresponding sound, we have embedded our image in a spectrogram.

The game DOOM used a similar technique to [hide satanic figures inside its soundtrack](https://www.theverge.com/2016/5/31/11825606/doom-2016-soundtrack-satan-666-inverted-pentagram). Now everyone can do the same! :)

## Set-up

Get the command-line tool `spectrographic` via `pip` by running `pip install spectrographic`. You can also simply use `spectrographic.py` from `stand-alone\` as a command-line tool directly.
Furthermore, make sure you meet all the dependencies inside the `requirements.txt`. `Numpy simpleaudio wavio` are crucial.

After installation with `pip` one simply needs to run `spectrographic [...]` in the console and with the stand-alone script you have to use `python spectrographic.py [...]` inside the folder containing `spectrographic.py`.

You could also simply import the `SpectroGraphic` class from `spectrographic`

## Command-line tool usage
```
usage: primify.py [-h] [--image IMAGE_PATH] [--max_digits MAX_DIGITS]
                  [--method {0,1,2}] [--output_dir OUTPUT_DIR]
                  [--output_file OUTPUT_FILE] [-v]

Command-line tool for converting images to primes

optional arguments:
  -h, --help            show this help message and exit
  --image IMAGE_PATH    Source image to be converted.
  --max_digits MAX_DIGITS
                        Maximal number of digits the prime can have.
  --method {0,1,2}      Method for converting image. Tweak 'till happy
  --output_dir OUTPUT_DIR
                        Directory of the output text file
  --output_file OUTPUT_FILE
                        File name of the text file containing the prime.
  -v                    Verbose output (Recommended!)
```
Thus, if you have the source image at `./source.png` and you want to generate a 10s long sound in the frequency range of 10kHz to 20kHz. You also want to save the resulting .wav-file as `sound.wav` and also play the resulting sound. Then you need to run:

`spectrographic --image ./source.png --min_freq 10000 --max_freq 20000 --duration 10 --save sound.wav --play`

or if you are using the stand-alone script:

`python spectrographic.py --image ./source.png --min_freq 10000 --max_freq 20000 --duration 10 --save sound.wav --play`

### Importing the PrimeImage class

you can also simply import the `PrimeImage` class from `primify.py` and use that class in your own code. Take a look at the source code to see what methods and attributes there are.
