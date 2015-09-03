__author__ = 'Michael'
import re, glob, os

def renamer():

    file_list = '...path to andrews list from excel...'
    flistfile = open(file_list,'r')


    for pathname in glob.glob(files):
        basename= os.path.basename(pathname)
        new_filename= re.sub(pattern, replacement, basename)
        if new_filename != basename:
            os.rename(
              pathname,
              os.path.join(os.path.dirname(pathname), new_filename))
    



renamer("*.pdf", r"^(.*)\.pdf$", r"new(\1).pdf")
