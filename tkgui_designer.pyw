#Tkinter GUI designer
#It uses tkinter Grid geometry manager. (https://effbot.org/tkinterbook/grid.htm)
#You will get pure Python tkinter code.
#
#1. Select the desired widgets*
#2. If you use rowsapan/colspan press "Check" button
#3. Press "Start" to generate codes
#4. Set the opened options windows and Apply
#5. Press "Finalize" and copy the generated code with Ctrl+C
#
#Hint:
#- rowspan must be placed under the expanded widget
#- columnspan must be placed to right side of the widget
#- maximum 4 column and 4 rowspan cells can be selected for one widget 
#  (rowspan/col.span=5)
#- if you use col.span and/or rowspan press "Check" button to check your selection.
#  (all missplaced span selection will be reseted and common merged cells disabled)
#- Canvas does not accept col./rowspan
#- Open second session of Python IDLE and use it for checking the generated code
#   without closing the running GUI generator
#- widget name with (s) means simple. It uses default parameters and does not open 
#   option window.
#Supported widgets: 
#menu, button, canvas, text with slide, entry, label, combobox, optionmenu,
#radio, message, frame, listbox, scale
#
#
# v0.4:    selection area 4x4
# v0.4.6:  selection area 5x5
# v0.5:    bigger widget selection area 5x7
# v0.5.9:  Label, Canvas, Text options
# v0.6:   All elements with uniqe numbers
# v0.6.5: CheckBox window options, canvas and text color options
# v0.6.8: Customizable Radio and Option menu
# v0.7:   rowspan,columnspan implemented, 5x9
# v0.8:   universal 2x2 frame
# v0.8.1  In case of 1 button there is no frame. You can use W+E to span button
#          Universal frame numbering bugs fixed
# v0.8.3  Universal frame with text: LabelFrame; without: Frame
# v0.8.4  tk and ttk import optimalization (for slide)
# v0.8.5  Menubar and Menubutton supported
# v0.8.6  new Menubar function: separate and checkbox
# v0.8.7  new Menubutton options menu
# v0.8.8  Listbox
# v0.8.9  Scale
# v0.9    Spinbox
# v0.9.1  Progressbar
# v0.9.2  Toolbar (buttons with images and tolltip text)
# v0.9.3  Notebook added
# v0.9.4  Widget selection save/load
# v0.9.5  interface improved
# v0.9.6  hints
# v0.9.7  it can generate functions and object, too
# v0.9.8  default parameter settings applied
# v1.0    it can save/load default parameters with widget selections
# v1.1    improved Comobox, Optionmenu and Radio
#
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import colorchooser
from tkinter import filedialog
import webbrowser

class ToolTip(object):
#source:
#https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
    def __init__(self, widget):
        self.widget=widget
        self.tipwindow=None
        self.id=None
        self.x=self.y=0
    def showtip(self, text):
        'Display text in tooltip window'
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox('insert')
        x = x + self.widget.winfo_rootx() + 20
        y = y + cy + self.widget.winfo_rooty() +40
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry('+%d+%d' % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background='#ffffe0', relief=SOLID, borderwidth=1,
                      font=('tahoma', '8', 'normal'))
        label.pack(ipadx=1)
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)

class Menbar:
    "Menubar code generator"
    def __init__(self,rc,inputlist,frame_name):
        self.frame_name=frame_name
        self.col=rc[0]
        self.row=rc[1]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.menuszam=0
        self.keretszam=''
        self.inputlist=inputlist
        self.kret=''
        self.inputlist.pop(-1) #remove orientation from the list
        self.msz1=''
        self.tab=getresulttype()[0]
        self.slf=getresulttype()[1]
#        print(str(self.tab)+str(self.slf))
    def proc(self):
        self.i2=[] #temporary list for work
        self.x=0 #counter
        
        while (self.x<len(self.inputlist)): #create emptyt list that contains exactly as much empty [] list as mush element its have
            self.i2.append([]) 
            self.x=self.x+1
        self.subm=[]  #empty list for sub elements (submenu)
        self.mainm=[] #empty list for first elements (mainmenu)  
        for self.i in range(len(self.inputlist)):  # read all list in inputlist
            for self.j in self.inputlist[self.i]:      #read all sub list
                if (self.j!=''):
                    self.i2[self.i].append(self.j)    #put all valid values to i2 temporary list
        for self.i in range(len(self.i2)):         
            if (self.i2[self.i]!=[]):		    #if element of i2 is not ''
                   self.subm.append(self.i2[self.i]) #put it into the subm list
            
        for self.i in range(len(self.subm)):       #first element of subm put into mainm list and...
            self.mainm.append(self.subm[self.i][0])
            self.subm[self.i].pop(0)                #... remove it from subm list
                            
        for self.i in self.subm:  # if there was only 1 main menu it create an empty '' text element in the list
            if (self.i==[]):
                self.i.append('')
        self.x=0
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.kret=str(self.tab)+str(self.slf)+'menubar'+self.keretszam+'= Menu('+str(self.slf)+'ablak)'
        while(self.menuszam<len(self.mainm)):
            self.msz1=self.msz1+str(self.tab)+str(self.slf)+'submenu'+self.keretszam+str(self.menuszam)+'=Menu('+str(self.slf)+'menubar'+self.keretszam+', tearoff=0)\n'+str(self.tab)+str(self.slf)+'menubar'+self.keretszam+'.add_cascade(label='+"'"+str(self.mainm[self.menuszam])+"'"+', menu='+str(self.slf)+'submenu'+self.keretszam+str(self.menuszam)+')\n'
            while(self.x<len(self.subm[self.menuszam])):
                if(self.subm[self.menuszam][self.x]=='-'): # '-' = separator
                    self.msz1=self.msz1+str(self.tab)+str(self.slf)+'submenu'+self.keretszam+str(self.menuszam)+'.add_separator()\n'
                try:
                    if(self.subm[self.menuszam][self.x][0]=='#'): #first char of text is # checkbox
                        self.msz1=self.msz1+str(self.tab)+str(self.slf)+'v'+self.keretszam+str(self.menuszam)+str(self.x)+'= BooleanVar('+str(self.slf)+'ablak)\n'+str(self.tab)+str(self.slf)+'submenu'+self.keretszam+str(self.menuszam)+'.add_checkbutton(label='+"'"+str(self.subm[self.menuszam][self.x][1:])+"'"+', variable='+str(self.slf)+'v'+self.keretszam+str(self.menuszam)+str(self.x)+')\n'
                    if((self.subm[self.menuszam][self.x][0]!='#') and (self.subm[self.menuszam][self.x]!='-')):   
                        self.msz1=self.msz1+str(self.tab)+str(self.slf)+'submenu'+self.keretszam+str(self.menuszam)+'.add_command(label='+"'"+str(self.subm[self.menuszam][self.x])+"'"+', command='+str(self.slf)+'k_ablak.destroy)\n'
                except:
                    pass
                self.x=self.x+1
            self.x=0
            self.menuszam=self.menuszam+1
        self.mszv=str(self.tab)+str(self.slf)+'k_ablak.config(menu='+str(self.slf)+'menubar'+self.keretszam+')'
        self.osszes=self.kret+'\n'+self.msz1+self.mszv
        return self.osszes
           

class Menuk:
    "Menubuton generator modul"
    def __init__(self,rc,inputlist,frame_name):
        self.frame_name=frame_name
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.menuszam=0
        self.keretszam=''
        self.inputlist=inputlist
        self.kret=''
        self.o=self.inputlist[4]
        self.inputlist.pop(-1) #remove orientation from the list
        self.msz1=''
        self.msz2=''
        self.msz3=''
        self.tab=getresulttype()[0]
        self.slf=getresulttype()[1]
    def proc(self):
        self.i2=[] #temporary list for work
        self.x=0 #counter
        
        while (self.x<len(self.inputlist)): #create emptyt list that contains exactly as much empty [] list as mush element its have
            self.i2.append([]) 
            self.x=self.x+1
        self.subm=[]  #empty list for sub elements (submenu)
        self.mainm=[] #empty list for first elements (mainmenu)  
        for self.i in range(len(self.inputlist)):  # read all list in inputlist
            for self.j in self.inputlist[self.i]:      #read all sub list
                if (self.j!=''):
                    self.i2[self.i].append(self.j)    #put all valid values to i2 temporary list
        for self.i in range(len(self.i2)):         
            if (self.i2[self.i]!=[]):		    #if element of i2 is not ''
                   self.subm.append(self.i2[self.i]) #put it into the subm list
            
        for self.i in range(len(self.subm)):       #first element of subm put into mainm list and...
            self.mainm.append(self.subm[self.i][0])
            self.subm[self.i].pop(0)                #... remove it from subm list
                            
        for self.i in self.subm:  # if there was only 1 main menu it create an empty '' text element in the list
            if (self.i==[]):
                self.i.append('')
#        print('main: ',self.mainm,'\nsubm: ',self.subm)
        self.x=0
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.kret=str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'=Frame('+str(self.slf)+self.frame_name+', relief='+"'"+'raised'+"'"+', borderwidth=1)\n'+str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+str(self.o)+')'
        while(self.menuszam<len(self.mainm)):
            self.msz1=self.msz1+str(self.tab)+str(self.slf)+'menu'+self.keretszam+str(self.menuszam)+'=ttk.Menubutton('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.mainm[self.menuszam])+"'"+')\n'+str(self.tab)+str(self.slf)+'mf'+self.keretszam+str(self.menuszam)+'=Menu('+str(self.slf)+'menu'+self.keretszam+str(self.menuszam)+')\n'
            self.msz3=self.msz3+str(self.tab)+str(self.slf)+'menu'+self.keretszam+str(self.menuszam)+'.configure(menu='+str(self.slf)+'mf'+self.keretszam+str(self.menuszam)+')\n'
            self.msz3=self.msz3+str(self.tab)+str(self.slf)+'menu'+self.keretszam+str(self.menuszam)+'.grid(row=0, column='+str(self.menuszam)+', sticky=NW)\n'
            while(self.x<len(self.subm[self.menuszam])):
                self.msz2=self.msz2+str(self.tab)+str(self.slf)+'mf'+self.keretszam+str(self.menuszam)+'.add_command(label='+"'"+str(self.subm[self.menuszam][self.x])+"'"+',command='+str(self.slf)+'k_ablak.destroy, state=NORMAL)\n'
                self.x=self.x+1
            self.x=0
            self.menuszam=self.menuszam+1
        self.osszes=self.kret+'\n'+self.msz1+self.msz2+self.msz3
        return self.osszes

class Gombokx:
    "Button generator modul"
    def __init__(self,rc,inputlist,frame_name):
        self.frame_name=frame_name
        self.inputlist=inputlist
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.gombszam=0 #button nuber for unique numbering
        self.bn=0       #button counter 
        self.keretszam=''
        self.kret=''
        self.f1, self.f2, self.f3=inputlist[0],inputlist[1],inputlist[2]
        self.f11, self.f21, self.f31=inputlist[3],inputlist[4],inputlist[5]
        self.f12, self.f22, self.f32=inputlist[6],inputlist[7],inputlist[8]
        self.f13, self.f23, self.f33=inputlist[9],inputlist[10],inputlist[11]
        self.o=self.inputlist[12]
        self.tab=getresulttype()[0]
        self.slf=getresulttype()[1]
    def butt_number(self):
        for self.i in range(len(self.inputlist)-1):
            if self.inputlist[self.i]!='':
                self.bn=self.bn+1
        return self.bn
    def generator(self):
        self.x=self.butt_number()
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.ombszamstr=self.keretszam+str(self.gombszam)
        if(self.x==1): #in case of 1 button there is no Frame (possible to create wide button with N+W)
            self.gsz=str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'=ttk.Button('+str(self.slf)+str(self.frame_name)+',text='+"'"+str(self.f1)+"'"+',command='+str(self.slf)+'k_ablak.destroy)'
            self.gszv=str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+str(self.o)+')'
        else:
            self.kret=str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'=Frame('+str(self.slf)+str(self.frame_name)+', relief='+"'flat'"+', borderwidth=1)\n'+str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+str(self.o)+')'
            self.gsz=str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'=ttk.Button('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.f1)+"'"+',command='+str(self.slf)+'k_ablak.destroy)'
            self.gszv=str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'.grid(row=0, column=0)'
        if(self.f2!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'=ttk.Button('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.f2)+"'"+',command='+str(self.slf)+'k_ablak.destroy)'
            self.gszv=self.gszv+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'.grid(row=0, column=1)'
        if(self.f3!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'=ttk.Button('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.f3)+"'"+',command='+str(self.slf)+'k_ablak.destroy)'
            self.gszv=self.gszv+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'.grid(row=0, column=2)'
        if(self.f11!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'=ttk.Button('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.f11)+"'"+',command='+str(self.slf)+'k_ablak.destroy)'
            self.gszv=self.gszv+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'.grid(row=1, column=0)'
        if(self.f21!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'=ttk.Button('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.f21)+"'"+',command='+str(self.slf)+'k_ablak.destroy)'
            self.gszv=self.gszv+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'.grid(row=1, column=1)'
        if(self.f31!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'=ttk.Button('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.f31)+"'"+',command='+str(self.slf)+'k_ablak.destroy)'
            self.gszv=self.gszv+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'.grid(row=1, column=2)'
        if(self.f12!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'=ttk.Button('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.f12)+"'"+',command='+str(self.slf)+'k_ablak.destroy)'
            self.gszv=self.gszv+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'.grid(row=2, column=0)'
        if(self.f22!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'=ttk.Button('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.f22)+"'"+',command='+str(self.slf)+'k_ablak.destroy)'
            self.gszv=self.gszv+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'.grid(row=2, column=1)'
        if(self.f32!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'=ttk.Button('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.f32)+"'"+',command='+str(self.slf)+'k_ablak.destroy)'
            self.gszv=self.gszv+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'.grid(row=2, column=2)'
        if(self.f13!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'=ttk.Button('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.f13)+"'"+',command='+str(self.slf)+'k_ablak.destroy)'
            self.gszv=self.gszv+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'.grid(row=3, column=0)'
        if(self.f23!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'=ttk.Button('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.f23)+"'"+',command='+str(self.slf)+'k_ablak.destroy)'
            self.gszv=self.gszv+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'.grid(row=3, column=1)'
        if(self.f33!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'=ttk.Button('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.f33)+"'"+',command='+str(self.slf)+'k_ablak.destroy)'
            self.gszv=self.gszv+'\n'+str(self.tab)+str(self.slf)+'btn'+str(self.keretszam)+str(self.gombszam)+'.grid(row=3, column=2)'
        self.osszes=self.kret+'\n'+self.gsz+'\n'+self.gszv
        return self.osszes


class Toolbargen:
    "Toolbar code generator"
    def __init__(self,rc,inputlist,frame_name):
        self.frame_name=frame_name
        self.inputlist=inputlist #img1,img2,img3,img4,img5,tiptxt1,tiptxt2,tiptxt3,tiptxt4,tiptxt5,orient
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.keretszam=''
        self.kret=''
        self.o=inputlist[10] #orient.
        self.gsz=''
        self.tab=getresulttype()[0]
        self.slf=getresulttype()[1]
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.kret=self.kret+str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'=Frame('+str(self.slf)+self.frame_name+', relief='+"'flat'"+', borderwidth=1)\n'+str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+str(self.o)+')\n'
        for self.i in range(5):
            if(self.inputlist[self.i]!='---'):
                self.gsz=self.gsz+str(self.tab)+str(self.slf)+'photo'+str(self.keretszam)+str(self.i)+'=PhotoImage(file='+"'ico/"+str(self.inputlist[self.i])+'.png'+"'"+')\n'
                self.gsz=self.gsz+str(self.tab)+str(self.slf)+'tb'+str(self.keretszam)+str(self.i)+'=ttk.Button('+str(self.slf)+'frm'+str(self.keretszam)+',text='+"'"+str(self.i)+"'"+',image='+str(self.slf)+'photo'+str(self.keretszam)+str(self.i)+',command='+str(self.slf)+'k_ablak.destroy)\n'
                self.gsz=self.gsz+str(self.tab)+str(self.slf)+'tb'+str(self.keretszam)+str(self.i)+'.grid(row=0, column='+str(self.i)+')\n'
                if(self.inputlist[self.i+5]!=''):
                    self.gsz=self.gsz+str(self.tab)+'CreateToolTip('+str(self.slf)+'tb'+str(self.keretszam)+str(self.i)+',text='+"'"+str(self.inputlist[self.i+5])+"'"+')\n'
        self.osszes=self.kret+self.gsz
        return self.osszes                

        

class Vaszon:
    "Canvas generator modul"
    def __init__(self,rc,inputlist,frame_name):
        self.frame_name=frame_name
        self.inputlist=inputlist
        self.col=rc[0]
        self.row=rc[1]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.canszam=0
        self.canw=inputlist[0] #width
        self.canh=inputlist[1] #height
        self.canc=inputlist[2] #color
        self.cano=inputlist[3] #orientation
        self.keretszam=''
        self.tab=getresulttype()[0]
        self.slf=getresulttype()[1]
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.csz=str(self.tab)+str(self.slf)+'can'+self.keretszam+str(self.canszam)+'=Canvas('+str(self.slf)+str(self.frame_name)+',bg='+"'"+self.canc+"'"+',height='+str(self.canh)+', width='+str(self.canw)+')'
        self.cszv=str(self.tab)+str(self.slf)+'can'+self.keretszam+str(self.canszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+',sticky='+self.cano+')'
        self.osszes=self.csz+'\n'+self.cszv
        return self.osszes

class Szovegmezocs:
    "Text area with slide generator modul"
    def __init__(self,rc,inputlist,frame_name):
        self.frame_name=frame_name
        self.inputlist=inputlist
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.mezoszam=0
        self.keretszam=''
        self.w=inputlist[0]  #width
        self.h=inputlist[1]  #height
        self.o=inputlist[2]  #orientation
        self.s=inputlist[3]  #slide
        self.t=inputlist[4]  #default text
        self.bg=inputlist[5] #background color
        self.fg=inputlist[6] #foreground color
        self.wrap=''
        self.tab=getresulttype()[0]
        self.slf=getresulttype()[1]
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        if(self.s[0]=='3' or self.s[0]=='4'):
            self.wrap=',wrap=NONE'
        self.kret=str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'=Frame('+str(self.slf)+self.frame_name+', relief='+"'flat'"+', borderwidth=1)\n'+str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky=N)'
        self.sz1=str(self.tab)+str(self.slf)+'text'+self.keretszam+str(self.mezoszam)+'=Text('+str(self.slf)+'frm'+str(self.keretszam)+',height='+str(self.h)+',width='+str(self.w)+str(self.wrap)+',bg='+"'"+self.bg+"'"+',fg='+"'"+self.fg+"'"+')'
        if(self.s[0]=='2'): # függ csúszka
            self.sz2=str(self.tab)+str(self.slf)+'scrolly'+self.keretszam+str(self.mezoszam)+'=Scrollbar('+str(self.slf)+'frm'+str(self.keretszam)+', orient=VERTICAL,command='+str(self.slf)+'text'+self.keretszam+str(self.mezoszam)+'.yview)'
            self.sz3=str(self.tab)+str(self.slf)+'text'+self.keretszam+str(self.mezoszam)+'['+"'yscrollcommand'"+']='+str(self.slf)+'scrolly'+self.keretszam+str(self.mezoszam)+'.set'
            self.szcsv=str(self.tab)+str(self.slf)+'scrolly'+self.keretszam+str(self.mezoszam)+'.grid(row=0, column=1 ,sticky=N+S)'
        if(self.s[0]=='3'): # víz csúszka
            self.sz2=str(self.tab)+str(self.slf)+'scrollx'+self.keretszam+str(self.mezoszam)+'=Scrollbar('+str(self.slf)+'frm'+str(self.keretszam)+', orient=HORIZONTAL,command='+str(self.slf)+'text'+self.keretszam+str(self.mezoszam)+'.xview)'
            self.sz3=str(self.tab)+str(self.slf)+'text'+self.keretszam+str(self.mezoszam)+'['+"'xscrollcommand'"+']='+str(self.slf)+'scrollx'+self.keretszam+str(self.mezoszam)+'.set'
            self.szcsv=str(self.tab)+str(self.slf)+'scrollx'+self.keretszam+str(self.mezoszam)+'.grid(row=1, column=0 ,sticky=E+W)'
        if(self.s[0]=='4'): # mindkettő
            self.sz2=str(self.tab)+str(self.slf)+'scrolly'+self.keretszam+str(self.mezoszam)+'=Scrollbar('+str(self.slf)+'frm'+str(self.keretszam)+', orient=VERTICAL,command='+str(self.slf)+'text'+self.keretszam+str(self.mezoszam)+'.yview)\n'
            self.sz2=self.sz2+str(self.tab)+str(self.slf)+'scrollx'+self.keretszam+str(self.mezoszam)+'=Scrollbar('+str(self.slf)+'frm'+str(self.keretszam)+', orient=HORIZONTAL,command='+str(self.slf)+'text'+self.keretszam+str(self.mezoszam)+'.xview)'
            self.sz3=str(self.tab)+str(self.slf)+'text'+self.keretszam+str(self.mezoszam)+'['+"'yscrollcommand'"+']='+str(self.slf)+'scrolly'+self.keretszam+str(self.mezoszam)+'.set\n'
            self.sz3=self.sz3+str(self.tab)+str(self.slf)+'text'+self.keretszam+str(self.mezoszam)+'['+"'xscrollcommand'"+']='+str(self.slf)+'scrollx'+self.keretszam+str(self.mezoszam)+'.set'
            self.szcsv=str(self.tab)+str(self.slf)+'scrolly'+self.keretszam+str(self.mezoszam)+'.grid(row=0, column=1 ,sticky=N+S)\n'+str(self.tab)+str(self.slf)+'scrollx'+self.keretszam+str(self.mezoszam)+'.grid(row=1, column=0 ,sticky=E+W)'
        if(self.s[0]=='1'): #nincs csúszka
            self.szcsv, self.sz2, self.sz3='','',''
        self.szv=str(self.tab)+str(self.slf)+'text'+self.keretszam+str(self.mezoszam)+'.grid(row=0, column=0,sticky='+self.o+')'
        if (self.t!=''):
            self.szv=self.szv+'\n'+str(self.tab)+str(self.slf)+'text'+self.keretszam+str(self.mezoszam)+'.insert(INSERT,'+"'"+str(self.t)+"'"+')'
        
        self.osszes=self.kret+'\n'+self.sz1+'\n'+self.sz2+'\n'+self.sz3+'\n'+self.szv+'\n'+self.szcsv
        return self.osszes


