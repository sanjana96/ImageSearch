import os
from get_image_text import get_image_text
from search_text import search_in_image_text


def _is_text_present(path, text):
    image_text = get_image_text(path)
    return search_in_image_text(image_text, text)


def find(path, text):

    if os.path.isdir(path):
        input = os.listdir(path)
        dir_name = path
    else:
        input = os.path.basename(path)
        dir_name = os.path.dirname(path)

    for file_name in input:
        curr_path = os.path.join(dir_name, file_name)
        if _is_text_present(curr_path, text):
            yield file_name


__all__ = ['find']