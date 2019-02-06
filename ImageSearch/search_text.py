from ImageSearch import get_image_text_tesseract


def is_text_present(path, text):
    image_text = get_image_text_tesseract(path)
    if text in image_text:
        return True
    return False
