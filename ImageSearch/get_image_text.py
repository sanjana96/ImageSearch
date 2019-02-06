try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract


def get_image_text_tesseract(path):
    return pytesseract.image_to_string(Image.open(path))