import json
import re
from os import listdir
from os.path import isfile, join

IMAGES_DIR = 'assets/images/items'


def generate_gallery(image_descriptions):
    print("gallery:")
    for file_name in sorted(listdir(IMAGES_DIR)):
        path = join(IMAGES_DIR, file_name)
        if not isfile(path) or file_name.startswith('.'):
            continue
        description = image_descriptions[re.sub('\..*', '', file_name)]
        print("  - image_path: {:s}".format(path))
        print("    url: {:s}".format(path))
        print("    alt: \"{:s}\"".format(description))
        print("    title: \"{:s}\"".format(description))


if __name__ == '__main__':
    with open('image_descriptions.json') as f:
        data = json.load(f)
        generate_gallery(data)
