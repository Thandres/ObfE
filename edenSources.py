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