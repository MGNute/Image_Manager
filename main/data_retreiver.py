__author__ = 'Michael'
import ConfigParser, os
import mysql.connector
from globals import *



global conn
global cursor


cfg=ConfigParser.ConfigParser()
cfg.read(db_config_file)
dbargs={}
dbargs['user']=cfg.get('db_config', 'user')
dbargs['database']=cfg.get('db_config', 'database')
dbargs['password']=cfg.get('db_config', 'password')
# try:
conn=mysql.connector.connect(**dbargs)
cursor=conn.cursor()
    

def get_form_id_by_name(name):
    strsql='''
    select id from tbl_form_defs where form_name = %s;
    '''
    cursor.execute(strsql,[name])
    rec = cursor.fetchall()
    return rec[0][0]

def add_location_to_form_def(form,loc):
    strsql1='''select count(*) from tbl_form_folders where folder = %s;'''
    cursor.execute(strsql1,[loc])
    rec=cursor.fetchall()
    if rec[0][0]==0:
        strsql='''
        insert into tbl_form_folders (form_id, folder) values (%s, %s);
        '''
        if isinstance(form,str) or isinstance(form,unicode):
            fid = get_form_id_by_name(form)
        else:
            fid = form
        cursor.execute(strsql,(fid,loc))
        conn.commit()
        return True
    else:
        return False

def get_locations_by_form_def(form_def):
    fid = get_form_id_by_name(form_def)
    strsql = '''select folder_id, folder from tbl_form_folders where form_id = %s;'''
    cursor.execute(strsql,[fid])
    recs = cursor.fetchall()
    locs = [i[1] for i in recs]
    return locs

def get_folder_info_by_path(path):
    strsql='''select form_id, folder_id from tbl_form_folders where folder = %s;
    '''
    cursor.execute(strsql,[path])
    recs = cursor.fetchall()
    if len(recs)>0:
        return recs[0]
    else:
        return None

def get_folder_info_by_id(folder_id):
    strsql='''select form_id, folder from tbl_form_folders where folder_id = %s;
    '''
    cursor.execute(strsql,[folder_id])
    recs = cursor.fetchall()
    if len(recs)>0:
        return recs[0]
    else:
        return None

def get_pdf_info_by_path(path):
    fo, fi = os.path.split(path)
    folder_info=get_folder_info_by_path(fo)
    strsql='''select * from tbl_form_pdf_files where folder_id=%s and file_name=%s;'''
    cursor.execute(strsql,(folder_info[1],fi))
    file_info=cursor.fetchall()
    if len(file_info)>0:
        return file_info[0]
    else:
        return None

def add_pdf(file_name,folder_id,form_id):
    strsql='insert into tbl_form_pdf_files (folder_id,file_name,form_type) values (%s,%s,%s);'
    cursor.execute(strsql,(folder_id,file_name,form_id))
    conn.commit()
    str_sql_get = 'select pdf_id from tbl_form_pdf_files where folder_id = %s and file_name = %s;'
    cursor.execute(str_sql_get,(folder_id,file_name))
    r=cursor.fetchall()
    return r[0][0]

def add_jpg(pdf_id,folder,page,file_name):
    str_sql='insert into tbl_image_files (pdf_file_id,folder,page,file_name) values (%s,%s,%s,%s);'
    cursor.execute(str_sql,(pdf_id,folder,page,file_name))
    conn.commit()

def get_registered_pdfs_by_folder(folder_id):
    str_sql='select * from tbl_form_pdf_files where folder_id=%s;'
    cursor.execute(str_sql,[folder_id])
    files=cursor.fetchall()
    return files

def get_jpg_filepaths_by_pdf(pdf_id=None,pdf_path=None):
    '''
    returns the child jpg file list as a list ordered by page number
    :param pdf_id:
    :param pdf_path:
    :return:
    '''
    if pdf_id ==None:
        pdf_id = get_pdf_info_by_path(pdf_path)

    strsql = '''
    select * from tbl_image_files where pdf_file_id=%s order by page asc;
    '''
    cursor.execute(strsql,[pdf_id])
    return cursor.fetchall()

def get_jpg_target_by_folder(folder_id):
    if isinstance(folder_id,str) or isinstance(folder_id,unicode):
        fid=get_folder_info_by_path(folder_id)
    else:
        fid = folder_id

    str_sql='''select img_folder from tbl_form_folders a left join tbl_form_defs b on a.form_id = b.id
    where a.folder_id = %s;
    '''
    cursor.execute(str_sql,[fid])
    recs = cursor.fetchall()
    return recs[0][0]

def get_jpg_path_by_file_id(fid):
    str_sql = '''
       select folder, file_name from tbl_image_files where image_id = %s;
    '''
    cursor.execute(str_sql,[fid])
    recs = cursor.fetchall()
    if len(recs)==0:
        return False
    else:
        return os.path.join(recs[0][0],recs[0][1])