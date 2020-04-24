import os
from edenSources import destination_list, get_destination_file_name, get_top_tag


def build(output_folder=os.getcwd()):
    destination_folder_dict = get_build_folders()
    for destination in destination_folder_dict.keys():
        folders = destination_folder_dict[destination]
        content = ""
        extension = destination[-3:]
        for folder in folders:
            content += get_strings(os.path.join(os.getcwd(), folder),extension)
        if content != "":
            if  "xml"in extension:
                open_tag, close_tag = get_top_tag(destination)
                file_content = open_tag + content + "\n" + close_tag
            else:
                file_content = content
            with open(os.path.join(output_folder, destination), "w") as f:
                f.write(file_content)


def get_strings(file_path, extension):
    content = ""
    for root, _, files in os.walk(file_path):
        extension_files = [f for f in files if f.endswith(extension)]
        for file in extension_files:
            with open(os.path.join(root, file), "r") as f:
                lines = f.readlines()
            data = "\n" + "".join(lines)
            content += data
    return content


"""Returns a map of the destination XML and all folders containing files for that XML"""
def get_build_folders():
    destination_folder_dict = {}
    # init empty lists to fill later
    for destination in set(destination_list()):
        destination_folder_dict[destination] = []
    for root, dir, files in os.walk(".", False):
        if get_destination_file_name() in files:
            file_path = os.path.join(root, get_destination_file_name())
            with open(file_path, "r") as f:
                destinations = [l.replace("\n","") for l in f.readlines() if l != "\n"]
            for destination in destinations:
                destination_folder_dict[destination].append(os.path.basename(root))
            continue
    return destination_folder_dict


if __name__ == "__main__":
    build()