class Beviteli:
    "Entry generator modul"
    def __init__(self,rc,output,frame_name):
        self.frame_name=frame_name
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.bevszam=0
        self.keretszam=''
        self.o=output[0] # orient.
        self.w=output[1] # width
        self.value=output[2] # default value
        self.tab=getresulttype()[0]
        self.slf=getresulttype()[1]
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.b1=str(self.tab)+str(self.slf)+'entr'+self.keretszam+str(self.bevszam)+'=ttk.Entry('+str(self.slf)+self.frame_name+' ,width='+"'"+str(self.w)+"'"+')\n'
        self.bv=str(self.tab)+str(self.slf)+'entr'+self.keretszam+str(self.bevszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+str(self.o)+')'
        if(self.value!=''):
            self.bv=self.bv+'\n'+str(self.tab)+str(self.slf)+'entr'+self.keretszam+str(self.bevszam)+'.insert(0,'+'"'+str(self.value)+'"'+')'
        self.osszes=self.b1+self.bv
        return self.osszes

class Cimke:
    "Label generator modul"
    def __init__(self,rc,output,frame_name):
        self.frame_name=frame_name
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.labtxt=output[0]
        self.labo=output[1]
        self.cimkeszam=0
        self.keretszam=''
        self.tab=getresulttype()[0]
        self.slf=getresulttype()[1]
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.c1=str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.cimkeszam)+'=Label('+str(self.slf)+self.frame_name+', text='+"'"+str(self.labtxt)+"'"+')'
        self.cv=str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.cimkeszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.labo+')'
        self.osszes=self.c1+'\n'+self.cv
        return self.osszes

class Keret:
    "Frame generator modul"
    def __init__(self,rc,output,nbframe):
        self.nbframe=nbframe #notebook_frame name
        self.ftext=output[1] #frame text
        self.labo=output[0] #orientation
        self.keretszam=0
        self.h=200
        self.w=250
        self.r='flat'
        self.bw=1
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.krtszam=''
        self.krt_name=''
        self.tab=getresulttype()[0]
        self.slf=getresulttype()[1]
    def generator(self):
        self.krtszam=str(self.row)+str(self.col)
        if(self.nbframe!='ablak'):
            self.krt_name='frm'+self.krtszam+str(self.keretszam)+str(self.nbframe)
        else:
            self.krt_name='frm'+self.krtszam+str(self.keretszam)

        if(self.ftext==''): # if there is not any text: (normal) Frame
             self.k1=str(self.tab)+str(self.slf)+str(self.krt_name)+'=Frame('+str(self.slf)+str(self.nbframe)+', height='+str(self.h)+', width='+str(self.w)+', relief='+"'"+str(self.r)+"'"+', borderwidth='+str(self.bw)+')'
        else:  # if there is any text: LabelFrame
             self.k1=str(self.tab)+str(self.slf)+str(self.krt_name)+'=ttk.LabelFrame('+str(self.slf)+str(self.nbframe)+', text='+"'"+self.ftext+"'"+', height='+str(self.h)+', width='+str(self.w)+', relief='+"'"+str(self.r)+"'"+', borderwidth='+str(self.bw)+')'
        self.kv=str(self.tab)+str(self.slf)+str(self.krt_name)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.labo+')'
        self.osszes=self.k1+'\n'+self.kv
        return self.osszes, self.krt_name

class Uzenet:
    "Message window generator modul"
    def __init__(self,rc):
        self.uzenszam=0
        self.w=250
        self.py=30
        self.px=40
        self.szoveg='This is a system message!'
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.keretszam=''
        self.tab=getresulttype()[0]
        self.slf=getresulttype()[1]
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)
        self.u1=str(self.tab)+str(self.slf)+'msg'+self.keretszam+str(self.uzenszam)+'=Message('+str(self.slf)+'ablak, width='+str(self.w)+', pady='+str(self.py)+', padx='+str(self.px)+', text='+"'"+str(self.szoveg)+"'"+')'
        self.uv=str(self.tab)+str(self.slf)+'msg'+self.keretszam+str(self.uzenszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+')'
        self.osszes=self.u1+'\n'+self.uv
        return self.osszes

class Combox:
    "Combox generator modul"
    def __init__(self,rc,inputs,frame_name):
        self.frame_name=frame_name
        self.cboxszam=0
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.keretszam=''
        self.inputs=inputs
        self.cb1=''
        self.cb2=''
        self.cb3=''
        self.cbv=''
        self.v1=self.inputs[0] #field values
        self.v2=self.inputs[1]
        self.v3=self.inputs[2]
        self.v4=self.inputs[3]
        self.l1,self.l2,self.l3,self.l4=self.inputs[4],self.inputs[5],self.inputs[6],self.inputs[7] # label values
        self.orient=self.inputs[8] #orientation
        self.cw=self.inputs[9]     #cell width
        self.x=0
        self.tab=getresulttype()[0]
        self.slf=getresulttype()[1]
        self.v1=list2tuple(self.v1)
        self.v2=list2tuple(self.v2)
        self.v3=list2tuple(self.v3)
        self.v4=list2tuple(self.v4)
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.kret=str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'=Frame('+str(self.slf)+self.frame_name+', relief='+"'flat'"+', borderwidth=1)\n'+str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.orient+')'
        if(self.v1!=()):
            self.cb1=self.cb1+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'=ttk.Combobox('+str(self.slf)+'frm'+str(self.keretszam)+', width='+str(self.cw)+')'
            self.cb2=self.cb2+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'['+"'values'"+']='+str(self.v1)
            self.cb3=self.cb3+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'.current(0)'
            self.cbv=self.cbv+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'.grid(row=0, column=1,sticky=N)\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.cboxszam)+'=Label('+str(self.slf)+'frm'+str(self.keretszam)+', text='+"'"+self.l1+"'"+')\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.cboxszam)+'.grid(row=0, column=0,sticky=N)'
        if(self.v2!=()):
            self.cboxszam=1
            self.cb1=self.cb1+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'=ttk.Combobox('+str(self.slf)+'frm'+str(self.keretszam)+', width='+str(self.cw)+')'
            self.cb2=self.cb2+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'['+"'values'"+']='+str(self.v2)
            self.cb3=self.cb3+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'.current(0)'
            self.cbv=self.cbv+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'.grid(row=0, column=3,sticky=N)\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.cboxszam)+'=Label('+str(self.slf)+'frm'+str(self.keretszam)+', text='+"'"+self.l2+"'"+')\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.cboxszam)+'.grid(row=0, column=2,sticky=N)'
        if(self.v3!=()):
            self.cboxszam=2
            self.cb1=self.cb1+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'=ttk.Combobox('+str(self.slf)+'frm'+str(self.keretszam)+', width='+str(self.cw)+')'
            self.cb2=self.cb2+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'['+"'values'"+']='+str(self.v3)
            self.cb3=self.cb3+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'.current(0)'
            self.cbv=self.cbv+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'.grid(row=1, column=1,sticky=N)\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.cboxszam)+'=Label('+str(self.slf)+'frm'+str(self.keretszam)+', text='+"'"+self.l3+"'"+')\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.cboxszam)+'.grid(row=1, column=0,sticky=N)'
        if(self.v4!=()):
            self.cboxszam=3
            self.cb1=self.cb1+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'=ttk.Combobox('+str(self.slf)+'frm'+str(self.keretszam)+', width='+str(self.cw)+')'
            self.cb2=self.cb2+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'['+"'values'"+']='+str(self.v4)
            self.cb3=self.cb3+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'.current(0)'
            self.cbv=self.cbv+'\n'+str(self.tab)+str(self.slf)+'chbox'+self.keretszam+str(self.cboxszam)+'.grid(row=1, column=3,sticky=N)\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.cboxszam)+'=Label('+str(self.slf)+'frm'+str(self.keretszam)+', text='+"'"+self.l4+"'"+')\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.cboxszam)+'.grid(row=1, column=2,sticky=N)'
        self.osszes=self.kret+'\n'+self.cb1+self.cb2+self.cb3+self.cbv
        return self.osszes
        

class Optmenu:
    "Option menu generator modul"
    def __init__(self,rc,inputs,frame_name):
        self.frame_name=frame_name
        self.inputs=inputs
        self.omszam=0
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.keretszam=''
        self.v1=removeempty(self.inputs[0]) #field values
        self.v2=removeempty(self.inputs[1])
        self.v3=removeempty(self.inputs[2])
        self.v4=removeempty(self.inputs[3])
        self.l1,self.l2,self.l3,self.l4=self.inputs[4],self.inputs[5],self.inputs[6],self.inputs[7] # label values
        self.orient=self.inputs[8] #orientation
        self.osszes=''
        self.om1,self.om2,self.om3,self.omv='','','',''
        self.tab=getresulttype()[0]
        self.slf=getresulttype()[1]
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.kret=str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'=Frame('+str(self.slf)+self.frame_name+', relief='+"'flat'"+', borderwidth=1)\n'+str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.orient+')\n'
        if(self.v1!=[]):
            self.omszam=0
            self.om1=self.om1+str(self.tab)+str(self.slf)+'var'+self.keretszam+str(self.omszam)+' = StringVar('+str(self.slf)+'frm'+str(self.keretszam)+')\n'
            self.om2=self.om2+str(self.tab)+str(self.slf)+'var'+self.keretszam+str(self.omszam)+'.set(0)\n'
            self.om3=self.om3+str(self.tab)+str(self.slf)+'opmenu'+self.keretszam+str(self.omszam)+'=ttk.OptionMenu('+str(self.slf)+'frm'+str(self.keretszam)+', '+str(self.slf)+'var'+self.keretszam+str(self.omszam)+', '+"'"+'select'+"'"
            for self.i in self.v1: #remove empty cells
                if (self.i!=''):
                    self.om3=self.om3+','+"'"+str(self.i)+"'"+' '
            self.om3=self.om3+')\n'
            self.omv=self.omv+str(self.tab)+str(self.slf)+'opmenu'+self.keretszam+str(self.omszam)+'.grid(row=0, column=1, sticky=W)\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.omszam)+'=Label('+str(self.slf)+'frm'+str(self.keretszam)+', text='+"'"+self.l1+"'"+')\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.omszam)+'.grid(row=0, column=0,sticky=W)\n'
        
        if(self.v2!=[]):
            self.omszam=1
            self.om1=self.om1+str(self.tab)+str(self.slf)+'var'+self.keretszam+str(self.omszam)+' = StringVar('+str(self.slf)+'frm'+str(self.keretszam)+')\n'
            self.om2=self.om2+str(self.tab)+str(self.slf)+'var'+self.keretszam+str(self.omszam)+'.set(0)\n'
            self.om3=self.om3+str(self.tab)+str(self.slf)+'opmenu'+self.keretszam+str(self.omszam)+'=ttk.OptionMenu('+str(self.slf)+'frm'+str(self.keretszam)+', '+str(self.slf)+'var'+self.keretszam+str(self.omszam)+', '+"'"+'select'+"'"
            for self.i in self.v2:
                if (self.i!=''):
                    self.om3=self.om3+','+"'"+str(self.i)+"'"+' '
            self.om3=self.om3+')\n'
            self.omv=self.omv+str(self.tab)+str(self.slf)+'opmenu'+self.keretszam+str(self.omszam)+'.grid(row=0, column=3, sticky=W)\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.omszam)+'=Label('+str(self.slf)+'frm'+str(self.keretszam)+', text='+"'"+self.l2+"'"+')\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.omszam)+'.grid(row=0, column=2,sticky=W)\n'

        if(self.v3!=[]):
            self.omszam=2
            self.om1=self.om1+str(self.tab)+str(self.slf)+'var'+self.keretszam+str(self.omszam)+' = StringVar('+str(self.slf)+'frm'+str(self.keretszam)+')\n'
            self.om2=self.om2+str(self.tab)+str(self.slf)+'var'+self.keretszam+str(self.omszam)+'.set(0)\n'
            self.om3=self.om3+str(self.tab)+str(self.slf)+'opmenu'+self.keretszam+str(self.omszam)+'=ttk.OptionMenu('+str(self.slf)+'frm'+str(self.keretszam)+', '+str(self.slf)+'var'+self.keretszam+str(self.omszam)+', '+"'"+'select'+"'"
            for self.i in self.v3:
                if (self.i!=''):
                    self.om3=self.om3+','+"'"+str(self.i)+"'"+' '
            self.om3=self.om3+')\n'
            self.omv=self.omv+str(self.tab)+str(self.slf)+'opmenu'+self.keretszam+str(self.omszam)+'.grid(row=1, column=1, sticky=W)\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.omszam)+'=Label('+str(self.slf)+'frm'+str(self.keretszam)+', text='+"'"+self.l3+"'"+')\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.omszam)+'.grid(row=1, column=0,sticky=W)\n'

        if(self.v4!=[]):
            self.omszam=3
            self.om1=self.om1+str(self.tab)+str(self.slf)+'var'+self.keretszam+str(self.omszam)+' = StringVar('+str(self.slf)+'frm'+str(self.keretszam)+')\n'
            self.om2=self.om2+str(self.tab)+str(self.slf)+'var'+self.keretszam+str(self.omszam)+'.set(0)\n'
            self.om3=self.om3+str(self.tab)+str(self.slf)+'opmenu'+self.keretszam+str(self.omszam)+'=ttk.OptionMenu('+str(self.slf)+'frm'+str(self.keretszam)+', '+str(self.slf)+'var'+self.keretszam+str(self.omszam)+', '+"'"+'select'+"'"
            for self.i in self.v4:
                if (self.i!=''):
                    self.om3=self.om3+','+"'"+str(self.i)+"'"+' '
            self.om3=self.om3+')\n'
            self.omv=self.omv+str(self.tab)+str(self.slf)+'opmenu'+self.keretszam+str(self.omszam)+'.grid(row=1, column=3, sticky=W)\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.omszam)+'=Label('+str(self.slf)+'frm'+str(self.keretszam)+', text='+"'"+self.l4+"'"+')\n'+str(self.tab)+str(self.slf)+'labl'+self.keretszam+str(self.omszam)+'.grid(row=1, column=2,sticky=W)\n'
        self.osszes=self.kret+self.om1+'\n'+self.om2+'\n'+self.om3+'\n'+self.omv
        return self.osszes

class Radiobox:
    "Radio box generator modul"
    def __init__(self,rc,inputs,frame_name):
        self.frame_name=frame_name
        self.inputs=inputs
        self.chbszam=0
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.kret=''
        self.keretszam=''
        self.v1=removeempty(self.inputs[0]) #field values
        self.v2=removeempty(self.inputs[1])
        self.v3=removeempty(self.inputs[2])
        self.v4=removeempty(self.inputs[3])
        if(len(self.v1)>len(self.v2)): # chbszam the lower (v3 and v4) radio elements starting rows
            self.chbszam=len(self.v1)
        else:
            self.chbszam=len(self.v2)
        self.orient=self.inputs[8] #orientation
        self.chb1=''
        self.chb2=''
        self.tab=getresulttype()[0] #tab for object or empty for function
        self.slf=getresulttype()[1] #self. for object or empty for func.
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.kret=str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'=Frame('+str(self.slf)+self.frame_name+', relief='+"'"+'flat'+"'"+', borderwidth=1)\n'+str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.orient+')\n'
        if(self.v1!=[]):
            self.chb1=self.chb1+str(self.tab)+str(self.slf)+'v1'+self.keretszam+' = IntVar()\n'
            for self.i in range(len(self.v1)):
                self.chb2=self.chb2+str(self.tab)+str(self.slf)+'radiob1'+self.keretszam+str(self.i)+'=ttk.Radiobutton('+str(self.slf)+'frm'+str(self.keretszam)+', text='+"'"+str(self.v1[self.i])+"'"+',variable='+str(self.slf)+'v1'+self.keretszam+', value='+str(self.i+1)+')\n'+str(self.tab)+str(self.slf)+'radiob1'+self.keretszam+str(self.i)+'.grid(row='+str(self.i)+', column=0, sticky=W)\n'
        if(self.v2!=[]):
            self.chb1=self.chb1+str(self.tab)+str(self.slf)+'v2'+self.keretszam+' = IntVar()\n'
            for self.i in range(len(self.v2)):
                self.chb2=self.chb2+str(self.tab)+str(self.slf)+'radiob2'+self.keretszam+str(self.i)+'=ttk.Radiobutton('+str(self.slf)+'frm'+str(self.keretszam)+', text='+"'"+str(self.v2[self.i])+"'"+',variable='+str(self.slf)+'v2'+self.keretszam+', value='+str(self.i+1)+')\n'+str(self.tab)+str(self.slf)+'radiob2'+self.keretszam+str(self.i)+'.grid(row='+str(self.i)+', column=1, sticky=W)\n'
        if(self.v3!=[]):
            self.chb1=self.chb1+str(self.tab)+str(self.slf)+'v3'+self.keretszam+' = IntVar()\n'
            for self.i in range(len(self.v3)):
                self.chb2=self.chb2+str(self.tab)+str(self.slf)+'radiob3'+self.keretszam+str(self.i)+'=ttk.Radiobutton('+str(self.slf)+'frm'+str(self.keretszam)+', text='+"'"+str(self.v3[self.i])+"'"+',variable='+str(self.slf)+'v3'+self.keretszam+', value='+str(self.i+1)+')\n'+str(self.tab)+str(self.slf)+'radiob3'+self.keretszam+str(self.i)+'.grid(row='+str(self.i+self.chbszam)+', column=0, sticky=W)\n'
        if(self.v4!=[]):
            self.chb1=self.chb1+str(self.tab)+str(self.slf)+'v4'+self.keretszam+' = IntVar()\n'
            for self.i in range(len(self.v4)):
                self.chb2=self.chb2+str(self.tab)+str(self.slf)+'radiob4'+self.keretszam+str(self.i)+'=ttk.Radiobutton('+str(self.slf)+'frm'+str(self.keretszam)+', text='+"'"+str(self.v4[self.i])+"'"+',variable='+str(self.slf)+'v4'+self.keretszam+', value='+str(self.i+1)+')\n'+str(self.tab)+str(self.slf)+'radiob4'+self.keretszam+str(self.i)+'.grid(row='+str(self.i+self.chbszam)+', column=1, sticky=W)\n'
        self.osszes=self.kret+self.chb1+self.chb2
        return self.osszes


