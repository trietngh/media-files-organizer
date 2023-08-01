import os
import sorting as sort

def select_work_dirs():
    return input('Please chose a directory perform a sort: ')

def select_dest_dirs():
    dest_path = input('Please chose the directory to move in all sorted files: ')
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    return dest_path

if __name__ == "__main__":
    try:
        work_dirs = select_work_dirs()
        while not os.path.isdir(work_dirs):
            print('Please enter the path of a valide directory!')
            work_dirs = select_work_dirs()
        sorted_dirs = select_dest_dirs()
        
        print("Start sorting media files...")

        for item in os.listdir(work_dirs):
            item_path = os.path.join(work_dirs, item)
            if os.path.isfile(item_path): 
                sort.rename_and_move_to_sorted(sorted_dirs, item_path)

        print("Finished sorting media files.")
        print("%s files renamed"%sort.success_count)
        print("%s files failed to renamed"%sort.failed_count)
        
    except KeyboardInterrupt:
        print('\n')
        print('Stopping the program.')
