__author__ = 'Michael'

import data_retreiver as dtr
import skimage.io as skio
import skimage.transform as sktr
import sklearn.decomposition as skdecomp
import sklearn.mixture as skmixture
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
    mypool = Pool(8)
    files = get_all_image_ids_by_page(pagenum)
    n =  len(files)
    # tgt = np.zeros((n*4,10000),dtype=np.float64)
    tgt = np.zeros((n*4,20000),dtype=np.float64)
    paths = []
    for i in range(n):
        # print i
        paths.append(dtr.get_jpg_path_by_file_id(files[i][0]))

    output = mypool.map(make_raveled_line,paths)
    # textf = open(test_folder + '/path_reference.txt','w')
    textf = open(test_folder + '/path_reference_plain.txt','w')
    for i in range(n):
        textf.write(str(i) + '\t' + output[i][0] + '\n')
        tgt[i*4:(i*4+4)]=output[i][1]
    textf.close()

    # outpath = test_folder + '/fft_matrix.npy'
    outpath = test_folder + '/plain_matrix.npy'
    np.save(outpath,tgt)

def make_raveled_line(p):
    fo,fi = os.path.split(p)
    print p
    img = skio.imread(p,as_grey=True)
    img100=sktr.resize(img,(100,100))
    skio
    img100_2=sktr.rotate(img100,90)
    img100_3=sktr.rotate(img100,180)
    img100_4=sktr.rotate(img100,270)
    # imgfft = np.array([np.fft.fft2(img100).real.ravel(),np.fft.fft2(sktr.rotate(img100,90)).real.ravel(),
    #                   np.fft.fft2(sktr.rotate(img100,180)).real.ravel(),np.fft.fft2(sktr.rotate(img100,270)).real.ravel()])
    imgvect = np.array([np.hstack((img100[0:50].ravel(),img100[50:100].ravel(),img100[:,0:50].ravel(),img100[:,50:100].ravel())),
                       np.hstack((img100_2[0:50].ravel(),img100_2[50:100].ravel(),img100_2[:,0:50].ravel(),img100_2[:,50:100].ravel())),
                       np.hstack((img100_3[0:50].ravel(),img100_3[50:100].ravel(),img100_3[:,0:50].ravel(),img100_3[:,50:100].ravel())),
                       np.hstack((img100_4[0:50].ravel(),img100_4[50:100].ravel(),img100_4[:,0:50].ravel(),img100_4[:,50:100].ravel()))])

    del img
    # np.save(test_folder + '/numpy_raveled/' + fi[:-4] + '.npy',imgfft)
    np.save(test_folder + '/numpy_raveled_plain/' + fi[:-4] + '.npy',imgvect)
    return (p,imgvect)

def do_pca_and_cluster():
    # fftmatrixfile = test_folder + '/fft_matrix.npy'
    print "loading data..."
    fft_pca_file = test_folder + '/pca_25_components.npy'
    myfft = np.load(fft_pca_file)
    datamatrixfile = test_folder + '/plain_matrix.npy'
    mydata = np.load(datamatrixfile)

    mydata_top = mydata[:,0:5000]
    mydata_bot = mydata[:,5000:10000]
    mydata_lef = mydata[:,10000:15000]
    mydata_rgt = mydata[:,15000:20000]

    print "running PCA:"
    mypca = skdecomp.PCA(n_components=4)
    data_top_4 = mypca.fit_transform(mydata_top)
    print "...top halves done"
    data_bot_4 = mypca.fit_transform(mydata_bot)
    print "...bottom halves done"
    data_lef_4 = mypca.fit_transform(mydata_lef)
    print "...left halves done"
    data_rgt_4 = mypca.fit_transform(mydata_rgt)
    print "...right halves done"

    full_data = np.hstack((myfft,data_top_4,data_bot_4,data_lef_4,data_rgt_4)) # (25 cols fft), (4 cols top), (4 cols bot), (4 cols left), (4 cols right)
    np.save(test_folder + '/full_data.npy',full_data)
    print "saved full data"

    mygmm = skmixture.GMM(n_components=4)
    mygmm.fit(full_data)
    print '\n\nDid the GMM fitting converge:'
    print mygmm.converged_
    mygmm_probs = mygmm.predict_proba(full_data)
    np.savetxt(test_folder + '/mygmm_probs_fulldata.txt',mygmm_probs,delimiter='\t')
    np.save(test_folder + '/mygmm_probs_fulldata.npy',mygmm_probs)

def attempt_2():
    full_data = np.load(test_folder + '/full_data.npy')
    half_data = full_data[:,25:]
    half_data4 = half_data[:,[0,4,8,12]]
    print half_data4.shape
    mygmm = skmixture.GMM(n_components=4)
    mygmm.fit(half_data4)
    print mygmm.converged_
    print mygmm.means_
    print mygmm.weights_
    mygmm_probs = mygmm.predict_proba(half_data4)
    np.savetxt(test_folder + '/mygmm_probs_halfdata4.txt',fmt='%10.5f',X=mygmm_probs,delimiter='\t')
    np.savetxt(test_folder + '/mygmm_means_halfdata4.txt',fmt='%10.5f',X=mygmm.means_,delimiter='\t')
    np.savetxt(test_folder + '/half_data_4cols.txt',fmt='%10.5f',X=half_data4,delimiter='\t')
    return mygmm, half_data4

if __name__=='__main__':
    # make_feature_matrix(0)
    # do_pca_and_cluster()
    attempt_2()
    pass