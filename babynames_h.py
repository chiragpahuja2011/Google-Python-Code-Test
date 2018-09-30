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

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # file operations
  html_file = open(filename, 'rU')
  file_data = html_file.read()
  html_file.close()

  #create empty list
  baby_list = []

  #regex patter to get year value
  find_year = re.search(r'Popularity \w\w \d\d\d\d', file_data)

  #append year in list
  baby_list.append(find_year.group().split()[2])

  #regex for extracting rank and names
  # (\w+) extracts the word between td tag.
  #this expression provides a list like the one mentioned below
  #['1', 'Michael', 'Jessica', '2', 'Christopher', 'Ashley']

  rank_name_list = re.findall(r'<td>(\w+)</td>', file_data)

  #
  i = 0
  name_dict={}
  while i < len(rank_name_list):
    #unpack 3 elements at the same time
    rank,name1,name2 = rank_name_list[i:i+3]
    if name1 not in name_dict:
      name_dict[name1] = rank

    if name2 not in name_dict:
      name_dict[name2] = rank

    i += 3
  for name in sorted(name_dict.keys()):
    baby_list.append(name + ' ' + name_dict[name])

  return baby_list


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

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for files in args:
    baby_list = extract_names(files)
    if summary:
      try:
        f = open((files + '.summary'),'w')
      except:
        print('file write error')
        sys.exit(1)

    for elem in baby_list:
      if summary:
        f.write(elem + '\n')
      else:
        print(elem)
    f.close()

if __name__ == '__main__':
  main()