class Listboxgen:
    "Listbox generator modul"
    def __init__(self,rc,inputlist,frame_name):
        self.frame_name=frame_name
        self.inputlist=inputlist
        self.chbszam=0
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.kret=''
        self.keretszam=''
        self.listitems=inputlist[0] # list items in list
        self.orient=inputlist[1] #orient.
        self.w=inputlist[2]
        self.lbx1=''
        self.tab=getresulttype()[0] #tab for object or empty for function
        self.slf=getresulttype()[1] #self. for object or empty for func.
    def proc(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.kret=str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'=Frame('+str(self.slf)+str(self.frame_name)+', relief='+"'flat'"+', borderwidth=1)\n'+str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.orient+')\n'
        self.lbx1=self.lbx1+str(self.tab)+str(self.slf)+'lbx'+self.keretszam+'= Listbox('+str(self.slf)+'frm'+str(self.keretszam)+', width='+str(self.w)+')\n'
        for self.i in range(len(self.listitems)):
            if (self.listitems[self.i]!=''):
                self.lbx1=self.lbx1+str(self.tab)+str(self.slf)+'lbx'+self.keretszam+'.insert('+str(self.i)+','+"'"+str(self.listitems[self.i])+"'"+')\n'
        self.lbx1=self.lbx1+str(self.tab)+str(self.slf)+'lbx'+self.keretszam+'.grid(row=0, column=0, sticky=N)\n'
        self.osszes=self.kret+self.lbx1
        return self.osszes

class Spinboxgen:
    "SpinBox generator modul"
    def __init__(self,rc,inputlist,frame_name):
        self.frame_name=frame_name
        self.inputlist=inputlist
        self.items=inputlist[0]   # list items
        self.orient=inputlist[1]  #orien
        self.w=inputlist[2]       #width
        self.wrp=inputlist[3]     #wrap
        self.from_=inputlist[4]   #from
        self.to_=inputlist[5]     #to
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.kret=''
        self.keretszam=''
        self.sbx1=''
        self.tab=getresulttype()[0] #tab for object or empty for function
        self.slf=getresulttype()[1] #self. for object or empty for func.
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.kret=str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'=Frame('+str(self.slf)+str(self.frame_name)+', relief='+"'flat'"+', borderwidth=1)\n'+str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.orient+')\n'
        self.sbx1=self.sbx1+str(self.tab)+str(self.slf)+'spb'+self.keretszam+'=Spinbox('+str(self.slf)+'frm'+str(self.keretszam)+', width='+str(self.w)+', from_='+str(self.from_)+', to='+str(self.to_)+', wrap='+str(self.wrp)+', values='+str(self.items)+')\n'      
        self.sbx1=self.sbx1+str(self.tab)+str(self.slf)+'spb'+self.keretszam+'.grid(row=0, column=0, sticky=N)'
        self.osszes=self.kret+self.sbx1
        return self.osszes

class Scalegen:
    "Scale generator modul"
    def __init__(self,rc,inputlist,frame_name):
        self.frame_name=frame_name
        self.inputlist=inputlist
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.kret=''
        self.keretszam=''
        self.from_=inputlist[0] #from
        self.to_=inputlist[1] #to
        self.res=inputlist[2] #resolution
        self.l=inputlist[3] #length
        self.w=inputlist[4] #scale width
        self.thick=inputlist[5] #thick
        self.title=inputlist[6] #title
        self.set=inputlist[7] #set value
        self.orient=inputlist[8] #widget orien
        self.sc_ori=inputlist[9] #scale orien
        self.sc1=''
        self.tab=getresulttype()[0] #tab for object or empty for function
        self.slf=getresulttype()[1] #self. for object or empty for func.
    def generator(self):
        if (self.inputlist[10]=='on'):
            self.sv='1' #show value on
        else:
            self.sv='0' #show value off
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.kret=str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'=Frame('+str(self.slf)+str(self.frame_name)+', relief='+"'flat'"+', borderwidth=1)\n'+str(self.tab)+str(self.slf)+'frm'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.orient+')\n'
        self.sc1=self.sc1+str(self.tab)+str(self.slf)+'scal'+str(self.keretszam)+'=Scale('+str(self.slf)+'frm'+str(self.keretszam)+', label='+"'"+self.title+"'"+', from_='+self.from_+', to='+self.to_+', tickinterval='+self.thick+', length='+self.l+', width='+self.w+', resolution='+self.res+', orient='+self.sc_ori+', showvalue='+self.sv+')\n'
        self.sc1=self.sc1+str(self.tab)+str(self.slf)+'scal'+str(self.keretszam)+'.grid(row=0, column=0, sticky=N)\n'
        self.sc1=self.sc1+str(self.tab)+str(self.slf)+'scal'+str(self.keretszam)+'.set('+str(self.set)+')'
        self.osszes=self.kret+self.sc1
        return self.osszes


class Progressgen:
    "Progressbar generator modul"
    def __init__(self,rc,inputlist,frame_name):
        self.frame_name=frame_name
        self.inputlist=inputlist
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.kret=''
        self.keretszam=''
        self.max=inputlist[0] #maximum
        self.v=inputlist[1] #value
        self.l=inputlist[2] #length
        self.orient=inputlist[3] #widget orient.
        self.pb_ori=inputlist[4] #pbar orient.
        self.mod=inputlist[5] #mode
        self.pb1=''
        self.tab=getresulttype()[0] #tab for object or empty for function
        self.slf=getresulttype()[1] #self. for object or empty for func.
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.pb1=self.pb1+str(self.tab)+str(self.slf)+'prgress'+str(self.keretszam)+'=ttk.Progressbar('+str(self.slf)+str(self.frame_name)+', orient='+str(self.pb_ori)+', length='+str(self.l)+', maximum='+str(self.max)+', mode='+"'"+str(self.mod)+"'"+', value='+str(self.v)+')\n'
        self.pb1=self.pb1+str(self.tab)+str(self.slf)+'prgress'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.orient+')\n'
        self.osszes=self.pb1
        return self.osszes

class Nbookgen:
    "Progressbar generator modul"
    def __init__(self,rc,inputlist):
        self.nbframe=''
        self.rc=rc
        self.inputlist=inputlist
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.kret=''
        self.keretszam=''
        self.orient=inputlist[0] #widget orient.
        self.count=int(inputlist[1]) #tab counter
        self.nb1=''
        self.nb2=''
        self.nv=''
        self.tab=getresulttype()[0] #tab for object or empty for function
        self.slf=getresulttype()[1] #self. for object or empty for func.
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.nb1=self.nb1+str(self.tab)+str(self.slf)+'nb'+str(self.keretszam)+'=ttk.Notebook('+str(self.slf)+'ablak)\n'+str(self.tab)+str(self.slf)+'nb'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.orient+')\n'
        for self.i in range(self.count):
            self.nbframe='f'+str(self.i)
            univablak(self.rc,self.nbframe)
            self.nb2=self.nb2+str(self.tab)+str(self.slf)+'f'+str(self.i)+'=Frame('+str(self.slf)+'nb'+str(self.keretszam)+')\n'
            self.nb2=self.nb2+str(self.tab)+str(self.slf)+'nb'+str(self.keretszam)+'.add('+str(self.slf)+'f'+str(self.i)+',text='+"'tab"+str(self.i)+"'"+')\n'
        self.nv=self.nv+str(self.tab)+str(self.slf)+'nb'+str(self.keretszam)+'.select('+str(self.slf)+'f0)\n'
        self.nv=self.nv+str(self.tab)+str(self.slf)+'nb'+str(self.keretszam)+'.enable_traversal()'
        self.osszes=self.nb1+self.nb2+self.nv
        return self.osszes
    
        
#---- Option windows
# menubar/menubutton windows    
def menbarablak(rc,frame_name='ablak'):
    global window_counter
    window_counter=window_counter+1
    tipus=rc[6] #1: menubar 5: menubutton
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    name=selection[rc[6]][3:]
    def mb_ertek():
        global window_counter
        field1=(text11aa0.get(0.0,END).split('\n'))
        field2=(text12aa0.get(0.0,END).split('\n'))
        field3=(text13aa0.get(0.0,END).split('\n'))
        field4=(text14aa0.get(0.0,END).split('\n'))
        labo=chboxaa0.get()
        output=[field1,field2,field3,field4,labo]
        if(tipus==1):
            mbar=Menbar(rc,output,frame_name)
            osszes=mbar.proc()
            kiir('#-'+str(m)+'----Menubar: c'+str(c)+', r'+str(r)+'----')
            kiir(osszes)
            abl2.destroy()
            window_counter=window_counter-1
            msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget code generated')
            check_state()
        if(tipus==5):
            mbutt=Menuk(rc,output,frame_name)
            osszes=mbutt.proc()
            kiir('#-'+str(m)+'----Menubutton: c'+str(c)+', r'+str(r)+'----')
            kiir(osszes)
            abl2.destroy()
            window_counter=window_counter-1
            msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget code generated')
            check_state()
    def on_exit():
        global window_counter
        cellak[rc[8]].current(0)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget closed')
        check_state()
    abl2=Toplevel(abl1)
    if(tipus==1):
        abl2.title('Menubar options: c'+str(c)+', r'+str(r)+'   ('+str(m)+')')
    else:
        abl2.title('Menubutton options: c'+str(c)+', r'+str(r)+'   ('+str(m)+')')
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    kretaa=Frame(ablak, relief='flat', borderwidth=1)
    kretaa.grid(row=4, column=0, columnspan=1, rowspan=1, sticky=N)
    if(tipus==1):
        chboxaa0=Combobox(kretaa, width=4, state=DISABLED)
    else:
        chboxaa0=Combobox(kretaa, width=4, state=NORMAL)
    chboxaa0['values']=orient_values
    chboxaa0.current(0)
    chboxaa0.grid(row=0, column=1,sticky=N)
    cmkeaa0=Label(kretaa, text='')
    cmkeaa0.grid(row=0, column=0,sticky=N)
    cmke10aa0=Label(ablak, text='Mainmenu (1st row) ->')
    cmke10aa0.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
    cmkei=Label(ablak, text='hint', foreground='black', background='orange')
    cmkei.grid(row=5, column=1,sticky=W)
    if(tipus==1):
        cmke20aa0=Label(ablak, text='Submenus ->{\nseparate:  -\ncheckbox: #')
        CreateToolTip(cmkei, text=menubar_tip)
    else:
        cmke20aa0=Label(ablak, text='Submenus ->{')
        CreateToolTip(cmkei, text=menubutton_tip)
    cmke20aa0.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=E)
    cmke30aa0=Label(ablak, text='orient.')
    cmke30aa0.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=S)
    gmb50aa0=Button(ablak,text='Apply',command=mb_ertek)
    gmb50aa0.grid(row=5, column=0, columnspan=1, rowspan=1, sticky=S)
    kret14aa=Frame(ablak, relief='flat', borderwidth=1)
    kret14aa.grid(row=1, column=4, columnspan=1, rowspan=4, sticky=N)
    text14aa0=Text(kret14aa,height=10,width=10,bg='light yellow',fg='black')
    scrolly14aa0=Scrollbar(kret14aa, orient=VERTICAL,command=text14aa0.yview)
    text14aa0['yscrollcommand']=scrolly14aa0.set
    text14aa0.grid(row=0, column=0,sticky=N)
    scrolly14aa0.grid(row=0, column=1 ,sticky=N+S)
    kret11aa=Frame(ablak, relief='flat', borderwidth=1)
    kret11aa.grid(row=1, column=1, columnspan=1, rowspan=4, sticky=N)
    text11aa0=Text(kret11aa,height=10,width=10,bg='light yellow',fg='black')
    scrolly11aa0=Scrollbar(kret11aa, orient=VERTICAL,command=text11aa0.yview)
    text11aa0['yscrollcommand']=scrolly11aa0.set
    text11aa0.grid(row=0, column=0,sticky=N)
    text11aa0.insert(INSERT,'File\nOpen')
    scrolly11aa0.grid(row=0, column=1 ,sticky=N+S)
    kret12aa=Frame(ablak, relief='flat', borderwidth=1)
    kret12aa.grid(row=1, column=2, columnspan=1, rowspan=4, sticky=N)
    text12aa0=Text(kret12aa,height=10,width=10,bg='light yellow',fg='black')
    scrolly12aa0=Scrollbar(kret12aa, orient=VERTICAL,command=text12aa0.yview)
    text12aa0['yscrollcommand']=scrolly12aa0.set
    text12aa0.grid(row=0, column=0,sticky=N)
    text12aa0.insert(INSERT,'Settings')
    scrolly12aa0.grid(row=0, column=1 ,sticky=N+S)
    kret13aa=Frame(ablak, relief='flat', borderwidth=1)
    kret13aa.grid(row=1, column=3, columnspan=1, rowspan=4, sticky=N)
    text13aa0=Text(kret13aa,height=10,width=10,bg='light yellow',fg='black')
    scrolly13aa0=Scrollbar(kret13aa, orient=VERTICAL,command=text13aa0.yview)
    text13aa0['yscrollcommand']=scrolly13aa0.set
    text13aa0.grid(row=0, column=0,sticky=N)
    scrolly13aa0.grid(row=0, column=1 ,sticky=N+S)
    abl2.protocol('WM_DELETE_WINDOW', on_exit)


def menuablak(rc,frame_name='ablak'):
    menbarablak(rc,frame_name)

def listboxablak(rc,frame_name='ablak'):
    global window_counter
    window_counter=window_counter+1
    tipus=rc[6]
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    name=selection[rc[6]][3:]
    def mb_ertek():
        global window_counter
        field1=(text11aa0.get(0.0,END).split('\n'))
        labo=chboxaa0.get()
        w=lbmezo1.get()
        output=[field1,labo,w]
        mlb=Listboxgen(rc,output,frame_name)
        osszes=mlb.proc()
        kiir('#-'+str(m)+'----Listbox: c'+str(c)+', r'+str(r)+'----')
        kiir(osszes)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget code generated')
        check_state()
    def on_exit():
        global window_counter
        cellak[rc[8]].current(0)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget closed')
        check_state()
    abl2=Toplevel(abl1, width=300)
    abl2.title('c'+str(c)+', r'+str(r)+' ('+str(m)+') Listbox options')
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    kretaa=Frame(ablak, relief='flat', borderwidth=1)
    kretaa.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=N)
    chboxaa0=Combobox(kretaa, width=4, state=NORMAL)
    chboxaa0['values']=orient_values
    chboxaa0.current(0)
    chboxaa0.grid(row=2, column=0,sticky=N)
    lbmezo1=Entry(kretaa, width=6)
    lbmezo1.grid(row=4, column=0,sticky=N)
    lbmezo1.insert(0,'14')
    cmkeaa0=Label(kretaa, text='width')
    cmkeaa0.grid(row=3, column=0,sticky=N)
    cmke10aa0=Label(ablak, text='List ->')
    cmke10aa0.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
    cmke30aa0=Label(kretaa, text='orient.')
    cmke30aa0.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=S)
    gmb50aa0=Button(ablak,text='Apply',command=mb_ertek)
    gmb50aa0.grid(row=4, column=0, columnspan=1, rowspan=1, sticky=S)
    kret11aa=Frame(ablak, relief='flat', borderwidth=1)
    kret11aa.grid(row=1, column=1, columnspan=1, rowspan=4, sticky=N)
    text11aa0=Text(kret11aa,height=10,width=20,bg='light yellow',fg='black')
    scrolly11aa0=Scrollbar(kret11aa, orient=VERTICAL,command=text11aa0.yview)
    text11aa0['yscrollcommand']=scrolly11aa0.set
    text11aa0.grid(row=0, column=0,sticky=N)
    text11aa0.insert(INSERT,'List element1\nList element2')
    scrolly11aa0.grid(row=0, column=1 ,sticky=N+S)
    cmkei=Label(kretaa, text='hint', foreground='black', background='orange')
    cmkei.grid(row=5, column=0,sticky=S)
    CreateToolTip(cmkei, text=listbox_tip)
    abl2.protocol('WM_DELETE_WINDOW', on_exit)
    

def gombablak(rc,frame_name='ablak'):
    global window_counter
    window_counter=window_counter+1
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    rspan=rc[2]
    cspan=rc[3]
    name=selection[rc[6]][3:]
    def g_ertek():
        global window_counter
        output=['','','', #button1, 2 ,3
                '','','', #button4, 5 ,6
                '','','', #button7, 8 ,9
                '','','', #button10, 11 ,12
                '']       #orientation
        output[0],output[1],output[2]=bmezof1.get(),bmezof2.get(),bmezof3.get()
        output[3],output[4],output[5]=bmezof1_1.get(),bmezof2_1.get(),bmezof3_1.get()
        output[6],output[7],output[8]=bmezof1_2.get(),bmezof2_2.get(),bmezof3_2.get()
        output[9],output[10],output[11]=bmezof1_3.get(),bmezof2_3.get(),bmezof3_3.get()        
        output[12]=chbox1g.get()
        gombokx=Gombokx(rc,output,frame_name)
        osszes=gombokx.generator()
        kiir('#-'+str(m)+'----Button: c'+str(c)+', r'+str(r)+'------')
        kiir(osszes)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget code generated')
        check_state()
    def on_exit():
        global window_counter
        cellak[rc[8]].current(0)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget closed')
        check_state()
    abl2=Toplevel(abl1)
    abl2.title('Button options: c'+str(c)+', r'+str(r)+'   ('+str(m)+')')
    gmb=Button(abl2,text='Apply',command=g_ertek)
    cmke1=Label(abl2, text='Label:')
    bmezof1=Entry(abl2)
    bmezof1.insert(0,"Ok")
    bmezof2=Entry(abl2)
    bmezof3=Entry(abl2)
    bmezof1_1=Entry(abl2)
    bmezof2_1=Entry(abl2)
    bmezof3_1=Entry(abl2)
    bmezof1_2=Entry(abl2)
    bmezof2_2=Entry(abl2)
    bmezof3_2=Entry(abl2)
    bmezof1_3=Entry(abl2)
    bmezof2_3=Entry(abl2)
    bmezof3_3=Entry(abl2)
    cmke1.grid(row=0, column=0)
    bmezof1.grid(row=0, column=1)
    bmezof2.grid(row=0, column=2)
    bmezof3.grid(row=0, column=3)
    bmezof1_1.grid(row=1, column=1)
    bmezof2_1.grid(row=1, column=2)
    bmezof3_1.grid(row=1, column=3)
    bmezof1_2.grid(row=2, column=1)
    bmezof2_2.grid(row=2, column=2)
    bmezof3_2.grid(row=2, column=3)
    bmezof1_3.grid(row=3, column=1)
    bmezof2_3.grid(row=3, column=2)
    bmezof3_3.grid(row=3, column=3)
    gmb.grid(row=3,column=0)
    chbox1g=Combobox(abl2, width=4)
    chbox1g['values']=orient_values
    chbox1g.current(0)
    chbox1g.grid(row=2, column=0,sticky=S)
    cmkei=Label(abl2, text='hint', foreground='black', background='orange')
    cmkei.grid(row=1, column=0,sticky=N)
    CreateToolTip(cmkei, text=button_tip)
    abl2.protocol('WM_DELETE_WINDOW', on_exit)

