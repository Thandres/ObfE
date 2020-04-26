from buildEden import build_local
from edenSources import get_local_mod_path, prompt_props

if __name__ == '__main__':
    prompt_props()
    path_to_mod = get_local_mod_path()
    try:
        build_local(path_to_mod)
    except Exception as e:
        print(e)
    input("Finished, press enter to close")
