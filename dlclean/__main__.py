"""Report on and clean up the downloads folder"""

import argparse
import os
import shutil
import sys
from termcolor import colored

def list_download_files():
    """List all of the download files for the user"""

    downloads_path = os.path.expanduser('~/Downloads')
    for item in os.listdir(downloads_path):
        if os.path.isdir(os.path.join(downloads_path, item)):
            print(colored(item, 'red', attrs=['bold']))
        else:
            print(colored(item, 'yellow'))

def delete_download_items():
    """Delete all files and dirs in Downloads"""

    download_path = os.path.expanduser('~/Downloads')
    for item in os.listdir(download_path):
        if os.path.isdir(os.path.join(download_path, item)):
            shutil.rmtree(os.path.join(download_path, item))
        else:
            os.remove(os.path.join(download_path, item))

def main():
    """The main processing when run as a script"""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-l', '--list',
        help='display all files and dirs in ~/Downloads',
        action='store_true')
    parser.add_argument(
        '-c', '--clean',
        help='delete all files and dirs in ~/Downloads',
        action='store_true')

    args = parser.parse_args()

    if args.list:
        list_download_files()
        sys.exit(0)
    elif args.clean:
        delete_download_items()
        sys.exit(0)
    else:
        parser.print_help()
        sys.exit(0)

if __name__ == 'main':
    main()
