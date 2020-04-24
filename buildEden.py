import os

from edenSources import get_destination_file_name, get_top_tag


def build(output_folder=os.getcwd()):
    destination_folder_dict = get_build_folders()
    for destination in destination_folder_dict.keys():
        folders = destination_folder_dict[destination]
        content = ""
        extension = destination[-3:]
        for folder in folders:
            content += get_strings(folder, extension)
        if content != "":
            if "xml" in extension:
                open_tag, close_tag = get_top_tag(destination)
                file_content = open_tag + content + "\n" + close_tag
            else:
                file_content = content
            with open(os.path.join(output_folder, destination), "w") as f:
                f.write(file_content)


def get_strings(file_path, extension, same_destination=True):
    content = ""

    items = os.listdir(file_path)
    if not same_destination:
        new_destination = get_destination_file_name() in items
        if new_destination:  # When there is a new Destination file dont look into subfolders
            return ""
    folders = [d for d in items if os.path.isdir(os.path.join(file_path, d))]
    extension_files = [f for f in items if f.endswith(extension)]

    for file in extension_files:
        with open(os.path.join(file_path, file), "r") as f:
            lines = f.readlines()
        data = "\n" + "".join(lines)
        content += data

    for folder in folders:
        content += get_strings(os.path.join(file_path, folder), extension, False)
    return content


"""Returns a map of the destination XML and all folders containing files for that XML"""


def get_build_folders():
    destination_folder_dict = {}

    for root, dir, files in os.walk(".", False):
        if get_destination_file_name() in files:
            file_path = os.path.join(root, get_destination_file_name())
            with open(file_path, "r") as f:
                destinations = [l.replace("\n", "") for l in f.readlines() if l != "\n"]
            if len(destinations) == 0:
                continue
            xml = [l for l in destinations if l.endswith(".xml")]
            lua = [l for l in destinations if l.endswith(".lua")]
            root_folder = os.path.abspath(root)
            if len(xml) > 0:
                put_in_dict(xml, destination_folder_dict, root_folder, ".xml")
            if len(xml) > 1:
                too_many_destination_error(xml, ".xml", root)
            if len(lua) > 0:
                put_in_dict(lua, destination_folder_dict, root_folder, ".lua")
            if len(lua) > 1:
                too_many_destination_error(lua, ".lua", root)
            continue
    return destination_folder_dict


def too_many_destination_error(amount, extension, folder):
    print("There were {0} destinations in {1}. {2}-Files will not be collected into any of them"
          .format(amount, folder,
                  extension))


def put_in_dict(list, dictionary, value, extension):
    if list[0] in dictionary.keys():
        dictionary[list[0]].append(value)
    else:
        dictionary[list[0]] = [value]


if __name__ == "__main__":
    build()
