# ObfE - One build from Eden
Bundle of python skripts that help setup and manage mods for **One step from Eden**

You can simply download `scripts.zip` if you want to use it

_Requires python to be installed on your system to work_
https://www.python.org/downloads/

## What does it do?
Have you been modding **One Step from Eden**? Do you have a Spells.xml with hundreds of lines?
It sure would be easier to have several smaller files like MySpell.xml to keep it straight in your head
and make managing your multiple cool spells easier.

Thats where these scripts come in:
### 1. Set up the location for your new mod with setupEden.py
This will create some default folders with `Destination.txt` in dem and bring all the 
scripts you need to manage your mod. Delete any of the folders you dont need and begin!
It will also ask for the location of your steam installation and what your mod should be called.

### 2. Put as many XML-files with any name you want into any directory with a Destination.txt
All XMLs in a folder with a `Destination.txt` get combined into the file specified in `Destination.txt`.
So if `Spells.xml` is in your `Destination.txt` then all .xml files in this folder will be put into `Spells.xml`.
If there are subfolders then any .xml files also get combined into `Spells.xml` if you dont include a new `Destination.xml` for them

This means that you cant put two .xml destinations into a `Destination.txt`. **All files with multiple destinations get ignored!**


**Note:** your XML should not contain the outer tags of the respective file. So your spell XMLs should not 
contain the `<Spells>` tag, just `<Spell>` tags and the stuff between that. The scripts put all your XMLs between these outer
tags in the combine step, so no need to do it yourself.

### 3. When you are ready to test your mod, execute buildEdenToLocal.py
This will ask you for your steam location and the name of your mod if you havent specified it yet and then put all
your mod files into your local mods folder for you. If you changed something, simply save your files and run the script 
again!

### 4. Install the mod ingame and test it out!
All your files are where Steam needs them, now you can test your mod and see how it plays!

### 5. When you want to update your mod on the Steam workshop just execute buildEdenToWorkshop.py
If you set up a `WorkshopItemInfo.xml` destination then **ObfE** will look for the `<PublishedFileId>` tag and put 
all your files into the workshop folder with the corresponding ID. No need to look for the folder yourself! Just make
sure that all the information Steam needs for their workshop mods are present. Afterwards just hit "Update Mod" in **One step from Eden** and you are done!

Like with all other .xml files you dont need
to include the outer `<WorkshopItemInfo>` tag in your files, **ObfE** will do that for you.

### That all sounds too complicated! I just want to move my mod to the workshop with the click of a button!
Well then you are in luck! If you dont care for all the `Destination.txt` organization simply put all your mod files like usual 
in the folder with the **ObfE** scripts and run the `copyEdenToLocal.py` for your local mod installation or `copyEdenToWorkshop.py`
to prepare the update for your mod. 

This will simply copy the whole folder structure over to steam,
 without all the **ObfE** files of course. 
 
 **Note:** When you use this approach everything but the automatic detection of your `<PublishedFileId>` dont apply to you, 
 so no cheaping out on the folder names in your animation XMLs or leaving out the outer tags of XML files! 

## A note on animations and other file types

### Other file types
All .png, .aseprite and .lua files in any folder get transported to your mod folder in the build step, 
no need to define a destination for them!

### Animations
If you have taken a look at the example mod for the character Lea you may have noticed that the .png and .aseprite
files for the movement animations is in a subfolder `char` and get referenced in `Lea_AnimInfo.xml` like this:

```
<Frame image="char/Lea_cast01Start1.png"></Frame>
<Frame image="char/Lea_cast01Start2.png"></Frame>
```
With **ObfE** you dont need to do that. Instead just reference the name of the correct file like this:
```
<Frame image="Lea_cast01Start1.png"></Frame>
<Frame image="Lea_cast01Start2.png"></Frame>
```
This works no matter where in your folder structure the .png files are, because they later all get put into a single folder together with 
all your .xml, .lua and .aseprite files and dont have any hierarchy to them


## How does it work?
The scripts look in the current directory for any subdirectories with Destination.txt.
Then it combines all files in directories with the same destination, and any subfolders 
that dont contain Destination.txt into a single file and finally sends
 it over to your **One step from Eden** Mods folder.

This lets you organize your mod in as many directories and files as you want, given that the 
directories reside in the your base directory with the ObfE scripts and that each directory with mod files in them 
to combine contains a Destination.txt

Destination names are fixed for XML files, so use them as Destination if you set up your own structure.

**Only put one destination in each `Destination.txt`, as otherwise the folder and all subfolders without a new `Destination.txt`
will be ignored.**

### Valid XML destinations
- Artifacts.xml
- Battles.xml
- Enemies.xml
- Heroes.xml
- HeroesExtra.xml
- Pacts.xml
- Spells.xml
- Structures.xml
- Tilefields.xml
- Zones.xml
- ZonesStorage.xml
- XXXAnimInfo.xml       <- you can put anything in place of the "XXX"
- WorkshopItemInfo.xml
## Contribution
Pull and feature requests are always welcome, i will credit you accordingly

## Planned
- ~~transfer files to Steam Workshop~~ **DONE!**
- ~~support other files(sprites and stuff)~~ **DONE!**
- ~~support default organization of files~~ **DONE!**
- Userinterface
  
