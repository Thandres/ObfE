import os
from edenSources import destination_list, get_destination_file_name, get_top_tag


def build(output_folder=os.getcwd()):
    destination_folder_dict = get_build_folders()
    for destination in destination_folder_dict.keys():
        folders = destination_folder_dict[destination]
        content = ""
        for folder in folders:
            content += get_strings(os.path.join(os.getcwd(), folder))
        if content != "":
            open_tag, close_tag = get_top_tag(destination)
            file_content = open_tag + content + "\n" + close_tag
            with open(os.path.join(output_folder, destination), "w") as f:
                f.write(file_content)


def get_strings(file_path):
    content = ""
    for root, _, files in os.walk(file_path):
        xml_files = [xml for xml in files if xml.endswith(".xml")]
        for file in xml_files:
            with open(os.path.join(root, file), "r") as f:
                xml_lines = f.readlines()
            xml = "\n" + "".join(xml_lines)
            content += xml
    return content


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
            continue
    return destination_folder_dict


if __name__ == "__main__":
    build()
