#!/usr/bin/python3.10
# may need to change this to your interpreter path
from sys import argv
from audio_metadata import load
from pathlib import Path
from os import path, urandom, system
from binascii import b2a_hex
from subprocess import check_output

if __name__=="__main__":
    default_bg = '' # replace with whatever your default wallpaper is
    filename = argv[4]
    try:
        meta = load(Path(filename))
        cover = meta["pictures"][0].data
        tmp_filename_bin = path.join(path.abspath("/tmp"), F"{b2a_hex(urandom(10)).decode('ascii')}.bin")
        with open(tmp_filename_bin, "wb") as f:
            f.write(cover)
        system(F"gsettings set org.cinnamon.desktop.background picture-uri \"file://{tmp_filename_bin}\"")
        with open("bg_logs.txt", "a") as log:
            log.write(F"gsettings set org.cinnamon.desktop.background picture-uri \"file://{tmp_filename_bin}\"")
    except Exception:
        system(F"gsettings set org.cinnamon.desktop.background picture-uri '{default_bg}'")
        with open("bg_logs.txt", "a") as log:
            log.write(F"gsettings set org.cinnamon.desktop.background picture-uri '{default_bg}'")