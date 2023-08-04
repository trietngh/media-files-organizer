import functions as func

def main() -> None:
    option_to_run = func.select_option()
    if option_to_run == 0:
        func.sort_files_in_dirs()
    elif option_to_run == 1:
        func.sort_file()
    elif option_to_run == 2:
        func.show_metadata()
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\n')
        print('Stopping the program.')
