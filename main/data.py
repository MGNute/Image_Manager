__author__ = 'Michael'

import mysql.connector
import utilities
import ConfigParser
# import os.path
# import shutil
from globals import *
import data_retreiver as drt


class DataRetreiver():
    __metaclass__ = utilities.Singleton
    def __init__(self):
        self.initialize_db_connection()
        self.get_form_def_names()


    def initialize_db_connection(self,settings_file='main/db_config'):
        cfg=ConfigParser.ConfigParser()
        cfg.read(settings_file)
        dbargs={}
        dbargs['user']=cfg.get('db_config', 'user')
        dbargs['database']=cfg.get('db_config', 'database')
        dbargs['password']=cfg.get('db_config', 'password')
        # try:
        self.conn=mysql.connector.connect(**dbargs)
        self.cursor=self.conn.cursor()
        # except:
        #     print 'database error, configure settings in file db_config'

    def get_form_def_names(self):
        strsql = '''
        select distinct form_name,id from tbl_form_defs;
        '''
        self.cursor.execute(strsql)
        recs=self.cursor.fetchall()
        self.form_defs_full=recs
        self.form_defs=[]
        for i in recs:
            self.form_defs.append(i[0])

    def get_form_id_by_name(self,name):
        strsql='''
        select id from tbl_form_defs where form_name = %s;
        '''
        self.cursor.execute(strsql,[name])
        rec = self.cursor.fetchall()
        return rec[0][0]

    def add_location_to_form_def(self,form,loc):
        strsql1='''select count(*) from tbl_form_folders where folder = %s;'''
        self.cursor.execute(strsql1,[loc])
        rec=self.cursor.fetchall()
        if rec[0][0]==0:
            strsql='''
            insert into tbl_form_folders (form_id, folder) values (%s, %s);
            '''
            fid = self.get_form_id_by_name(form)
            self.cursor.execute(strsql,(fid,loc))
            self.conn.commit()
            return True
        else:
            return False

    def get_locations_by_form_def(self,form_def):
        fid = self.get_form_id_by_name(form_def)
        strsql = '''select folder_id, folder from tbl_form_folders where form_id = %s;'''
        self.cursor.execute(strsql,[fid])
        recs = self.cursor.fetchall()
        locs = [i[1] for i in recs]
        return locs

    def get_folder_info_by_path(self,path):
        strsql='''select form_id, folder_id from tbl_form_folders where folder = %s;
        '''
        self.cursor.execute(strsql,[path])
        recs = self.cursor.fetchall()
        if len(recs)>0:
            return recs[0]
        else:
            return None

    def get_folder_info_by_id(self,folder_id):
        strsql='''select form_id, folder from tbl_form_folders where folder_id = %s;
        '''
        self.cursor.execute(strsql,[folder_id])
        recs = self.cursor.fetchall()
        if len(recs)>0:
            return recs[0]
        else:
            return None

    def get_pdf_info_by_path(self,path):
        fo, fi = os.path.split(path)
        folder_info=self.get_folder_info_by_path(fo)
        strsql='''select * from tbl_form_pdf_files where folder_id=%s and file_name=%s;'''
        self.cursor.execute(strsql,(folder_info[1],fi))
        file_info=self.cursor.fetchall()
        if len(file_info)>0:
            return file_info[0]
        else:
            return None

    def add_pdf(self,file_name,folder_id,form_id):
        strsql='insert into tbl_form_pdf_files (folder_id,file_name,form_type) values (%s,%s,%s);'
        self.cursor.execute(strsql,(folder_id,file_name,form_id))
        str_sql_get = 'select pdf_id from tbl_form_pdf_files where folder_id = %s and file_name = %s;'
        self.cursor.execute(str_sql_get,(folder_id,file_name))
        r=self.cursor.fetchall()
        return r[0][0]

    def add_jpg(self,pdf_id,folder,page,file_name):
        str_sql='insert into tbl_image_files (pdf_file_id,folder,page,file_name) values (%s,%s,%s,%s);'
        self.cursor.execute(str_sql,(pdf_id,folder,page,file_name))

    def get_registered_pdfs_by_folder(self,folder_id):
        str_sql='select * from tbl_form_pdf_files where folder_id=%s;'
        self.cursor.execute(str_sql,[folder_id])
        files=self.cursor.fetchall()



class CurrentViewData():
    __metaclass__=utilities.Singleton

    def __init__(self):
        self.dr=DataRetreiver()
        self.form_defs=self.dr.get_form_def_names()
        self.active_form_index=None
        self.active_files=None
        self.folders_for_active_form=[]

    def set_active_form_index_by_name(self,form_name):
        self.active_form_index=self.dr.get_form_id_by_name(form_name)
        self.load_active_folders()

    def load_active_folders(self,paths_list):
        for i in self.folders_for_active_form:
            del i
        for i in paths_list:
            self.folders_for_active_form.append(Folder(i))
        for i in self.folders_for_active_form:
            i.load_registered_files()

    def unregister_folder(self,folder):
        pass

    # def load_files_from_db(self):
    #     strsql='''
    #     select * from tbl_form_pdf_files where form_type=%s;
    #     '''
    #     self.dr.cursor.execute(strsql,[self.active_form_index])
    #     self.active_files=self.dr.cursor.fetchall()

