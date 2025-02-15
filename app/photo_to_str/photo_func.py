"""
1- files uploading to dir
2- ocr photo to string(dict?) -- done
3-dict browsing
4- sqlite
4- posgree and sending dicts by api

"""
from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'
img_path = '../../input_photos/t2.png'

def photo_to_String(img_path=img_path):
    return pytesseract.image_to_string(Image.open(img_path))

def words_string_to_dict(words_string):
    re_pattern = r'\b[A-Za-z-]+\b'
    is_key=True
    wordlist = words_string.split()
    words_dict = {}

    for word in wordlist:
        if re.match(re_pattern, word):
            if is_key:
                key = word
                is_key = False
            else:
                value = word
                is_key = True
                words_dict[key] = value

    return words_dict



