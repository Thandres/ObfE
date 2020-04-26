from buildEden import build_local
from edenSources import get_properties_file_name, get_local_mod_path, props_missing
from updateSteamInfo import create_info_file

if __name__ == '__main__':
    if props_missing():
        create_info_file()
        if props_missing():
            input("{} is still not found. Cant update your mod without that file.\n"
                  "Press enter to exit".format(get_properties_file_name()))
            exit()
    path_to_mod = get_local_mod_path()
    try:
        build_local(path_to_mod)
    except Exception as e:
        print(e)
    input("Finished, press enter to close")
