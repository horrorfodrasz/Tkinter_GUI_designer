# python Tkinter GUI designer
Python Tkinter GUI designer

It uses tkinter Grid geometry manager. (https://effbot.org/tkinterbook/grid.htm)
You will get pure Python (v3.x) tkinter code.

1. Select the desired widgets*
2. If you use rowsapan/colspan press "Check" button
3. Press "Start" to generate codes
4. Set the opened options windows and Apply
5. Press "Finalize" and copy the generated code with Ctrl+C

Hint:
- rowspan must be placed under the expanded widget
- columnspan must be placed to right side of the widget
- maximum 4 column and 4 rowspan cells can be selected for one widget 
  (rowspan/col.span=5)
- if you use col.span and/or rowspan press "Check" button to check your selection.
  (all missplaced span selection will be reseted and common merged cells disabled)
- Canvas, Menubar does not accept col./rowspan
- Open second session of Python IDLE and use it for checking the generated code
  without closing the running GUI generator
- widget name with (s) means simple. It uses default parameters and does not open
  option window.
- You can save and load widget selection with default widget parameters
- Generated code can be Function or Object type

Supported widgets: 
Menubar, MenuButton, Button, Canvas with scroll, Text with scroll, Entry, Label, Combobox, Optionmenu,
Radio, Message, Frame/LabelFrame (universal 2x2 widget selection), Listbox, Scale, Spinbox,
Toolbar with Tooltip text (sample PNG files are in the package), Notebook, Treeview with scroll

<< please download the user maual >>

update history:

 ...
 
 v0.7:  rowspan,columnspan implemented, 5x9 widget selection area
 
 v0.8:  universal 2x2 frame added
 
 v0.8.1 Improved Button widget. In case of 1 button there is no frame. You can use W+E to span button
        Universal frame numbering bugs fixed
        
v0.8.3  Improved Universal frame: with text: LabelFrame; without: Frame

v0.8.4  tk and ttk import optimalization (for slide)

v0.8.5  Menubar and Menubutton added

v0.8.6  new Menubar function: separate and checkbox

v0.8.7  new Menubutton options menu

v0.8.8  Listbox added

v0.8.9  Scale added

v0.9    Spinbox added

v0.9.1  Progressbar added

v0.9.2  Toolbar (buttons with images and tolltip text) added

v0.9.3  Notebook added

v0.9.4  Widget selection save/load added

v0.9.5  interface improved

v0.9.6  hints added

v0.9.7  it can generate functions and object, too

v0.9.8  default parameter settings added

v1.0    it can save/load default parameters with widget selections

v1.1    improved Comobox, Optionmenu and Radio

v1.2    Treeview added, scrollbar supported in case of Canvas and Treeview, minor bug fixes

