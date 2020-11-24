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
#radio, message, frame
#
#
# v0.4:    selection area 4x4
# v0.4.6:  selection area 5x5
# v0.5:    bigger widget selection area 5x7
# v0.5.9:  Label, Canvas, Text options
# v.0.6:   All elements with uniqe numbers
# v.0.6.5: CheckBox window options, canvas and text color options
# v.0.6.8: Customizable Radio and Option menu
# v.0.7:   rowspan,columnspan implemented, 5x9
# v.0.8:   universal 2x2 frame
# v.0.8.1  In case of 1 button there is no frame. You can use W+E to span button
#          Universal frame numbering bugs fixed
# v.0.8.3  Universal frame with text: LabelFrame; without: Frame 
#
# plans:      
#      * save cell selection
#
#
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import colorchooser

# --- Windows moduls
class Boxablak:
    "Checkbox and option selection window modul"
    def __init__(self,abl1,tipus,rc,frame_name):
        self.frame_name=frame_name
        self.tipus=tipus # 0=combobox, 1=optionmenu, 2=radio
        self.rc=rc
        self.c=rc[0]
        self.r=rc[1]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.o=''
        self.x=''
        self.output=['','','',      #value lines
                     '','','',
                     '','','',
                     '','','',
                     '','','','',   #text field texts 1,2,3,4
                     '','']            #orient.
        self.abl1=abl1
        self.abl2=Toplevel(self.abl1)
        if(self.tipus==0):
            self.abl2.title('ComboBox options: c'+str(self.c)+', r'+str(self.r))
        if(self.tipus==1):
            self.abl2.title('Option menu options: c'+str(self.c)+', r'+str(self.r))
        if(self.tipus==2):
            self.abl2.title('Radio options: c'+str(self.c)+', r'+str(self.r))
        self.ablak=Frame(self.abl2, relief='flat', borderwidth=1)
        self.ablak.grid(row=0, column=0)
        self.bmezo1_1_1=Entry(self.ablak)
        self.bmezo1_1_1.grid(row=0, column=2,sticky=N)
        self.bmezo1_1_1.insert(0, "One")
        self.bmezo1_1_2=Entry(self.ablak)
        self.bmezo1_1_2.grid(row=1, column=2,sticky=N)
        self.bmezo1_1_2.insert(0, "Two")
        self.bmezo1_1_3=Entry(self.ablak)
        self.bmezo1_1_3.grid(row=2, column=2,sticky=N)        
        self.bmezo1_2_1=Entry(self.ablak)
        self.bmezo1_2_1.grid(row=0, column=4,sticky=N)
        self.bmezo1_2_2=Entry(self.ablak)
        self.bmezo1_2_2.grid(row=1, column=4,sticky=N)
        self.bmezo1_2_3=Entry(self.ablak)
        self.bmezo1_2_3.grid(row=2, column=4,sticky=N)
        self.bmezo2_1_1=Entry(self.ablak)
        self.bmezo2_1_1.grid(row=4, column=2,sticky=N)
        self.bmezo2_1_2=Entry(self.ablak)
        self.bmezo2_1_2.grid(row=5, column=2,sticky=N)
        self.bmezo2_1_3=Entry(self.ablak)
        self.bmezo2_1_3.grid(row=6, column=2,sticky=N)        
        self.bmezo2_2_1=Entry(self.ablak)
        self.bmezo2_2_1.grid(row=4, column=4,sticky=N)
        self.bmezo2_2_2=Entry(self.ablak)
        self.bmezo2_2_2.grid(row=5, column=4,sticky=N)
        self.bmezo2_2_3=Entry(self.ablak)
        self.bmezo2_2_3.grid(row=6, column=4,sticky=N)

        if(self.tipus!=2):
            self.bmezo1=Entry(self.ablak)
            self.bmezo1.grid(row=1, column=1,sticky=N)
            self.bmezo2=Entry(self.ablak)
            self.bmezo2.grid(row=1, column=3,sticky=N)
            self.bmezo3=Entry(self.ablak)
            self.bmezo3.grid(row=5, column=1,sticky=N)
            self.bmezo4=Entry(self.ablak)
            self.bmezo4.grid(row=5, column=3,sticky=N)
            self.bmezo1.insert(0, "Label-1")
            self.bmezo2.insert(0, "Label-2")
            self.bmezo3.insert(0, "Label-3")
            self.bmezo4.insert(0, "Label-4")
        
        self.cmke1=Label(self.ablak, text='Orient.')
        self.cmke1.grid(row=1, column=0,sticky=N)
        self.cmke6=Label(self.ablak, text='Cell width')
        self.cmke6.grid(row=3, column=0,sticky=N)
        self.cmke2=Label(self.ablak, text='1/1')
        self.cmke2.grid(row=0, column=1,sticky=E)
        self.cmke3=Label(self.ablak, text='1/2')
        self.cmke3.grid(row=0, column=3,sticky=E)
        self.cmke4=Label(self.ablak, text='2/1')
        self.cmke4.grid(row=4, column=1,sticky=E)
        self.cmke5=Label(self.ablak, text='2/2')
        self.cmke5.grid(row=4, column=3,sticky=E)
        self.kret60=Frame(self.ablak, relief='flat', borderwidth=1)
        self.kret60.grid(row=6, column=0, sticky=N)
        self.gmb1=Button(self.kret60,text='Apply',command=self.cb_ertek)
        self.gmb1.grid(row=0, column=0)
        self.chbox1=Combobox(self.ablak, width=4)
        self.chbox1['values']=('N','NE','E','SE','S','SW','W','NW','N+S','E+W')
        self.chbox1.current(0)
        self.chbox1.grid(row=2, column=0,sticky=S)
        self.chbox2=Combobox(self.ablak, width=4)
        self.chbox2['values']=('auto','4','6','10','12','14','')
        self.chbox2.current(0)
        self.chbox2.grid(row=4, column=0,sticky=S)
        if (self.tipus>0):
            self.chbox2.configure(state=DISABLED)
            
    def cb_ertek(self):
        self.output[0],self.output[1],self.output[2]=self.bmezo1_1_1.get(),self.bmezo1_1_2.get(),self.bmezo1_1_3.get() #field value to output list
        self.output[3],self.output[4],self.output[5]=self.bmezo1_2_1.get(),self.bmezo1_2_2.get(),self.bmezo1_2_3.get() #first 12 elements of combox values
        self.output[6],self.output[7],self.output[8]=self.bmezo2_1_1.get(),self.bmezo2_1_2.get(),self.bmezo2_1_3.get()
        self.output[9],self.output[10],self.output[11]=self.bmezo2_2_1.get(),self.bmezo2_2_2.get(),self.bmezo2_2_3.get()
        if(self.tipus!=2):
            self.output[12],self.output[13],self.output[14],self.output[15]=self.bmezo1.get(),self.bmezo2.get(),self.bmezo3.get(),self.bmezo4.get() #label texts
        self.output[16]=self.chbox1.get() #oriantation
        self.output[17]=self.chbox2.get() #cell width
        if (self.output[17]):
            self.output[17]=self.cellaw()
        self.abl2.destroy()
        if (self.tipus==0):
            self.comboxablak()
        if (self.tipus==1):
            self.omenuablak()
        if (self.tipus==2):
            self.radioboxablak()
    def kiir(self,x):
        self.x=x
        if(self.x!=''):
            gomb2.configure(state=NORMAL) #activate Finalize button
            text1.insert(INSERT,self.x)   #text insert
            text1.insert(INSERT,'\n')

    def cellaw(self): #determine cell width
        self.templist=[]
        for self.i in range(12):
            self.templist.append(len(self.output[self.i]))
        self.cw=(max(self.templist))+4
        return self.cw
    
    def comboxablak(self):
        self.combox=Combox(self.rc,self.output,self.frame_name)
        self.osszes=self.combox.generator()
        self.kiir('#------ComboBox: c'+str(self.c)+', r'+str(self.r)+'------')
        self.kiir(self.osszes)
    def omenuablak(self):
        self.optmenu=Optmenu(self.rc,self.output,self.frame_name)
        self.osszes=self.optmenu.generator()
        self.kiir('#------Option menu: c'+str(self.c)+', r'+str(self.r)+'------')
        self.kiir(self.osszes)
    def radioboxablak(self):
        self.radiobox=Radiobox(self.rc,self.output,self.frame_name)
        self.osszes=self.radiobox.generator()
        self.kiir('#------Radio: c'+str(self.c)+', r'+str(self.r)+'------')
        self.kiir(self.osszes)
        

