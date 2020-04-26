from buildEden import build_default
from edenSources import prompt_props, get_workshop_mod_path

if __name__ == '__main__':
    prompt_props()
    try:
        build_default(get_workshop_mod_path(), True)
    except Exception as e:
        print(e)
    input("Finished, press enter to close")