def vaszonablak_s(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    vaszon=Vaszon(rc,canvas_defaults,frame_name)
    osszes=vaszon.generator()
    kiir('#-'+str(m)+'----Canvas: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)

def vaszonablak(rc,frame_name='ablak'):
    global window_counter
    window_counter=window_counter+1
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    rspan=rc[2]
    cspan=rc[3]
    name=selection[rc[6]][3:]
    def v_ertek():
        global window_counter
        output=['','','',''] # width, height, color, irány
        try:
            output[0]=int(bmezo1.get())
            output[1]=int(bmezo2.get())
        except:
            print('Számot kell megadni!')
            return
        output[2]=chbox2.get()
        if(output[2]=='pick a color'):
            output[2]=colorset()
        output[3]=chbox1.get()
        vaszon=Vaszon(rc,output,frame_name)
        osszes=vaszon.generator()
        kiir('#-'+str(m)+'----Canvas: c'+str(c)+', r'+str(r)+'------')
        kiir(osszes)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget code generated')
        check_state()
    def on_exit():
        global window_counter
        cellak[rc[8]].current(0)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget closed')
        check_state()
    abl2=Toplevel(abl1)
    abl2.title('Canvas options: c'+str(c)+', r'+str(r)+'   ('+str(m)+')')       
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    chbox1=Combobox(ablak, width=4)
    chbox1['values']=orient_values
    chbox1.current(0)
    chbox1.grid(row=1, column=1,sticky=W)
    bmezo1=Entry(ablak, width=14)
    bmezo1.grid(row=1, column=2,sticky=N)
    bmezo1.insert(0,'200')
    bmezo2=Entry(ablak, width=14)
    bmezo2.grid(row=1, column=3,sticky=N)
    bmezo2.insert(0,'250')
    chbox2=Combobox(ablak)
    chbox2['values']=('white','light yellow','snow','bisque','gray','cyan','sienna1','thistle','pick a color')
    chbox2.current(0)
    chbox2.grid(row=1, column=4,sticky=W)
    kret60=Frame(ablak, relief='flat', borderwidth=1)
    kret60.grid(row=6, column=0, sticky=N)
    gmb0=Button(kret60,text='Apply',command=v_ertek)
    gmb0.grid(row=0, column=0)
    cmke1=Label(ablak, text='orient:')
    cmke1.grid(row=0, column=1,sticky=S)
    cmke2=Label(ablak, text='width:')
    cmke2.grid(row=0, column=2,sticky=S)
    cmke3=Label(ablak, text='height:')
    cmke3.grid(row=0, column=3,sticky=S)
    cmke4=Label(ablak, text='color:')
    cmke4.grid(row=0, column=4,sticky=S)
    cmkei=Label(ablak, text='hint', foreground='black', background='orange')
    cmkei.grid(row=0, column=0,sticky=S)
    CreateToolTip(cmkei, text=canvas_tip)
    abl2.protocol('WM_DELETE_WINDOW', on_exit)

def omenuwindow(rc,frame_name='ablak'):
    comboxwindow(rc,frame_name)

def omenuablak_s(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    name=selection[rc[6]][3:]
    optmenu=Optmenu(rc,optmenu_defaults,frame_name)
    osszes=optmenu.generator()
    kiir('#-'+str(m)+'-----Option menu: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)

def radioxwindow(rc,frame_name='ablak'):
    comboxwindow(rc,frame_name)
 
def radioxablak_s(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    name=selection[rc[6]][3:]
    radiobox=Radiobox(rc,radio_defaults,frame_name)
    osszes=radiobox.generator()
    kiir('#-'+str(m)+'-----Radio: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)

def comboxablak_s(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    combox=Combox(rc,chbox_defaults,frame_name)
    osszes=combox.generator()
    kiir('#-'+str(m)+'----ComboBox: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)

def comboxwindow(rc,frame_name='ablak'):
    global window_counter
    window_counter=window_counter+1
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    rspan=rc[2]
    cspan=rc[3]
    tipus=rc[6] #12:combo, 14: opt, 16: radio
    name=selection[rc[6]][3:]
    def combox_ertek():
        global window_counter
        output=[[],[],[],[],'','','','','',''] # elementlist1,2,3,4, label1,2,3,4, orient, width
        output[0]=(text11.get(0.0,END).split('\n'))
        output[1]=(text12.get(0.0,END).split('\n'))
        output[2]=(text21.get(0.0,END).split('\n'))
        output[3]=(text22.get(0.0,END).split('\n'))
        if(tipus==12 or tipus==14): # if combo or opt.menu
            output[4],output[5],output[6],output[7]=entr11.get(),entr12.get(),entr21.get(),entr22.get() #label texts
        output[8]=chbox1.get() # orient
        if(tipus==12): #if combo
            output[9]=chbox2.get() # width
            if (output[9]=='auto'):
                output[9]=cellaw(output)
            combox=Combox(rc,output,frame_name)
            osszes=combox.generator()
        if(tipus==14): #if opt.menu
            optmenu=Optmenu(rc,output,frame_name)
            osszes=optmenu.generator()
        if(tipus==16): #if radio
            radiobox=Radiobox(rc,output,frame_name)
            osszes=radiobox.generator()
        kiir('#-'+str(m)+'----'+name+': c'+str(c)+', r'+str(r)+'------')
        kiir(osszes) 
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget code generated')
        check_state()
    def on_exit():
        global window_counter
        cellak[rc[8]].current(0)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget closed')
        check_state()    
    abl2=Toplevel(abl1)
    abl2.title(name+' options: c'+str(c)+', r'+str(r)+'   ('+str(m)+')')
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    #-1st------
    frm11=LabelFrame(ablak, text='1st '+name, height=200, width=250, relief='flat', borderwidth=1)
    frm11.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N)
    text11=Text(frm11,height=5,width=12,bg='white',fg='black')
    scrolly11aa0=Scrollbar(frm11, orient=VERTICAL,command=text11.yview)
    text11['yscrollcommand']=scrolly11aa0.set
    text11.grid(row=1, column=1,sticky=N)
    text11.insert(INSERT,'One\nTwo\nThree')
    scrolly11aa0.grid(row=1, column=2 , rowspan=2, sticky=N+S)
    labl1a=Label(frm11, text='Elements:')
    labl1a.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
    if(tipus!=16):
        labl1=Label(frm11, text='title:')
        labl1.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
        entr11=Entry(frm11 ,width='17')
        entr11.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
        entr11.insert(0,'label')
    #-2nd------
    frm12=LabelFrame(ablak, text='2nd '+name, height=200, width=250, relief='flat', borderwidth=1)
    frm12.grid(row=1, column=3, columnspan=1, rowspan=1, sticky=N)
    text12=Text(frm12,height=5,width=12,bg='white',fg='black')
    scrolly12aa0=Scrollbar(frm12, orient=VERTICAL,command=text12.yview)
    text12['yscrollcommand']=scrolly12aa0.set
    text12.grid(row=1, column=1,sticky=N)
    scrolly12aa0.grid(row=1, column=2 , rowspan=2, sticky=N+S)
    labl12a=Label(frm12, text='Elements:')
    labl12a.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
    if(tipus!=16):
        labl12=Label(frm12, text='title:')
        labl12.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
        entr12=Entry(frm12 ,width='17')
        entr12.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
    #-3rd------
    frm21=LabelFrame(ablak, text='3rd '+name, height=200, width=250, relief='flat', borderwidth=1)
    frm21.grid(row=2, column=2, columnspan=1, rowspan=1, sticky=N)
    text21=Text(frm21,height=5,width=12,bg='white',fg='black')
    scrolly21aa0=Scrollbar(frm21, orient=VERTICAL,command=text21.yview)
    text21['yscrollcommand']=scrolly21aa0.set
    text21.grid(row=1, column=1,sticky=N)
    scrolly21aa0.grid(row=1, column=2 , rowspan=2, sticky=N+S)
    labl21a=Label(frm21, text='Elements:')
    labl21a.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
    if(tipus!=16):
        labl21=Label(frm21, text='title:')
        labl21.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
        entr21=Entry(frm21 ,width='17')
        entr21.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
    #-4th------
    frm22=LabelFrame(ablak, text='4th '+name, height=200, width=250, relief='flat', borderwidth=1)
    frm22.grid(row=2, column=3, columnspan=1, rowspan=1, sticky=N, padx=5)
    text22=Text(frm22,height=5,width=12,bg='white',fg='black')
    scrolly22aa0=Scrollbar(frm22, orient=VERTICAL,command=text22.yview)
    text22['yscrollcommand']=scrolly22aa0.set
    text22.grid(row=1, column=1,sticky=N)
    scrolly22aa0.grid(row=1, column=2 , rowspan=2, sticky=N+S)
    labl22a=Label(frm22, text='Elements:')
    labl22a.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
    if(tipus!=16):
        labl22=Label(frm22, text='title:')
        labl22.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
        entr22=Entry(frm22 ,width='17')
        entr22.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
    #-m-
    frm100=Frame(ablak, height=200, width=250, relief='flat', borderwidth=1)
    frm100.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
    labl=Label(frm100, text='orient.:')
    labl.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
    labl0=Label(frm100, text='hint', foreground='black', background='orange')
    labl0.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
    frm1010=Frame(frm100, relief='flat', borderwidth=1)
    frm1010.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=N)
    chbox1=Combobox(frm1010, width=4)
    chbox1['values']=orient_values
    chbox1.current(0)
    chbox1.grid(row=0, column=1,sticky=N)
    labl101=Label(frm1010, text='')
    labl101.grid(row=0, column=0,sticky=N)
    labl011=Label(frm100, text='width:')
    labl011.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=N)
    frm1110=Frame(frm100, relief='flat', borderwidth=1)
    frm1110.grid(row=4, column=0, columnspan=1, rowspan=1, sticky=N)
    chbox2=Combobox(frm1110, width=4)
    chbox2['values']=('auto','4','6','10','12','14','')
    chbox2.current(0)
    chbox2.grid(row=0, column=1,sticky=N)
    if(tipus!=12):
        chbox2.configure(state=DISABLED)
    labl111=Label(frm1110, text='')
    labl111.grid(row=0, column=0,sticky=N)
    btn=Button(ablak,text='Apply',command=combox_ertek)
    btn.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=S)
    CreateToolTip(labl0, text=combox_tip)
    abl2.protocol('WM_DELETE_WINDOW', on_exit)

def szovegmezablak_s(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    szovegmezo=Szovegmezocs(rc,text_defaults,frame_name)
    osszes=szovegmezo.generator()
    kiir('#-'+str(m)+'----Text: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)
    
def szovegmezablak(rc,frame_name='ablak'):
    global window_counter
    window_counter=window_counter+1
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    rspan=rc[2]
    cspan=rc[3]
    name=selection[rc[6]][3:]
    def t_ertek():
       global window_counter
       output=['','','','','','',''] # w,h,orient,slide,def.text,bg.color, text.color
       try:
           output[0]=int(bmezo3.get())
           output[1]=int(bmezo4.get())
       except:
           print('Enter numbers only!')
           return
       output[2]=chbox3.get() #orient.
       output[3]=chbox4.get() #slide
       output[4]=bmezo0.get() #default text
       output[5]=chbox5.get()
       if(output[5]=='pick a color'):
           output[5]=colorset()
       output[6]=chbox6.get()
       if(output[6]=='pick a color'):
           output[6]=colorset()
       szovegmezo=Szovegmezocs(rc,output,frame_name)
       osszes=szovegmezo.generator()
       kiir('#-'+str(m)+'----Text: c'+str(c)+', r'+str(r)+'------')
       kiir(osszes) 
       abl2.destroy()
       window_counter=window_counter-1
       msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget code generated')
       check_state()
    def on_exit():
        global window_counter
        cellak[rc[8]].current(0)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget closed')
        check_state()
    abl2=Toplevel(abl1)
    abl2.title('Text options: c'+str(c)+', r'+str(r)+'   ('+str(m)+')')        
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    bmezo0=Entry(ablak)
    bmezo0.grid(row=1, column=1,columnspan=4,sticky=E+W)
    chbox3=Combobox(ablak, width=4)
    chbox3['values']=orient_values
    chbox3.current(0)
    chbox3.grid(row=3, column=1,sticky=E)
    bmezo3=Entry(ablak, width=14)
    bmezo3.grid(row=3, column=2,sticky=N)
    bmezo3.insert(0,'10')
    bmezo4=Entry(ablak, width=14)
    bmezo4.grid(row=3, column=3,sticky=N)
    bmezo4.insert(0,'10')
    chbox4=Combobox(ablak)
    chbox4['values']=('1: w/o scroll','2: w vertical scroll','3: w horizontal scroll','4: with v/h scroll')
    chbox4.current(0)
    chbox4.grid(row=3, column=4,sticky=W)
    chbox5=Combobox(ablak, width=11)
    chbox5['values']=('white','light yellow','snow','bisque','gray','cyan','sienna1','thistle','pick a color')
    chbox5.current(0)
    chbox5.grid(row=5, column=3,sticky=W)
    chbox6=Combobox(ablak)
    chbox6['values']=('black','gray','cyan','thistle','pick a color')
    chbox6.current(0)
    chbox6.grid(row=5, column=4,sticky=W)
    kret60=Frame(ablak, relief='flat', borderwidth=1)
    kret60.grid(row=5, column=0, sticky=N)
    gmb0=Button(kret60,text='Apply',command=t_ertek)
    gmb0.grid(row=0, column=0)
    cmke0=Label(ablak, text='default text')
    cmke0.grid(row=0, column=1,sticky=S)
    cmke2=Label(ablak, text='orient:')
    cmke2.grid(row=2, column=1,sticky=E)
    cmke2=Label(ablak, text='width:')
    cmke2.grid(row=2, column=2,sticky=S)
    cmke2=Label(ablak, text='height:')
    cmke2.grid(row=2, column=3,sticky=S)
    cmke2=Label(ablak, text='scrollbar')
    cmke2.grid(row=2, column=4,sticky=S)
    cmke3=Label(ablak, text='bg color:')
    cmke3.grid(row=4, column=3, sticky=S)
    cmke4=Label(ablak, text='text color:')
    cmke4.grid(row=4, column=4, sticky=S)
    cmkei=Label(ablak, text='hint', foreground='black', background='orange')
    cmkei.grid(row=4, column=0,sticky=S)
    CreateToolTip(cmkei, text=text_tip)
    abl2.protocol('WM_DELETE_WINDOW', on_exit)


def beviteliablak(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
#    entry_defaults=['N','17',''] # orient, width, text
    beviteli=Beviteli(rc,entry_defaults,frame_name)
    osszes=beviteli.generator()
    kiir('#-'+str(m)+'----Entry: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)


def cimkeablak(rc,frame_name='ablak'):
    global window_counter
    window_counter=window_counter+1
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    name=selection[rc[6]][3:]
    def c_ertek():
        global window_counter
        output=['',''] #title, orient
        output[0]=bmezo0.get() #title
        output[1]=chbox0.get() #orient
        cimke=Cimke(rc,output,frame_name)
        osszes=cimke.generator()
        kiir('#-'+str(m)+'----Label: c'+str(c)+', r'+str(r)+'------')
        kiir(osszes)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget code generated')
        check_state()
    def on_exit():
        global window_counter
        cellak[rc[8]].current(0)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget closed')
        check_state()
    abl2=Toplevel(abl1)
    abl2.title('Label options: c'+str(c)+', r'+str(r)+'   ('+str(m)+')')        
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    cmke0=Label(ablak, text='Text')
    cmke0.grid(row=0, column=1,sticky=S)
    cmke1=Label(ablak, text='Orientation')
    cmke1.grid(row=0, column=2,sticky=S)
    bmezo0=Entry(ablak)
    bmezo0.grid(row=1, column=1,sticky=E)
    bmezo0.insert(0, "Label")
    chbox0=Combobox(ablak, width=4)
    chbox0['values']=orient_values
    chbox0.current(0)
    chbox0.grid(row=1, column=2, sticky=EW)
    gmb0=Button(ablak,text='Apply',command=c_ertek)
    gmb0.grid(row=1, column=0, sticky=S)
    cmkei=Label(ablak, text='hint', foreground='black', background='orange')
    cmkei.grid(row=0, column=0,sticky=S)
    CreateToolTip(cmkei, text=label_tip)
    abl2.protocol('WM_DELETE_WINDOW', on_exit)
 
def cimkeablak_s(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
#    defaults=['title','N']
    cimke=Cimke(rc,label_defaults,frame_name)
    osszes=cimke.generator()
    kiir('#-'+str(m)+'----Label: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)

def keretablak(rc,output,nbframe): #col-row, orientation
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    keret=Keret(rc,output,nbframe)
    osszes,keretszam=keret.generator()
    if (nbframe=='ablak'):
        kiir('#-'+str(m)+'----Univ.Frame: c'+str(c)+', r'+str(r)+'------')
    else:
        kiir('#-'+str(m)+'----Notebook: (tab'+str(nbframe)[1:]+') c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)
    return keretszam

def uzenablak(rc):
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    uzi=Uzenet(rc)
    osszes=uzi.generator()
    kiir('#-'+str(m)+'----Message: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)

def scaleablak(rc,frame_name='ablak'):
    global window_counter
    window_counter=window_counter+1
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    name=selection[rc[6]][3:]
    def sc_ertek():
        global window_counter
        output=['','','','','','','','','','',''] 
        output[0]=bmezo12.get() #from
        output[1]=bmezo13.get() #to
        output[2]=bmezo10.get() #resolution
        output[3]=bmezo31.get() #length
        output[4]=bmezo32.get() #scale width
        output[5]=bmezo33.get() #thick
        output[6]=bmezo11.get() #title
        output[7]=bmezo34.get() #set value
        output[8]=chbox51aa0.get() #widget orien
        output[9]=chbox52aa0.get() #scale orien
        output[10]=chbox53aa0.get() #show value
        sc=Scalegen(rc,output,frame_name)
        osszes=sc.generator()
        kiir('#-'+str(m)+'----Scale: c'+str(c)+', r'+str(r)+'------')
        kiir(osszes)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget code generated')
        check_state()
    def on_exit():
        global window_counter
        cellak[rc[8]].current(0)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget closed')
        check_state()
    abl2=Toplevel(abl1)
    abl2.title('Scale options: c'+str(c)+', r'+str(r)+'   ('+str(m)+')')
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    bmezo11=Entry(ablak)
    bmezo11.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N)
    bmezo11.insert(0,'title')
    bmezo12=Entry(ablak)
    bmezo12.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N)
    bmezo12.insert(0,'0')
    bmezo13=Entry(ablak)
    bmezo13.grid(row=1, column=3, columnspan=1, rowspan=1, sticky=N)
    bmezo13.insert(0,'100')
    bmezo10=Entry(ablak)
    bmezo10.grid(row=1, column=4, columnspan=1, rowspan=1, sticky=N)
    bmezo10.insert(0,'10')
    bmezo31=Entry(ablak)
    bmezo31.grid(row=3, column=1, columnspan=1, rowspan=1, sticky=N)
    bmezo31.insert(0,'150')
    bmezo32=Entry(ablak)
    bmezo32.grid(row=3, column=2, columnspan=1, rowspan=1, sticky=N)
    bmezo32.insert(0,'15')
    bmezo33=Entry(ablak)
    bmezo33.grid(row=3, column=3, columnspan=1, rowspan=1, sticky=N)
    bmezo33.insert(0,'50')
    bmezo34=Entry(ablak)
    bmezo34.grid(row=3, column=4, columnspan=1, rowspan=1, sticky=N)
    bmezo34.insert(0,'0')
    kret51aa=Frame(ablak, relief='flat', borderwidth=1)
    kret51aa.grid(row=5, column=1, columnspan=1, rowspan=1, sticky=N)
    chbox51aa0=Combobox(kret51aa, width=4)
    chbox51aa0['values']=orient_values
    chbox51aa0.current(0)
    chbox51aa0.grid(row=0, column=1,sticky=N)
    cmke51aa0=Label(kret51aa, text='')
    cmke51aa0.grid(row=0, column=0,sticky=N)
    kret52aa=Frame(ablak, relief='flat', borderwidth=1)
    kret52aa.grid(row=5, column=2, columnspan=1, rowspan=1, sticky=N)
    chbox52aa0=Combobox(kret52aa, width=12)
    chbox52aa0['values']=('HORIZONTAL', 'VERTICAL')
    chbox52aa0.current(0)
    chbox52aa0.grid(row=0, column=1,sticky=N)
    kret53aa=Frame(ablak, relief='flat', borderwidth=1)
    kret53aa.grid(row=5, column=3, columnspan=1, rowspan=1, sticky=N)
    chbox53aa0=Combobox(kret53aa, width=4)
    chbox53aa0['values']=('on', 'off')
    chbox53aa0.current(0)
    chbox53aa0.grid(row=0, column=1,sticky=N)
    cmke01aa0=Label(ablak, text='from:')
    cmke01aa0.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=W)
    cmke02aa0=Label(ablak, text='to:')
    cmke02aa0.grid(row=0, column=3, columnspan=1, rowspan=1, sticky=W)
    cmke03aa0=Label(ablak, text='resolution:')
    cmke03aa0.grid(row=0, column=4, columnspan=1, rowspan=1, sticky=W)
    cmke21aa0=Label(ablak, text='scale length:')
    cmke21aa0.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=W)
    cmke22aa0=Label(ablak, text='scale width:')
    cmke22aa0.grid(row=2, column=2, columnspan=1, rowspan=1, sticky=W)
    cmke23aa0=Label(ablak, text='tickinterval:')
    cmke23aa0.grid(row=2, column=3, columnspan=1, rowspan=1, sticky=W)
    cmke44aa0=Label(ablak, text='set value:')
    cmke44aa0.grid(row=2, column=4, columnspan=1, rowspan=1, sticky=W)
    cmke41aa0=Label(ablak, text='widget oriantation:')
    cmke41aa0.grid(row=4, column=1, columnspan=1, rowspan=1, sticky=N)
    cmke42aa0=Label(ablak, text='scale orientation:')
    cmke42aa0.grid(row=4, column=2, columnspan=1, rowspan=1, sticky=N)
    cmke43aa0=Label(ablak, text='show value on scale:')
    cmke43aa0.grid(row=4, column=3, columnspan=1, rowspan=1, sticky=N)
    gmb50aa0=Button(ablak,text='Apply',command=sc_ertek)
    gmb50aa0.grid(row=5, column=0, columnspan=1, rowspan=1, sticky=N)
    cmkei=Label(ablak, text='hint', foreground='black', background='orange')
    cmkei.grid(row=0, column=0,sticky=S)
    CreateToolTip(cmkei, text=scale_tip)
    abl2.protocol('WM_DELETE_WINDOW', on_exit)

def progressablak(rc,frame_name='ablak'):
    global window_counter
    window_counter=window_counter+1
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    name=selection[rc[6]][3:]
    def sc_ertek():
        global window_counter
        output=['','','','','',''] 
        output[0]=bmezo12.get() #maximum
        output[1]=bmezo13.get() #value
        output[2]=bmezo11.get() #length
        output[3]=chbox51aa0.get() #widget orien
        output[4]=chbox52aa0.get() #pbar orien
        output[5]=chbox53aa0.get() #mode
        prg=Progressgen(rc,output,frame_name)
        osszes=prg.generator()
        kiir('#-'+str(m)+'----Progressbar: c'+str(c)+', r'+str(r)+'------')
        kiir(osszes)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget code generated')
        check_state()
    def on_exit():
        global window_counter
        cellak[rc[8]].current(0)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget closed')
        check_state()
    abl2=Toplevel(abl1)
    abl2.title('Progressbar options: c'+str(c)+', r'+str(r)+'   ('+str(m)+')')
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    bmezo11=Entry(ablak) #length
    bmezo11.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N)
    bmezo11.insert(0,'100')
    bmezo12=Entry(ablak) #maximum
    bmezo12.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N)
    bmezo12.insert(0,'100')
    bmezo13=Entry(ablak) #to-value
    bmezo13.grid(row=1, column=3, columnspan=1, rowspan=1, sticky=N)
    bmezo13.insert(0,'0')
    kret51aa=Frame(ablak, relief='flat', borderwidth=1)
    kret51aa.grid(row=5, column=1, columnspan=1, rowspan=1, sticky=N)
    chbox51aa0=Combobox(kret51aa, width=4)
    chbox51aa0['values']=orient_values
    chbox51aa0.current(0)
    chbox51aa0.grid(row=0, column=1,sticky=N)
    cmke51aa0=Label(kret51aa, text='')
    cmke51aa0.grid(row=0, column=0,sticky=N)
    kret52aa=Frame(ablak, relief='flat', borderwidth=1)
    kret52aa.grid(row=5, column=2, columnspan=1, rowspan=1, sticky=N)
    chbox52aa0=Combobox(kret52aa, width=12)
    chbox52aa0['values']=('HORIZONTAL', 'VERTICAL')
    chbox52aa0.current(0)
    chbox52aa0.grid(row=0, column=1,sticky=N)
    kret53aa=Frame(ablak, relief='flat', borderwidth=1)
    kret53aa.grid(row=5, column=3, columnspan=1, rowspan=1, sticky=N)
    chbox53aa0=Combobox(kret53aa, width=12)
    chbox53aa0['values']=('determinate', 'indeterminate')
    chbox53aa0.current(0)
    chbox53aa0.grid(row=0, column=1,sticky=N)
    cmke01aa0=Label(ablak, text='maximum:')
    cmke01aa0.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=W)
    cmke02aa0=Label(ablak, text='start value:')
    cmke02aa0.grid(row=0, column=3, columnspan=1, rowspan=1, sticky=W)
    cmke03aa0=Label(ablak, text='length:')
    cmke03aa0.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=W)
    cmke41aa0=Label(ablak, text='widget oriantation:')
    cmke41aa0.grid(row=4, column=1, columnspan=1, rowspan=1, sticky=N)
    cmke42aa0=Label(ablak, text='progressbar orient.:')
    cmke42aa0.grid(row=4, column=2, columnspan=1, rowspan=1, sticky=N)
    cmke43aa0=Label(ablak, text='mode:')
    cmke43aa0.grid(row=4, column=3, columnspan=1, rowspan=1, sticky=N)
    gmb50aa0=Button(ablak,text='Apply',command=sc_ertek)
    gmb50aa0.grid(row=5, column=0, columnspan=1, rowspan=1, sticky=N)
    cmkei=Label(ablak, text='hint', foreground='black', background='orange')
    cmkei.grid(row=0, column=0,sticky=S)
    CreateToolTip(cmkei, text=progress_tip)
    abl2.protocol('WM_DELETE_WINDOW', on_exit)
    
def spinablak(rc,frame_name='ablak'):
    global window_counter
    window_counter=window_counter+1
    tipus=rc[6]
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    name=selection[rc[6]][3:]
    def sp_ertek():
        global window_counter
        output=['','','','','','']
        lista=text11aa0.get(0.0,END).split('\n')
        output[0]=clearlist(lista,1) #list area
        output[1]=chboxaa0.get() #orient
        output[2]=lbmezo1.get() #width
        if(chbox33.get()=='off'): #wrap
            output[3]='0'
        else:
            output[3]='1'
        output[4]=bmezo31.get() #from
        output[5]=bmezo32.get() #to
        spbox=Spinboxgen(rc,output,frame_name)
        osszes=spbox.generator()
        kiir('#-'+str(m)+'----Spinbox: c'+str(c)+', r'+str(r)+'----')
        kiir(osszes)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget code generated')
        check_state()
    def on_exit():
        global window_counter
        cellak[rc[8]].current(0)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget closed')
        check_state()
    abl2=Toplevel(abl1, width=300)
    abl2.title('Spinbox options: c'+str(c)+', r'+str(r)+' ('+str(m)+')')
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    kretaa=Frame(ablak, relief='flat', borderwidth=1)
    kretaa.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
    cmke30aa0=Label(kretaa, text='orient.')
    cmke30aa0.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=S)
    chboxaa0=Combobox(kretaa, width=4, state=NORMAL)
    chboxaa0['values']=orient_values
    chboxaa0.current(0)
    chboxaa0.grid(row=1, column=0,sticky=N)
    lbmezo1=Entry(kretaa, width=6)
    lbmezo1.grid(row=3, column=0,sticky=N)
    lbmezo1.insert(0,'14')
    cmkeaa0=Label(kretaa, text='width')
    cmkeaa0.grid(row=2, column=0,sticky=N)
    cmke10aa0=Label(ablak, text='List ->')
    cmke10aa0.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
    cmke33=Label(kretaa, text='wrap')
    cmke33.grid(row=4, column=0, columnspan=1, rowspan=1, sticky=N)
    chbox33=Combobox(ablak, width=4, state=NORMAL)
    chbox33['values']=('off','on')
    chbox33.current(0)
    chbox33.grid(row=5, column=0,sticky=N)
    gmb50aa0=Button(ablak,text='Apply',command=sp_ertek)
    gmb50aa0.grid(row=6, column=0, columnspan=1, rowspan=1, sticky=S)
    kret11aa=Frame(ablak, relief='flat', borderwidth=1)
    kret11aa.grid(row=0, column=1, columnspan=1, rowspan=7, sticky=N)
    text11aa0=Text(kret11aa,height=10,width=20,bg='light yellow',fg='black')
    scrolly11aa0=Scrollbar(kret11aa, orient=VERTICAL,command=text11aa0.yview)
    text11aa0['yscrollcommand']=scrolly11aa0.set
    text11aa0.grid(row=0, column=0,sticky=N)
    text11aa0.insert(INSERT,'Element1\nElement2\n#comment:\n#if this field is\n#empty, use "'"from"'"\n#and "'"to"'" fields\n#for numbers')
    scrolly11aa0.grid(row=0, column=1 ,sticky=N+S)
    kretab=Frame(ablak, relief='flat', borderwidth=1)
    kretab.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N)
    cmke31=Label(kretab, text='from')
    cmke31.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=S)
    bmezo31=Entry(kretab, width=7)
    bmezo31.grid(row=1, column=0, sticky=N)
    bmezo31.insert(0,'1')
    cmke32=Label(kretab, text='to')
    cmke32.grid(row=2, column=0, sticky=N)
    bmezo32=Entry(kretab, width=7)
    bmezo32.grid(row=3, column=0, sticky=N)
    bmezo32.insert(0,'10')
    cmkei=Label(kretab, text='hint', foreground='black', background='orange')
    cmkei.grid(row=4, column=0, sticky=S)
    CreateToolTip(cmkei, text=spin_tip)
    abl2.protocol('WM_DELETE_WINDOW', on_exit)

def toolbarablak(rc,frame_name='ablak'):
    global window_counter
    window_counter=window_counter+1
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    name=selection[rc[6]][3:]
    v=('---','addressbook','advanced','archive','back','bookmarked','calculator','copy','deletearchive',
       'down','edit','exclamation','folder','forward','help','ichat','info','install','lock',
       'newarchive','newdoc','newmail','notebook','ok','open','pause','picture','play','plus',
       'preferences','refresh','save','search','server','smiley','smileysad','stop')
    def tb_ertek():
        global toolbar_counter, window_counter
        toolbar_counter=1
        output=['','','','','','','','','','',''] 
        output[0]=chbox11aa0.get() #button 1. image name
        output[1]=chbox12aa0.get() #button 2. image name
        output[2]=chbox13aa0.get() #button 3. image name
        output[3]=chbox14aa0.get() #button 4. image name
        output[4]=chbox15aa0.get() #button 5. image name
        output[5]=clearenter(text12aa0.get(0.0,END)) #tooltip text1
        output[6]=clearenter(text13aa0.get(0.0,END)) #tooltip text2
        output[7]=clearenter(text14aa0.get(0.0,END)) #tooltip text3
        output[8]=clearenter(text15aa0.get(0.0,END)) #tooltip text4
        output[9]=clearenter(text11aa0.get(0.0,END)) #tooltip text5
        output[10]=chbox41aa0.get() #tooltip orient.
        tbar=Toolbargen(rc,output,frame_name)
        osszes=tbar.generator()
        kiir('#-'+str(m)+'----Toolbar: c'+str(c)+', r'+str(r)+'------')
        kiir(osszes)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget code generated')
        check_state()
    def on_exit():
        global window_counter
        cellak[rc[8]].current(0)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget closed')
        check_state()
    abl2=Toplevel(abl1, width=300)
    abl2.title('Toolbar options: c'+str(c)+', r'+str(r)+' ('+str(m)+')')        
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    cmke01aa0=Label(ablak, text='1')
    cmke01aa0.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
    cmke02aa0=Label(ablak, text='2')
    cmke02aa0.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=N)
    cmke03aa0=Label(ablak, text='3')
    cmke03aa0.grid(row=0, column=3, columnspan=1, rowspan=1, sticky=N)
    cmke04aa0=Label(ablak, text='4')
    cmke04aa0.grid(row=0, column=4, columnspan=1, rowspan=1, sticky=N)
    cmke04aa0=Label(ablak, text='5')
    cmke04aa0.grid(row=0, column=5, columnspan=1, rowspan=1, sticky=N)
    kret11aa=Frame(ablak, relief='flat', borderwidth=1)
    kret11aa.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N)
    chbox11aa0=Combobox(kret11aa, width=14)
    chbox11aa0['values']=v
    chbox11aa0.current(1)
    chbox11aa0.grid(row=0, column=1,sticky=N)
    cmke11aa0=Label(kret11aa, text='image name:')
    cmke11aa0.grid(row=0, column=0,sticky=N)
    cmke11aa0=Label(kret11aa, text='tooltip text:')
    cmke11aa0.grid(row=2, column=0,sticky=N)
    kret12aa=Frame(ablak, relief='flat', borderwidth=1)
    kret12aa.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N)
    chbox12aa0=Combobox(kret12aa, width=14)
    chbox12aa0['values']=v
    chbox12aa0.current(0)
    chbox12aa0.grid(row=0, column=1,sticky=N)
    kret13aa=Frame(ablak, relief='flat', borderwidth=1)
    kret13aa.grid(row=1, column=3, columnspan=1, rowspan=1, sticky=N)
    chbox13aa0=Combobox(kret13aa, width=14)
    chbox13aa0['values']=v
    chbox13aa0.current(0)
    chbox13aa0.grid(row=0, column=1,sticky=N)
    kret14aa=Frame(ablak, relief='flat', borderwidth=1)
    kret14aa.grid(row=1, column=4, columnspan=1, rowspan=1, sticky=N)
    chbox14aa0=Combobox(kret14aa, width=14)
    chbox14aa0['values']=v
    chbox14aa0.current(0)
    chbox14aa0.grid(row=0, column=1,sticky=N)
    kret15aa=Frame(ablak, relief='flat', borderwidth=1)
    kret15aa.grid(row=1, column=5, columnspan=1, rowspan=1, sticky=N)
    chbox15aa0=Combobox(kret15aa, width=14)
    chbox15aa0['values']=v
    chbox15aa0.current(0)
    chbox15aa0.grid(row=0, column=1,sticky=N)
    text11aa0=Text(kret15aa, width=14, height=3, background='light yellow')
    text11aa0.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=N)
    text12aa0=Text(kret11aa, width=14, height=3, background='light yellow')
    text12aa0.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=N)
    text13aa0=Text(kret12aa, width=14, height=3, background='light yellow')
    text13aa0.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=N)
    text14aa0=Text(kret13aa, width=14, height=3, background='light yellow')
    text14aa0.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=N)
    text15aa0=Text(kret14aa, width=14, height=3, background='light yellow')
    text15aa0.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=N)
    kret41aa=Frame(ablak, relief='flat', borderwidth=1)
    kret41aa.grid(row=4, column=3, columnspan=1, rowspan=1, sticky=W)
    chbox41aa0=Combobox(kret41aa, width=4)
    chbox41aa0['values']=orient_values
    chbox41aa0.current(0)
    chbox41aa0.grid(row=0, column=1,sticky=W)
    cmke41aa0=Label(kret41aa, text='orient.')
    cmke41aa0.grid(row=0, column=0,sticky=N)
    gmb40aa0=Button(ablak,text='Apply',command=tb_ertek)
    gmb40aa0.grid(row=4, column=1, columnspan=1, rowspan=1, sticky=W)
    cmkei=Label(ablak, text='hint', foreground='black', background='orange')
    cmkei.grid(row=4, column=2,sticky=W)
    CreateToolTip(cmkei, text=toolbar_tip)
    abl2.protocol('WM_DELETE_WINDOW', on_exit)


