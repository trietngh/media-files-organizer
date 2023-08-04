import os, getopt, sys
import sorting as sort
from image_metadata import get_exif_info, get_exif_info_png
from video_metadata import get_metadata_hachoir

def usage() -> None:
    print('''
    -----------------------------------------------------------------------------------------
    Usage : mediaorganizer.py [-d | -h | -f | -m]
          
    Options :
        None    Equivalent to -d  
        -d      Renaming all supported files in a directory and move them to a new directory
        -f      Renaming a specifique file and move it to a new directory
        -m      Display the metadata of a specifique file
        -h      Display help
    -----------------------------------------------------------------------------------------
''')

def select_option() -> int:
    option_chosed = -1
    multi_opt_flag = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hfdm")

        if len(args) != 0:
            raise getopt.GetoptError('There is no need for arguments after the option.')
        
        # Defaut option is -d
        if len(opts) == 0:
            option_chosed = 0
        else:
            for opt, arg in opts:
                if opt == '-h':
                    usage()
                    sys.exit()
                elif opt == '-d':
                    option_chosed = 0
                    multi_opt_flag += 1
                elif opt == '-f':
                    option_chosed = 1
                    multi_opt_flag += 1
                elif opt == '-m':
                    option_chosed = 2
                    multi_opt_flag += 1
            
            if multi_opt_flag != 1:
                raise getopt.GetoptError('Multiple option provided, only one is allowed.')
        
        return option_chosed
    
    except getopt.GetoptError:
        print('------------------------------------------------------------------------')
        print ('Uncorrect option provided, please type de following command for help:')
        print ('====> mediaorganizer.py -h')
        print('------------------------------------------------------------------------')
        sys.exit(2)

def select_work_object() -> str:
    return input('Please chose a directory/file to work with: ')

def select_dest_dirs() -> str:
    dest_path = input('Please chose the directory to move in all sorted files: ')
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    return dest_path

def sort_files_in_dirs() -> None:
    work_dirs = select_work_object()
    while not os.path.isdir(work_dirs):
        print('Please enter the path of a valide directory!')
        print('To rename a single file, use the option -f')
        work_dirs = select_work_object()
    print("Selected directory: %s"%work_dirs)

    sorted_dirs = select_dest_dirs()
    print("Files will be move to: %s"%sorted_dirs)
    
    print("Start sorting media files...")

    for item in os.listdir(work_dirs):
        item_path = os.path.join(work_dirs, item)
        if os.path.isfile(item_path): 
            sort.rename_and_move_to_sorted(sorted_dirs, item_path)

    print("Finished sorting media files.")
    print("%s files renamed"%sort.success_count)
    print("%s files failed to renamed"%sort.failed_count) 

def sort_file() -> None:
    work_file = select_work_object()
    while not os.path.isfile(work_file):
        print('Please enter the path of a valide file!')
        print('To rename a whole directory, use the option -d')
        work_file = select_work_object()
    print("Selected directory: %s"%work_file)

    sorted_dirs = select_dest_dirs()
    print("File will be move to: %s"%sorted_dirs)
    
    print("Start renaming media files...")
    sort.rename_and_move_to_sorted(sorted_dirs, work_file)
    print("Finished sorting media files.")
    print("%s files renamed"%sort.success_count)
    print("%s files failed to renamed"%sort.failed_count)

def show_metadata() -> None:
    work_file = select_work_object()
    while not os.path.isfile(work_file):
        print('Please enter the path of a valide file!')
        print('To rename a whole directory, use the option -d')
        work_file = select_work_object()
    print("Selected directory: %s"%work_file)

    print("Metadata :")
    print("------------------------------------------------")
    try:
        file_type = sort.find_file_type(work_file)
        if file_type == '.png':
            get_exif_info_png(work_file)
        elif file_type == '.jpg' or file_type == '.jpeg':
            get_exif_info(work_file)
        elif file_type == '.heic':
            get_exif_info(work_file)
        elif file_type in ['.mp4', '.mov']:
            get_metadata_hachoir(work_file)
        else:
            raise TypeError
    except TypeError:
        print("Unsupported file type (%s)"%file_type)
    print("------------------------------------------------")