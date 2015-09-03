__author__ = 'Michael'
import os

def main():
    folder = 'C:/Users/Michael/Projects/Andrew_Project/data/Dropbox Sync/'
    outfile = 'C:/Users/Michael/Projects/Andrew_Project/data/file_list.txt'
    outf = open(outfile,'w')
    outf.write('file\tfolder\n')
    for r, d, f in os.walk(folder):
        for j in f:
            outf.write(j + '\t' + r + '\n')




    pass

if __name__=='__main__':
    main()