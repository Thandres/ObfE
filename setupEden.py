"""Sets up the structure of the workspace"""
import os
from shutil import copyfile

from edenSources import destination_tuples, get_destination_file_name
from updateSteamInfo import create_info_file


def setup_folders(path_to_workspace):
    print("setting up folders...")
    for folder, destination in destination_tuples():
        path_to_folder = os.path.join(path_to_workspace, folder)
        try:
            os.mkdir(path_to_folder)
        except:
            print("{} already exists".format(path_to_folder))
        dest_file = os.path.join(path_to_folder,get_destination_file_name())
        with open(dest_file, "a") as f:
            f.write(destination+"\n")
    print("finished folders")

def setup_scripts(path_to_workspace):
    print("setting up scripts...")
    script_execution_path = os.path.dirname(os.path.abspath(__file__))

    dirs =os.listdir(script_execution_path)
    py_files = [f for f in dirs if f.endswith(".py")]
    for file in py_files:
        dst_filename = os.path.join(path_to_workspace, file)
        copyfile(file, dst_filename)
    print("finished scripts")

# first goal: XML, Lua second
def setup_workspace(path_to_workspace = os.getcwd()):
    print("setting up workspace...")
    setup_folders(path_to_workspace)
    if not path_to_workspace == os.getcwd():
        setup_scripts(path_to_workspace)
    print("finished workspace")


if __name__ == "__main__":
    path_to_workspace = os.path.join(os.getcwd(), "sample")
    # path_to_workspace = input("""Please enter the directory in which you want to set up.
    # If you want to set up in the current directory just press Enter:\n""")
    create_info_file(path_to_workspace)
    if path_to_workspace == "":
        setup_workspace()
    else:
        setup_workspace(path_to_workspace)