def nbookablak(rc,frame_name='ablak'):
    global window_counter
    window_counter=window_counter+1
    c=rc[0]              
    r=rc[1]
    m=rc[7] #started from main or univ.frame
    name=selection[rc[6]][3:]
    def nb_ertek():
        global window_counter
        output=['','','','','',''] 
        output[0]=chbox51aa0.get() #widget orien
        output[1]=bmezo11.get() #tab nr
        if(int(bmezo11.get())>10):
            output[1]=10
        nbk=Nbookgen(rc,output)
        osszes=nbk.generator()
        kiir('#-'+str(m)+'----Notebook: c'+str(c)+', r'+str(r)+'------')
        kiir(osszes)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: Notebook frame widget(s) opened / code generated')
        check_state()
    def on_exit():
        global window_counter
        cellak[rc[8]].current(0)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(c)+', r'+str(r)+' ('+str(m)+') '+str(name)+' widget closed')
        check_state()
    abl2=Toplevel(abl1, width=250)
    abl2.title('Notebook: c'+str(c)+', r'+str(r)+'   ('+str(m)+')')
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    bmezo11=Entry(ablak, width=3) #length
    bmezo11.grid(row=5, column=5, columnspan=1, rowspan=1, sticky=N)
    bmezo11.insert(0,'2')
    chbox51aa0=Combobox(ablak, width=4)
    chbox51aa0['values']=orient_values
    chbox51aa0.current(0)
    chbox51aa0.grid(row=5, column=3,sticky=N)
    cmke03aa0=Label(ablak, text='Orient.:')
    cmke03aa0.grid(row=5, column=2, columnspan=1, rowspan=1, sticky=NW)
    cmke03aa1=Label(ablak, text='Tab number:\n   (max 10)')
    cmke03aa1.grid(row=5, column=4, columnspan=1, rowspan=1, sticky=W)
    gmb50aa0=Button(ablak,text='Apply',command=nb_ertek)
    gmb50aa0.grid(row=5, column=0, columnspan=1, rowspan=1, sticky=N)
    cmkei=Label(ablak, text='hint', foreground='black', background='orange')
    cmkei.grid(row=4, column=0,sticky=N)
    CreateToolTip(cmkei, text=notebook_tip)
    abl2.protocol('WM_DELETE_WINDOW', on_exit)
    

def univablak(rc,nbframe='ablak'):
    global window_counter
    window_counter=window_counter+1
    name=selection[rc[6]][3:]
    def uni_ertek():
        global window_counter
        output=['',''] # orientation, frameText
        output[0]=chbox200.get() #orientaion
        output[1]=bmezo.get()    #frame text
        kivalaszto_uni(rc,cells_uni,output,nbframe)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: univ frame widget(s) opened / code generated')
        check_state()
    def on_exit():
        global window_counter
        cellak[rc[8]].current(0)
        abl2.destroy()
        window_counter=window_counter-1
        msg.configure(text='opened windows: '+str(window_counter)+'; message: c'+str(base_col)+', r'+str(base_row)+' '+str(name)+' widget closed')
        check_state()
    selection_uni1_1=('00: ---', '02: Canvas', '03: Canvas (s)', '05: MenuButton','06: Button',
                '07: Text', '08: Text (s)', '09: Entry (s)','10: Label',
                '11: Label (s)', '12: Combobox', '13: ComboBox (s)',
                '14: OptionMenu', '15: OptionMenu (s)', '16: Radio',
                '17: Radio (s)', '19: Listbox', '20: Scale', '21: Spinbox',
                '22: Progressbar','23: Toolbar')
    selection_uni1_2=('00: ---', '02: Canvas', '03: Canvas (s)', '05: MenuButton','06: Button',
                '07: Text', '08: Text (s)', '09: Entry (s)','10: Label',
                '11: Label (s)', '12: Combobox', '13: ComboBox (s)',
                '14: OptionMenu', '15: OptionMenu (s)', '16: Radio',
                '17: Radio (s)', '19: Listbox', '20: Scale', '21: Spinbox',
                '22: Progressbar','23: Toolbar','98: colspan <')
    selection_uni2_1=('00: ---', '02: Canvas', '03: Canvas (s)', '05: MenuButton','06: Button',
                '07: Text', '08: Text (s)', '09: Entry (s)','10: Label',
                '11: Label (s)', '12: Combobox', '13: ComboBox (s)',
                '14: OptionMenu', '15: OptionMenu (s)', '16: Radio',
                '17: Radio (s)', '19: Listbox', '20: Scale', '21: Spinbox',
                '22: Progressbar','23: Toolbar','99: rowspan ^')
    selection_uni2_2=('00: ---', '02: Canvas', '03: Canvas (s)', '05: MenuButton','06: Button',
                '07: Text', '08: Text (s)', '09: Entry (s)','10: Label',
                '11: Label (s)', '12: Combobox', '13: ComboBox (s)',
                '14: OptionMenu', '15: OptionMenu (s)', '16: Radio',
                '17: Radio (s)', '19: Listbox', '20: Scale', '21: Spinbox',
                '22: Progressbar','23: Toolbar','98: colspan <', '99: rowspan ^')
    nb_select=0
    base_col=rc[0]              
    base_row=rc[1]
    abl2=Toplevel(abl1)
    
    if (nbframe=='ablak'):
        abl2.title('Universal widget frame: c'+str(base_col)+', r'+str(base_row))
    else:
        abl2.title('Notebook widget frame (tab '+str(nbframe)[1:]+'): c'+str(base_col)+', r'+str(base_row))
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    kret12=Frame(ablak, relief='flat', borderwidth=1)
    kret12.grid(row=2, column=2, sticky=N)
    cmke110=Label(kret12, text='r0')
    cmke110.grid(row=1, column=0,sticky=E)
    cmke210=Label(kret12, text='r1')
    cmke210.grid(row=2, column=0,sticky=E)
    cmke020=Label(kret12, text='c0')
    cmke020.grid(row=0, column=2,sticky=N)
    cmke030=Label(kret12, text='c1')
    cmke030.grid(row=0, column=3,sticky=N)
    kret50=Frame(ablak, relief='flat', borderwidth=1)
    kret50.grid(row=5, column=0, sticky=N)
    bmezo=Entry(ablak)
    bmezo.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N)
    cmkefl=Label(ablak, text='Frame label:')
    cmkefl.grid(row=0, column=2,sticky=N)    
    gmb500=Button(ablak,text='Apply',command=uni_ertek)
    gmb500.grid(row=2, column=0, sticky=SW)
    u1_1=Combobox(kret12)
    u1_1['values']=selection_uni1_1
    u1_1.current(0)
    u1_1.grid(row=1, column=2,sticky=N)
    u1_2=Combobox(kret12)
    u1_2['values']=selection_uni1_2
    u1_2.current(0)
    u1_2.grid(row=1, column=3,sticky=N)
    cmke100=Label(ablak, text='Orientat.')
    cmke100.grid(row=1, column=0,sticky=N)
    u2_1=Combobox(kret12)
    u2_1['values']=selection_uni2_1
    u2_1.current(0)
    u2_1.grid(row=2, column=2,sticky=N)
    u2_2=Combobox(kret12)
    u2_2['values']=selection_uni2_2
    u2_2.current(0)
    u2_2.grid(row=2, column=3,sticky=N)
    kret20=Frame(ablak, relief='flat', borderwidth=1)
    kret20.grid(row=2, column=0, sticky=N)
    chbox200=Combobox(kret20, width=4)
    chbox200['values']=orient_values
    chbox200.current(0)
    chbox200.grid(row=0, column=1,sticky=N)
    cmke200=Label(kret20, text='')
    cmke200.grid(row=0, column=0,sticky=N)
    cells_uni=[u1_1, u1_2,
               u2_1, u2_2]
    cmkei=Label(ablak, text='hint', foreground='black', background='orange')
    cmkei.grid(row=0, column=0,sticky=S)
    CreateToolTip(cmkei, text=univ_tip)
    abl2.protocol('WM_DELETE_WINDOW', on_exit)


#ToolTip class for button w. image (toolbar) tooltip
str_tooltip='class ToolTip(object):\n\
#https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python\n\
    def __init__(self, widget):\n\
        self.widget=widget\n\
        self.tipwindow=None\n\
        self.id=None\n\
        self.x=self.y=0\n\
    def showtip(self, text):\n\
        '"'Display text in tooltip window'"'\n\
        self.text = text\n\
        if self.tipwindow or not self.text:\n\
            return\n\
        x, y, cx, cy = self.widget.bbox('"'insert'"')\n\
        x = x + self.widget.winfo_rootx() + 20\n\
        y = y + cy + self.widget.winfo_rooty() +40\n\
        self.tipwindow = tw = Toplevel(self.widget)\n\
        tw.wm_overrideredirect(1)\n\
        tw.wm_geometry('"'+%d+%d'"' % (x, y))\n\
        label = Label(tw, text=self.text, justify=LEFT,\n\
                      background='"'#ffffe0'"', relief=SOLID, borderwidth=1,\n\
                      font=('"'tahoma'"', '"'8'"', '"'normal'"'))\n\
        label.pack(ipadx=1)\n\
    def hidetip(self):\n\
        tw = self.tipwindow\n\
        self.tipwindow = None\n\
        if tw:\n\
            tw.destroy()\n\
def CreateToolTip(widget, text):\n\
    toolTip = ToolTip(widget)\n\
    def enter(event):\n\
        toolTip.showtip(text)\n\
    def leave(event):\n\
        toolTip.hidetip()\n\
    widget.bind("'"<Enter>"'", enter)\n\
    widget.bind("'"<Leave>"'", leave)\n\n'

