# MEDIA FILES ORGANIZER
## DESCRIPTION
**Media-Files-Organizer** is a Python program to **organize a various media file types** by renaming files based on **capture date/creation date** found in file's metadata.

Image metadata is extracting by using [PIL](https://github.com/python-pillow/Pillow) (10.0.0) librairy.

Video metadata is extracting by using [Hachoir](https://hachoir.readthedocs.io/en/latest/) (3.2.0) librairy.

See INSTALL GUIDE for required dependencies to run this code.
All contributions to this project is welcome.

## CAUTION

1. For safety, please make sure to **_backup your important files_** before put it in the program. 
This program is tested by me, but I will not be responsible for any file lost or corrupted due to undiscovered bugs.

2. **_Uncorrected naming may occured_** because the capture/creation date in file's metadata may refer to the date it is been create in the current working directory.

## SUPPORTED FILE TYPES
### Image
- JPEG/JPG
- PNG
- HEIC
### Video
- MP4
- MOV

## INSTALL GUIDE
1. Install the latest version of **Python** [here](https://www.python.org/downloads/), 
normally, it has _pip_ included
2. Install **Pillow** librairy

    ```
    pip install Pillow
    ```
3. Install **Hachoir** librairy
    ```
    pip install hachoir
    ```

## USER GUIDE
From the command line, make sure you are in the directory containing the source code, 
if not, change the path of the source code accordingly :
```
python mediaorganizer.py [-d | -h | -f | -m]
```  

| Options       | Description                     |
|:-------------:|---------------------------------|
| None          | Equivalent to -d    
| -d            | Renaming all supported files in a directory and move them to a new directory 
| -f            | Renaming a specifique file and move it to a new directory
| -m            | Display the metadata of a specifique file 
| -h            | Display help        
