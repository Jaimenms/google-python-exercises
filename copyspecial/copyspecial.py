#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise

"""

def get_special_paths(dir) :

    abs_dir = os.path.abspath(dir)

    files = ()
    for file in os.listdir(dir):
        if re.search('\_\_.*\_\_',file) is not None:
            files += (abs_dir + '/' + file,)
    return files

def copy_to(files,todir):
    for file in files:
        shutil.copy(file,todir)
    return

def zip_to(files,tozip):
    cmd_base = 'zip -j %s%s'
    str_files = ''
    for file in files :
        str_files += ' "' + file + '"'

    cmd = cmd_base % (tozip,str_files)

    print("Command I'm going to do is:\n%s" % cmd)

    subprocess.run(cmd, shell=True)

    return


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    files = get_special_paths(args[1])

    if not (todir + tozip):
        for file in files:
            print(file)

    if todir:
        copy_to(files,todir)

    if tozip:
        zip_to(files,tozip)


if __name__ == "__main__":
    main()
