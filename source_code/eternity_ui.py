import tkinter
from tkinter.constants import * 


WINDOW_WIDTH = '605'
WINDOW_HEIGHT = '674'



BUTTON_COLUMNS = 15
BUTTON_ROWS = 4

BUTTON_WIDTH = BUTTON_COLUMNS
BUTTON_HEIGHT = BUTTON_ROWS

print(BUTTON_HEIGHT)
print(BUTTON_WIDTH)

# UI Setup
mainWindow = tkinter.Tk()
mainWindow.title("Eternity")    # Window title
mainWindow.geometry(WINDOW_WIDTH + 'x' + WINDOW_HEIGHT)  # default window size
mainWindow.resizable(width=False, height=False) # Lock window size

#Specify grid growth rate
tkinter.Grid.columnconfigure(mainWindow, 0, weight=1)
# UI Setup END


# Display box
equationTextBox = tkinter.Entry(mainWindow, justify='right', font='Calibri 80')
equationTextBox.grid(row=0, column=0, sticky='NSEW')



# Frame for buttons
btnFrame = tkinter.Frame(mainWindow)
btnFrame.grid(row=1, column=0, sticky='NSEW')




# Num-pad buttons
numpad_0 = tkinter.Button(btnFrame, text ='0', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command ='')
numpad_0.grid(row=7, column=2, sticky='NSEW')

numpad_1 = tkinter.Button(btnFrame, text ='1', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command ='')
numpad_1.grid(row=6, column=1, sticky='NSEW')

numpad_2 = tkinter.Button(btnFrame, text ='2', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
numpad_2.grid(row=6, column=2, sticky='NSEW')

numpad_3 = tkinter.Button(btnFrame, text ='3', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
numpad_3.grid(row=6, column=3, sticky='NSEW')

numpad_4 = tkinter.Button(btnFrame, text ='4', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
numpad_4.grid(row=5, column=1, sticky='NSEW')

numpad_5 = tkinter.Button(btnFrame, text ='5', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
numpad_5.grid(row=5, column=2, sticky='NSEW')

numpad_6 = tkinter.Button(btnFrame, text ='6', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
numpad_6.grid(row=5, column=3, sticky='NSEW')

numpad_7 = tkinter.Button(btnFrame, text ='7', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
numpad_7.grid(row=4, column=1, sticky='NSEW')

numpad_8 = tkinter.Button(btnFrame, text ='8', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
numpad_8.grid(row=4, column=2, sticky='NSEW')

numpad_9 = tkinter.Button(btnFrame, text ='9', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
numpad_9.grid(row=4, column=3, sticky='NSEW')



# Aux buttons (temporary)
# column 1
btn1 = tkinter.Button(btnFrame, text ='btn_0', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn1.grid(row=1, column=0, sticky='NSEW')

btn2 = tkinter.Button(btnFrame, text ='btn_1', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn2.grid(row=2, column=0, sticky='NSEW')

btn3 = tkinter.Button(btnFrame, text ='btn_2', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn3.grid(row=3, column=0, sticky='NSEW')

btn4 = tkinter.Button(btnFrame, text ='btn_3', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn4.grid(row=4, column=0, sticky='NSEW')

btn5 = tkinter.Button(btnFrame, text ='btn_4', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn5.grid(row=5, column=0, sticky='NSEW')

btn6 = tkinter.Button(btnFrame, text ='btn_5', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn6.grid(row=6, column=0, sticky='NSEW')

btn7 = tkinter.Button(btnFrame, text ='btn_6', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn7.grid(row=7, column=0, sticky='NSEW')

# Column 2
btn8 = tkinter.Button(btnFrame, text ='btn_7', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn8.grid(row=1, column=1, sticky='NSEW')

btn9 = tkinter.Button(btnFrame, text ='btn_8', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn9.grid(row=2, column=1, sticky='NSEW')

btn10 = tkinter.Button(btnFrame, text ='btn_9', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn10.grid(row=3, column=1, sticky='NSEW')

btn11 = tkinter.Button(btnFrame, text ='btn_10', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn11.grid(row=7, column=1, sticky='NSEW')

# Column 3
btn12 = tkinter.Button(btnFrame, text ='btn_11', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn12.grid(row=1, column=2, sticky='NSEW')

btn13 = tkinter.Button(btnFrame, text ='btn_12', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn13.grid(row=2, column=2, sticky='NSEW')

btn14 = tkinter.Button(btnFrame, text ='btn_13', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn14.grid(row=3, column=2, sticky='NSEW')

# Column 4
btn15 = tkinter.Button(btnFrame, text ='btn_14', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn15.grid(row=1, column=3, sticky='NSEW')

btn16 = tkinter.Button(btnFrame, text ='btn_15', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn16.grid(row=2, column=3, sticky='NSEW')

btn17 = tkinter.Button(btnFrame, text ='btn_16', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn17.grid(row=3, column=3, sticky='NSEW')

btn18 = tkinter.Button(btnFrame, text ='btn_17', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn18.grid(row=7, column=3, sticky='NSEW')

# Column 4
btn19 = tkinter.Button(btnFrame, text ='btn_18', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn19.grid(row=1, column=4, sticky='NSEW')

btn20 = tkinter.Button(btnFrame, text ='btn_19', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn20.grid(row=2, column=4, sticky='NSEW')

btn21 = tkinter.Button(btnFrame, text ='btn_20', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn21.grid(row=3, column=4, sticky='NSEW')

btn22 = tkinter.Button(btnFrame, text ='btn_21', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn22.grid(row=4, column=4, sticky='NSEW')

btn23 = tkinter.Button(btnFrame, text ='btn_22', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn23.grid(row=5, column=4, sticky='NSEW')

btn24 = tkinter.Button(btnFrame, text ='btn_23', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn24.grid(row=6, column=4, sticky='NSEW')

btn25 = tkinter.Button(btnFrame, text ='btn_24', bd = '5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,  command ='')
btn25.grid(row=7, column=4, sticky='NSEW')





# Keep main window up till keyboard interrupt or mouse interrupt
mainWindow.mainloop()
