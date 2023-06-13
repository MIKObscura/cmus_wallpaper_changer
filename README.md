# cmus_wallpaper_changer
Small python script that will change your desktop wallpaper based on what cmus is playing. This script was only tested on Python 3.10 but it should work on any version that the package `audio_metadata` supports.

Dependencies: `audio_metadata`

To use it, launch cmus, press your command key (`:` by default) and type this command:
> set status_display_program=/path/to/script/main.py

It only works with Cinnamon for now but I may change that in the future
