import os
import image_metadata as img
import video_metadata as vid
from error_def import UnknownCaptureDateError

success_count = 0
failed_count = 0

def check_dublicate_file_name(dirs, file_name) -> bool:
    file_path = os.path.join(dirs, file_name)
    check_result = False
    if os.path.exists(file_path):
        check_result = True
    return check_result

def find_file_type(path) -> str:
    return os.path.splitext(path)[1].lower()

def build_file_name(dest_dirs, file_path) -> str:
    file_type = find_file_type(file_path)
    if file_type == '.png':
        date_capt = img.get_date_captured_png(file_path)
    elif file_type == '.jpg' or file_type == '.jpeg':
        date_capt = img.get_date_captured_jpg(file_path)
    elif file_type == '.heic':
        date_capt = img.get_date_captured_heic(file_path)
    elif file_type in ['.mp4', '.mov']:
        date_capt = vid.get_date_captured_vid(file_path)
    else:
        raise TypeError

    serial = 1

    file_name = date_capt + "_" + str(serial).zfill(4) + file_type
    while check_dublicate_file_name(dest_dirs, file_name):
        serial += 1
        file_name = date_capt + "_" + str(serial).zfill(4) + file_type

    return file_name


def rename_and_move_to_sorted(dest_dirs, file_path) -> None:
    global success_count, failed_count

    try:
        file_name = build_file_name(dest_dirs, file_path)
        #print("====> " + file_name)
        new_file_path = os.path.join(dest_dirs, file_name)
        os.rename(file_path, new_file_path)
        success_count += 1
    except UnknownCaptureDateError:
        #print("No information about date of capture.") 
        failed_count += 1
        pass
    except TypeError:
        #print("Unsupported file type.")
        failed_count += 1
        pass
    except FileNotFoundError:
        #print('Error opening this file %s'% file_path)
        failed_count += 1
        pass