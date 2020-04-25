import os

from edenSources import get_destination_file_name, get_top_tag


def build(output_folder=os.getcwd()):
    destination_dictionary = {}
    fill_with_content(destination_dictionary, os.getcwd(), [])
    for destination in destination_dictionary.keys():
        extension = destination.split(".")[1]
        content = "".join(destination_dictionary[destination])

        if content != "":
            if "xml" in extension:
                open_tag, close_tag = get_top_tag(destination)
                file_content = open_tag + content + "\n" + close_tag
            else:
                file_content = content
            if not os.path.exists(output_folder):
                os.mkdir(output_folder)
            with open(os.path.join(output_folder, destination), "w") as f:
                f.write(file_content)


def fill_with_content(dictionary, file_path, last_destinations):
    items = os.listdir(file_path)
    new_destinations = last_destinations
    if get_destination_file_name() in items:
        new_destinations = get_destination_names(os.path.join(file_path, get_destination_file_name()))

    folders = [d for d in items if os.path.isdir(os.path.join(file_path, d))]
    extensions = [ext.split(".")[1] for ext in new_destinations]
    for destination in new_destinations:
        extension = destination.split(".")[1]
        if extensions.count(extension) == 1:
            content = content_for_extension([f for f in items if f.endswith(extension)], file_path)
            put_in_dict(destination, dictionary, content)
        else:
            too_many_destination_error(extensions.count(extension), extension, file_path)

    for folder in folders:
        fill_with_content(dictionary, os.path.join(file_path, folder), new_destinations)


def content_for_extension(files, file_path):
    content = ""
    for file in files:
        with open(os.path.join(file_path, file), "r") as f:
            lines = f.readlines()
        data = "\n" + "".join(lines)
        content += data
    return content


def put_in_dict(key, dictionary, value):
    if key in dictionary.keys():
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]


def get_destination_names(file_path):
    with open(file_path, "r") as f:
        destinations = [l.replace("\n", "") for l in f.readlines() if l != "\n"]
    return destinations


def too_many_destination_error(amount, extension, folder):
    print("There were {0} destinations in {1}. {2}-Files will not be collected into any of them"
          .format(amount, folder,
                  extension))


if __name__ == "__main__":
    build()