def updatecell_uni(cells_uni):
        cstat=[['',[0,0],[1,1]],['',[1,0],[1,1]], #cells: ['content',[col,row],[colspan=1,rowspan=1]]
               ['',[0,1],[1,1]],['',[1,1],[1,1]]]
        r,c=0,0 # row and col counter
        a=0
        for i in cells_uni:
            i.configure(state=NORMAL)
            cstat[a][0]=int((i).get()[:2])
            a=a+1
        for i in range(len(cstat)):
###rowspan
            if((i>1) and (cstat[i][0]==99)): #rowspan must be in valid place/area
                if(cstat[i-2][0]<30 and cstat[i-2][0]!=0):                          # above rs (the 1st cell) there is valid cell (between 1-17) 
                    cstat[i-2][2][1]=cstat[i-2][2][1]+1                             # fölötte lévő cella rowspan értékét növelje 1-el
                if(cstat[i-2][0]<4 or cstat[i-2][0]==98):      # ha rs fölött üres cella vagy cs vagy canvas van akkor törölje
                       cells_uni[i].current(0)
###colspan            
            if((i!=0 and i!=2) and (cstat[i][0]==98)):                            #colspan must be in valid place/area
                if(cstat[i-1][0]<30 and cstat[i-1][0]!=0):                          #on the left side there is valid cell
                    cstat[i-1][2][0]=cstat[i-1][2][0]+1                             #balra lévő cella colspan értékét növelje 1-el
                if(cstat[i-1][0]<4 or cstat[i-1][0]==99):     # ha cs -től balra üres cella vagy rs vagy canvas van akkor törölje
                    cells_uni[i].current(0)
#        print(cstat)
        for i in range(len(cstat)):
            if(cstat[i][2]==[2,2]):
                cells_uni[i+3].configure(state=DISABLED)
                cells_uni[i+3].current(0)
        return cstat

def kivalaszto_uni(base_rc,cells_uni,output,nbframe):
        cstat=updatecell_uni(cells_uni)
        keretszam=keretablak(base_rc,output,nbframe)
        for i in range(len(cstat)):
            if cstat[i][0]!=0:
                if (nbframe!='ablak'): # if it is opened from Notebook
                    rc=['','','','',str(base_rc[0])+str(nbframe),base_rc[1],0,'nbook/uni',0] #c,r,rspan,cspan,base_c, base_r, marker
                else:    
                    rc=['','','','',base_rc[0],base_rc[1],0,'uni',0] #c,r,rspan,cspan,base_c, base_r, marker
                rc[0]=cstat[i][1][0] #col             
                rc[1]=cstat[i][1][1] #row
                rc[2]=cstat[i][2][0] #colspan
                rc[3]=cstat[i][2][1] #rowspan
                rc[6]=cstat[i][0]    #save type selector
                rc[8]=i              #cell index
                if(cstat[i][0]==2):
                    vaszonablak(rc,keretszam)
                if(cstat[i][0]==3):
                    vaszonablak_s(rc,keretszam)
                if(cstat[i][0]==5):
                    menuablak(rc,keretszam)
                if(cstat[i][0]==6):
                    gombablak(rc,keretszam)
                if(cstat[i][0]==7):
                    szovegmezablak(rc,keretszam)
                if(cstat[i][0]==8):
                    szovegmezablak_s(rc,keretszam)
                if(cstat[i][0]==9):
                    beviteliablak(rc,keretszam)
                if(cstat[i][0]==10):    
                    cimkeablak(rc,keretszam)
                if(cstat[i][0]==11):    
                    cimkeablak_s(rc,keretszam)
                if(cstat[i][0]==12):    
                    comboxwindow(rc,keretszam) #comboxablak(rc,keretszam)
                if(cstat[i][0]==13):    
                    comboxablak_s(rc,keretszam)
                if(cstat[i][0]==14):    
                    omenuwindow(rc,keretszam) #omenuablak(rc,keretszam)
                if(cstat[i][0]==15):    
                    omenuablak_s(rc,keretszam)
                if(cstat[i][0]==16):    
                    radioxwindow(rc,keretszam) #radioxablak(rc,keretszam)
                if(cstat[i][0]==17):    
                    radioxablak_s(rc,keretszam)
                if(cstat[i][0]==19):    
                    listboxablak(rc,keretszam)
                if(cstat[i][0]==20): 
                    scaleablak(rc,keretszam)
                if(cstat[i][0]==21): 
                    spinablak(rc,keretszam)
                if(cstat[i][0]==22): 
                    progressablak(rc,keretszam)
                if(cstat[i][0]==23): 
                    toolbarablak(rc,keretszam)
            

      
               
def updatecell():
        cstat=[['',[0,0],[1,1]],['',[1,0],[1,1]],['',[2,0],[1,1]],['',[3,0],[1,1]],['',[4,0],[1,1]], #cells: ['id',[col,row],[colspan=1,rowspan=1]]
               ['',[0,1],[1,1]],['',[1,1],[1,1]],['',[2,1],[1,1]],['',[3,1],[1,1]],['',[4,1],[1,1]],
               ['',[0,2],[1,1]],['',[1,2],[1,1]],['',[2,2],[1,1]],['',[3,2],[1,1]],['',[4,2],[1,1]],
               ['',[0,3],[1,1]],['',[1,3],[1,1]],['',[2,3],[1,1]],['',[3,3],[1,1]],['',[4,3],[1,1]],
               ['',[0,4],[1,1]],['',[1,4],[1,1]],['',[2,4],[1,1]],['',[3,4],[1,1]],['',[4,4],[1,1]],
               ['',[0,5],[1,1]],['',[1,5],[1,1]],['',[2,5],[1,1]],['',[3,5],[1,1]],['',[4,5],[1,1]],
               ['',[0,6],[1,1]],['',[1,6],[1,1]],['',[2,6],[1,1]],['',[3,6],[1,1]],['',[4,6],[1,1]],
               ['',[0,7],[1,1]],['',[1,7],[1,1]],['',[2,7],[1,1]],['',[3,7],[1,1]],['',[4,7],[1,1]],
               ['',[0,8],[1,1]],['',[1,8],[1,1]],['',[2,8],[1,1]],['',[3,8],[1,1]],['',[4,8],[1,1]]]

        r,c=0,0 # row and col counter
        a=0
        for i in cellak:
            i.configure(state=NORMAL)
            cstat[a][0]=int((i).get()[:2])
            a=a+1

        for i in range(len(cstat)):
            if(i==0 or i%5==0) and (cstat[i][0]==98): # in the first col. can't be colspan
                cellak[i].current(0)
            if(i<5) and (cstat[i][0]==99): # in the first row can't be rowspan
                cellak[i].current(0)
###rowspan
            if((i>4) and (cstat[i][0]==99)): #rowspan must be in valid place/area
                if(cstat[i-5][0]<30 and cstat[i-5][0]>3):      # ha fölötte 1-el érvényes (1-17 közötti) cella van 
                    cstat[i-5][2][1]=cstat[i-5][2][1]+1                             # fölötte lévő cella rowspan értékét növelje 1-el
                if(cstat[i-5][0]<4 or cstat[i-5][0]==98):                          # ha rs fölött üres cella vagy cs vagy canvas,menubar van akkor törölje
                       cellak[i].current(0)
                if((cstat[i-5][0]==99) and (cstat[i-10][0]<4 or cstat[i-10][0]==98)):  # ha rs fölött 1-el üres cella vagy cs vagy cancas ill menubar van akkor törölje
                       cellak[i].current(0)
                if((cstat[i-5][0]==99 and cstat[i-10][0]==99) and (cstat[i-15][0]<4 or cstat[i-15][0]==98)):  # ha rs fölött 2-vel üres cella vagy cs van akkor törölje
                       cellak[i].current(0)
                if((cstat[i-5][0]==99 and cstat[i-10][0]==99 and cstat[i-15][0]==99) and (cstat[i-20][0]<4 or cstat[i-20][0]==98)):  # ha rs fölött 2-vel üres cella vagy cs,canvas,manubar van akkor törölje
                       cellak[i].current(0)
                if(cstat[i-5][0]==99 and cstat[i-10][0]==99 and cstat[i-15][0]==99 and cstat[i-20][0]==99):  # az 5.rs kijelölés már nem engedélyezett
                       cellak[i].current(0)
                if(i>9 and cstat[i-5][0]==99 and (cstat[i-10][0]<30 and cstat[i-10][0]>3)): #ha a cella fölött rs utána érvényes cella 
                   cstat[i-10][2][1]=cstat[i-10][2][1]+1                            # 1-el fölötte lévő cella rowspan értékét növelje 1-el
                if(i>14 and cstat[i-5][0]==99 and cstat[i-10][0]==99 and (cstat[i-15][0]<30 and cstat[i-15][0]>3)): #ha a cella fölött rs+rs utána érvényes cella 
                   cstat[i-15][2][1]=cstat[i-15][2][1]+1                            # 2-el fölötte lévő cella rowspan értékét növelje 1-el
                if(i>19 and cstat[i-5][0]==99 and cstat[i-10][0]==99 and cstat[i-15][0]==99 and (cstat[i-20][0]<30 and cstat[i-20][0]>3)): #ha a cella fölött rs+rs utána érvényes cella 
                   cstat[i-20][2][1]=cstat[i-20][2][1]+1 

###colspan            
            if((i!=0 and i%5!=0) and (cstat[i][0]==98)):                            #colspan must be in valid place/area
                if(cstat[i-1][0]<30 and cstat[i-1][0]>3):      #ha balra érvényes cella van
                    cstat[i-1][2][0]=cstat[i-1][2][0]+1                             #balra lévő cella colspan értékét növelje 1-el
                if(cstat[i-1][0]<4 or cstat[i-1][0]==99):                          # ha cs -től balra üres cella vagy rs vagy canvas,menubar van akkor törölje
                    cellak[i].current(0)
                if(cstat[i-1][0]==98 and (cstat[i-2][0]<4 or cstat[i-2][0]==99)):  # ha cs -től balra 1-el cs, de utána üres cella vagy rs van akkor törölje
                    cellak[i].current(0)
                if(cstat[i-1][0]==98 and cstat[i-2][0]==98 and (cstat[i-3][0]<4  or cstat[i-3][0]==99)):  # ha cs -től balra 2-vel cs, de utána üres cella vagy rs van akkor törölje
                    cellak[i].current(0)
                if(cstat[i-1][0]==98 and cstat[i-2][0]==98 and cstat[i-3][0]==98 and (cstat[i-4][0]<4 or cstat[i-4][0]==99)):  # ha cs -től balra 3-al cs, de utána üres cella vagy rs van akkor törölje
                    cellak[i].current(0)
                if(i>0 and cstat[i-1][0]==98 and (cstat[i-2][0]<30 and cstat[i-2][0]>3)):                #ha a cella fölött rs utána érvényes cella 
                    cstat[i-2][2][0]=cstat[i-2][2][0]+1                            # 1-el fölötte lévő cella rowspan értékét növelje 1-el
                if(i>1 and cstat[i-1][0]==98 and cstat[i-2][0]==98 and (cstat[i-3][0]<30 and cstat[i-3][0]>3)):                #ha a cella fölött rs utána érvényes cella 
                    cstat[i-3][2][0]=cstat[i-3][2][0]+1                            # 1-el fölötte lévő cella rowspan értékét növelje 1-el
                if(i>2 and cstat[i-1][0]==98 and cstat[i-2][0]==98 and cstat[i-3][0]==98 and (cstat[i-4][0]<30 and cstat[i-4][0]>3)):                #ha a cella fölött rs utána érvényes cella 
                    cstat[i-4][2][0]=cstat[i-4][2][0]+1
        #check menubar only one widget possible
        counter=0
        for i in range(len(cstat)):
            if (cstat[i][0]==1 and counter==1):    #if counter increased and find manubar reset it
                    cellak[i].current(0)
            if (cstat[i][0]==1 and counter==0): #in case of first manubar increase the counter
                    counter=counter+1
        letilto(cstat)
        return cstat
               

            

                
def letilto(cstat):

    for i in range(len(cstat)):
        if(cstat[i][2]==[2,2]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+6].current(0)
        if(cstat[i][2]==[3,2]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+7].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+7].current(0)
        if(cstat[i][2]==[2,3]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+11].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+11].current(0)
        if(cstat[i][2]==[3,3]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+7].configure(state=DISABLED)
            cellak[i+11].configure(state=DISABLED)
            cellak[i+12].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+7].current(0)
            cellak[i+11].current(0)
            cellak[i+12].current(0)
        if(cstat[i][2]==[4,2]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+7].configure(state=DISABLED)
            cellak[i+8].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+7].current(0)
            cellak[i+8].current(0)
        if(cstat[i][2]==[2,4]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+11].configure(state=DISABLED)
            cellak[i+16].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+11].current(0)
            cellak[i+16].current(0)
        if(cstat[i][2]==[4,3]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+7].configure(state=DISABLED)
            cellak[i+8].configure(state=DISABLED)
            cellak[i+11].configure(state=DISABLED)
            cellak[i+12].configure(state=DISABLED)
            cellak[i+13].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+7].current(0)
            cellak[i+8].current(0)
            cellak[i+11].current(0)
            cellak[i+12].current(0)
            cellak[i+13].current(0)
        if(cstat[i][2]==[3,4]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+7].configure(state=DISABLED)
            cellak[i+11].configure(state=DISABLED)
            cellak[i+12].configure(state=DISABLED)
            cellak[i+16].configure(state=DISABLED)
            cellak[i+17].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+7].current(0)
            cellak[i+11].current(0)
            cellak[i+12].current(0)
            cellak[i+16].current(0)
            cellak[i+17].current(0)
        if(cstat[i][2]==[4,4]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+7].configure(state=DISABLED)
            cellak[i+8].configure(state=DISABLED)
            cellak[i+11].configure(state=DISABLED)
            cellak[i+12].configure(state=DISABLED)
            cellak[i+13].configure(state=DISABLED)
            cellak[i+16].configure(state=DISABLED)
            cellak[i+17].configure(state=DISABLED)
            cellak[i+18].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+7].current(0)
            cellak[i+8].current(0)
            cellak[i+11].current(0)
            cellak[i+12].current(0)
            cellak[i+13].current(0)
            cellak[i+16].current(0)
            cellak[i+17].current(0)
            cellak[i+18].current(0)
        if(cstat[i][2]==[5,2]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+7].configure(state=DISABLED)
            cellak[i+8].configure(state=DISABLED)
            cellak[i+9].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+7].current(0)
            cellak[i+8].current(0)
            cellak[i+9].current(0)
        if(cstat[i][2]==[2,5]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+11].configure(state=DISABLED)
            cellak[i+16].configure(state=DISABLED)
            cellak[i+21].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+11].current(0)
            cellak[i+16].current(0)
            cellak[i+21].current(0)
        if(cstat[i][2]==[5,3]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+7].configure(state=DISABLED)
            cellak[i+8].configure(state=DISABLED)
            cellak[i+9].configure(state=DISABLED)
            cellak[i+11].configure(state=DISABLED)
            cellak[i+12].configure(state=DISABLED)
            cellak[i+13].configure(state=DISABLED)
            cellak[i+14].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+7].current(0)
            cellak[i+8].current(0)
            cellak[i+9].current(0)
            cellak[i+11].current(0)
            cellak[i+12].current(0)
            cellak[i+13].current(0)
            cellak[i+14].current(0)
        if(cstat[i][2]==[3,5]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+7].configure(state=DISABLED)
            cellak[i+11].configure(state=DISABLED)
            cellak[i+12].configure(state=DISABLED)
            cellak[i+16].configure(state=DISABLED)
            cellak[i+17].configure(state=DISABLED)
            cellak[i+21].configure(state=DISABLED)
            cellak[i+22].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+7].current(0)
            cellak[i+11].current(0)
            cellak[i+12].current(0)
            cellak[i+16].current(0)
            cellak[i+17].current(0)
            cellak[i+21].current(0)
            cellak[i+22].current(0)
        if(cstat[i][2]==[5,4]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+7].configure(state=DISABLED)
            cellak[i+8].configure(state=DISABLED)
            cellak[i+9].configure(state=DISABLED)
            cellak[i+11].configure(state=DISABLED)
            cellak[i+12].configure(state=DISABLED)
            cellak[i+13].configure(state=DISABLED)
            cellak[i+14].configure(state=DISABLED)
            cellak[i+16].configure(state=DISABLED)
            cellak[i+17].configure(state=DISABLED)
            cellak[i+18].configure(state=DISABLED)
            cellak[i+19].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+7].current(0)
            cellak[i+8].current(0)
            cellak[i+9].current(0)
            cellak[i+11].current(0)
            cellak[i+12].current(0)
            cellak[i+13].current(0)
            cellak[i+14].current(0)
            cellak[i+16].current(0)
            cellak[i+17].current(0)
            cellak[i+18].current(0)
            cellak[i+19].current(0)
        if(cstat[i][2]==[4,5]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+7].configure(state=DISABLED)
            cellak[i+8].configure(state=DISABLED)
            cellak[i+11].configure(state=DISABLED)
            cellak[i+12].configure(state=DISABLED)
            cellak[i+13].configure(state=DISABLED)
            cellak[i+16].configure(state=DISABLED)
            cellak[i+17].configure(state=DISABLED)
            cellak[i+18].configure(state=DISABLED)
            cellak[i+21].configure(state=DISABLED) 
            cellak[i+22].configure(state=DISABLED)
            cellak[i+23].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+7].current(0)
            cellak[i+8].current(0)
            cellak[i+11].current(0)
            cellak[i+12].current(0)
            cellak[i+13].current(0)
            cellak[i+16].current(0)
            cellak[i+17].current(0)
            cellak[i+18].current(0)
            cellak[i+21].current(0)
            cellak[i+22].current(0)
            cellak[i+23].current(0)
        if(cstat[i][2]==[5,5]):
            cellak[i+6].configure(state=DISABLED)
            cellak[i+7].configure(state=DISABLED)
            cellak[i+8].configure(state=DISABLED)
            cellak[i+9].configure(state=DISABLED)
            cellak[i+11].configure(state=DISABLED)
            cellak[i+12].configure(state=DISABLED)
            cellak[i+13].configure(state=DISABLED)
            cellak[i+14].configure(state=DISABLED)
            cellak[i+16].configure(state=DISABLED)
            cellak[i+17].configure(state=DISABLED)
            cellak[i+18].configure(state=DISABLED)
            cellak[i+19].configure(state=DISABLED)
            cellak[i+21].configure(state=DISABLED)
            cellak[i+22].configure(state=DISABLED)
            cellak[i+23].configure(state=DISABLED)
            cellak[i+24].configure(state=DISABLED)
            cellak[i+6].current(0)
            cellak[i+7].current(0)
            cellak[i+8].current(0)
            cellak[i+9].current(0)
            cellak[i+11].current(0)
            cellak[i+12].current(0)
            cellak[i+13].current(0)
            cellak[i+14].current(0)
            cellak[i+16].current(0)
            cellak[i+17].current(0)
            cellak[i+18].current(0)
            cellak[i+19].current(0)
            cellak[i+21].current(0)
            cellak[i+22].current(0)
            cellak[i+23].current(0)
            cellak[i+24].current(0)
            

def kivalaszto2():
        reset() #close all opened sub-windows
        cstat=updatecell()
        for i in range(len(cstat)):
            if cstat[i][0]!=0:
                gomb.configure(text="Restart")
                submenu00aa1.entryconfig(2,label="Restart") # Start menu to Restart
                radiob0.configure(state=DISABLED)
                radiob1.configure(state=DISABLED)
                rc=['','','','','a','a',0,'m',0] #c,r,rspan,cspan,base_c,base_r, type, startred from main window or univframe m-main u-iniv, cell index
                rc[0]=cstat[i][1][0] #col             
                rc[1]=cstat[i][1][1] #row
                rc[2]=cstat[i][2][0] #colspan
                rc[3]=cstat[i][2][1] #rowspan
                rc[6]=cstat[i][0]    #save type selector
                rc[8]=i              #cell index
                if(cstat[i][0]==1):
                    menbarablak(rc)
                if(cstat[i][0]==2):
                    vaszonablak(rc)
                if(cstat[i][0]==3):
                    vaszonablak_s(rc)
                if(cstat[i][0]==4):    
                    univablak(rc)
                if(cstat[i][0]==5):
                    menuablak(rc)
                if(cstat[i][0]==6):
                    gombablak(rc)
                if(cstat[i][0]==7):
                    szovegmezablak(rc)
                if(cstat[i][0]==8):
                    szovegmezablak_s(rc)
                if(cstat[i][0]==9):
                    beviteliablak(rc)
                if(cstat[i][0]==10):    
                    cimkeablak(rc)
                if(cstat[i][0]==11):    
                    cimkeablak_s(rc)
                if(cstat[i][0]==12):    
                    comboxwindow(rc) 
                if(cstat[i][0]==13):    
                    comboxablak_s(rc)
                if(cstat[i][0]==14):    
                    omenuwindow(rc)
                if(cstat[i][0]==15):    
                    omenuablak_s(rc)
                if(cstat[i][0]==16):    
                    radioxwindow(rc) 
                if(cstat[i][0]==17):    
                    radioxablak_s(rc)
                if(cstat[i][0]==18):    
                    uzenablak(rc)
                if(cstat[i][0]==19):    
                    listboxablak(rc)
                if(cstat[i][0]==20): 
                    scaleablak(rc)
                if(cstat[i][0]==21): 
                    spinablak(rc)
                if(cstat[i][0]==22): 
                    progressablak(rc)
                if(cstat[i][0]==23): 
                    toolbarablak(rc)
                if(cstat[i][0]==24): 
                    nbookablak(rc)
        msg.configure(text='opened windows: '+str(window_counter)+'; message: Adjust all option windows')
        gomb2.configure(state=DISABLED) #Finalize button to normal state
        submenu00aa1.entryconfig(3,state=DISABLED) # Finalize menu to normal state
        check_state()

