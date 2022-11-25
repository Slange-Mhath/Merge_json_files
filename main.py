import shutil
import os
from argparse import ArgumentParser


def merge_json_files(list_of_json, output_file):
    """
    Merge the json files together. Reads the files chunk by chunk which should
    be more efficient and will work even if some files in the list are
    too large to fit into memory
    :param list_of_json:
    :param output_file:
    :return:
    """
    with open(output_file,'wb') as wfd:
        for f in list_of_json:
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)


def get_json_files(main_dir, file_prefix):
    """
    Get all the files from the given directory with the specified file prefix
    :param main_dir:
    :return:
    """
    jp2_file_paths = []
    for file in os.scandir(main_dir):
        if file.name.startswith(file_prefix):
            jp2_file_paths.append(file)
    return jp2_file_paths


def main(main_dir, file_prefix, output_file):
    files_to_merge = get_json_files(main_dir, file_prefix)
    merge_json_files(files_to_merge, output_file)


if __name__ == "__main__":
    parser = ArgumentParser(description="...")
    parser.add_argument("-main_dir", metavar="main_dir",
                        help="Path to the the dir with the jp2 files")
    parser.add_argument("-file_prefix", metavar="file_prefix",
                        help="Prefix of the files we want to merge")
    parser.add_argument("-output_file", "--output_file",
                        dest="output_file",
                        help="Path to write the json file")
    args = parser.parse_args()
    main(args.main_dir, args.file_prefix, args.output_file)