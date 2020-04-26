import os



def create_info_file(properties, property_file_name, path_to_workspace=os.getcwd()):
    file_path = os.path.join(path_to_workspace, property_file_name)
    if not os.path.exists(file_path):
        path_to_steam = [properties[0], input("""Please enter the path to you Steam installation folder(i.e. 'C:\Program Files\Steam').
If you want to do this later just press enter and you will be asked when you want to transfer your mod to steam:\n""")]
        if path_to_steam[1] != "":
            mod_folder = [properties[1],
                          input(
                              "Please enter the name your mod should be called in your StreamingAssets/Mods folder.\n If you leave it empty the name will be this folder:")]
            content = "\n".join([join_property(path_to_steam), join_property(mod_folder)])

            with open(file_path, "w") as f:
                f.write(content)


def join_property(prop_as_list):
    return "|".join(prop_as_list)


def move_to_workshop():
    print("hi")
