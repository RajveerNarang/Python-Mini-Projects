########################################################### TextWriter By- Rajveer Narang ###########################################################
###############################################################*************************************************************************************
##########################****     *      ******* *         *   ********      ********    *************
##########################** *   *...*       *      *      *    *             *           ************
##########################**   *       *     *        *   *     ****          ****        *********
#                                       *    *          *       *             *           ******
#                                                               ********      ********    *
#                                           *                                             * *
#                                                                                         * *
#                                                                                         * *
#                                                                                         *   *
#                                                                                         *     *
#                                                                                         *        *





import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import font


appwin = tkinter.Tk()
appwin.title("TextWriter - By Rajveer Narang ")
appwin.geometry("1200x600")
#delcare global and set to false as default (Mechanism part for Save option)
global open_name
open_name = False

global highlight
highlight = False

#new file create
def newfile():
    #delete previous file first
    textwidget.delete("1.0", END)
    #Update Status
    appwin.title("TextWriter New File - By Rajveer Narang ")
    sbar.config(text="New File        ")
    global open_name
    open_name = False
#openfile


def openfile():
    textwidget.delete("1.0", END)
    #grab files form storage
    textfile = filedialog.askopenfilename(title ="Open File" , filetypes =(("TEXT FILES","*.txt"),("HTML FILES","*.html"),("PYTHON FILES", "*.py"),("All FILES","*.*")))
#check for file
    if textfile:
        #make file global for later access
        global open_name
        open_name =textfile

    id = textfile
    sbar.config(text = id)

    #open the file readable mode
    id= open(id , 'r+')
    material = id.read()
#add file to text area
    textwidget.insert(END , material)
    # Updated Status
    if textfile:
        name = textfile
        sbar.config(text=f'Opened:{name}       ')
        name = name.replace("D:/python/Python Mini-Projects/texteditor/","")
        appwin.title(f'{name} - TextWriter -By Rajveer Narang')
# close the openfile
    id.close()

# Save AS
def saveas():
    textfile = filedialog.asksaveasfilename(defaultextension =".*", title ="Save File" , filetypes =(("TEXT FILES","*.txt"),("HTML FILES","*.html"),("PYTHON FILES", "*.py"),("All FILES","*.*")))
    if textfile:
         #update Statuses 
         name = textfile
         sbar.config(text=f'Saved:{name}       ')
         name = name.replace("D:/python/Python Mini-Projects/texteditor/","")
         appwin.title(f'{name} - TextWriter -By Rajveer Narang')
    #Save file
    textfile = open(textfile, 'w')
    textfile.write(textwidget.get(1.0, END))
    #close file
    textfile.close()
#save file function
def save():
    global open_name
    if open_name:
        #Save file
        open_name = open(open_name, 'w')
        open_name.write(textwidget.get(1.0, END))  
        #close file
        open_name.close()
        sbar.config(text=f'Updated and Saved:{open_name}     ')  
    else:
        saveas()
#cut code
def cut(e):
    global highlight
    # Check for binding presense
    if e:
        highlight =appwin.clipboard_get()
        appwin.clipboard_clear()
        appwin.clipboard_append(highlight)

    if textwidget.selection_get():
        #grab text
        highlight=textwidget.selection_get()
        #delete text 
        textwidget.delete("sel.first","sel.last")


#copy code
def copy(e):
    global highlight
    if textwidget.selection_get():
    # Grab Text
        highlight=textwidget.selection_get()
    
#paste code
def paste(e):
    global highlight
    if e:
        highlight = appwin.clipboard_get()
    else:
        if highlight:
            loc =textwidget.index(INSERT)
            textwidget.insert(loc, highlight)










def openabout():
    appwinab = tkinter.Tk()
    appwinab.title("About TextWriter ")
    content = Label(appwinab , text = "TextWriter is a simple Text Editor Program Made by Rajveer Narang \n Using Python language \n  This Program/Software is a result of Project Based Learning  Approch. \n you are free to use this code and improve on it just dont only copy , \n but learn by building and editing the code :-) .")
    content.pack(padx = 100 , pady = 60)
    appwinab.geometry("600x300")
    appwinab.mainloop()






  

   

#Main frame
mainfp = Frame(appwin)
mainfp.pack(pady = 5)

#ScrollBar
textscroll = Scrollbar(mainfp)
textscroll.pack(side =RIGHT, fill = Y)

#config scrollbar
textscroll.config(command="textwidget.yview")

#Horizontal ScrollBar
hbar = Scrollbar(mainfp, orient ="horizontal")
hbar.pack(side =BOTTOM, fill = X)


#Create text Box
textwidget =Text(mainfp,width =97,height=25,font=("Helvetica",16),selectbackground="orange", selectforeground="black", undo = True, yscrollcommand = textscroll.set, wrap ="none", xscrollcommand = hbar.set)
textwidget.pack()

#Configure ScrollBar 
textscroll.config(command = textwidget.yview)
hbar.config(command = textwidget.xview)


# Create Menu
editormenu = Menu(appwin)
appwin.config(menu=editormenu)


#Add a File Menu
filermenu = Menu(editormenu, tearoff = False)
editormenu.add_cascade(label = "File",menu = filermenu)
filermenu.add_command(label ="New", command = newfile)
filermenu.add_command(label ="Open", command = openfile)
filermenu.add_command(label ="Save", command = save)
filermenu.add_command(label ="Save As" , command =saveas)
filermenu.add_separator()
filermenu.add_command(label ="Exit" , command = appwin.quit)
##########################################################################


#Edit Menu
editmenu = Menu(editormenu, tearoff = False)
editormenu.add_cascade(label = "Edit",menu = editmenu)
editmenu.add_command(label ="Cut\t\t  {Ctrl+x}",command=lambda: cut(False), accelerator ="(Ctrl+x)")
editmenu.add_command(label ="Copy\t\t  {Ctrl+c}",command=lambda: copy(False), accelerator ="(Ctrl+c)")
editmenu.add_command(label ="Paste\t\t  {Ctrl+v}",command=lambda: paste(False), accelerator ="(Ctrl+v)")
editmenu.add_separator()
editmenu.add_command(label ="Undo\t\t  {Ctrl+z}",command =textwidget.edit_undo , accelerator ="(Ctrl+z)")
editmenu.add_separator()
editmenu.add_command(label ="Redo\t\t  {Ctrl+y}",command =textwidget.edit_redo , accelerator ="(Ctrl+y)")

#About
about = Menu(editormenu, tearoff = False)
editormenu.add_cascade(label = "About",menu =about)
about.add_command(label ="About TextWriter" , command = openabout)



#Status bar footer
sbar = Label(appwin, text ="Ready      " , anchor = E)
sbar.pack(fill = X, side= BOTTOM , ipady = 5)


# Alter Bindings
appwin.bind('<Control-Key-x>', cut)
appwin.bind('<Control-Key-c>', copy)
appwin.bind('<Control-Key-v>', paste)

appwin.mainloop()