def check_state():
    global window_counter
    if(window_counter==0):
        gomb2.configure(state=NORMAL) #Finalize button to normal state
        submenu00aa1.entryconfig(3,state=NORMAL) # Finalize menu to normal state
        msg.configure(text='opened windows: '+str(window_counter)+'; message: All code generated. Press Finalize')


def github():
    webbrowser.open_new(r"https://github.com/horrorfodrasz/Tkinter_GUI_designer")

def contact():
    msg.configure(text='Gmiki (2020) --- email: epromirok(a)gmail(.)com')

def donate():
    webbrowser.open_new(r"https://www.paypal.com/donate?hosted_button_id=A7QF7LQJM5SGS")
    

def clearenter(text):
    "replace in text enters with space"
    text2=''
    for i in range(len(text)-1):
        if (text[i]=='\n'):
            text2=text2+' '
        else:
            text2=text2+text[i]
    return text2

def clearlist(list,out_type):
    list_new=[]
    "remove '' and #... elements form list. It can return list (0) or tuple (1)"
    for i in range(len(list)):
            try:
                if(list[i][0]!='#' and list[i]!=''):
                    list_new.append(list[i])
            except:
                pass
    if(out_type==1):
        return tuple(list_new)
    else:
        return list_new

def cellaw(lista): #determine cell width
    templist=[]
    for x in range(4):
        for i in range(len(lista[x])):
           templist.append(len(lista[x][i]))
        cw=(max(templist))+4
    return cw

def kiir(x):
    if(x!=''):
        check_state()
        text1.insert(INSERT,x)        #text insert
        text1.insert(INSERT,'\n')

def finalize():
    tooltipclass=''
    tab=getresulttype()[0]
    slf=getresulttype()[1]
    init=getresulttype()[2]
    end=getresulttype()[3]
    sajatcim=title_entry.get()
    if(toolbar_counter==1):
        tooltipclass=str_tooltip
    else:
        tooltipclass=''
    s1_f='from tkinter import *\nfrom tkinter import ttk\n\n'+tooltipclass+str(init)+str(tab)+str(slf)+'k_ablak=Tk()\n'+str(tab)+str(slf)+'k_ablak.title('+"'"+str(sajatcim)+"'"+')\
        \n'+str(tab)+str(slf)+'ablak=Frame('+str(slf)+'k_ablak, relief='+"'"+'flat'+"'"+', borderwidth=1)\n'+str(tab)+str(slf)+'ablak.grid(row=0, column=0)\n'
    text1.insert(1.0,s1_f) #insert to the begining
    text1.insert(END,str(tab)+str(slf)+su+str(end))   #insert to the end
    gomb2.configure(state=DISABLED) # Disable to avoid repeated button click
    submenu00aa1.entryconfig(3,state=DISABLED) # Finalize menu OFF
    radiob0.configure(state=NORMAL)
    radiob1.configure(state=NORMAL)
    msg.configure(text='opened windows: '+str(window_counter)+'; message: Code finalized')

def colorset(): #color selection modul
    a=colorchooser.askcolor(initialcolor='#ff0000')
    return a[1] # the needed color code is in a[1]

def reset():
    global toolbar_counter, window_counter
    toolbar_counter=0
    window_counter=0
    text1.delete(1.0,END) #erase text area
    for widget in abl1.winfo_children(): #close all sub-windows
        if isinstance(widget, tk.Toplevel):
            widget.destroy()

def reset2():
    global toolbar_counter, window_counter
    toolbar_counter=0
    window_counter=0
    for i in cellak:
        i.configure(state=NORMAL)
    def_status() # reset all selction cells
    gomb.configure(text="Start")
    submenu00aa1.entryconfig(2,label="Start") # Start menu
    gomb2.configure(state=DISABLED) #Finalize button OFF
    submenu00aa1.entryconfig(3,state=DISABLED) # Finalize menu OFF
    radiob0.configure(state=NORMAL)
    radiob1.configure(state=NORMAL)
    text1.delete(1.0,END) #Erase text area
    for widget in abl1.winfo_children(): #close all sub-windows
        if isinstance(widget, tk.Toplevel):
            widget.destroy()
    msg.configure(text='opened windows: '+str(window_counter)+'; message: Select widgets')

def fileopen(): #load widget selection
    filename=filedialog.askopenfilename(filetypes=[("TKinterGUI","*.tki"),("All","*.*")])
    if (filename!=''): 
        fileobjekt=open(filename,'r') 
        tk_file=fileobjekt.read()
        fileobjekt.close() 
        savestr2cell(tk_file)
    msg.configure(text='opened windows: '+str(window_counter)+'; message: Widget selection file loaded')
        
  
def filesave(): # save widget selection
    tk_file=cell2savestr()
    filename=filedialog.asksaveasfilename(filetypes=[("TKinterGUI","*.tki")],defaultextension='.tki') 
    if (filename!=''): 
        fileobjekt=open(filename,'w')
        fileobjekt.write(tk_file)
        fileobjekt.close()
    msg.configure(text='opened windows: '+str(window_counter)+'; message: Widget selection file saved')

def cell2savestr(): # cell state list convert string
    cstr=''
    cstat=updatecell()
    for i in range(len(cstat)):
        cstr=cstr+str(cstat[i][0])+','
    cstr=cstr+'\n'+default2str(label_defaults)
    cstr=cstr+'\n'+default2str(chbox_defaults[0])+default2str(chbox_defaults[8:])
    cstr=cstr+'\n'+default2str(optmenu_defaults[0])+default2str(optmenu_defaults[8:])
    cstr=cstr+'\n'+default2str(radio_defaults[0])+default2str(radio_defaults[8:])
    cstr=cstr+'\n'+default2str(entry_defaults)
    cstr=cstr+'\n'+default2str(canvas_defaults)
    cstr=cstr+'\n'+default2str(text_defaults)
    return cstr

def chdefault2str(default):
    for i in range(len(default[0])):
        if(default[0][i]==''):
            cstr=cstr+'*'
        

def default2str(default):
    cstr=''
    for i in range(len(default)):
        if(default[i]==''):
            cstr=cstr+'*'
        cstr=cstr+str(default[i])+','
    return cstr

def savestr2cell(cstr): # save string convert to cell state list
    global label_defaults, chbox_defaults, optmenu_defaults, radio_defaults, entry_defaults, canvas_defaults, text_defaults
    lista=cstr.split('\n')
    x=''
    counter=0
    defs=[[],[],[],[],[],[],[]] #label,chbox,optm,radio,entr,canv,text 
    for n in range(len(lista)): #write cell state
        if (n==0):
            for i in range(len(lista[n])):
                if (lista[n][i]!=','):
                    x=x+lista[n][i]
                else:
                    if(x=='98'): # colspan index 23
                        x='25'
                    if(x=='99'): # rowspan index 24 
                        x='26'
                    cellak[counter].current(int(x))
                    counter=counter+1
                    x=''
            updatecell()
        if (n>0): #write default settings
            for i in range(len(lista[n])):
                if (lista[n][i]!=',' and lista[n][i]!='*'):
                    x=x+lista[n][i]
                if (lista[n][i]=='*'):
                    pass
                if (lista[n][i]==','):
                    defs[n-1].append(x)
                    x=''
    label_defaults = defs[0]
    chbox_defaults[0][0] = defs[1][0]
    chbox_defaults[0][1] = defs[1][1]
    chbox_defaults[0][2] = defs[1][2]
    chbox_defaults[8] = defs[1][3]
    optmenu_defaults[0][0] = defs[2][0]
    optmenu_defaults[0][1] = defs[2][1]
    optmenu_defaults[0][2] = defs[2][2]
    optmenu_defaults[8] = defs[2][3]
    radio_defaults[0][0] = defs[3][0]
    radio_defaults[0][1] = defs[3][1]
    radio_defaults[0][2] = defs[3][2]
    radio_defaults[8] = defs[3][3]
    entry_defaults = defs[4]
    canvas_defaults = defs[5]
    text_defaults = defs[6] 
    set_defaults()
        
def countwindows():
    counter=0
    for widget in abl1.winfo_children(): #close all sub-windows
        if isinstance(widget, tk.Toplevel):
            counter=counter+1
    return counter


def getresulttype():
    tab_slf=['','','',''] # tab, self., init of obj., ending of obj.
    rtype=resulttype.get()
    if(rtype==True):
        tab_slf[0]='        '
        tab_slf[1]='self.'
        tab_slf[2]='class Mywindow:\n    def __init__(self):\n'
        tab_slf[3]='\n\nif __name__ == "'"__main__"'":\n    mw=Mywindow()'
    else:
        tab_slf[0]=''
        tab_slf[1]=''
        tab_slf[2]=''
        tab_slf[3]=''
    return tab_slf   


def defaults():
    global label_defaults, chbox_defaults, optmenu_defaults, radio_defaults, entry_defaults, canvas_defaults, text_defaults
           
    label_defaults[0]=entr1.get()   # title
    label_defaults[1]=chbox1.get()  # orient
    chbox_defaults[0][0]=entr21.get()  # value1
    chbox_defaults[0][1]=entr22.get()  # value2
    chbox_defaults[0][2]=entr23.get()  # value3
    chbox_defaults[8]=chbox2.get() # orient
    optmenu_defaults[0][0]=entr31.get()  # value1
    optmenu_defaults[0][1]=entr32.get()  # value2
    optmenu_defaults[0][2]=entr33.get()  # value3
    optmenu_defaults[8]=chbox3.get() # orient
    radio_defaults[0][0]=entr41.get()  # value1
    radio_defaults[0][1]=entr42.get()  # value2
    radio_defaults[0][2]=entr43.get()  # value3
    radio_defaults[8]=chbox4.get() # orient
    entry_defaults[0]=chbox5.get() # orient
    entry_defaults[1]=entr51.get() # width
    entry_defaults[2]=entr52.get() # def.value
    canvas_defaults[0]=entr61.get() # width
    canvas_defaults[1]=entr62.get() # height
    canvas_defaults[2]=chbox62.get() # color
    if (canvas_defaults[2]=='pick a color'):
        canvas_defaults[2]=colorset()
        chbox62.delete(0,END)
        chbox62.insert(0,canvas_defaults[2])
    canvas_defaults[3]=chbox61.get() # orient
    text_defaults[0]=entr71.get() # width
    text_defaults[1]=entr72.get() # height
    text_defaults[2]=chbox71.get() # orient
    text_defaults[3]=chbox72.get() # scroll
    text_defaults[4]=entr73.get() # def.text
    entry_defaults[0]=chbox5.get() # orient
    msg.configure(text='opened windows: '+str(window_counter)+'; message: Default parameters applied')


def set_defaults():
    entr1.delete(0,END)
    entr1.insert(0,label_defaults[0])   # label title
    chbox1.delete(0,END)
    chbox1.insert(0,label_defaults[1])   # label orient
    entr21.delete(0,END)
    entr21.insert(0,chbox_defaults[0][0])  # chbox value1
    entr22.delete(0,END)
    entr22.insert(0,chbox_defaults[0][1])  # chboxvalue2
    entr23.delete(0,END)
    entr23.insert(0,chbox_defaults[0][2])  # chboxvalue3
    chbox2.delete(0,END)
    chbox2.insert(0,chbox_defaults[8])   # chbox orient
    entr31.delete(0,END)
    entr31.insert(0,optmenu_defaults[0][0])  # optm. value1
    entr32.delete(0,END)
    entr32.insert(0,optmenu_defaults[0][1])  # optm. value2
    entr33.delete(0,END)
    entr33.insert(0,optmenu_defaults[0][2])  # optm.value3
    chbox3.delete(0,END)
    chbox3.insert(0,optmenu_defaults[8])   # optm. orient
    entr41.delete(0,END)
    entr41.insert(0,radio_defaults[0][0])  # radio value1
    entr42.delete(0,END)
    entr42.insert(0,radio_defaults[0][1])  # radio value2
    entr43.delete(0,END)
    entr43.insert(0,radio_defaults[0][2])  # radio value3
    chbox4.delete(0,END)
    chbox4.insert(0,radio_defaults[8])   # radio. orient
    entr51.delete(0,END)
    entr51.insert(0,entry_defaults[1]) # entry width
    entr52.delete(0,END)
    entr52.insert(0,entry_defaults[2]) # entry def.value
    chbox5.delete(0,END)
    chbox5.insert(0,entry_defaults[0])   # entry orient
    entr61.delete(0,END)
    entr61.insert(0,canvas_defaults[0]) # canvas width
    entr62.delete(0,END)
    entr62.insert(0,canvas_defaults[1]) # canvas height
    chbox61.delete(0,END)
    chbox61.insert(0,canvas_defaults[3])   # canvas orient
    chbox62.delete(0,END)
    chbox62.insert(0,canvas_defaults[2])   # canvas color
    entr71.delete(0,END)
    entr71.insert(0,text_defaults[0]) # text width
    entr72.delete(0,END)
    entr72.insert(0,text_defaults[1]) # text height
    entr73.delete(0,END)
    entr73.insert(0,text_defaults[4]) # text height
    chbox71.delete(0,END)
    chbox71.insert(0,text_defaults[2])   # text orient
    chbox72.delete(0,END)
    chbox72.insert(0,text_defaults[3])   # text scroll

def list2tuple(lista):
        x=0
        for i in range(len(lista)): #remove '' empty items from v1 list and make tuple
            if(lista[i]==''):
               x=x+1     
        for i in range(x):
            lista.remove('')
        lista=tuple(lista)
        return lista

def removeempty(lista):
        newlist=[]
        for i in range(len(lista)):
            if (lista[i]!=''):
                newlist.append(lista[i])
        return newlist    

def def_status():
    i1_1.current(0)
    i1_2.current(0)
    i1_3.current(0)
    i1_4.current(0)
    i1_5.current(0)
    i2_1.current(0)
    i2_2.current(0)
    i2_3.current(0)
    i2_4.current(0)
    i2_5.current(0)
    i3_1.current(0)
    i3_2.current(0)
    i3_3.current(0)
    i3_4.current(0)
    i3_5.current(0)
    i3_1.current(0)
    i3_2.current(0)
    i3_3.current(0)
    i3_4.current(0)
    i3_5.current(0)
    i4_1.current(0)
    i4_2.current(0)
    i4_3.current(0)
    i4_4.current(0)
    i4_5.current(0)
    i5_1.current(0)
    i5_2.current(0)
    i5_3.current(0)
    i5_4.current(0)
    i5_5.current(0)
    i6_1.current(0)
    i6_2.current(0)
    i6_3.current(0)
    i6_4.current(0)
    i6_5.current(0)
    i7_1.current(0)
    i7_2.current(0)
    i7_3.current(0)
    i7_4.current(0)
    i7_5.current(0)
    i8_1.current(0)
    i8_2.current(0)
    i8_3.current(0)
    i8_4.current(0)
    i8_5.current(0)
    i9_1.current(0)
    i9_2.current(0)
    i9_3.current(0)
    i9_4.current(0)
    i9_5.current(0)

#----Main program
welcometext='Tkinter GUI designer\nIt uses tkinter Grid geometry manager. (https://effbot.org/tkinterbook/grid.htm)\nYou will get pure Python tkinter code.\n\n1. Select the desired widgets*\n2. If you use rowsapan/colspan press "'"Check"'" button\n3. Press "'"Start"'" to generate codes\
\n4. Set the opened options windows and Apply\n5. Press "'"Finalize"'" and copy the generated code with Ctrl+C\
\n\nHint:\n- rowspan must be placed under the expanded widget\n- columnspan must be placed to right side of the widget\n- maximum 4 column and 4 rowspan cells can be selected for one widget \n  (rowspan/col.span=5)\
\n- if you use col.span and/or rowspan press "'"Check"'" button to check your selection.\n  (all missplaced span selection will be reseted and common merged cells disabled)\
\n- Canvas, Manubar does not accept col./rowspan\n- Open second session of Python IDLE and use it for checking the generated code\n\
  without closing the running GUI generator\n- widget name with (s) means simple. It uses default parameters and does not open\n  option window.\n\nSupported widgets: \nMenubar, Menubutton, Button, Canvas, Text with slide, Entry, Label, Combobox, Optionmenu,\nRadio, Message, Frame/LabelFrame (universal 2x2), Listbox, Scale, Spinbox, Progressbar,\n\
Toolbar (buttons with images and Tooltip texts), Notebook'

toolbar_tip='Toolbar widget with png images and tooltips\n\n\
First row: PNG file name (without extension name)\n\
Select button images from prepared PNG icon file list or write\nthe name of your file (without extension) into entry field.\n\
In this case please put your PNG files into ico folder.\n\
For example: If path of your file is c\\myprog\\myprog.py, PNG files\n\
must be in c:\\myprog\\ico\\\n\n\
Second row: Tooltip text'

menubar_tip='First row: Main menu\n\
Other rows: Sub-menu\n\
Create separate marking: -\n\
Create checkbox menu: # (e.g: #yes)\n\n\
Default command is: destroy\n\
You can modify the command in the generated text:\n\
command=k_ablak.destroy'

menubutton_tip='First row: Main menu\n\
Other rows: Sub-menu\n\
orient.: orientation of your widget\n\n\
Default command is: destroy\n\
You can modify the command in the generated text:\n\
command=k_ablak.destroy'

button_tip='Every cell represents one button.\n\
Default command is: destroy\n\
You can modify the command in the generated text:\n\
command=k_ablak.destroy\n\n\
orient.: orientation of your widget\n\
In case of one button you can use E+W orientation\n\
to create as width button as width your widget.'

canvas_tip='orient.: orientation of your widget\n\
width: width of your canvas (in pixel). Type numbers only!\n\
height: height of your canvas (in pixel). Type numbers only!\n\
color: background color of your canvas.\n\n\
There are some default colors, but you can pick any with\n\
"'"pick a color"'" option or use a standard Python color code.'

text_tip='default text: This text will appear in your text area.\n\
orient.: orientation of your widget\n\
width: width of your text area (in char). Type numbers only!\n\
height: height of your canvas (in char). Type numbers only!\n\
scroll: you can create it with horizontal and/or vertical scrollbar.\n\
bg color: background color of your text area.\n\
text color: text color of your text area.\n\n\
There are some default colors, but you can pick any with\n\
"'"pick a color"'" option or use a standard Python color code.'

listbox_tip='Write your list elements into text area.\n\
Use enter to create new list element (new line).\n\n\
orient.: orientation of your widget\n\
Width: List element width. Type numbers only!'

label_tip='orient.: orientation of your widget\n\
text: This text will appear in your text area.'

combox_tip='You can create upto 4 widgets at once.\n\
If you leave any of them empty it wont be created.\n\n\
Title: label of widget. It can be empty.\n\
Elements of the widget: Any elements/label\n\
can be created.\n\n\
orient.: orientation of your widget\n\
width: width of your cell.\n\
There are some default numbers, but you can use any.\n\
Type numbers only!\n\
In case of auto, the width will be adapted to your content.'

univ_tip='You can select upto 4 widgets in any combination.\n\
If you leave any of them empty it wont be created.\n\n\
orient.: orientation of your widget\n\
Frame name: If you type text, the created widget group\n\
will be placed in LabelFrame and this text will appear\n\
above the widget group.'

scale_tip='title: title of your widget\n\
from: start value; to: end value. Type numbers only!\n\
resolution: resolution of your scale. Type numbers only!\n\
scale length: length of your scale (in pixel). Type numbers only!\n\
scale width: width of your scale (in pixel). Type numbers only!\n\
tickinterval: value change by one click. Type numbers only!\n\
set value: scale position to this value. Type numbers only!\n\
orient.: orientation of your widget\n\
scale orient.: Horizontal or Vertical scale\n\
show value: Show actual value'

spin_tip='Write your spinBox elements into the text area.\n\
Use enter to create new list element (new line).\n\n\
If row starts with # it will be considered as comment.\n\
If this area empty (or comment) your widget will use\n\
from and to fields for numbers. \n\n\
from: start value; to: end value. Type numbers only!\n\
orient.: orientation of your widget\n\
Width: cell width. Type numbers only!\n\
wrap: selected value can jump back to the begining after\n\
the last item.'

progress_tip='length: length of progressbar. Type numbers only!\n\
maximum: maximum value. Type numbers only!\n\
resolution: resolution of your scale. Type numbers only!\n\
start value: set the starting state of progressbar. Type numbers only!\n\
orient.: orientation of your widget\n\
progressbar orient.: Horizontal or Vertical scale\n\
mode: determine or indetermine'

