import os
from get_image_text import get_image_text_tesseract
from search_text import is_text_present


def find(path, text):

    input = os.listdir(path) if os.path.isdir(path) else [os.path.basename(path)]

    dir_name = os.path.dirname(path)

    for file_name in input:
        curr_path = os.path.join(dir_name, file_name)
        if is_text_present(curr_path, text):
            yield curr_path


__all__ = ['find']