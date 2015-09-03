# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Digitization Manager", pos = wx.DefaultPosition, size = wx.Size( 836,874 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 500,-1 ), wx.DefaultSize )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.pnl_form_config = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,-1 ), wx.TAB_TRAVERSAL )
		self.pnl_form_config.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.pnl_form_config.SetMinSize( wx.Size( 600,-1 ) )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer13.SetMinSize( wx.Size( 350,-1 ) ) 
		self.m_panel3 = wx.Panel( self.pnl_form_config, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_lbl_formname = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Form Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lbl_formname.Wrap( -1 )
		self.m_lbl_formname.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10.Add( self.m_lbl_formname, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 2 )
		
		m_FormDefsComboBoxChoices = []
		self.m_FormDefsComboBox = wx.ComboBox( self.m_panel3, wx.ID_ANY, u"(select from defined forms)", wx.DefaultPosition, wx.DefaultSize, m_FormDefsComboBoxChoices, 0 )
		bSizer10.Add( self.m_FormDefsComboBox, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_button3 = wx.Button( self.m_panel3, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button3, 0, wx.ALL, 2 )
		
		
		bSizer8.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer8.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_lbl_location = wx.StaticText( self.m_panel3, wx.ID_ANY, u"PDF Locations", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lbl_location.Wrap( -1 )
		self.m_lbl_location.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_lbl_location.SetToolTipString( u"Location of PDF files containing forms of this style" )
		
		bSizer11.Add( self.m_lbl_location, 0, wx.ALIGN_RIGHT|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		self.m_listBox1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 71, 90, 90, False, wx.EmptyString ) )
		
		bSizer11.Add( self.m_listBox1, 1, wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		self.m_dirPicker1 = wx.DirPickerCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer8.Add( self.m_dirPicker1, 0, wx.ALL|wx.EXPAND, 2 )
		
		self.m_button2 = wx.Button( self.m_panel3, wx.ID_ANY, u"Add Location", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_RIGHT, 2 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer8.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Template File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer12.Add( self.m_staticText6, 0, wx.ALIGN_RIGHT|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_filePicker1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer12.Add( self.m_filePicker1, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		bSizer8.Add( bSizer12, 0, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button4 = wx.Button( self.m_panel3, wx.ID_ANY, u"Load Files from DB", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button4, 1, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self.m_panel3, wx.ID_ANY, u"Find Files on Disk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button5, 1, wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( bSizer8 )
		self.m_panel3.Layout()
		bSizer8.Fit( self.m_panel3 )
		bSizer13.Add( self.m_panel3, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer13, 0, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.pnl_form_config, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer3.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText11 = wx.StaticText( self.pnl_form_config, wx.ID_ANY, u"Files", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer15.Add( self.m_staticText11, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_file_tree_ctrl = wx.TreeCtrl( self.pnl_form_config, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer15.Add( self.m_file_tree_ctrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		
		self.pnl_form_config.SetSizer( bSizer3 )
		self.pnl_form_config.Layout()
		bSizer18.Add( self.pnl_form_config, 1, wx.EXPAND|wx.TOP, 5 )
		
		
		self.SetSizer( bSizer18 )
		self.Layout()
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menubar2.Append( self.m_menu_file, u"File" ) 
		
		self.m_menu_edit = wx.Menu()
		self.m_menubar2.Append( self.m_menu_edit, u"Edit" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		self.m_toolBar2 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_tool2 = self.m_toolBar2.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_MENU ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar2.Realize() 
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_FormDefsComboBox.Bind( wx.EVT_COMBOBOX, self.FormDefBoxUpdate )
		self.m_button3.Bind( wx.EVT_BUTTON, self.define_new_form )
		self.m_button2.Bind( wx.EVT_BUTTON, self.AddPDFLocation )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FormDefBoxUpdate( self, event ):
		event.Skip()
	
	def define_new_form( self, event ):
		event.Skip()
	
	def AddPDFLocation( self, event ):
		event.Skip()
	

###########################################################################
## Class frame_full_image
###########################################################################

class frame_full_image ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Form Page (Full Image)", pos = wx.DefaultPosition, size = wx.Size( 824,773 ), style = wx.CAPTION|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.pnl_full_image = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pnl_full_image.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		self.pnl_full_image.SetMinSize( wx.Size( 600,-1 ) )
		
		bImgSizer = wx.BoxSizer( wx.VERTICAL )
		
		bPgBtnSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_prev_page = wx.StaticText( self.pnl_full_image, wx.ID_ANY, u"(ctrl + left-arrow) <<", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_prev_page.Wrap( -1 )
		bPgBtnSizer.Add( self.m_prev_page, 1, wx.ALL, 5 )
		
		self.m_page_label = wx.StaticText( self.pnl_full_image, wx.ID_ANY, u"page 1 of 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_page_label.Wrap( -1 )
		bPgBtnSizer.Add( self.m_page_label, 0, wx.ALL, 5 )
		
		self.m_next_page = wx.StaticText( self.pnl_full_image, wx.ID_ANY, u">> (ctrl + right-arrow)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_next_page.Wrap( -1 )
		bPgBtnSizer.Add( self.m_next_page, 1, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self.pnl_full_image, wx.ID_ANY, u"Zoom", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bPgBtnSizer.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_ZoomCtrl = wx.TextCtrl( self.pnl_full_image, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_RIGHT )
		self.m_ZoomCtrl.SetMaxSize( wx.Size( 30,-1 ) )
		
		bPgBtnSizer.Add( self.m_ZoomCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_staticText10 = wx.StaticText( self.pnl_full_image, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_staticText10.Wrap( -1 )
		bPgBtnSizer.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		
		bImgSizer.Add( bPgBtnSizer, 0, wx.EXPAND, 5 )
		
		self.img_holder = wx.Panel( self.pnl_full_image, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.img_holder.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		bImgSizer.Add( self.img_holder, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.pnl_full_image.SetSizer( bImgSizer )
		self.pnl_full_image.Layout()
		bImgSizer.Fit( self.pnl_full_image )
		bSizer8.Add( self.pnl_full_image, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_ZoomCtrl.Bind( wx.EVT_TEXT_ENTER, self.AdjustZoom )
		self.img_holder.Bind( wx.EVT_PAINT, self.OnImgPaint )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def AdjustZoom( self, event ):
		event.Skip()
	
	def OnImgPaint( self, event ):
		event.Skip()
	

###########################################################################
## Class frame_template_manager
###########################################################################

class frame_template_manager ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 599,803 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_template_manager = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_template_manager.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self.m_template_manager, wx.ID_ANY, u"Form Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer6.Add( self.m_staticText7, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.m_template_manager, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		bSizer6.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_new_field = wx.Button( self.m_template_manager, wx.ID_ANY, u"New Field", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_new_field, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer6, 0, 0, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_template_mgr_fields_lbl = wx.StaticText( self.m_template_manager, wx.ID_ANY, u"Fields", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_template_mgr_fields_lbl.Wrap( -1 )
		bSizer7.Add( self.m_template_mgr_fields_lbl, 0, wx.ALIGN_BOTTOM|wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_dataViewCtrl1 = wx.dataview.DataViewCtrl( self.m_template_manager, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_dataViewCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		self.m_template_manager.SetSizer( bSizer5 )
		self.m_template_manager.Layout()
		bSizer5.Fit( self.m_template_manager )
		bSizer16.Add( self.m_template_manager, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer16 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

