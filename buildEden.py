import os
from edenSources import destination_list, destination_tuples, get_destination_file_name


def build():
    destination_folder_dict = get_build_folders()


"""Returns a map of the destination XML and all folders containing files for that XML"""


def get_build_folders():
    destination_folder_dict = {}
    # init empty lists to fill later
    for destination in destination_list():
        destination_folder_dict[destination] = []
    for root, dir, files in os.walk(".", False):
        if get_destination_file_name() in files:
            file_path = os.path.join(root, get_destination_file_name())
            with open(file_path, "r") as f:
                destination = f.readline()
            destination_folder_dict[destination].append(os.path.basename(root))
    return destination_folder_dict


if __name__ == "__main__":
    get_build_folders()