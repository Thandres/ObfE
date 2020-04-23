import os
def destination_list():
    return [
        "Artifacts.xml",
        "Battles.xml",
        "Enemies.xml",
        "Heroes.xml",
        "HeroesExtra.xml",
        "Pacts.xml",
        "Spells.xml",
        "Structures.xml",
        "Tilefields.xml",
        "Zones.xml",
        "ZonesStorage.xml",
        "Spells.xml"
    ]


def folder_list():
    return [
        "artifacts",
        "battles",
        "enemies",
        "heroes",
        "heroesXtra",
        "pacts",
        "spells",
        "structures",
        "tilefields",
        "zones",
        "zonesStorage",
        "weapons"
    ]


"""Returns a list of tuples with each tuple containing the folder name and 
the .xml file the folder contents should be added to"""


def destination_tuples():
    return zip(folder_list(), destination_list())


def get_destination_file_name():
    return "Destination.txt"

def get_properties_file_name():
    return "SteamInfos.txt"

def get_properties():
    return [
        "steam_folder",
        "mod_folder_name"
    ]

def get_local_mod_folder_path():
    return os.path.join("steamapps","common","One Step From Eden","OSFE_Data","StreamingAssets","Mods")

def get_top_tag(destination):
    top_tags = {
        "Artifacts.xml": "Artifacts",
        "Battles.xml": "document",
        "Enemies.xml": "Beings",
        "Heroes.xml": "Beings",
        "HeroesExtra.xml": "Beings",
        "Pacts.xml": "Pacts",
        "Spells.xml": "Spells",
        "Structures.xml": "Beings",
        "Tilefields.xml": "document",
        "Zones.xml": "document",
        "ZonesStorage.xml": "",
    }
    xml_info = r'<?xml version="1.0" encoding="UTF-8" ?>'
    if destination == "ZonesStorage.xml":
        return (xml_info, "")
    open_tag = xml_info + "\n" + "<" + top_tags[destination] + ">"
    close_tag = "</" + top_tags[destination] + ">"
    return (open_tag, close_tag)

def prop_split():
    return "|"