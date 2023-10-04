#!/usr/bin/python3.10
from sys import argv
from audio_metadata import load
from pathlib import Path
from os import path, system, environ
from subprocess import check_output
import dbus

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
    tmp_filename_bin = path.join(path.abspath("/tmp"), "wallpaper.jpeg")
    with open(tmp_filename_bin, "wb") as f:
        f.write(cover)
    if environ['XDG_CURRENT_DESKTOP'] == 'KDE':
        script = """var Desktops = desktops();
        for (i=0;i<Desktops.length;i++) {
                d = Desktops[i];
                d.wallpaperPlugin = "org.kde.image";
                d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
                d.writeConfig("Image", "file://%s");
            }
        """
        bus = dbus.SessionBus()
        plasma_bus = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
        plasma_bus.evaluateScript(script % tmp_filename_bin)
        log.write(F"{filename} \n")
        log.write(script % tmp_filename_bin)
        log.write("\n")
    else:
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
        if filename.startswith('cue'):
            new_filename = get_file_from_cue(filename)
            try:
                set_bg(new_filename)
            except Exception:
                system(F"gsettings set org.cinnamon.desktop.background picture-uri '{default_bg}'")
        else:
            system(F"gsettings set org.cinnamon.desktop.background picture-uri '{default_bg}'")
        with open("bg_logs.txt", "a") as log:
            log.write(F"{filename} \n")
            log.write(F"gsettings set org.cinnamon.desktop.background picture-uri '{default_bg}' \n")
