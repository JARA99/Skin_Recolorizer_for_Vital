# Skin Recolorizer for Vital

This is a short python program, for adjusting colors from an existing .vitalskin file.

##  Documentation

### Install and run
Just `clone` the repository and run the [Main.py](src/Main.py) file via the virtual environment:

```bash
git clone https://github.com/JARA99/Skin_Recolorizer_for_Vital.git
cd ./Skin_Recolorizer_for_Vital
source ./PythonVEnv_SkinRecolorizer/bin/activate
python3 -u './src/Main.py'
```

### Usage

Once you run the code above, it will be requested a path for loading a skin file. If you leve it in blank it will use the [default.vitalskin](src/default.vitalskin).

Hit `<Enter>` and it will poup-up a widow with the colors of the skin and it's `HEX` codes. From there you can change a color by filling the color number (the one in parenthesis) on the first box and the `HEX` color of the new color on the second box.

Hit the `to:`  button and it will apply the changes. You should see that the color have changed, and now it has a vertical band that indicates the original color.

Once you finish your re colorization you can hit `save` and enter the save path on the terminal.

##  Screenshot

![](Graphics/Screenshot.png)

## To-Do:

- [ ] Improve the GUI
- [ ] Add a load and save path selectors
- [ ] Improve the documentation
- [ ] English revision of the documentation (spanish is my native language)
- [ ] Add a `reset color` button for resetting a color to the original
