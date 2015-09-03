__author__ = 'Michael'

import data_retreiver as dtr
import skimage.io as skio
import skimage.transform as sktr
import numpy as np
from globals import *
from multiprocessing import Pool

def update_lw(img_id):
    '''
    takes in an image_id and updates its dimensions in the database

    :param img_id:
    :return:
    '''
    path = dtr.get_jpg_path_by_file_id(img_id)
    img = skio.imread(path,as_grey=True)
    hgt = img.shape[0]
    wdt = img.shape[1]
    ar = float(wdt)/float(hgt)

    str_sql = '''
    update tbl_image_files set height = %s, width=%s, aspect_ratio=%s where image_id = %s;
    '''
    dtr.cursor.execute(str_sql,(hgt,wdt,ar,img_id))
    dtr.conn.commit()

def get_all_image_ids_by_page(pagenum):
    str_sql = '''select image_id from tbl_image_files where page = %s;'''
    dtr.cursor.execute(str_sql,[pagenum])
    recs = dtr.cursor.fetchall()
    return recs

def make_feature_matrix(pagenum):
    mypool = Pool(6)
    files = get_all_image_ids_by_page(pagenum)
    n =  len(files)
    tgt = np.zeros((n,10000),dtype=np.float64)
    paths = []
    for i in range(n):
        # print i
        paths.append(dtr.get_jpg_path_by_file_id(files[i][0]))

    output = mypool.map(make_raveled_line,paths)
    textf = open(test_folder + '/path_reference.txt','w')
    for i in range(n):
        textf.write(str(i) + '\t' + output[i][0] + '\n')
        tgt[i]=output[i][1]
    textf.close()

    outpath = test_folder + '/fft_matrix.npy'
    np.save(outpath,tgt)

def make_raveled_line(p):
    print p
    img = skio.imread(p,as_grey=True)
    imgfft = np.fft.fft2(img).real
    return (p,imgfft.ravel())

if __name__=='__main__':
    make_feature_matrix(0)