import os
import re
import shutil

from edenSources import get_destination_file_name, get_top_tag


def build_local(output_folder):
    build(output_folder)


def build_workshop(output_folder):
    build(output_folder, True)


def build(output_folder=os.getcwd(), update_workshop=False):
    destination_dictionary = {}
    fill_with_content(destination_dictionary, os.getcwd(), [])
    if update_workshop:
        workshop_xml = "WorkshopItemInfo.xml"
        if not workshop_xml in destination_dictionary.keys():
            raise Exception(
                "There were no files for {}. Please make sure you have a Destination.txt set up and .xml files in the correct folder".format(
                    workshop_xml))
        workshop_info = destination_dictionary["WorkshopItemInfo.xml"]
        output_folder = workshop(workshop_info, output_folder)
        if not os.path.exists(output_folder):
            raise Exception(
                "You are not subscribed to the mod with the ID {}. Please subscribe to your mod via the Steam  and try again.".format(
                    os.path.basename(output_folder)))
    for destination in destination_dictionary.keys():
        if destination == "notXML":
            process_general_files(destination_dictionary[destination], output_folder)
            continue
        content = "\n".join(destination_dictionary[destination])

        if content != "":
            open_tag, close_tag = get_top_tag(destination)
            file_content = open_tag + content + close_tag
            if not os.path.exists(output_folder):
                os.mkdir(output_folder)
            with open(os.path.join(output_folder, destination), "w") as f:
                f.write(file_content)


def workshop(workshop_info, file_path):
    for item in workshop_info:
        id_pattern = r"<PublishedFileId>\d+</PublishedFileId>"
        match = re.search(id_pattern, item)
        if match:
            workhop_update_folder = re.search(r"\d+", match.group(0)).group(0)
            return os.path.join(file_path, workhop_update_folder)
    raise Exception("No ID found in WorkshopItemInfo.xml. Please make sure that you included a <PublishedFileId> tag")


def process_general_files(general_files, output_folder):
    for src in general_files:
        file_name = os.path.basename(src)
        dest = os.path.join(output_folder, file_name)
        shutil.copyfile(src, dest)


def fill_with_content(dictionary, file_path, last_destination):
    items = os.listdir(file_path)
    general_files = [os.path.join(file_path, f)
                     for f in items if f.endswith(".png") or f.endswith(".aseprite") or f.endswith(".lua")]

    put_in_dict("notXML", dictionary, general_files)
    new_destination = last_destination
    if get_destination_file_name() in items:
        new_destination = get_destination_names(os.path.join(file_path, get_destination_file_name()))

    folders = [os.path.join(file_path, d) for d in items if os.path.isdir(os.path.join(file_path, d))]
    if len(new_destination) == 1:
        destination = new_destination[0]
        content = content_for_extension([f for f in items if f.endswith(".xml")], file_path)
        put_in_dict(destination, dictionary, content)
    else:
        too_many_destination_error(len(new_destination), ".xml", file_path)

    for folder in folders:
        fill_with_content(dictionary, folder, new_destination)


def content_for_extension(files, file_path):
    content = []
    for file in files:
        with open(os.path.join(file_path, file), "r") as f:
            lines = f.readlines()
        content += [l.replace("\n", "") for l in lines]
    return content


def put_in_dict(key, dictionary, list):
    if key in dictionary.keys():
        dictionary[key] += list
    else:
        dictionary[key] = list


def get_destination_names(file_path):
    with open(file_path, "r") as f:
        destinations = [l.replace("\n", "") for l in f.readlines() if l != "\n"]
    return destinations


def too_many_destination_error(amount, extension, folder):
    print("There were {0} destinations in {1}. {2}-Files will not be collected into any destination"
          .format(amount, folder,
                  extension))


if __name__ == "__main__":
    build()