class Form():
    def __init__(self,name=None,pages=None,):
        if name==None:
            self.id = drt.get_form_id_by_name(name)
        else:
            self.name = name
            self.pages=pages
            self.id = self.register()


    def register(self):
        self.img_folder = os.path.join(primary_jpg_store,self.name)
        os.mkdir(self.img_folder)
        str_sql = '''
        insert into tbl_form_defs (form_name,pages,img_folder) values (%s,%s,%s);
        '''
        drt.cursor.execute(str_sql,(self.name,self.pages,self.img_folder))
        drt.conn.commit()
        self.id = drt.get_form_id_by_name(self.name)

    def set_template(self,template):
        pass


class Folder():
    def __init__(self,path,type=None):
        # TODO: Check that type is integer, and if not get the integer (right now downstream needs integer)
        self.path=path
        if isinstance(type,str):
            self.type = drt.get_form_id_by_name(type)
        elif isinstance(type,int):
            self.type = type
        else:
            self.type = type
        self.register_me()
        self.pdf_files=[]

    def search_harddrive_for_files(self):
        files=os.listdir(self.path)
        for i in files:
            fpath = os.path.join(self.path ,i)
            a=PDFfile(path=fpath)
            a.register()
            self.pdf_files.append(a)

    def load_registered_files(self):
        files=drt.get_registered_pdfs_by_folder()
        for i in files:
            self.pdf_files.append(PDFfile(db_data=i))
        pass

    def register_me(self):
        self.folder_id=drt.get_folder_info_by_path(self.path)
        if self.folder_id==None:
            drt.add_location_to_form_def(self.type,self.path)

    def unregister_me(self):
        # TODO: make this function
        pass

class AbstractDataFile():
    def __init__(self,path):
        fo,fi=os.path.split(path)
        self.path=path
        self.folder = fo
        self.filename = fi

class PDFfile(AbstractDataFile):
    path=None
    folder = None
    filename = None
    folder_id = None
    form_id = None
    child_jpgs=None
    pdf_id = None
    parsed_to_jpgs=None
    missing_from_disk=None
    jpg_target = None

    def __init__(self,path=None,type=None,folder_index=None,form_id=None,db_data=None,*args):
        if path<>None:
            AbstractDataFile.__init__(self,path)
            # self.folder_id=None
            if isinstance(form_id,str):
                self.form_id=drt.get_form_id_by_name(form_id)
            elif isinstance(form_id,int):
                self.form_id=form_id
            # self.child_jpgs=[]
            # self.pdf_id=None
            # self.parsed_to_jpgs=None
            # self.missing_from_disk=None
        elif db_data<>None:
            self.pdf_id=db_data[0]
            self.folder_id=db_data[1]
            self.filename=db_data[2]
            self.form_id=db_data[3]
            self.parsed_to_jpgs=db_data[4]
            self.missing_from_disk=db_data[5]
            self.folder=drt.get_folder_info_by_id(self.folder_id)
        self.register()

    def register(self):
        if self.folder_id==None or self.form_id==None:
            self.get_folder_id()
            self.get_jpg_target_path()
        # dr=DataRetreiver()
        file_info=drt.get_pdf_info_by_path(self.path)
        if file_info==None:
            self.pdf_id=drt.add_pdf(self.filename,self.folder_id,self.form_id)
        else:
            self.pdf_id=file_info[0]
            self.parsed_to_jpgs=file_info[4]
            self.missing_from_disk=file_info[5]

    def get_folder_id(self):
        if self.folder_id==None:
            f=drt.get_folder_info_by_path(self.folder)
            self.form_id=f[0]
            self.folder_id=f[1]

    def get_jpg_target_path(self):
        self.get_folder_id()
        self.jpg_target = drt.get_jpg_target_by_folder(self.folder_id)

    def get_child_jpgs(self):
        self.child_jpgs=drt.get_jpg_filepaths_by_pdf(self.pdf_id)

    def parse_to_jpgs(self):
        self.get_jpg_target_path()
        self.get_child_jpgs()
        if len(self.child_jpgs)>0:
            print 'ERROR: file %s was asked to parse jpgs, but this has already been done, manually delete files from HD and database to proceed. No action taken.' % self.filename
            return False
        if self.pdf_id==None:
            print 'File ' + self.filename + ' has not been registered and cannot be parsed.'
            return False
        else:
            jpglist=utilities.pdf_to_jpg(self.path,self.jpg_target,self.pdf_id)
            # dr=DataRetreiver()
            for i in jpglist:
                drt.add_jpg(self.pdf_id,self.jpg_target,i[1],i[0])







