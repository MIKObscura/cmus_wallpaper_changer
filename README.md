# cmus_wallpaper_changer
Small python script that will change your desktop wallpaper based on what cmus is playing. This script was only tested on Python 3.10 but it should work on any version that the package `audio_metadata` supports.

Dependencies: `audio_metadata`

To use it, first put your python interpreter path at the top of the file if the one there isn't correct, then make it executable with this command:
> chmod a+x main.py

Then change the `default_bg` variable to what your default background, note that it uses the URI format so it should look like this:
> file:///home/user/image.png

Then, launch cmus, press your command key (`:` by default) and type this command:
> set status_display_program=/path/to/script/main.py

Now it should be set and working for each time you launch cmus.

It only works with Cinnamon for now but I may change that in the future
