import tkinter

inital = tkinter.Tk()
inital.title("Calculator By Rajveer Narang")

#Global variable
expression = "  "

#functions
def add(value):
    global expression
    expression += value
    label_answer.config(text = expression)

def clear():
    global expression
    expression = ""
    label_answer.config(text = expression)

def calculate():
    global expression
    answer = ""
    if expression != "" :
        try:
            answer = eval(expression)
            label_answer.config(text = answer)
        except:
            result = "error"
            expression = ""
    label_answer.config(text = answer)


#GUI
label_answer = tkinter.Label(inital, text ="")
label_answer.grid(row=0, column = 0, columnspan=4)

button1 =tkinter.Button(inital, text ="1",width = 5 , command = lambda: add('1'))
button1.grid(row=1, column=0)

button2 =tkinter.Button(inital, text ="2",width = 5 , command = lambda: add("2"))
button2.grid(row=1, column=1)

button2 =tkinter.Button(inital, text ="3",width = 5 , command = lambda: add("3"))
button2.grid(row=1, column=2)

button3 =tkinter.Button(inital, text ="/",width = 5 , command = lambda: add("/"))
button3.grid(row=1, column=3)

button5 =tkinter.Button(inital, text ="5",width = 5 , command = lambda: add("5"))
button4 =tkinter.Button(inital, text ="4",width = 5 , command = lambda: add("4"))
button4.grid(row=2, column=0)

button5 =tkinter.Button(inital, text ="5",width = 5 , command = lambda: add("5"))
button5.grid(row=2, column=1)

button6 =tkinter.Button(inital, text ="6",width = 5 , command = lambda: add("6"))
button6.grid(row=2, column=2)

button7 =tkinter.Button(inital, text ="*",width = 5 , command = lambda: add("*"))
button7.grid(row=2, column=3)

button8 =tkinter.Button(inital, text ="7",width = 5 , command = lambda: add("7"))
button8.grid(row=3, column=0)

button9 =tkinter.Button(inital, text ="8",width = 5 , command = lambda: add("8"))
button9.grid(row=3, column=1)

button10 =tkinter.Button(inital, text ="9",width = 5 , command = lambda: add("9"))
button10.grid(row=3, column=2)

button11 =tkinter.Button(inital, text ="-",width = 5 , command = lambda: add("-"))
button11.grid(row=3, column=3)

button12 =tkinter.Button(inital, text ="C",width = 5 , command = lambda: clear())
button12.grid(row=4, column=0)

button13 =tkinter.Button(inital, text ="0",width = 5 , command = lambda: add("0"))
button13.grid(row=4, column=1)

button14 =tkinter.Button(inital, text =".", width = 5 , command = lambda: add("."))
button14.grid(row=4, column=2)

button15 =tkinter.Button(inital, text ="+",width = 5 , command = lambda: add("+"))
button15.grid(row=4, column=3)

button16 =tkinter.Button(inital, text ="=",width = 25 , command = lambda: calculate())
button16.grid(row=5, column=0, columnspan=4)






inital.mainloop()