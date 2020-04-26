from buildEden import build_default
from edenSources import prompt_props, get_local_mod_path

if __name__ == '__main__':
    prompt_props()
    try:
        build_default(get_local_mod_path())
    except Exception as e:
        print(e)
    input("Finished, press enter to close")
