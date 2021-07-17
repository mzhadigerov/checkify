import os

from pathlib import Path
import cv2
import pytesseract as tess
from pdf2image import convert_from_path
from ocr.ocr_utils import get_text_from_image
import logging as log

tess.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"  #substitute with local tesseract.exe path


def scanPdf2text(path):
    """Retrieves and returns text from pdf"""
    file = Path(path)
    if not file.is_file():
        err = f'File {path} not exists'
        log.error(err)
        raise Exception(err)
    if not path.endswith('pdf'):
        err = 'Not a pdf file'
        log.error(err)
        raise Exception(err)
    else:
        pages = convert_from_path(path, 500)
        image_counter = 1
        file_names = []
        for page in pages:
            filename = "page_" + str(image_counter) + ".jpg"
            page.save(filename, "JPEG")
            file_names.append(filename)
            image_counter += 1
        filelimit = image_counter - 1
        text = ''
        for i in range(1, filelimit + 1):
            filename = "page_" + str(i) + ".jpg"
            text += get_text_from_image(filename)
        for filename in file_names:
            if os.path.exists(filename):
                os.remove(filename)
        return text
