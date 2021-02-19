import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdforator = PyPDF2.PdfFileReader(book)
pages = pdforator.numPages

for num in range(0, pages):
    page =pdforator.getPage(num)
    text=page.extractText()
    audioplayer = pyttsx3.init()
    audioplayer.say(text)
    audioplayer.runAndWait()