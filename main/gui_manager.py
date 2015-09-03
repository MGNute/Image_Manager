__author__ = 'Michael'

import wxfb_classes
import wx
import skimage.io
import skimage.transform
import utilities
import data

class MyApp(wx.App):
    def OnInit(self):
        self.mainframe = gui_manager(None)
        self.SetTopWindow(self.mainframe)
        self.mainframe.Show()

        return True



class gui_manager(wxfb_classes.MainFrame):
    '''
    top level frame for this application
    '''
    def __init__(self,parent):
        wxfb_classes.MainFrame.__init__(self,parent)
        # self.image_frame=wxfb_classes.frame_full_image(self)
        self.image_frame=image_manager_frame(self)
        self.data_retreiver=data.DataRetreiver()
        for i in self.data_retreiver.form_defs:
            self.m_FormDefsComboBox.Append(i)
        self.active_data=data.CurrentViewData()


    def FormDefBoxUpdate(self,evt):
        form_def = self.m_FormDefsComboBox.GetValue()
        # print form_def
        self.load_form_definition(form_def)

    def load_form_definition(self,form_def_name):
        self.m_listBox1.Clear()
        for i in self.data_retreiver.get_locations_by_form_def(form_def_name):
            self.m_listBox1.Append(i)
            self.active_data.folders_for_active_form.append(i)
        self.active_data.load_active_folders()

    def AddPDFLocation( self, event ):
        fo = self.m_dirPicker1.GetTextCtrlValue()
        d = self.m_FormDefsComboBox.GetValue()
        self.data_retreiver.add_location_to_form_def(d,fo)
        self.load_form_definition(d)

    def load_pdf_tree_viewer(self):
        self.m_file_tree_ctrl.DeleteAllItems()
        rt=self.m_file_tree_ctrl.AddRoot(self.m_FormDefsComboBox.GetValue())
        for i in data.CurrentViewData().folders_for_active_form:
            loc=self.m_file_tree_ctrl.AppendItem(rt,i.path)
            for j in i.pdf_files:
                self.m_file_tree_ctrl.AppendItem(loc,j.filename)


    def load_PDFs_from_hard_drive(self):
        #TODO: have this refer to the active folders
        # path = 'C:\Users\Michael\Dropbox\DR, MOH record Images/12.6.2015 batey 7 census'
        paths=self.m_listBox1.GetStrings()
        import os
        self.m_file_tree_ctrl.DeleteAllItems()
        rt=self.m_file_tree_ctrl.AddRoot(self.m_FormDefsComboBox.GetValue())
        for i in paths:
            files=os.listdir(i)
            loc=self.m_file_tree_ctrl.AppendItem(rt,i)
            for j in files:
                self.m_file_tree_ctrl.AppendItem(loc,j)

        # loc=self.m_treeCtrl1.AppendItem(rt,path)
        # f1=self.m_treeCtrl1.AppendItem(loc,files[0])
        # self.m_treeCtrl1.AppendItem(loc,files[1])
        # print st.GetChildCount(wx.DataViewItem())

    def ShowImageFrame(self,eid):
        if eid.IsChecked()==True:
            self.image_frame.Show()
        else:
            self.image_frame.Hide()

    # def OnClose(self):
    #     self.image_frame.Close(True)
    #     self.image_frame.DestroyChildren()
    #     self.image_frame.Destroy()

class image_manager_frame(wxfb_classes.frame_full_image):
    def __init__(self,parent):
        wxfb_classes.frame_full_image.__init__(self,parent)
        self.Bind(wx.EVT_PAINT,self.OnPaint)
        self.active_image=ActiveDisplayImage()
        mypath = 'C:\Users\Michael\Projects\Andrew_Project\main\image\jpg3.jpg'
        self.active_image.set_image(mypath)

    def OnImgPaint(self,event):
        self.dc=wx.PaintDC(self.img_holder)
        # mypath = 'C:\Users\Michael\Projects\Andrew_Project\main\image\jpg0.jpg'
        # mybmp=pil_to_wx(mypath)
        # if self.active_image.wx_image<>None:
        self.dc.DrawBitmap(self.active_image.wx_image.ConvertToBitmap(),0,0)
        # self.img_holder.Refresh()

    def OnClose(self):
        # self.DestroyChildren()
        # self.Destroy()
        self.Hide()

    def AdjustZoom(self,event):
        z=self.m_ZoomCtrl.GetValue()
        # try:
        zoom=int(z)
        # print zoom
        self.active_image.set_zoom(zoom)
        self.img_holder.Refresh()
        # except:
        #     self.m_ZoomCtrl.SetValue(str(self.active_image.zoom))

class ActiveDisplayImage():
    __metaclass__= utilities.Singleton
    def __init__(self,path=None,zoom=100):
        self.path=path
        self.zoom=zoom
        if self.path<>None:
            self.set_image(path)
        else:
            self.clear_image()

    def set_zoom(self,zoom):
        self.zoom=zoom
        w=round(self.original_image.GetWidth()*self.zoom/100,0)
        h=round(self.original_image.GetHeight()*self.zoom/100,0)
        # print w
        # print h
        self.wx_image=self.original_image.Copy().Scale(w,h)

    def set_image(self,path):
        self.path=path
        self.original_image=wx.Image(path)
        self.wx_image = self.original_image.Copy()
        # self.resized_image = skimage.transform.rescale(self.disk_image,self.zoom/100)
        # img=wx.EmptyImage(self.resized_image.shape[1],self.resized_image.shape[0])
        # print img.Size
        # img.SetData(self.resized_image.tostring())
        # self.wx_image=img

    def clear_image(self):
        self.path = None
        self.original_image = None
        self.wx_image = wx.EmptyImage(1,1)



# def get_image(path):
#     pass
#
# def pil_to_wx(path):
#     # from PIL import Image
#     # image=Image.open(path,'r')
#     #
#     # width, height = image.size
#     # buffer = image.convert('RGB').tostring()
#     # bitmap = wx.BitmapFromBuffer(width, height, buffer)
#     bitmap = wx.Bitmap(path)
#     return bitmap
#     # def OnMainFrameClose(self,eid):
#     #     self.Close()

