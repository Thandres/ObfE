import os
from buildEden import build
from edenSources import get_properties_file_name, get_local_mod_folder_path, prop_split
from updateSteamInfo import create_info_file

property_path = os.path.join(os.getcwd(), get_properties_file_name())

def props_missing():
    return not os.path.exists(property_path)

def get_path_to_mod():
    lines = []
    with open(property_path,"r") as f:
        lines = [l.replace("\n","") for l in f.readlines()]

    path_to_steam = get_property(lines[0])
    mod_name = get_property(lines[1])
    return os.path.join(path_to_steam,get_local_mod_folder_path(),mod_name)

def get_property(line):
    return line.split(prop_split())[1]

if __name__ == '__main__':
    if props_missing():
        create_info_file()
        if props_missing():
            input("{} is still not found. Cant update your local mod without that file.\n"
                  "Press enter to exit".format(get_properties_file_name()))
            exit()
    path_to_mod = get_path_to_mod()
    build(path_to_mod)
