#!/usr/bin/python3.10
from sys import argv
from audio_metadata import load
from pathlib import Path
from os import path, urandom, system
from binascii import b2a_hex
from subprocess import check_output

def get_file_from_cue(filename):
    slashes = [index for index, value in enumerate(filename) if value == '/']
    parent_dir = filename[6:slashes[len(slashes) - 2]]
    sheet_name =  filename[6:filename.rindex('/')]
    with open(sheet_name, "r") as sheet:
        for line in sheet:
            if line.strip().startswith("FILE"):
                end = line.index("WAVE")
                return parent_dir + '/' + line[6:end-2]

def set_bg(filename):
    meta = load(Path(filename))
    cover = meta["pictures"][0].data
    tmp_filename_bin = path.join(path.abspath("/tmp"), F"{b2a_hex(urandom(10)).decode('ascii')}.bin")
    with open(tmp_filename_bin, "wb") as f:
        f.write(cover)
    system(F"gsettings set org.cinnamon.desktop.background picture-uri \"file://{tmp_filename_bin}\"")
    with open("bg_logs.txt", "a") as log:
        log.write(F"{filename} \n")
        log.write(F"gsettings set org.cinnamon.desktop.background picture-uri \"file://{tmp_filename_bin}\" \n")

if __name__=="__main__":
    default_bg = ''
    filename = argv[4]
    try:
        set_bg(filename)
    except Exception:
        system(F"gsettings set org.cinnamon.desktop.background picture-uri '{default_bg}'")
        with open("bg_logs.txt", "a") as log:
            log.write(F"{filename} \n")
            log.write(F"gsettings set org.cinnamon.desktop.background picture-uri '{default_bg}' \n")
            log.write(F"{filename} \n")
            log.write(F"gsettings set org.cinnamon.desktop.background picture-uri '{default_bg}' \n")