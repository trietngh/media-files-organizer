from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from error_def import UnknownCaptureDateError

def get_date_captured_vid(file_path):
    parser = createParser(file_path)
    if not parser:
        raise FileNotFoundError

    with parser:
        try:
            metadata = extractMetadata(parser)
        except Exception as err:
            raise FileNotFoundError

    if not metadata:
        raise UnknownCaptureDateError

    for line in metadata.exportPlaintext():
        if line[2:15] == 'Creation date':
            return line[17:21] + line[22:24] + line[25:27]

    raise UnknownCaptureDateError

def get_metadata_hachoir(file_path):
    parser = createParser(file_path)
    if not parser:
        raise FileNotFoundError

    with parser:
        try:
            metadata = extractMetadata(parser)
        except Exception as err:
            print("Metadata extraction error: %s" % err)
            metadata = None
    if not metadata:
        print("Unable to extract metadata")
        exit(1)

    for line in metadata.exportPlaintext():
        print(line)