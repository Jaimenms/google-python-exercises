#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    output = ()
    with open(filename,'r') as f:
        for line in f:
            #line_re = re.search('GET (\/.*\.(jpg|png|tif)) ', line)
            line_re = re.search('GET (\/.*\.jpg) ', line)
            if line_re is not None:
                #output += ('http://' + filename + line_re.group(1),)
                output += ('http://code.google.com' + line_re.group(1),)

    output_sorted = sorted(set(output))

    return output_sorted




import urllib.request, urllib.parse, urllib.error
def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    if not (os.path.isdir(dest_dir)) :
        print('Folder "' + dest_dir + '" does not exists!!')
        sys.exit(1)

    index_str = ''
    for img_url in img_urls :
        img_filename = img_url.split('/')[-1]
        img_dest = dest_dir + '/' + img_filename
        try:
            f = urllib.request.urlopen(img_url)
            data = f.read();
            with open(img_dest,'wb') as code:
                code.write(data)
            f.close()
            print('Sucessful download of ' + img_url)
        except:
            print('Not possible to access ' + img_url)

        index_str += '<img src="%s">' % img_dest

    index_file = open( dest_dir + '/index.html' , 'w')
    index_file.write ("<html><body><h1>Logpuzzle</h1>%s</body></html>" % index_str )
    index_file.close()

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
