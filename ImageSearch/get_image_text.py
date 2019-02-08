try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract


def get_image_text(path):
    # TODO: Add segmentation and more processing here to overcome the limitations of pytesseract
    return _get_image_text_tesseract(path)


def _get_image_text_tesseract(path):
    return pytesseract.image_to_string(Image.open(path))