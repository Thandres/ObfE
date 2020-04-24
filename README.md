# One build from Eden
Bundle of python skripts that help setup and manage mods for **One step from Eden**

You can simply download scripts.zip if you want to use it

_Requires python to be installed on your system to work_

## What does it do?
Have you been modding **One Step from Eden**? Do you have a Spells.xml with hundreds of lines?
It sure would be easier to have several smaller files like MySpell.xml to keep it straight in your head
and make managing your multiple cool spells easier.

Thats where these scripts come in:
1. Set up the location for your new mod with setupEden.py
2. Put as many XML-files with any name you want into any directory with a Destination.txt
3. When you are ready to test your mod, execute moveToLocalEden.py
4. Install the mod ingame and test it out!

## How does it work?
The scripts look in the current directory for any subdirectories with Destination.txt.
Then it combines all files in directories with the same destination, and any subfolders 
that dont contain Destination.txt into a single file and finally sends
 it over to your **One step from Eden** Mods folder.

This lets you organize your mod in as many directories and files as you want, given that the 
directories reside in the your base directory with the ObfE scripts and that each directory with mod files in them 
to combine contains a Destination.txt

Destination names are fixed for XML files, so use them as Destination if you set up your own structure:

Otherwise setupEden.py will set up the names used in the StreamAssets/Data directory:

 - Artifacts.xml
- Artifacts.lua
 - Battles.xml
- Effects.lua
- Enemies.xml
- Heroes.xml
- HeroesExtra.xml
- Pacts.xml
- Spells.xml
- Spells.lua
- Structures.xml
- Tilefields.xml
- Zones.xml
- ZonesStorage.xml
## Contribution
Pull and feature requests are always welcome, i will credit you accordingly

## Planned
- transfer files to Steam Workshop
- support other files(sprites and stuff)
- Userinterface
  