notebook_tip='This widget acts as tabs or tabbed notebook.\n\n\
orient.: orientation of your widget\n\
Tab number: number of tabs (max 10). Type numbers only!\n\n\
It will open as many universal frame option windows as\n\
tab numbers you set.\n\
You can select upto 4 widgets in any combination for each tab.\n\n\
Tab text can be modified in generated code:\n\
default 1st tab: nb*.add(text="'"tab0"'")'

main_tip='1. Select the desired widgets\n\
2. If you use rowsapan/colspan press "'"Check"'" button\n\
3. Press "'"Start"'" to generate codes\n\
4. Set the opened options windows and Apply\n\
5. Press "'"Finalize"'" and copy the generated code with Ctrl+C\n\n\
Menu:\n\
- File: You can save and load cell selection\n\
- Function: Check, Start, Finalize and Reset\n\
- info: download latest version from Github and contact email\n\n\
Tabs:\n\
- Widget selection\n\
- Settings:\n  Generated code: Functions or Object\n\
  Set the default parameters for simplified widgets\n\n\
r0-r8/c0-c4:\n\
- Every cell represents a cell of grid for widget selection.\n\n\
Text area:\n\
Generated code appear here. Use Ctrl+C to copy that.\n\n\
Bottom message label:\n\
- Opened windows: It shows the number of opened option windows.\n\
  You can click Finalizte button only if this number 0.\n\
- message: system messages'

su='k_ablak.mainloop()'
toolbar_counter=0
window_counter=0
started=0
selection=('00: ---', '01: Menu', '02: Canvas', '03: Canvas (s)', '04: Univ.Frame',
           '05: MenuButton','06: Button', '07: Text', '08: Text (s)', '09: Entry (s)',
           '10: Label', '11: Label (s)', '12: Combobox', '13: ComboBox (s)',
           '14: OptionMenu', '15: OptionMenu (s)', '16: Radio', '17: Radio (s)',
           '18: Message', '19: Listbox', '20: Scale', '21: Spinbox',
           '22: Progressbar','23: Toolbar', '24: Notebook',
           '98: colspan <', '99: rowspan ^')

orient_values=('N','NE','E','SE','S','SW','W','NW','N+S','E+W')

label_defaults=['title','N']
chbox_defaults=[['One','Two','Three'], #values of 1st
                [],[],[],
                '','','','', #title cell
                'N','16']    #orientation, cell width
optmenu_defaults=[['One','Two','Three'], #values of 1st
                [],[],[],
                '','','','', #title cell
                'N','16']    #orientation, cell width
radio_defaults=[['One','Two','Three'], #values of 1st
                [],[],[],
                '','','','', #title cell
                'N','16']    #orientation, cell width
entry_defaults=['N','17',''] # orient, width, text
canvas_defaults=['200','250','white','N'] # width, height, color, orient
text_defaults=['10','10','N','1: w/o scroll','','white','black'] # w,h,orient,slide,def.text,bg.color, text.color

### main window
abl1=Tk()
abl1.title("Tkinter GUI designer v1.1")

nb00aa=Notebook(abl1)
nb00aa.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
f0=Frame(nb00aa)
nb00aa.add(f0,text='Widget selection')
f1=Frame(nb00aa)
nb00aa.add(f1,text='Settings')
nb00aa.select(f0)
nb00aa.enable_traversal()

frame1=Frame(f0, borderwidth=1)
frame1.grid(row=2, column=1)
i1_1=Combobox(frame1)
i1_2=Combobox(frame1)
i1_3=Combobox(frame1)
i1_4=Combobox(frame1)
i1_5=Combobox(frame1)
i2_1=Combobox(frame1)
i2_2=Combobox(frame1)
i2_3=Combobox(frame1)
i2_4=Combobox(frame1)
i2_5=Combobox(frame1)
i3_1=Combobox(frame1)
i3_2=Combobox(frame1)
i3_3=Combobox(frame1)
i3_4=Combobox(frame1)
i3_5=Combobox(frame1)
i4_1=Combobox(frame1)
i4_2=Combobox(frame1)
i4_3=Combobox(frame1)
i4_4=Combobox(frame1)
i4_5=Combobox(frame1)
i5_1=Combobox(frame1)
i5_2=Combobox(frame1)
i5_3=Combobox(frame1)
i5_4=Combobox(frame1)
i5_5=Combobox(frame1)
i6_1=Combobox(frame1)
i6_2=Combobox(frame1)
i6_3=Combobox(frame1)
i6_4=Combobox(frame1)
i6_5=Combobox(frame1)
i7_1=Combobox(frame1)
i7_2=Combobox(frame1)
i7_3=Combobox(frame1)
i7_4=Combobox(frame1)
i7_5=Combobox(frame1)
i8_1=Combobox(frame1)
i8_2=Combobox(frame1)
i8_3=Combobox(frame1)
i8_4=Combobox(frame1)
i8_5=Combobox(frame1)
i9_1=Combobox(frame1)
i9_2=Combobox(frame1)
i9_3=Combobox(frame1)
i9_4=Combobox(frame1)
i9_5=Combobox(frame1)

cellak=[i1_1, i1_2, i1_3, i1_4, i1_5,
        i2_1, i2_2, i2_3, i2_4, i2_5,
        i3_1, i3_2, i3_3, i3_4, i3_5,
        i4_1, i4_2, i4_3, i4_4, i4_5,
        i5_1, i5_2, i5_3, i5_4, i5_5,
        i6_1, i6_2, i6_3, i6_4, i6_5,
        i7_1, i7_2, i7_3, i7_4, i7_5,
        i8_1, i8_2, i8_3, i8_4, i8_5,
        i9_1, i9_2, i9_3, i9_4, i9_5]

gombkeret=Frame(f0, borderwidth=0)
gombkeret.grid(row=2, column=3)
gomb=Button(gombkeret,text='Start',command=kivalaszto2)
gomb2=Button(gombkeret,text='Finalize',command=finalize, state=DISABLED) # Finalize button OFF, avoid early or repeated click
gomb3=Button(f0,text='Reset',command=reset2)                      
gomb4=Button(gombkeret,text='Check',command=updatecell) #colspan,rowspan update
i1_1['values']=selection
i1_2['values']=selection
i1_3['values']=selection
i1_4['values']=selection
i1_5['values']=selection
i2_1['values']=selection
i2_2['values']=selection
i2_3['values']=selection
i2_4['values']=selection
i2_5['values']=selection
i3_1['values']=selection
i3_2['values']=selection
i3_3['values']=selection
i3_4['values']=selection
i3_5['values']=selection
i3_1['values']=selection
i3_2['values']=selection
i3_3['values']=selection
i3_4['values']=selection
i3_5['values']=selection
i4_1['values']=selection
i4_2['values']=selection
i4_3['values']=selection
i4_4['values']=selection
i4_5['values']=selection
i5_1['values']=selection
i5_2['values']=selection
i5_3['values']=selection
i5_4['values']=selection
i5_5['values']=selection
i6_1['values']=selection
i6_2['values']=selection
i6_3['values']=selection
i6_4['values']=selection
i6_5['values']=selection
i7_1['values']=selection
i7_2['values']=selection
i7_3['values']=selection
i7_4['values']=selection
i7_5['values']=selection
i8_1['values']=selection
i8_2['values']=selection
i8_3['values']=selection
i8_4['values']=selection
i8_5['values']=selection
i9_1['values']=selection
i9_2['values']=selection
i9_3['values']=selection
i9_4['values']=selection
i9_5['values']=selection
def_status()
cmke1=Label(frame1, foreground='red', text='r0')
cmke2=Label(frame1, foreground='red',text='r1')
cmke3=Label(frame1, foreground='red',text='r2')
cmke4=Label(frame1, foreground='red',text='r3')
cmke5=Label(frame1, foreground='red',text='r4')
cmke6=Label(frame1, foreground='red',text='r5')
cmke7=Label(frame1, foreground='red',text='r6')
cmke8=Label(frame1, foreground='red',text='r7')
cmke9=Label(frame1, foreground='red',text='r8')
cmke1x=Label(frame1, foreground='green',text='c0')
cmke2x=Label(frame1, foreground='green',text='c1')
cmke3x=Label(frame1, foreground='green',text='c2')
cmke4x=Label(frame1, foreground='green',text='c3')
cmke5x=Label(frame1, foreground='green',text='c4')
msg=Label(abl1, foreground='black',text='opened windows: '+str(window_counter)+'; message: Select widgets')
cmke1.grid(row=1, column=0,sticky=N)
cmke2.grid(row=2, column=0,sticky=N)
cmke3.grid(row=3, column=0,sticky=N)
cmke4.grid(row=4, column=0,sticky=N)
cmke5.grid(row=5, column=0,sticky=N)
cmke6.grid(row=6, column=0,sticky=N)
cmke7.grid(row=7, column=0,sticky=N)
cmke8.grid(row=8, column=0,sticky=N)
cmke9.grid(row=9, column=0,sticky=N)
cmke1x.grid(row=0, column=1,sticky=N)
cmke2x.grid(row=0, column=2,sticky=N)
cmke3x.grid(row=0, column=3,sticky=N)
cmke4x.grid(row=0, column=4,sticky=N)
cmke5x.grid(row=0, column=5,sticky=N)
msg.grid(row=1, column=0, columnspan=5 ,sticky=W)
titlekeret=Frame(f0, borderwidth=0)
titlekeret.grid(row=0, column=1)
titlcmke=Label(titlekeret, text='    Window title:')
titlcmke.grid(row=0, column=1,sticky=E)
title_entry=Entry(titlekeret, width=30)
title_entry.insert(0, "My window")
title_entry.grid(row=0, column=2, sticky=E)
cmkei=Label(titlekeret, text='hint', foreground='black', background='orange')
cmkei.grid(row=0, column=0, sticky=N)
CreateToolTip(cmkei, text=main_tip)

menubar00aa=Menu(abl1)
submenu00aa0=Menu(menubar00aa, tearoff=0)
menubar00aa.add_cascade(label='File', menu=submenu00aa0)
submenu00aa0.add_separator()
submenu00aa0.add_command(label='Open selection & settings', command=fileopen)
submenu00aa0.add_command(label='Save selection & settings', command=filesave)
submenu00aa0.add_separator()
submenu00aa0.add_command(label='Exit', command=abl1.destroy)
submenu00aa1=Menu(menubar00aa, tearoff=0)
menubar00aa.add_cascade(label='Function', menu=submenu00aa1)
submenu00aa1.add_separator()
submenu00aa1.add_command(label='Check', command=updatecell)
submenu00aa1.add_command(label='Start', command=kivalaszto2)
submenu00aa1.add_command(label='Finalize', command=finalize, state=DISABLED)
submenu00aa1.add_separator()
submenu00aa1.add_command(label='Reset', command=reset2)
submenu00aa3=Menu(menubar00aa, tearoff=0)
menubar00aa.add_cascade(label='Info', menu=submenu00aa3)
submenu00aa3.add_separator()
submenu00aa3.add_command(label='Open Github', command=github)
submenu00aa3.add_command(label='Show email at bottom', command=contact)
submenu00aa3.add_command(label='Open Paypal donate', command=donate)
abl1.config(menu=menubar00aa)

textkeret=Frame(f0, relief='flat', borderwidth=1)
textkeret.grid(row=5, column=1, sticky=NE)
text1=Text(textkeret,height=18,width=88, background='light yellow', wrap=NONE)
scrolly1=Scrollbar(textkeret, orient=VERTICAL,command=text1.yview)
scrolly2=Scrollbar(textkeret, orient=HORIZONTAL,command=text1.xview)
text1['yscrollcommand']=scrolly1.set
text1['xscrollcommand']=scrolly2.set
text1.grid(row=0, column=0, sticky=E)
scrolly1.grid(row=0, column=1, sticky=N+S)
scrolly2.grid(row=1, column=0, sticky=W+E)
text1.insert(INSERT,welcometext)
i1_1.grid(row=1, column=1, sticky=W)
i1_2.grid(row=1, column=2, sticky=W)
i1_3.grid(row=1,column=3, sticky=W)
i1_4.grid(row=1,column=4, sticky=W)
i1_5.grid(row=1,column=5, sticky=W)
i2_1.grid(row=2, column=1, sticky=W)
i2_2.grid(row=2, column=2, sticky=W)
i2_3.grid(row=2,column=3, sticky=W)
i2_4.grid(row=2,column=4, sticky=W)
i2_5.grid(row=2,column=5, sticky=W)
i3_1.grid(row=3, column=1, sticky=W)
i3_2.grid(row=3, column=2, sticky=W)
i3_3.grid(row=3,column=3, sticky=W)
i3_4.grid(row=3,column=4, sticky=W)
i3_5.grid(row=3,column=5, sticky=W)
i4_1.grid(row=4, column=1, sticky=W)
i4_2.grid(row=4, column=2, sticky=W)
i4_3.grid(row=4,column=3, sticky=W)
i4_4.grid(row=4,column=4, sticky=W)
i4_5.grid(row=4,column=5, sticky=W)
i5_1.grid(row=5, column=1, sticky=W)
i5_2.grid(row=5, column=2, sticky=W)
i5_3.grid(row=5,column=3, sticky=W)
i5_4.grid(row=5,column=4, sticky=W)
i5_5.grid(row=5,column=5, sticky=W)
i6_1.grid(row=6, column=1, sticky=W)
i6_2.grid(row=6, column=2, sticky=W)
i6_3.grid(row=6,column=3, sticky=W)
i6_4.grid(row=6,column=4, sticky=W)
i6_5.grid(row=6,column=5, sticky=W)
i7_1.grid(row=7, column=1, sticky=W)
i7_2.grid(row=7, column=2, sticky=W)
i7_3.grid(row=7,column=3, sticky=W)
i7_4.grid(row=7,column=4, sticky=W)
i7_5.grid(row=7,column=5, sticky=W)
i8_1.grid(row=8, column=1, sticky=W)
i8_2.grid(row=8, column=2, sticky=W)
i8_3.grid(row=8,column=3, sticky=W)
i8_4.grid(row=8,column=4, sticky=W)
i8_5.grid(row=8,column=5, sticky=W)
i9_1.grid(row=9, column=1, sticky=W)
i9_2.grid(row=9, column=2, sticky=W)
i9_3.grid(row=9,column=3, sticky=W)
i9_4.grid(row=9,column=4, sticky=W)
i9_5.grid(row=9,column=5, sticky=W)
gomb4.grid(row=0,column=0, sticky=N)
gomb.grid(row=1,column=0, sticky=N)
gomb2.grid(row=2,column=0, sticky=N)
gomb3.grid(row=5,column=3, sticky=S)
#2nd tab (default settings
frm0=LabelFrame(f1, text='Default parameters for widgets without option window.\n(Where is (s) located at the end of widget name)', height=200, width=250, relief='flat', borderwidth=1)
frm0.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=W, padx=10, pady=10)
labl1=Label(frm0, text='')
labl1.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=W)
#label
frm1=LabelFrame(frm0, text='Label (s)', height=200, width=250, relief='flat', borderwidth=1)
frm1.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=W)
labl1=Label(frm1, text='Orient.:')
labl1.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
labl11=Label(frm1, text='Text:')
labl11.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
chbox1=Combobox(frm1, width=4)
chbox1['values']=orient_values
chbox1.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
chbox1.current(0)
entr1=Entry(frm1)
entr1.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N)
#combobox
frm2=LabelFrame(frm0, text='ComboBox (s)', height=200, width=250, relief='flat', borderwidth=1)
frm2.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=W)
labl21=Label(frm2, text='Orient.:')
labl21.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
labl22=Label(frm2, text='value 1:')
labl22.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
labl23=Label(frm2, text='value 2:')
labl23.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=N)
labl24=Label(frm2, text='value 3:')
labl24.grid(row=0, column=3, columnspan=1, rowspan=1, sticky=N)
chbox2=Combobox(frm2, width=4)
chbox2['values']=orient_values
chbox2.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
chbox2.current(0)
entr21=Entry(frm2)
entr21.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N)
entr22=Entry(frm2)
entr22.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N)
entr23=Entry(frm2)
entr23.grid(row=1, column=3, columnspan=1, rowspan=1, sticky=N)
#optionmenu
frm3=LabelFrame(frm0, text='OptionMenu (s)', height=200, width=250, relief='flat', borderwidth=1)
frm3.grid(row=3, column=1, columnspan=1, rowspan=1, sticky=W)
labl31=Label(frm3, text='Orient.:')
labl31.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
labl32=Label(frm3, text='value 1:')
labl32.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
labl33=Label(frm3, text='value 2:')
labl33.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=N)
labl34=Label(frm3, text='value 3:')
labl34.grid(row=0, column=3, columnspan=1, rowspan=1, sticky=N)
chbox3=Combobox(frm3, width=4)
chbox3['values']=orient_values
chbox3.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
chbox3.current(0)
entr31=Entry(frm3)
entr31.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N)
entr32=Entry(frm3)
entr32.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N)
entr33=Entry(frm3)
entr33.grid(row=1, column=3, columnspan=1, rowspan=1, sticky=N)
#radio
frm4=LabelFrame(frm0, text='Radio (s)', height=200, width=250, relief='flat', borderwidth=1)
frm4.grid(row=4, column=1, columnspan=1, rowspan=1, sticky=W)
labl41=Label(frm4, text='Orient.:')
labl41.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
labl42=Label(frm4, text='value 1:')
labl42.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
labl43=Label(frm4, text='value 2:')
labl43.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=N)
labl44=Label(frm4, text='value 3:')
labl44.grid(row=0, column=3, columnspan=1, rowspan=1, sticky=N)
chbox4=Combobox(frm4, width=4)
chbox4['values']=orient_values
chbox4.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
chbox4.current(0)
entr41=Entry(frm4)
entr41.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N)
entr42=Entry(frm4)
entr42.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N)
entr43=Entry(frm4)
entr43.grid(row=1, column=3, columnspan=1, rowspan=1, sticky=N)
#entry
frm5=LabelFrame(frm0, text='Entry (s)', height=200, width=250, relief='flat', borderwidth=1)
frm5.grid(row=5, column=1, columnspan=1, rowspan=1, sticky=W)
labl51=Label(frm5, text='Orient.:')
labl51.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
labl52=Label(frm5, text='width:')
labl52.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
labl53=Label(frm5, text='default value:')
labl53.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=N)
chbox5=Combobox(frm5, width=4)
chbox5['values']=orient_values
chbox5.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
chbox5.current(0)
entr51=Entry(frm5)
entr51.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N)
entr52=Entry(frm5)
entr52.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N)
#canvas
frm6=LabelFrame(frm0, text='Canvas (s)', height=200, width=250, relief='flat', borderwidth=1)
frm6.grid(row=6, column=1, columnspan=1, rowspan=1, sticky=W)
labl61=Label(frm6, text='Orient.:')
labl61.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
labl62=Label(frm6, text='width:')
labl62.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
labl63=Label(frm6, text='height:')
labl63.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=N)
labl63=Label(frm6, text='color:')
labl63.grid(row=0, column=3, columnspan=1, rowspan=1, sticky=N)
chbox61=Combobox(frm6, width=4)
chbox61['values']=orient_values
chbox61.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
chbox61.current(0)
entr61=Entry(frm6)
entr61.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N)
entr62=Entry(frm6)
entr62.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N)
chbox62=Combobox(frm6, width=17)
chbox62['values']=('white','light yellow','snow','bisque','gray','cyan','sienna1','thistle','pick a color')
chbox62.current(0)
chbox62.grid(row=1, column=3,sticky=N)
#text
frm7=LabelFrame(frm0, text='Text (s)', height=200, width=250, relief='flat', borderwidth=1)
frm7.grid(row=7, column=1, columnspan=1, rowspan=1, sticky=W, pady=5)
labl71=Label(frm7, text='Orient.:')
labl71.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)
labl72=Label(frm7, text='width:')
labl72.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
labl73=Label(frm7, text='height:')
labl73.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=N)
labl73=Label(frm7, text='scroll:')
labl73.grid(row=0, column=3, columnspan=1, rowspan=1, sticky=N)
labl74=Label(frm7, text='default text:')
labl74.grid(row=0, column=4, columnspan=1, rowspan=1, sticky=N)
chbox71=Combobox(frm7, width=4)
chbox71['values']=orient_values
chbox71.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)
chbox71.current(0)
entr71=Entry(frm7)
entr71.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N)
entr72=Entry(frm7)
entr72.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N)
chbox72=Combobox(frm7, width=17)
chbox72['values']=('1: w/o scroll','2: w vertical scroll','3: w horizontal scroll','4: with v/h scroll')
chbox72.current(0)
chbox72.grid(row=1, column=3,sticky=N)
entr73=Entry(frm7)
entr73.grid(row=1, column=4, columnspan=1, rowspan=1, sticky=N)
## func/obj
frm8=LabelFrame(f1, text='Generated code type:', height=200, width=250, relief='flat', borderwidth=1)
frm8.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)
resulttype = IntVar()
radiob0=Radiobutton(frm8, text='Functions',variable=resulttype, value=0)
radiob0.grid(row=0, column=0, sticky=W)
radiob1=Radiobutton(frm8, text='Object (class)',variable=resulttype, value=1)
radiob1.grid(row=1, column=0, sticky=W)

##
set_defaults()
btntab1=Button(frm0,text='Apply',command=defaults)
btntab1.grid(row=10, column=1, columnspan=1, rowspan=1, sticky=SW)

abl1.mainloop()

