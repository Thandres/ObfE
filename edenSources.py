import os

from updateSteamInfo import create_info_file


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
        "Spells.xml",
        "XXXAnimInfo.xml",
        "WorkshopItemInfo.xml"
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
        "weapons",
        "animations",
        "workshopInfo"
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


def props_missing():
    return not os.path.exists(property_path())


def prompt_props():
    if props_missing():
        create_info_file(get_properties(), get_properties_file_name())
        if props_missing():
            input("{} is still not found. Cant update your mod without that file.\n"
                  "Press enter to exit".format(get_properties_file_name()))
            exit()


def get_local_mod_folder_path():
    return os.path.join("steamapps", "common", "One Step From Eden", "OSFE_Data", "StreamingAssets", "Mods")


def get_workshop_mod_folder_path():
    return os.path.join("steamapps", "workshop", "content", "960690")


def get_backup_folder_name():
    return "backup"


def property_path():
    return os.path.join(os.getcwd(), get_properties_file_name())


def get_local_mod_path():
    lines = []
    with open(property_path(), "r") as f:
        lines = [l.replace("\n", "") for l in f.readlines()]

    path_to_steam = get_property(lines[0])
    mod_name = get_property(lines[1])
    return os.path.join(path_to_steam, get_local_mod_folder_path(), mod_name)


def get_workshop_mod_path():
    lines = []
    with open(property_path(), "r") as f:
        lines = [l.replace("\n", "") for l in f.readlines()]

    path_to_steam = get_property(lines[0])
    return os.path.join(path_to_steam, get_workshop_mod_folder_path())


def get_property(line):
    return line.split(prop_split())[1]


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
        "AnimInfo": "Animations",
        "WorkshopItemInfo.xml": "WorkshopItemInfo"
    }
    tag_info = {
        "WorkshopItemInfo.xml": r'xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
    }
    xml_info = r'<?xml version="1.0" encoding="UTF-8" ?>'
    if destination == "ZonesStorage.xml":
        return (xml_info, "")
    if "AnimInfo" in destination:
        destination = "AnimInfo"
    if destination in tag_info.keys():
        open_tag = xml_info + "\n" + "<" + top_tags[destination] + " " + tag_info[destination] + ">\n"
    else:
        open_tag = xml_info + "\n" + "<" + top_tags[destination] + ">\n"
    close_tag = "\n</" + top_tags[destination] + ">"
    return (open_tag, close_tag)


def prop_split():
    return "|"
