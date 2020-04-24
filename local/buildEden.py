import os
from edenSources import destination_list, get_destination_file_name, get_top_tag


def build(output_folder=os.getcwd()):
    destination_folder_dict = get_build_folders()
    for destination in destination_folder_dict.keys():
        folders = destination_folder_dict[destination]
        content = ""
        extension = destination[-3:]
        for folder in folders:
            content += get_strings(os.path.join(os.getcwd(), folder), extension)
        if content != "":
            if "xml" in extension:
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
                destinations = [l.replace("\n", "") for l in f.readlines() if l != "\n"]
            xml = [l for l in destination if l.endswith(".xml")]
            lua = [l for l in destination if l.endswith(".lua")]
            root_folder = os.path.basename(root)
            put_in_dict(xml, destination_folder_dict, root_folder)
            put_in_dict(lua, destination_folder_dict, root_folder)
            continue
    return destination_folder_dict


def put_in_dict(list, dictionary, value):
    if len(list) > 1:
        print("There were multiple {0} destinations. {0}-Files will not be collected into any of them"
            .format(
            list[0][-4:]))
    else:
        dictionary[list[0]].append(value)


if __name__ == "__main__":
    build()