# ------ Menu generator
class Menuk:
    "Menu generator modul"
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
        self.f1, self.f2, self.f3=inputlist[0],inputlist[1],inputlist[2]
        self.f11, self.f21, self.f31=inputlist[3],inputlist[4],inputlist[5]
        self.f12, self.f22, self.f32=inputlist[6],inputlist[7],inputlist[8]
        self.f13, self.f23, self.f33=inputlist[9],inputlist[10],inputlist[11]
        self.o=self.inputlist[12]
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.kret='kret'+str(self.keretszam)+'=Frame('+self.frame_name+', relief='+"'"+'raised'+"'"+', borderwidth=1)\nkret'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+str(self.o)+')'
        self.msz1='menu'+self.keretszam+str(self.menuszam)+'=Menubutton(kret'+str(self.keretszam)+',text='+"'"+str(self.f1)+"'"+')'
        self.msz2='mf'+self.keretszam+str(self.menuszam)+'=Menu(menu'+self.keretszam+str(self.menuszam)+')'
        self.msz3='mf'+self.keretszam+str(self.menuszam)+'.add_command(label='+"'"+str(self.f11)+"'"+',command=k_ablak.destroy, state=NORMAL)'
        if(self.f12!=''):
            self.msz3=self.msz3+'\nmf'+self.keretszam+str(self.menuszam)+'.add_command(label='+"'"+str(self.f12)+"'"+',command=k_ablak.destroy, state=NORMAL)'
            if(self.f13!=''):
                self.msz3=self.msz3+'\nmf'+self.keretszam+str(self.menuszam)+'.add_command(label='+"'"+str(self.f13)+"'"+',command=k_ablak.destroy, state=NORMAL)'    
        self.msz5='menu'+self.keretszam+str(self.menuszam)+'.configure(menu=mf'+self.keretszam+str(self.menuszam)+')'
        self.mszv='menu'+self.keretszam+str(self.menuszam)+'.grid(row=0, column=0, sticky=NW)'

        if(self.f2!=''):
            self.msz1=self.msz1+'\nmenu'+self.keretszam+str(self.menuszam+1)+'=Menubutton(kret'+str(self.keretszam)+',text='+"'"+str(self.f2)+"'"+')'
            self.msz2=self.msz2+'\nmf'+self.keretszam+str(self.menuszam+1)+'=Menu(menu'+self.keretszam+str(self.menuszam+1)+')'
            self.msz3=self.msz3+'\nmf'+self.keretszam+str(self.menuszam+1)+'.add_command(label='+"'"+str(self.f21)+"'"+',command=k_ablak.destroy, state=NORMAL)'
            if(self.f22!=''):
                self.msz3=self.msz3+'\nmf'+self.keretszam+str(self.menuszam+1)+'.add_command(label='+"'"+str(self.f22)+"'"+',command=k_ablak.destroy, state=NORMAL)'
                if(self.f23!=''):
                    self.msz3=self.msz3+'\nmf'+self.keretszam+str(self.menuszam+1)+'.add_command(label='+"'"+str(self.f23)+"'"+',command=k_ablak.destroy, state=NORMAL)'    
            self.msz5=self.msz5+'\nmenu'+self.keretszam+str(self.menuszam+1)+'.configure(menu=mf'+self.keretszam+str(self.menuszam+1)+')'
            self.mszv=self.mszv+'\nmenu'+self.keretszam+str(self.menuszam+1)+'.grid(row=0, column=1, sticky=NW)'

            if(self.f3!=''):
                self.msz1=self.msz1+'\nmenu'+self.keretszam+str(self.menuszam+2)+'=Menubutton(kret'+str(self.keretszam)+',text='+"'"+str(self.f3)+"'"+')'
                self.msz2=self.msz2+'\nmf'+self.keretszam+str(self.menuszam+2)+'=Menu(menu'+self.keretszam+str(self.menuszam+2)+')'
                self.msz3=self.msz3+'\nmf'+self.keretszam+str(self.menuszam+2)+'.add_command(label='+"'"+str(self.f31)+"'"+',command=k_ablak.destroy, state=NORMAL)'
                if(self.f32!=''):
                    self.msz3=self.msz3+'\nmf'+self.keretszam+str(self.menuszam+2)+'.add_command(label='+"'"+str(self.f32)+"'"+',command=k_ablak.destroy, state=NORMAL)'
                    if(self.f33!=''):
                        self.msz3=self.msz3+'\nmf'+self.keretszam+str(self.menuszam+2)+'.add_command(label='+"'"+str(self.f33)+"'"+',command=k_ablak.destroy, state=NORMAL)'    
                self.msz5=self.msz5+'\nmenu'+self.keretszam+str(self.menuszam+2)+'.configure(menu=mf'+self.keretszam+str(self.menuszam+2)+')'
                self.mszv=self.mszv+'\nmenu'+self.keretszam+str(self.menuszam+2)+'.grid(row=0, column=2, sticky=NW)'   
        self.osszes=self.kret+'\n'+self.msz1+'\n'+self.msz2+'\n'+self.msz3+'\n'+self.msz5+'\n'+self.mszv
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
            self.gsz='gmb'+str(self.keretszam)+str(self.gombszam)+'=Button('+str(self.frame_name)+',text='+"'"+str(self.f1)+"'"+',command=k_ablak.destroy)'
            self.gszv='gmb'+str(self.keretszam)+str(self.gombszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+str(self.o)+')'
        else:
            self.kret='kret'+str(self.keretszam)+'=Frame('+self.frame_name+', relief='+"'flat'"+', borderwidth=1)\nkret'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+str(self.o)+')'
            self.gsz='gmb'+str(self.keretszam)+str(self.gombszam)+'=Button(kret'+str(self.keretszam)+',text='+"'"+str(self.f1)+"'"+',command=k_ablak.destroy)'
            self.gszv='gmb'+str(self.keretszam)+str(self.gombszam)+'.grid(row=0, column=0)'
        if(self.f2!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'=Button(kret'+str(self.keretszam)+',text='+"'"+str(self.f2)+"'"+',command=k_ablak.destroy)'
            self.gszv=self.gszv+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'.grid(row=0, column=1)'
        if(self.f3!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'=Button(kret'+str(self.keretszam)+',text='+"'"+str(self.f3)+"'"+',command=k_ablak.destroy)'
            self.gszv=self.gszv+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'.grid(row=0, column=2)'
        if(self.f11!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'=Button(kret'+str(self.keretszam)+',text='+"'"+str(self.f11)+"'"+',command=k_ablak.destroy)'
            self.gszv=self.gszv+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'.grid(row=1, column=0)'
        if(self.f21!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'=Button(kret'+str(self.keretszam)+',text='+"'"+str(self.f21)+"'"+',command=k_ablak.destroy)'
            self.gszv=self.gszv+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'.grid(row=1, column=1)'
        if(self.f31!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'=Button(kret'+str(self.keretszam)+',text='+"'"+str(self.f31)+"'"+',command=k_ablak.destroy)'
            self.gszv=self.gszv+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'.grid(row=1, column=2)'
        if(self.f12!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'=Button(kret'+str(self.keretszam)+',text='+"'"+str(self.f12)+"'"+',command=k_ablak.destroy)'
            self.gszv=self.gszv+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'.grid(row=2, column=0)'
        if(self.f22!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'=Button(kret'+str(self.keretszam)+',text='+"'"+str(self.f22)+"'"+',command=k_ablak.destroy)'
            self.gszv=self.gszv+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'.grid(row=2, column=1)'
        if(self.f32!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'=Button(kret'+str(self.keretszam)+',text='+"'"+str(self.f32)+"'"+',command=k_ablak.destroy)'
            self.gszv=self.gszv+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'.grid(row=2, column=2)'
        if(self.f13!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'=Button(kret'+str(self.keretszam)+',text='+"'"+str(self.f13)+"'"+',command=k_ablak.destroy)'
            self.gszv=self.gszv+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'.grid(row=3, column=0)'
        if(self.f23!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'=Button(kret'+str(self.keretszam)+',text='+"'"+str(self.f23)+"'"+',command=k_ablak.destroy)'
            self.gszv=self.gszv+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'.grid(row=3, column=1)'
        if(self.f33!=''):
            self.gombszam=self.gombszam+1
            self.gsz=self.gsz+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'=Button(kret'+str(self.keretszam)+',text='+"'"+str(self.f33)+"'"+',command=k_ablak.destroy)'
            self.gszv=self.gszv+'\ngmb'+str(self.keretszam)+str(self.gombszam)+'.grid(row=3, column=2)'
        self.osszes=self.kret+'\n'+self.gsz+'\n'+self.gszv
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
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.csz='can'+self.keretszam+str(self.canszam)+'=Canvas('+self.frame_name+',bg='+"'"+self.canc+"'"+',height='+str(self.canh)+', width='+str(self.canw)+')'
        self.cszv='can'+self.keretszam+str(self.canszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+',sticky='+self.cano+')'
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
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        if(self.s[0]=='3' or self.s[0]=='4'):
            self.wrap=',wrap=NONE'
        self.kret='kret'+str(self.keretszam)+'=Frame('+self.frame_name+', relief='+"'flat'"+', borderwidth=1)\nkret'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky=N)'
        self.sz1='text'+self.keretszam+str(self.mezoszam)+'=Text(kret'+str(self.keretszam)+',height='+str(self.h)+',width='+str(self.w)+str(self.wrap)+',bg='+"'"+self.bg+"'"+',fg='+"'"+self.fg+"'"+')'
        if(self.s[0]=='2'): # függ csúszka
            self.sz2='scrolly'+self.keretszam+str(self.mezoszam)+'=Scrollbar(kret'+str(self.keretszam)+', orient=VERTICAL,command=text'+self.keretszam+str(self.mezoszam)+'.yview)'
            self.sz3='text'+self.keretszam+str(self.mezoszam)+'['+"'yscrollcommand'"+']=scrolly'+self.keretszam+str(self.mezoszam)+'.set'
            self.szcsv='scrolly'+self.keretszam+str(self.mezoszam)+'.grid(row=0, column=1 ,sticky=N+S)'
        if(self.s[0]=='3'): # víz csúszka
            self.sz2='scrollx'+self.keretszam+str(self.mezoszam)+'=Scrollbar(kret'+str(self.keretszam)+', orient=HORIZONTAL,command=text'+self.keretszam+str(self.mezoszam)+'.xview)'
            self.sz3='text'+self.keretszam+str(self.mezoszam)+'['+"'xscrollcommand'"+']=scrollx'+self.keretszam+str(self.mezoszam)+'.set'
            self.szcsv='scrollx'+self.keretszam+str(self.mezoszam)+'.grid(row=1, column=0 ,sticky=E+W)'
        if(self.s[0]=='4'): # mindkettő
            self.sz2='scrolly'+self.keretszam+str(self.mezoszam)+'=Scrollbar(kret'+str(self.keretszam)+', orient=VERTICAL,command=text'+self.keretszam+str(self.mezoszam)+'.yview)\n'
            self.sz2=self.sz2+'scrollx'+self.keretszam+str(self.mezoszam)+'=Scrollbar(kret'+str(self.keretszam)+', orient=HORIZONTAL,command=text'+self.keretszam+str(self.mezoszam)+'.xview)'
            self.sz3='text'+self.keretszam+str(self.mezoszam)+'['+"'yscrollcommand'"+']=scrolly'+self.keretszam+str(self.mezoszam)+'.set\n'
            self.sz3=self.sz3+'text'+self.keretszam+str(self.mezoszam)+'['+"'xscrollcommand'"+']=scrollx'+self.keretszam+str(self.mezoszam)+'.set'
            self.szcsv='scrolly'+self.keretszam+str(self.mezoszam)+'.grid(row=0, column=1 ,sticky=N+S)\nscrollx'+self.keretszam+str(self.mezoszam)+'.grid(row=1, column=0 ,sticky=E+W)'
        if(self.s[0]=='1'): #nincs csúszka
            self.szcsv, self.sz2, self.sz3='','',''
        self.szv='text'+self.keretszam+str(self.mezoszam)+'.grid(row=0, column=0,sticky='+self.o+')'
        if (self.t!=''):
            self.szv=self.szv+'\ntext'+self.keretszam+str(self.mezoszam)+'.insert(INSERT,'+"'"+str(self.t)+"'"+')'
        
        self.osszes=self.kret+'\n'+self.sz1+'\n'+self.sz2+'\n'+self.sz3+'\n'+self.szv+'\n'+self.szcsv
        return self.osszes


class Beviteli:
    "Entry generator modul"
    def __init__(self,rc,frame_name):
        self.frame_name=frame_name
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.bevszam=0
        self.keretszam=''
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.b1='bmezo'+self.keretszam+str(self.bevszam)+'=Entry('+self.frame_name+')'
        self.bv='bmezo'+self.keretszam+str(self.bevszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky=N)'
        self.osszes=self.b1+'\n'+self.bv
        return self.osszes

class Cimke:
    "Label generator modul"
    def __init__(self,rc,labtxt,labo,frame_name):
        self.frame_name=frame_name
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.labtxt=labtxt
        self.labo=labo
        self.cimkeszam=0
        self.keretszam=''
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.c1='cmke'+self.keretszam+str(self.cimkeszam)+'=Label('+self.frame_name+', text='+"'"+str(self.labtxt)+"'"+')'
        self.cv='cmke'+self.keretszam+str(self.cimkeszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.labo+')'
        self.osszes=self.c1+'\n'+self.cv
        return self.osszes

class Keret():
    "Frame generator modul"
    def __init__(self,rc,output):
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
    def generator(self):
        self.krtszam=str(self.row)+str(self.col)
        if(self.ftext==''): # if there is not any text: (normal) Frame
            self.k1='kret'+self.krtszam+str(self.keretszam)+'=Frame(ablak, height='+str(self.h)+', width='+str(self.w)+', relief='+"'"+str(self.r)+"'"+', borderwidth='+str(self.bw)+')'
        else:  # if there is any text: LabelFrame
            self.k1='kret'+self.krtszam+str(self.keretszam)+'=LabelFrame(ablak, text='+"'"+self.ftext+"'"+', height='+str(self.h)+', width='+str(self.w)+', relief='+"'"+str(self.r)+"'"+', borderwidth='+str(self.bw)+')'
        self.kv='kret'+self.krtszam+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.labo+')'
        self.osszes=self.k1+'\n'+self.kv
        self.krt_name='kret'+self.krtszam+str(self.keretszam)
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
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)
        self.u1='uzent'+self.keretszam+str(self.uzenszam)+'=Message(ablak, width='+str(self.w)+', pady='+str(self.py)+', padx='+str(self.px)+', text='+"'"+str(self.szoveg)+"'"+')'
        self.uv='uzent'+self.keretszam+str(self.uzenszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+')'
        self.osszes=self.u1+'\n'+self.uv
        return self.osszes

class Combox:
    "Combox generator modul"
    def __init__(self,rc,lista,frame_name):
        self.frame_name=frame_name
        self.cboxszam=0
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.keretszam=''
        self.lista=lista
        self.cb1=''
        self.cb2=''
        self.cb3=''
        self.cbv=''
        self.v1=[self.lista[0],self.lista[1],self.lista[2]] #field values
        self.v2=[self.lista[3],self.lista[4],self.lista[5]]
        self.v3=[self.lista[6],self.lista[7],self.lista[8]]
        self.v4=[self.lista[9],self.lista[10],self.lista[11]]
        self.l1,self.l2,self.l3,self.l4=self.lista[12],self.lista[13],self.lista[14],self.lista[15] # label values
        self.orient=self.lista[16] #orientation
        self.cw=self.lista[17]     #cell width
     
        self.x=0
        for self.i in range(len(self.v1)): #remove '' empty items from v1 list and make tuple
            if(self.v1[self.i]==''):
               self.x=self.x+1     
        for self.i in range(self.x):
            self.v1.remove('')
        self.v1=tuple(self.v1)
        self.x=0

        for self.i in range(len(self.v2)): #remove '' empty items from v2 list and make tuple
            if(self.v2[self.i]==''):
               self.x=self.x+1     
        for self.i in range(self.x):
            self.v2.remove('')
        self.v2=tuple(self.v2)
        self.x=0

        for self.i in range(len(self.v3)): #remove '' empty items from v3 list and make tuple
            if(self.v3[self.i]==''):
               self.x=self.x+1     
        for self.i in range(self.x):
            self.v3.remove('')
        self.v3=tuple(self.v3)
        self.x=0

        for self.i in range(len(self.v4)): #remove '' empty items from v4 list and make tuple
            if(self.v4[self.i]==''):
               self.x=self.x+1     
        for self.i in range(self.x):
            self.v4.remove('')
        self.v4=tuple(self.v4)
        self.x=0
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.kret='kret'+str(self.keretszam)+'=Frame('+self.frame_name+', relief='+"'flat'"+', borderwidth=1)\nkret'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.orient+')'
        if(self.v1!=()):
            self.cb1=self.cb1+'\nchbox'+self.keretszam+str(self.cboxszam)+'=Combobox('+'kret'+str(self.keretszam)+', width='+str(self.cw)+')'
            self.cb2=self.cb2+'\nchbox'+self.keretszam+str(self.cboxszam)+'['+"'values'"+']='+str(self.v1)
            self.cb3=self.cb3+'\nchbox'+self.keretszam+str(self.cboxszam)+'.current(0)'
            self.cbv=self.cbv+'\nchbox'+self.keretszam+str(self.cboxszam)+'.grid(row=0, column=1,sticky=N)\ncmke'+self.keretszam+str(self.cboxszam)+'=Label('+'kret'+str(self.keretszam)+', text='+"'"+self.l1+"'"+')\ncmke'+self.keretszam+str(self.cboxszam)+'.grid(row=0, column=0,sticky=N)'
        if(self.v2!=()):
            self.cboxszam=1
            self.cb1=self.cb1+'\nchbox'+self.keretszam+str(self.cboxszam)+'=Combobox('+'kret'+str(self.keretszam)+', width='+str(self.cw)+')'
            self.cb2=self.cb2+'\nchbox'+self.keretszam+str(self.cboxszam)+'['+"'values'"+']='+str(self.v2)
            self.cb3=self.cb3+'\nchbox'+self.keretszam+str(self.cboxszam)+'.current(0)'
            self.cbv=self.cbv+'\nchbox'+self.keretszam+str(self.cboxszam)+'.grid(row=0, column=3,sticky=N)\ncmke'+self.keretszam+str(self.cboxszam)+'=Label('+'kret'+str(self.keretszam)+', text='+"'"+self.l2+"'"+')\ncmke'+self.keretszam+str(self.cboxszam)+'.grid(row=0, column=2,sticky=N)'
        if(self.v3!=()):
            self.cboxszam=2
            self.cb1=self.cb1+'\nchbox'+self.keretszam+str(self.cboxszam)+'=Combobox('+'kret'+str(self.keretszam)+', width='+str(self.cw)+')'
            self.cb2=self.cb2+'\nchbox'+self.keretszam+str(self.cboxszam)+'['+"'values'"+']='+str(self.v3)
            self.cb3=self.cb3+'\nchbox'+self.keretszam+str(self.cboxszam)+'.current(0)'
            self.cbv=self.cbv+'\nchbox'+self.keretszam+str(self.cboxszam)+'.grid(row=1, column=1,sticky=N)\ncmke'+self.keretszam+str(self.cboxszam)+'=Label('+'kret'+str(self.keretszam)+', text='+"'"+self.l3+"'"+')\ncmke'+self.keretszam+str(self.cboxszam)+'.grid(row=1, column=0,sticky=N)'
        if(self.v4!=()):
            self.cboxszam=3
            self.cb1=self.cb1+'\nchbox'+self.keretszam+str(self.cboxszam)+'=Combobox('+'kret'+str(self.keretszam)+', width='+str(self.cw)+')'
            self.cb2=self.cb2+'\nchbox'+self.keretszam+str(self.cboxszam)+'['+"'values'"+']='+str(self.v4)
            self.cb3=self.cb3+'\nchbox'+self.keretszam+str(self.cboxszam)+'.current(0)'
            self.cbv=self.cbv+'\nchbox'+self.keretszam+str(self.cboxszam)+'.grid(row=1, column=3,sticky=N)\ncmke'+self.keretszam+str(self.cboxszam)+'=Label('+'kret'+str(self.keretszam)+', text='+"'"+self.l4+"'"+')\ncmke'+self.keretszam+str(self.cboxszam)+'.grid(row=1, column=2,sticky=N)'
        self.osszes=self.kret+'\n'+self.cb1+self.cb2+self.cb3+self.cbv
        return self.osszes
        

class Optmenu:
    "Option menu generator modul"
    def __init__(self,rc,lista,frame_name):
        self.frame_name=frame_name
        self.lista=lista
        self.omszam=0
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.keretszam=''
        self.v1=[lista[0],lista[1],lista[2]] #field values
        self.v2=[lista[3],lista[4],lista[5]]
        self.v3=[lista[6],lista[7],lista[8]]
        self.v4=[lista[9],lista[10],lista[11]]
        self.l1,self.l2,self.l3,self.l4=lista[12],lista[13],lista[14],lista[15] # label values
        self.orient=lista[16] #orient.
        self.osszes=''
        self.om1,self.om2,self.om3,self.omv='','','',''
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.kret='kret'+str(self.keretszam)+'=Frame('+self.frame_name+', relief='+"'flat'"+', borderwidth=1)\nkret'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.orient+')\n'
        if(self.v1[0]!='' or self.v1[1]!='' or self.v1[2]!=''):
            self.omszam=0
            self.om1=self.om1+'var'+self.keretszam+str(self.omszam)+' = StringVar(kret'+str(self.keretszam)+')\n'
            self.om2=self.om2+'var'+self.keretszam+str(self.omszam)+'.set(0)\n'
            self.om3=self.om3+'opmenu'+self.keretszam+str(self.omszam)+'=OptionMenu(kret'+str(self.keretszam)+', var'+self.keretszam+str(self.omszam)+', '+"'"+'select'+"'"
            for self.i in self.v1: #remove empty cells
                if (self.i!=''):
                    self.om3=self.om3+','+"'"+str(self.i)+"'"+' '
            self.om3=self.om3+')\n'
            self.omv=self.omv+'opmenu'+self.keretszam+str(self.omszam)+'.grid(row=0, column=1, sticky=W)\ncmke'+self.keretszam+str(self.omszam)+'=Label('+'kret'+str(self.keretszam)+', text='+"'"+self.l1+"'"+')\ncmke'+self.keretszam+str(self.omszam)+'.grid(row=0, column=0,sticky=W)\n'
        
        if(self.v2[0]!='' or self.v2[1]!='' or self.v2[2]!=''):
            self.omszam=1
            self.om1=self.om1+'var'+self.keretszam+str(self.omszam)+' = StringVar(kret'+str(self.keretszam)+')\n'
            self.om2=self.om2+'var'+self.keretszam+str(self.omszam)+'.set(0)\n'
            self.om3=self.om3+'opmenu'+self.keretszam+str(self.omszam)+'=OptionMenu(kret'+str(self.keretszam)+', var'+self.keretszam+str(self.omszam)+','+"'"+'select'+"'"
            for self.i in self.v2:
                if (self.i!=''):
                    self.om3=self.om3+','+"'"+str(self.i)+"'"+' '
            self.om3=self.om3+')\n'
            self.omv=self.omv+'opmenu'+self.keretszam+str(self.omszam)+'.grid(row=0, column=3, sticky=W)\ncmke'+self.keretszam+str(self.omszam)+'=Label('+'kret'+str(self.keretszam)+', text='+"'"+self.l2+"'"+')\ncmke'+self.keretszam+str(self.omszam)+'.grid(row=0, column=2,sticky=W)\n'

        if(self.v3[0]!='' or self.v3[1]!='' or self.v3[2]!=''):
            self.omszam=2
            self.om1=self.om1+'var'+self.keretszam+str(self.omszam)+' = StringVar(kret'+str(self.keretszam)+')\n'
            self.om2=self.om2+'var'+self.keretszam+str(self.omszam)+'.set(0)\n'
            self.om3=self.om3+'opmenu'+self.keretszam+str(self.omszam)+'=OptionMenu(kret'+str(self.keretszam)+', var'+self.keretszam+str(self.omszam)+','+"'"+'select'+"'"
            for self.i in self.v3:
                if (self.i!=''):
                    self.om3=self.om3+','+"'"+str(self.i)+"'"+' '
            self.om3=self.om3+')\n'
            self.omv=self.omv+'opmenu'+self.keretszam+str(self.omszam)+'.grid(row=1, column=1, sticky=W)\ncmke'+self.keretszam+str(self.omszam)+'=Label('+'kret'+str(self.keretszam)+', text='+"'"+self.l3+"'"+')\ncmke'+self.keretszam+str(self.omszam)+'.grid(row=1, column=0,sticky=W)\n'

        if(self.v4[0]!='' or self.v4[1]!='' or self.v4[2]!=''):
            self.omszam=3
            self.om1=self.om1+'var'+self.keretszam+str(self.omszam)+' = StringVar(kret'+str(self.keretszam)+')\n'
            self.om2=self.om2+'var'+self.keretszam+str(self.omszam)+'.set(0)\n'
            self.om3=self.om3+'opmenu'+self.keretszam+str(self.omszam)+'=OptionMenu(kret'+str(self.keretszam)+', var'+self.keretszam+str(self.omszam)+','+"'"+'select'+"'"
            for self.i in self.v4:
                if (self.i!=''):
                    self.om3=self.om3+','+"'"+str(self.i)+"'"+' '
            self.om3=self.om3+')\n'
            self.omv=self.omv+'opmenu'+self.keretszam+str(self.omszam)+'.grid(row=1, column=3, sticky=W)\ncmke'+self.keretszam+str(self.omszam)+'=Label('+'kret'+str(self.keretszam)+', text='+"'"+self.l4+"'"+')\ncmke'+self.keretszam+str(self.omszam)+'.grid(row=1, column=2,sticky=W)\n'
        self.osszes=self.kret+self.om1+'\n'+self.om2+'\n'+self.om3+'\n'+self.omv
        return self.osszes

class Radiobox:
    "Radio box generator modul"
    def __init__(self,rc,lista,frame_name):
        self.frame_name=frame_name
        self.lista=lista
        self.chbszam=0
        self.col=rc[0]
        self.row=rc[1]
        self.cspan=rc[2]
        self.rspan=rc[3]
        self.base_c=rc[4]
        self.base_r=rc[5]
        self.kret=''
        self.keretszam=''
        self.v1=[lista[0],lista[1],lista[2]] #field values
        self.v2=[lista[3],lista[4],lista[5]]
        self.v3=[lista[6],lista[7],lista[8]]
        self.v4=[lista[9],lista[10],lista[11]]
        self.orient=lista[16] #orient.
        self.chb1=''
        self.chb2=''
        self.chb3=''
        self.chbv=''
    def generator(self):
        self.keretszam=str(self.row)+str(self.col)+str(self.base_r)+str(self.base_c)
        self.kret='kret'+str(self.keretszam)+'=Frame('+self.frame_name+', relief='+"'"+'flat'+"'"+', borderwidth=1)\nkret'+str(self.keretszam)+'.grid(row='+str(self.row)+', column='+str(self.col)+', columnspan='+str(self.cspan)+', rowspan='+str(self.rspan)+', sticky='+self.orient+')'
        if(self.v1[0]!=''):
            self.chb1=self.chb1+'v = IntVar()\n'
            self.chb2=self.chb2+'radiob'+self.keretszam+str(self.chbszam)+'=Radiobutton(kret'+str(self.keretszam)+', text='+"'"+str(self.v1[0])+"'"+',variable=v, value=1)\nradiob'+self.keretszam+str(self.chbszam)+'.grid(row=0, column=0, sticky=W)\n'
            if(self.v1[1]!=''):
                self.chb3=self.chb3+'radiob'+self.keretszam+str(self.chbszam+1)+'=Radiobutton(kret'+str(self.keretszam)+', text='+"'"+str(self.v1[1])+"'"+',variable=v, value=2)\nradiob'+self.keretszam+str(self.chbszam+1)+'.grid(row=1, column=0, sticky=W)\n'
                if(self.v1[2]!=''):
                    self.chb3=self.chb3+'radiob'+self.keretszam+str(self.chbszam+2)+'=Radiobutton(kret'+str(self.keretszam)+', text='+"'"+str(self.v1[2])+"'"+',variable=v, value=3)\nradiob'+self.keretszam+str(self.chbszam+2)+'.grid(row=2, column=0, sticky=W)\n'
        if(self.v2[0]!=''):
            self.chb1=self.chb1+'v1 = IntVar()\n'
            self.chb2=self.chb2+'radiob'+self.keretszam+str(self.chbszam+3)+'=Radiobutton(kret'+str(self.keretszam)+', text='+"'"+str(self.v2[0])+"'"+',variable=v1, value=1)\nradiob'+self.keretszam+str(self.chbszam+3)+'.grid(row=0, column=1, sticky=W)\n'
            if(self.v2[1]!=''):
                self.chb3=self.chb3+'radiob'+self.keretszam+str(self.chbszam+4)+'=Radiobutton(kret'+str(self.keretszam)+', text='+"'"+str(self.v2[1])+"'"+',variable=v1, value=2)\nradiob'+self.keretszam+str(self.chbszam+4)+'.grid(row=1, column=1, sticky=W)\n'
                if(self.v2[2]!=''):
                    self.chb3=self.chb3+'radiob'+self.keretszam+str(self.chbszam+5)+'=Radiobutton(kret'+str(self.keretszam)+', text='+"'"+str(self.v2[2])+"'"+',variable=v1, value=3)\nradiob'+self.keretszam+str(self.chbszam+5)+'.grid(row=2, column=1, sticky=W)\n'
        if(self.v3[0]!=''):
            self.chb1=self.chb1+'v2 = IntVar()\n'
            self.chb2=self.chb2+'radiob'+self.keretszam+str(self.chbszam+6)+'=Radiobutton(kret'+str(self.keretszam)+', text='+"'"+str(self.v3[0])+"'"+',variable=v2, value=1)\nradiob'+self.keretszam+str(self.chbszam+6)+'.grid(row=3, column=0, sticky=W)\n'
            if(self.v3[1]!=''):
                self.chb3=self.chb3+'radiob'+self.keretszam+str(self.chbszam+7)+'=Radiobutton(kret'+str(self.keretszam)+', text='+"'"+str(self.v3[1])+"'"+',variable=v2, value=2)\nradiob'+self.keretszam+str(self.chbszam+7)+'.grid(row=4, column=0, sticky=W)\n'
                if(self.v3[2]!=''):
                    self.chb3=self.chb3+'radiob'+self.keretszam+str(self.chbszam+8)+'=Radiobutton(kret'+str(self.keretszam)+', text='+"'"+str(self.v3[2])+"'"+',variable=v2, value=3)\nradiob'+self.keretszam+str(self.chbszam+8)+'.grid(row=5, column=0, sticky=W)\n'            
        if(self.v4[0]!=''):
            self.chb1=self.chb1+'v3 = IntVar()\n'
            self.chb2=self.chb2+'radiob'+self.keretszam+str(self.chbszam+9)+'=Radiobutton(kret'+str(self.keretszam)+', text='+"'"+str(self.v4[0])+"'"+',variable=v3, value=1)\nradiob'+self.keretszam+str(self.chbszam+9)+'.grid(row=3, column=1, sticky=W)\n'
            if(self.v4[1]!=''):
                self.chb3=self.chb3+'radiob'+self.keretszam+str(self.chbszam+10)+'=Radiobutton(kret'+str(self.keretszam)+', text='+"'"+str(self.v4[1])+"'"+',variable=v3, value=2)\nradiob'+self.keretszam+str(self.chbszam+10)+'.grid(row=4, column=1, sticky=W)\n'
                if(self.v4[2]!=''):
                    self.chb3=self.chb3+'radiob'+self.keretszam+str(self.chbszam+11)+'=Radiobutton(kret'+str(self.keretszam)+', text='+"'"+str(self.v4[2])+"'"+',variable=v3, value=3)\nradiob'+self.keretszam+str(self.chbszam+11)+'.grid(row=5, column=1, sticky=W)'            

        self.osszes=self.kret+'\n'+self.chb1+'\n'+self.chb2+'\n'+self.chb3+'\n'
        return self.osszes

#---- Option windows
def menuablak(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
#    rspan=rc[2]
#    cspan=rc[3]

    def m_ertek():
        output=['','','', #Főmenü 1   ,2   ,3
                '','','', #almenü 1.1 ,2.1 ,3.1
                '','','',  #almenü 1.2 ,2.2 ,3.2
                '','','',  #almenü 1.3 ,2.3 ,3.3
                '']        #orientation
        output[0],output[1],output[2]=bmezof1.get(),bmezof2.get(),bmezof3.get()
        output[3],output[4],output[5]=bmezof1_1.get(),bmezof2_1.get(),bmezof3_1.get()
        output[6],output[7],output[8]=bmezof1_2.get(),bmezof2_2.get(),bmezof3_2.get()
        output[9],output[10],output[11]=bmezof1_3.get(),bmezof2_3.get(),bmezof3_3.get()
        output[12]=chbox1m.get()
        menuk=Menuk(rc,output,frame_name)
        osszes=menuk.generator()
        kiir('#------Menu: c'+str(c)+', r'+str(r)+'------')
        kiir(osszes)
        abl2.destroy()
        
    abl2=Toplevel(abl1)
    abl2.title('Menu options: c'+str(c)+', r'+str(r))
    gmb=Button(abl2,text='Apply',command=m_ertek)
    cmke1=Label(abl2, text='Main menu:')
    cmke2=Label(abl2, text='Submenu:')
    bmezof1=Entry(abl2, textvariable=f1)
    bmezof1.insert(0,"File")
    bmezof2=Entry(abl2, textvariable=f2)
    bmezof3=Entry(abl2, textvariable=f3)
    bmezof1_1=Entry(abl2, textvariable=f11)
    bmezof1_1.insert(0,"Close")
    bmezof2_1=Entry(abl2, textvariable=f21)
    bmezof3_1=Entry(abl2, textvariable=f31)
    bmezof1_2=Entry(abl2, textvariable=f12)
    bmezof2_2=Entry(abl2, textvariable=f22)
    bmezof3_2=Entry(abl2, textvariable=f32)
    bmezof1_3=Entry(abl2, textvariable=f13)
    bmezof2_3=Entry(abl2, textvariable=f23)
    bmezof3_3=Entry(abl2, textvariable=f33)
    cmke1.grid(row=0, column=0)
    cmke2.grid(row=1, column=0)
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
    chbox1m=Combobox(abl2, width=4)
    chbox1m['values']=('N','NE','E','SE','S','SW','W','NW','N+S','E+W')
    chbox1m.current(0)
    chbox1m.grid(row=2, column=0,sticky=S)
    gmb.grid(row=3,column=0)
    bmezof1.configure(foreground='blue')
    bmezof2.configure(foreground='blue')
    bmezof3.configure(foreground='blue')

def gombablak(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    rspan=rc[2]
    cspan=rc[3]
    def g_ertek():
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
        kiir('#------Button: c'+str(c)+', r'+str(r)+'------')
        kiir(osszes)
        abl2.destroy()

    abl2=Toplevel(abl1)
    abl2.title('Button options: c'+str(c)+', r'+str(r))
    gmb=Button(abl2,text='Apply',command=g_ertek)
    cmke1=Label(abl2, text='Label:')
    bmezof1=Entry(abl2, textvariable=f1)
    bmezof1.insert(0,"Ok")
    bmezof2=Entry(abl2, textvariable=f2)
    bmezof3=Entry(abl2, textvariable=f3)
    bmezof1_1=Entry(abl2, textvariable=f11)
    bmezof2_1=Entry(abl2, textvariable=f21)
    bmezof3_1=Entry(abl2, textvariable=f31)
    bmezof1_2=Entry(abl2, textvariable=f12)
    bmezof2_2=Entry(abl2, textvariable=f22)
    bmezof3_2=Entry(abl2, textvariable=f32)
    bmezof1_3=Entry(abl2, textvariable=f13)
    bmezof2_3=Entry(abl2, textvariable=f23)
    bmezof3_3=Entry(abl2, textvariable=f33)
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
    chbox1g['values']=('N','NE','E','SE','S','SW','W','NW','N+S','E+W')
    chbox1g.current(0)
    chbox1g.grid(row=2, column=0,sticky=S)

def vaszonablak(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    rspan=rc[2]
    cspan=rc[3]
    def v_ertek():
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
        kiir('#------Canvas: c'+str(c)+', r'+str(r)+'------')
        kiir(osszes)
        abl2.destroy()
    
    abl2=Toplevel(abl1)
    abl2.title('Canvas options: c'+str(c)+', r'+str(r))       
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    chbox1=Combobox(ablak, width=4)
    chbox1['values']=('N','NE','E','SE','S','SW','W','NW','N+S','E+W')
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
    cmke1=Label(ablak, text='orientation/width/height/color:')
    cmke1.grid(row=1, column=0,sticky=E)
    
def szovegmezablak(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    rspan=rc[2]
    cspan=rc[3]
    def t_ertek():
       output=['','','','','','',''] # w,h,orient,slide,def.text,bg.color, text.color
       try:
           output[0]=int(bmezo3.get())
           output[1]=int(bmezo4.get())
       except:
           print('Számot kell megadni!')
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
       kiir('#------Text: c'+str(c)+', r'+str(r)+'------')
       kiir(osszes) 
       abl2.destroy()
    
    abl2=Toplevel(abl1)
    abl2.title('Text options: c'+str(c)+', r'+str(r))        
    ablak=Frame(abl2, relief='flat', borderwidth=1)
    ablak.grid(row=0, column=0)
    bmezo0=Entry(ablak)
    bmezo0.grid(row=0, column=1,columnspan=4,sticky=E+W)
    chbox3=Combobox(ablak, width=4)
    chbox3['values']=('N','NE','E','SE','S','SW','W','NW','N+S','E+W')
    chbox3.current(0)
    chbox3.grid(row=2, column=1,sticky=W)
    bmezo3=Entry(ablak, width=14)
    bmezo3.grid(row=2, column=2,sticky=N)
    bmezo3.insert(0,'10')
    bmezo4=Entry(ablak, width=14)
    bmezo4.grid(row=2, column=3,sticky=N)
    bmezo4.insert(0,'10')
    chbox4=Combobox(ablak)
    chbox4['values']=('1: w/o slide','2: w vertical slide','3: w horizontal slide','4: with v/h slide')
    chbox4.current(0)
    chbox4.grid(row=2, column=4,sticky=W)

    chbox5=Combobox(ablak, width=11)
    chbox5['values']=('white','light yellow','snow','bisque','gray','cyan','sienna1','thistle','pick a color')
    chbox5.current(0)
    chbox5.grid(row=3, column=3,sticky=W)
    chbox6=Combobox(ablak)
    chbox6['values']=('black','gray','cyan','thistle','pick a color')
    chbox6.current(0)
    chbox6.grid(row=3, column=4,sticky=W)
    
    kret60=Frame(ablak, relief='flat', borderwidth=1)
    kret60.grid(row=6, column=0, sticky=N)
    gmb0=Button(kret60,text='Apply',command=t_ertek)
    gmb0.grid(row=0, column=0)
    cmke0=Label(ablak, text='default text')
    cmke0.grid(row=0, column=0,sticky=E)
    cmke2=Label(ablak, text='orientation/width/height/slide')
    cmke2.grid(row=2, column=0,sticky=E)
    cmke3=Label(ablak, text='bg color/text color')
    cmke3.grid(row=3, column=1, columnspan=2, sticky=E)


def beviteliablak(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    beviteli=Beviteli(rc,frame_name)
    osszes=beviteli.generator()
    kiir('#------Entry: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)


def cimkeablak(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    def c_ertek():
        labtxt=bmezo0.get()
        labo=chbox0.get()
        cimke=Cimke(rc,labtxt,labo,frame_name)
        osszes=cimke.generator()
        kiir('#------Label: c'+str(c)+', r'+str(r)+'------')
        kiir(osszes)
        abl2.destroy()
    abl2=Toplevel(abl1)
    abl2.title('Label options: c'+str(c)+', r'+str(r))        
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
    chbox0['values']=('N','NE','E','SE','S','SW','W','NW','N+S','E+W')
    chbox0.current(0)
    chbox0.grid(row=1, column=2, sticky=EW)
    gmb0=Button(ablak,text='Apply',command=c_ertek)
    gmb0.grid(row=1, column=0, sticky=S)
 
def cimkeablak_s(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    labtxt='title'
    labo='N'
    cimke=Cimke(rc,labtxt,labo,frame_name)
    osszes=cimke.generator()
    kiir('#------Label: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)

def keretablak(rc,output): #col-row, orientation
    c=rc[0]              
    r=rc[1]
    keret=Keret(rc,output)
    osszes,keretszam=keret.generator()
    kiir('#------Frame: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)
    return keretszam

def uzenablak(rc):
    c=rc[0]              
    r=rc[1]
    uzi=Uzenet(rc)
    osszes=uzi.generator()
    kiir('#------Message: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)

        
def comboxablak(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    tipus=0
    cmbx1=Boxablak(abl1,tipus,rc,frame_name) 

def comboxablak_s(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    lista=['One','Two','Three', #cells 0-11
           '','','',
           '','','',
           '','','',
           '','','','', #title cell
           'N','16']      #orientation, cell width
    combox=Combox(rc,lista,frame_name)
    osszes=combox.generator()
    kiir('#------ComboBox: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)

def omenuablak(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    tipus=1
    optmenu=Boxablak(abl1,tipus,rc,frame_name)


def omenuablak_s(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    lista=['One','Two','Three', #cells 0-11
           '','','',
           '','','',
           '','','',
           '','','','', #title cell
           'N','16']      #orientation, cell width
    optmenu=Optmenu(rc,lista,frame_name)
    osszes=optmenu.generator()
    kiir('#------Option menu: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)

def radioxablak(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    tipus=2
    radio=Boxablak(abl1,tipus,rc,frame_name)


def radioxablak_s(rc,frame_name='ablak'):
    c=rc[0]              
    r=rc[1]
    lista=['One','Two','Three', #cells 0-11
           '','','',
           '','','',
           '','','',
           '','','','', #title cell
           'N','16']      #orientation, cell width
    radiobox=Radiobox(rc,lista,frame_name)
    osszes=radiobox.generator()
    kiir('#------Radio: c'+str(c)+', r'+str(r)+'------')
    kiir(osszes)

def univablak(rc):
    def uni_ertek():
        output=['',''] # orientation, frameText
        output[0]=chbox200.get() #orientaion
        output[1]=bmezo.get()    #frame text
        kivalaszto_uni(rc,cells_uni,output)
        abl2.destroy()
    selection_uni1_1=('00: ---','01: Menu','02: Button','03: Canvas',
                '04: Text', '05: Entry','06: Label',
                '07: Label (s)', '08: Combobox', '09: ComboBox (s)',
                '10: OptionMenu', '11: OptionMenu (s)', '12: Radio',
                '13: Radio (s)')
    selection_uni1_2=('00: ---','01: Menu','02: Button','03: Canvas',
                '04: Text', '05: Entry','06: Label',
                '07: Label (s)', '08: Combobox', '09: ComboBox (s)',
                '10: OptionMenu', '11: OptionMenu (s)', '12: Radio',
                '13: Radio (s)', '14: colspan <')
    selection_uni2_1=('00: ---','01: Menu','02: Button','03: Canvas',
                '04: Text', '05: Entry','06: Label',
                '07: Label (s)', '08: Combobox', '09: ComboBox (s)',
                '10: OptionMenu', '11: OptionMenu (s)', '12: Radio',
                '13: Radio (s)', '15: rowspan ^')
    selection_uni2_2=('00: ---','01: Menu','02: Button','03: Canvas',
                '04: Text', '05: Entry','06: Label',
                '07: Label (s)', '08: Combobox', '09: ComboBox (s)',
                '10: OptionMenu', '11: OptionMenu (s)', '12: Radio',
                '13: Radio (s)', '98: colspan <', '99: rowspan ^')
    base_col=rc[0]              
    base_row=rc[1]
    abl2=Toplevel(abl1)
    abl2.title('Universal widget frame: c'+str(base_col)+', r'+str(base_row))        
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
    chbox200['values']=('N','NE','E','SE','S','SW','W','NW','N+S','E+W')
    chbox200.current(0)
    chbox200.grid(row=0, column=1,sticky=N)
    cmke200=Label(kret20, text='')
    cmke200.grid(row=0, column=0,sticky=N)
    cells_uni=[u1_1, u1_2,
               u2_1, u2_2] 

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
                if(cstat[i-2][0]<14 and cstat[i-2][0]!=0):                          # above rs (the 1st cell) there is valid cell (between 1-15) 
                    cstat[i-2][2][1]=cstat[i-2][2][1]+1                             # fölötte lévő cella rowspan értékét növelje 1-el
                if(cstat[i-2][0]==0 or cstat[i-2][0]==98 or cstat[i-2][0]==3):      # ha rs fölött üres cella vagy cs vagy canvas van akkor törölje
                       cells_uni[i].current(0)
###colspan            
            if((i!=0 and i!=2) and (cstat[i][0]==98)):                            #colspan must be in valid place/area
                if(cstat[i-1][0]<13 and cstat[i-1][0]!=0):                          #on the left side there is valid cell
                    cstat[i-1][2][0]=cstat[i-1][2][0]+1                             #balra lévő cella colspan értékét növelje 1-el
                if(cstat[i-1][0]==0 or cstat[i-1][0]==99 or cstat[i-1][0]==3):                          # ha cs -től balra üres cella vagy rs vagy canvas van akkor törölje
                    cells_uni[i].current(0)
#        print(cstat)
        for i in range(len(cstat)):
            if(cstat[i][2]==[2,2]):
                cells_uni[i+3].configure(state=DISABLED)
                cells_uni[i+3].current(0)
        return cstat

def kivalaszto_uni(base_rc,cells_uni,output):
        cstat=updatecell_uni(cells_uni)
        keretszam=keretablak(base_rc,output)
        for i in range(len(cstat)):
            if cstat[i][0]!=0:
                rc=['','','','',base_rc[0],base_rc[1]] #c,r,rspan,cspan,base_c, base_r
                rc[0]=cstat[i][1][0] #col             
                rc[1]=cstat[i][1][1] #row
                rc[2]=cstat[i][2][0] #colspan
                rc[3]=cstat[i][2][1] #rowspan
                if(cstat[i][0]==1):
                    menuablak(rc,keretszam)
                if(cstat[i][0]==2):
                    gombablak(rc,keretszam)
                if(cstat[i][0]==3):
                    vaszonablak(rc,keretszam)
                if(cstat[i][0]==4):
                    szovegmezablak(rc,keretszam)
                if(cstat[i][0]==5):
                    beviteliablak(rc,keretszam)
                if(cstat[i][0]==6):    
                    cimkeablak(rc,keretszam)
                if(cstat[i][0]==7):    
                    cimkeablak_s(rc,keretszam)
                if(cstat[i][0]==8):    
                    comboxablak(rc,keretszam)
                if(cstat[i][0]==9):    
                    comboxablak_s(rc,keretszam)
                if(cstat[i][0]==10):    
                    omenuablak(rc,keretszam)
                if(cstat[i][0]==11):    
                    omenuablak_s(rc,keretszam)
                if(cstat[i][0]==12):    
                    radioxablak(rc,keretszam)
                if(cstat[i][0]==13):    
                    radioxablak_s(rc,keretszam)
            

      
               
def updatecell():
        cstat=[['',[0,0],[1,1]],['',[1,0],[1,1]],['',[2,0],[1,1]],['',[3,0],[1,1]],['',[4,0],[1,1]], #cells: ['content',[col,row],[colspan=1,rowspan=1]]
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
                if(cstat[i-5][0]<16 and cstat[i-5][0]!=0):                          # ha fölötte 1-el érvényes (1-15 közötti) cella van 
                    cstat[i-5][2][1]=cstat[i-5][2][1]+1                             # fölötte lévő cella rowspan értékét növelje 1-el
                if(cstat[i-5][0]==0 or cstat[i-5][0]==98 or cstat[i-5][0]==3):                          # ha rs fölött üres cella vagy cs vagy canvas van akkor törölje
                       cellak[i].current(0)
                if((cstat[i-5][0]==99) and (cstat[i-10][0]==0 or cstat[i-10][0]==98 or cstat[i-10][0]==3)):  # ha rs fölött 1-el üres cella vagy cs van akkor törölje
                       cellak[i].current(0)
                if((cstat[i-5][0]==99 and cstat[i-10][0]==99) and (cstat[i-15][0]==0 or cstat[i-15][0]==98 or cstat[i-15][0]==3)):  # ha rs fölött 2-vel üres cella vagy cs van akkor törölje
                       cellak[i].current(0)
                if((cstat[i-5][0]==99 and cstat[i-10][0]==99 and cstat[i-15][0]==99) and (cstat[i-20][0]==0 or cstat[i-20][0]==98 or cstat[i-20][0]==3)):  # ha rs fölött 2-vel üres cella vagy cs van akkor törölje
                       cellak[i].current(0)
                if(cstat[i-5][0]==99 and cstat[i-10][0]==99 and cstat[i-15][0]==99 and cstat[i-20][0]==99):  # az 5.rs kijelölés már nem engedélyezett
                       cellak[i].current(0)
                if(i>9 and cstat[i-5][0]==99 and (cstat[i-10][0]<16 and cstat[i-10][0]!=0)): #ha a cella fölött rs utána érvényes cella 
                   cstat[i-10][2][1]=cstat[i-10][2][1]+1                            # 1-el fölötte lévő cella rowspan értékét növelje 1-el
                if(i>14 and cstat[i-5][0]==99 and cstat[i-10][0]==99 and (cstat[i-15][0]<16 and cstat[i-15][0]!=0)): #ha a cella fölött rs+rs utána érvényes cella 
                   cstat[i-15][2][1]=cstat[i-15][2][1]+1                            # 2-el fölötte lévő cella rowspan értékét növelje 1-el
                if(i>19 and cstat[i-5][0]==99 and cstat[i-10][0]==99 and cstat[i-15][0]==99 and (cstat[i-20][0]<16 and cstat[i-20][0]!=0)): #ha a cella fölött rs+rs utána érvényes cella 
                   cstat[i-20][2][1]=cstat[i-20][2][1]+1 

###colspan            
            if((i!=0 and i%5!=0) and (cstat[i][0]==98)):                            #colspan must be in valid place/area
                if(cstat[i-1][0]<16 and cstat[i-1][0]!=0):                          #ha balra érvényes cella van
                    cstat[i-1][2][0]=cstat[i-1][2][0]+1                             #balra lévő cella colspan értékét növelje 1-el
                if(cstat[i-1][0]==0 or cstat[i-1][0]==99 or cstat[i-1][0]==3):                          # ha cs -től balra üres cella vagy rs vagy canvas van akkor törölje
                    cellak[i].current(0)
                if(cstat[i-1][0]==98 and (cstat[i-2][0]==0 or cstat[i-2][0]==99 or cstat[i-2][0]==3)):  # ha cs -től balra 1-el cs, de utána üres cella vagy rs van akkor törölje
                    cellak[i].current(0)
                if(cstat[i-1][0]==98 and cstat[i-2][0]==98 and (cstat[i-3][0]==0  or cstat[i-3][0]==99 or cstat[i-3][0]==3)):  # ha cs -től balra 2-vel cs, de utána üres cella vagy rs van akkor törölje
                    cellak[i].current(0)
                if(cstat[i-1][0]==98 and cstat[i-2][0]==98 and cstat[i-3][0]==98 and (cstat[i-4][0]==0 or cstat[i-4][0]==99 or cstat[i-4][0]==3)):  # ha cs -től balra 3-al cs, de utána üres cella vagy rs van akkor törölje
                    cellak[i].current(0)
                if(i>0 and cstat[i-1][0]==98 and (cstat[i-2][0]<16 and cstat[i-2][0]!=0)):                #ha a cella fölött rs utána érvényes cella 
                    cstat[i-2][2][0]=cstat[i-2][2][0]+1                            # 1-el fölötte lévő cella rowspan értékét növelje 1-el
                if(i>1 and cstat[i-1][0]==98 and cstat[i-2][0]==98 and (cstat[i-3][0]<16 and cstat[i-3][0]!=0)):                #ha a cella fölött rs utána érvényes cella 
                    cstat[i-3][2][0]=cstat[i-3][2][0]+1                            # 1-el fölötte lévő cella rowspan értékét növelje 1-el
                if(i>2 and cstat[i-1][0]==98 and cstat[i-2][0]==98 and cstat[i-3][0]==98 and (cstat[i-4][0]<16 and cstat[i-4][0]!=0)):                #ha a cella fölött rs utána érvényes cella 
                    cstat[i-4][2][0]=cstat[i-4][2][0]+1  
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
                rc=['','','','','a','a'] #c,r,rspan,cspan
                rc[0]=cstat[i][1][0] #col             
                rc[1]=cstat[i][1][1] #row
                rc[2]=cstat[i][2][0] #colspan
                rc[3]=cstat[i][2][1] #rowspan
                
                if(cstat[i][0]==1):
                    menuablak(rc)
                if(cstat[i][0]==2):
                    gombablak(rc)
                if(cstat[i][0]==3):
                    vaszonablak(rc)
                if(cstat[i][0]==4):
                    szovegmezablak(rc)
                if(cstat[i][0]==5):
                    beviteliablak(rc)
                if(cstat[i][0]==6):    
                    cimkeablak(rc)
                if(cstat[i][0]==7):    
                    cimkeablak_s(rc)
                if(cstat[i][0]==8):    
                    comboxablak(rc)
                if(cstat[i][0]==9):    
                    comboxablak_s(rc)
                if(cstat[i][0]==10):    
                    omenuablak(rc)
                if(cstat[i][0]==11):    
                    omenuablak_s(rc)
                if(cstat[i][0]==12):    
                    radioxablak(rc)
                if(cstat[i][0]==13):    
                    radioxablak_s(rc)
                if(cstat[i][0]==14):    
                    uzenablak(rc)
                if(cstat[i][0]==15):    
                    univablak(rc)
                


def kiir(x):
    if(x!=''):
        gomb2.configure(state=NORMAL) #Finalize button to normal state
        text1.insert(INSERT,x)        #text insert
        text1.insert(INSERT,'\n')

def finalize():
    sajatcim=title_entry.get()
    s1_f='from tkinter import *\nfrom tkinter.ttk import *\nk_ablak=Tk()\nk_ablak.title('+"'"+str(sajatcim)+"'"+')\
        \nablak=Frame(k_ablak, relief='+"'"+'flat'+"'"+', borderwidth=1)\nablak.grid(row=0, column=0)\n'
    text1.insert(1.0,s1_f) #insert to the begining
    text1.insert(END,su)   #insert to the end
    gomb2.configure(state=DISABLED) # Disable to avoid repeated button click

def colorset(): #color selection modul
    a=colorchooser.askcolor(initialcolor='#ff0000')
    return a[1] # the needed color code is in a[1]

def reset():
    text1.delete(1.0,END) #erase text area
    for widget in abl1.winfo_children(): #close all sub-windows
        if isinstance(widget, tk.Toplevel):
            widget.destroy()

def reset2():
    for i in cellak:
        i.configure(state=NORMAL)
    def_status() # reset all selction cells
    gomb.configure(text="Start")
    gomb2.configure(state=DISABLED) #Finalize button ON
    text1.delete(1.0,END) #Erase text area
    for widget in abl1.winfo_children(): #close all sub-windows
        if isinstance(widget, tk.Toplevel):
            widget.destroy()

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


# Menu arguments
f1, f2, f3, f11, f21, f31, f12, f22, f32, f13, f23, f33='','','','','','','','','','','',''
welcometext='Tkinter GUI designer\nIt uses tkinter Grid geometry manager. (https://effbot.org/tkinterbook/grid.htm)\nYou will get pure Python tkinter code.\n\n1. Select the desired widgets*\n2. If you use rowsapan/colspan press "'"Check"'" button\n3. Press "'"Start"'" to generate codes\
\n4. Set the opened options windows and Apply\n5. Press "'"Finalize"'" and copy the generated code with Ctrl+C\
\n\nHint:\n- rowspan must be placed under the expanded widget\n- columnspan must be placed to right side of the widget\n- maximum 4 column and 4 rowspan cells can be selected for one widget \n  (rowspan/col.span=5)\
\n- if you use col.span and/or rowspan press "'"Check"'" button to check your selection.\n  (all missplaced span selection will be reseted and common merged cells disabled)\
\n- Canvas does not accept col./rowspan\n- Open second session of Python IDLE and use it for checking the generated code\n\
  without closing the running GUI generator\n- widget name with (s) means simple. It uses default parameters and does not open\n  option window.\n\nSupported widgets: \nmenu, button, canvas, text with slide, entry, label, combobox, optionmenu,\nradio, message, Frame/LabelFrame (universal 2x2)\n'

labtxt,labo='This is a label','N'
su='ablak.mainloop()'

selection=('00: ---','01: Menu','02: Button','03: Canvas',
                '04: Text', '05: Entry','06: Label',
                '07: Label (s)', '08: Combobox', '09: ComboBox (s)',
                '10: OptionMenu', '11: OptionMenu (s)', '12: Radio',
                   '13: Radio (s)', '14: Message', '15: Univ.Frame',
                   '98: colspan <', '99: rowspan ^')


### main window
abl1=Tk()
abl1.title("Tkinter GUI designer v0.8.3")
frame1=Frame(abl1, borderwidth=1)
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


        
gombkeret=Frame(abl1, borderwidth=0)
gombkeret.grid(row=2, column=3)
gomb=Button(gombkeret,text='Start',command=kivalaszto2)
gomb2=Button(gombkeret,text='Finalize',command=finalize, state=DISABLED) # Finalize button OFF, avoid early or repeated click
gomb3=Button(abl1,text='Reset',command=reset2)                      
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
cmkemsg=Label(abl1, foreground='black',text='Gmiki (2020) epromirok@gmail.com')


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
cmkemsg.grid(row=6, column=1, columnspan=5 ,sticky=W)

titlekeret=Frame(abl1, borderwidth=0)
titlekeret.grid(row=0, column=1)
titlcmke=Label(titlekeret, text='Window title:')
titlcmke.grid(row=0, column=0,sticky=E)
title_entry=Entry(titlekeret, width=30)
title_entry.insert(0, "My window")
title_entry.grid(row=0, column=1, sticky=E)



textkeret=Frame(abl1, relief='flat', borderwidth=1)
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
abl1.mainloop()
