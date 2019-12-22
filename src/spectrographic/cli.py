# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         spectrographic = spectrographic.cli:run

Then run `python setup.py install` which will install the command `spectrographic`
inside your current environment.
"""

import argparse
import sys
from pathlib import Path

from spectrographic import __version__
from spectrographic.base import SpectroGraphic

__author__ = "Levi Borodenko"
__copyright__ = "Levi Borodenko"
__license__ = "mit"


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Turn any image into sound.", epilog="By Levi B."
    )
    parser.add_argument(
        "--version",
        action="version",
        version="spectrographic {ver}".format(ver=__version__),
    )
    parser.add_argument(
        "-i",
        "--image",
        dest="path_to_image",
        help="Path of image that we want to embed in a spectrogram.",
        type=Path,
        action="store",
        required=True,
    )
    parser.add_argument(
        "-d",
        "--duration",
        dest="duration",
        help="Duration of generated sound.",
        action="store",
        default=20,
        type=int,
    )
    parser.add_argument(
        "-m",
        "--min_freq",
        dest="min_freq",
        help="Smallest frequency used for drawing the image.",
        action="store",
        default=500,
        type=int,
    )
    parser.add_argument(
        "-M",
        "--max_freq",
        dest="max_freq",
        help="Largest frequency used for drawing the image.",
        action="store",
        default=7500,
        type=int,
    )
    parser.add_argument(
        "-r",
        "--resolution",
        dest="resolution",
        help="Vertical resolution of the image in the spectrogram.",
        action="store",
        default=150,
        type=int,
    )
    parser.add_argument(
        "-c",
        "--contrast",
        dest="contrast",
        help="Contrast of the image in the spectrogram.",
        action="store",
        default=3,
        type=int,
    )
    parser.add_argument(
        "-p",
        "--play",
        action="store_true",
        dest="play",
        help="Directly play the resulting sound.",
    )
    parser.add_argument(
        "-s",
        "--save",
        dest="save_file",
        help="Path to .wav file in which to save the resulting sound.",
        action="store",
        default="SoundGraphic.wav",
        type=str,
    )
    return parser.parse_args(args)


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)

    sg = SpectroGraphic(
        path=args.path_to_image,
        height=args.resolution,
        duration=args.duration,
        min_freq=args.min_freq,
        max_freq=args.max_freq,
        contrast=args.contrast,
    )

    if args.play:
        sg.play()

    sg.save(wav_file=args.save_file)


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
