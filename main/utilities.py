__author__ = 'Michael'

class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if not cls.instance:
            # Not created or has been Destroyed
            obj = super(Singleton, cls).__call__(*args, **kw)
            cls.instance = obj
        return cls.instance

def pdf_to_jpg(infile,outpath,pref=''):
    """
    Converts pdf files into a series of jpg files. Pdf must be formatted according to the specs in the ones Andrew has
    sent, which is to say each page must basically be an embedded jpg file.
    :param infile: input pdf (full path)
    :param outpath: output location
    :return: None
    """
    import os
    out_list=[]
    p,f = os.path.split(infile)
    f=f.replace('.pdf','')
    pdf = file(infile, "rb").read()
    if outpath[len(outpath)-1] not in ['\\','/']:
        outpath = outpath + '/'

    prefix = str(pref)

    startmark = "\xff\xd8"
    startfix = 0
    endmark = "\xff\xd9"
    endfix = 2
    i = 0

    njpg = 0
    while True:
        istream = pdf.find("stream", i)
        if istream < 0:
            break
        istart = pdf.find(startmark, istream, istream+20)
        if istart < 0:
            i = istream+20
            continue
        iend = pdf.find("endstream", istart)
        if iend < 0:
            raise Exception("Didn't find end of stream!")
        iend = pdf.find(endmark, iend-20)
        if iend < 0:
            raise Exception("Didn't find end of JPG!")

        istart += startfix
        iend += endfix
        print "JPG %d from %d to %d" % (njpg, istart, iend)
        jpg = pdf[istart:iend]
        jpgfile = file(os.path.join(outpath,prefix + "-%d.jpg" % njpg), "wb")
        jpgfile.write(jpg)
        jpgfile.close()
        out_list.append((prefix + "-%d.jpg" % njpg,njpg))

        njpg += 1
        i = iend
    return out_list

def select_query_to_tab_delimited(strsql, filepath, mycursor, myargs=None):
    if myargs==None:
        mycursor.execute(strsql)
    else:
        mycursor.execute(strsql,myargs)
    names=mycursor.column_names
    recs=mycursor.fetchall()

    recordset_to_tab_delimited(filepath, names, recs)

def recordset_to_tab_delimited(filepath, names, recs):
    # open the file
    outf = open(filepath, 'w')
    for i in range(len(names) - 1):
        outf.write(names[i] + '\t')
    outf.write(names[len(names) - 1] + '\n')
    for i in recs:
        for j in range(len(i) - 1):
            if i[j] == None:
                item = ''
            else:
                item = str(i[j])
            outf.write(item + '\t')
        item = str(i[len(i) - 1])
        outf.write(item + '\n')
    outf.close()

if __name__=='__main__':
    path = 'C:/Users/Michael/Projects/Andrew_Project/data/'
    mf = 'C:/Users/Michael/Projects/Andrew_Project/data/test_contrast_level.pdf'
    pdf_to_jpg(mf, path)
