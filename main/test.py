__author__ = 'Michael'
# from data import *
import skimage.io as ski
import skimage.transform as skt
import numpy as np
import image_mgr
from globals import *

def main():

    # f = Form('census',4)
    # folist = ['batey 6 census','batey 7 census','batey 8 census','batey 9 census','Los Robles census','pescaradia census']
    # for j in folist:
    #     mypath = 'C:/Users/Michael/Projects/Andrew_Project/data/final_renamed_files/Census/' + j
    #     f = Folder(mypath,'census')
    #     f.search_harddrive_for_files()
    #     for a in f.pdf_files:
    #         print a.filename
    #         a.parse_to_jpgs()
    pass

def main2():
    # tmpfo='C:/Users/Michael/Projects/Andrew_Project/jpg_archive/census/'
    # tmpfi = '81-0.jpg'
    # img = ski.imread(tmpfo + tmpfi,as_grey=True)
    # print img.shape
    pagezero = image_mgr.get_all_image_ids_by_page(0)
    for i in pagezero:
        print i
        image_mgr.update_lw(i[0])

def main3():

    tmpfo='C:/Users/Michael/Projects/Andrew_Project/jpg_archive/census/'
    tmpfi = '81-0.jpg'
    img = ski.imread(tmpfo + '/' + tmpfi,as_grey=True)
    ski.imsave(test_folder + '/81-0-resize.jpg',skt.resize(img,(100,100)))
    # print img.shape

if __name__=='__main__':
    main3()