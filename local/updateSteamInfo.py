import os
from edenSources import get_properties_file_name, get_properties, prop_split


def create_info_file(path_to_workspace=os.getcwd()):
    file_path = os.path.join(path_to_workspace, get_properties_file_name())
    if  not os.path.exists(file_path):
        path_to_steam = [get_properties()[0], input("""Please enter the path to you Steam installation folder(i.e. 'C:\Program Files\Steam').
        if you want to do this later just press enter and run updateSteamInfo.py whenyou are ready:\n""")]
        if path_to_steam[1] != "":
            mod_folder = ([get_properties()[1],
                          input("Please enter the name of the folder in your StreamingAssets/Mods folder:\n")])

            content = "\n".join([join_property(path_to_steam), join_property(mod_folder)])

            with open(file_path, "w") as f:
                f.write(content)

def join_property(prop_as_list):
    return prop_split().join(prop_as_list)

if __name__ == '__main__':
    create_info_file()
