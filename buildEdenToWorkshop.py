from buildEden import build_workshop
from edenSources import get_workshop_mod_path, prompt_props

if __name__ == '__main__':
    prompt_props()
    path_to_mod = get_workshop_mod_path()
    try:
        build_workshop(path_to_mod, True)
    except Exception as e:
        print(e)
    input("Finished, press enter to close")
