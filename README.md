# python Tkinter GUI designer
Python Tkinter GUI designer

It uses tkinter Grid geometry manager. (https://effbot.org/tkinterbook/grid.htm)
You will get pure Python tkinter code.

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

Supported widgets: 
Menubar, MenuButton, Button, Canvas, Text with scroll, Entry, Label, Combobox, Optionmenu,
Radio, Message, Frame/LabelFrame (universal 2x2 widget selection), Listbox, Scale, Spinbox,
Toolbar with Tooltip text (sample PNG files are in the package)

<< please download the user maual >>
