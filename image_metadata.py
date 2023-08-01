from PIL import Image
from PIL.ExifTags import TAGS
from pillow_heif import register_heif_opener
from error_def import UnknownCaptureDateError


register_heif_opener()

EXIFTAG_DateTimeOriginal = 306

def get_exif_info(file_path) -> None:
    img = Image.open(file_path)
    full_date = img.getexif()
    print(full_date)
    img.close()

def get_exif_info_png(file_path) -> None:
    img = Image.open(file_path)
    img.load()
    print(img.info)
    img.close()

def get_date_captured_jpg(file_path) -> str:
    try:
        img = Image.open(file_path)
        full_date = img.getexif()[EXIFTAG_DateTimeOriginal]
        img.close()
        return full_date[0:4] + full_date[5:7] + full_date[8:10]
    except KeyError:
        raise UnknownCaptureDateError
 
def get_date_captured_heic(file_path) -> str:
    try:
        img = Image.open(file_path)
        full_date = img.getexif()[EXIFTAG_DateTimeOriginal]
        img.close()
        return full_date[0:4] + full_date[5:7] + full_date[8:10]
    except KeyError:
            raise UnknownCaptureDateError

def get_date_captured_png(file_path) -> str:
    img = Image.open(file_path)
    img.load()
    if 'DateCreated' in img.info['XML:com.adobe.xmp']:
        full_date = img.info['XML:com.adobe.xmp'][320:330]
    else:
        raise UnknownCaptureDateError
    img.close()
    return full_date[0:4] + full_date[5:7] + full_date[8:10]