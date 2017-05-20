#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

import re

def get_year(text):
    year_re = re.search('Popularity in (\d{4})', text)
    if year_re is not None:
        year = year_re.group(1);
    else :
        year = None
    return year

def get_data(line):
    line_re = re.search('<td>(\d*)</td><td>(.*)</td><td>(.*)</td>', line)
    if line_re is not None:
        output = (line_re.group(2) + ' ' + line_re.group(1),
                  line_re.group(3) + ' ' + line_re.group(1));
    else :
        output = None
    return output



def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """

    year = None
    output = ()
    with open(filename,'r') as f:
        for line in f:
            if year is None:
                year = get_year(line)
                continue

            if year is not None :
                data = get_data(line)
                if data is not None :
                    output += data

    output_w_year = [year,] + sorted(output)

    return output_w_year


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    if summary :
        file = open('babynames.out', 'w')

    for filename in args:
        # For each filename, get the names, then either print the text output
        # or write it to a summary file
        output = extract_names(filename)
        if summary :
            file.write('%s\n' % output)
        else :
            print(output)



if __name__ == '__main__':
    main()
