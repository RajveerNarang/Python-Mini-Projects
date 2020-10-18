import wolframalpha
client = wolframalpha.Client(akiai)

import wikipedia

import PySimpleGUI as ai
import pyttsx3
#import PyPDF2
#from tkinter.filedialog import *

#window color scheme
ai.theme('DarkTeal')	
#window layout
layout = [  [ai.Text('J.A.S.S.I : what would you like me to do ?')],
            [ai.Text('A.I User'), ai.InputText()],
            [ai.Button('Search'), ai.Button('Exit')] ]


#window execution
window = ai.Window('J.A.S.S.I - Created by Rajveer Narang ', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    res = client.query(values[0])
    wolfram_res = next(res.results).text
    wiki_res =  wikipedia.summary(values[0], sentences=2)
    audioplayer = pyttsx3.init()
    audioplayer.say(wolfram_res+wiki_res)
    ai.PopupNonBlocking("Result from Wolfram :"+wolfram_res, "Result from Wikipedia: "+wiki_res)
    audioplayer.runAndWait()
    print (values[0]) 
   
    
window.close()
