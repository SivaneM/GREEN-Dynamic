import tkinter as tk # module to create a GUI
import time
from PIL import ImageTk # module to add a background picture
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

"""root= tk.Tk()
 
canvas1 = tk.Canvas(root, width = 1000, height = 350) # create the canvas (tkinter module)
canvas1.pack()
 
 
image1 = ImageTk.PhotoImage(file = "eco.png") # PIL module
canvas1.create_image(700, 300, image = image1) # create a canvas image to place the background image
 
 
button1 = tk.Button (root, text='Exit', command=root.destroy) # create an Exit button to close the main window
canvas1.create_window(45, 350, window=button1) # create a canvas window to place the Exit Application button on top of the background image
"""
""" 
 
entry1 = tk.Entry (root) # create 1st entry box
canvas1.create_window(100, 200, window=entry1) # create a canvas window to place the 1st entry box on top of the background image
 
entry2 = tk.Entry (root) # create 2st entry box
canvas1.create_window(100, 220, window=entry2) # create a canvas window to place the 2nd entry box on top of the background image
         
entry3 = tk.Entry (root) # create 3st entry box
canvas1.create_window(100, 240, window=entry3) # create a canvas window to place the 3rd entry box on top of the background image
 
entry4 = tk.Entry (root) 
canvas1.create_window(100, 260, window=entry4)
 
entry5 = tk.Entry (root)
canvas1.create_window(100, 280, window=entry5) 
         
entry6 = tk.Entry (root) 
canvas1.create_window(100, 300, window=entry6) 

entry7 = tk.Entry (root) 
canvas1.create_window(100, 320, window=entry7) 


def insert_number(): # create a function/command to be called by the button (i.e., button2 below)
    global x1 # add 'global' before the variable x1, so that you can use that variable outside of the command/function if ever needed 
    global x2 # add 'global' before the variable x2, so that you can use that variable outside of the command/function if ever needed 
    global x3 # add 'global' before the variable x3, so that you can use that variable outside of the command/function if ever needed
    global x4 
    global x5
    global x6 
    global x7
    x1 = float(entry1.get()) # store the data input by the user as a variable x1 (float is added to handle any formatting issues)
    x2 = float(entry2.get()) # store the data input by the user as a variable x2 (float is added to handle any formatting issues)
    x3 = float(entry3.get()) # store the data input by the user as a variable x3 (float is added to handle any formatting issues)
    x4 = float(entry4.get()) 
    x5 = float(entry5.get()) 
    x6 = float(entry6.get()) 
    x7 = float(entry7.get()) 
    """

root = tk.Tk()
root.title('Green Dynamic')

def deplacement():
    img_coords = cv.coords(image)
    img_width = img_2.width()

    if img_coords[0] + img_width <= 800:
        cv.move(image, 5, 0)
        root.after(40,deplacement)

root.minsize(height=1000, width=1000)
root.maxsize(height=1000, width=1000)

fname = "eco.png"
bg_image = tk.PhotoImage(file=fname)

w = bg_image.width()
h = bg_image.height()


root.geometry("%dx%d+50+30" % (w, h))
cv = tk.Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=bg_image, anchor='nw')

cv.create_text(50, 20, text="                                            Welcome to Green Dynamic : Developed by AMINE, ARIEL, SIVANE, MATHEO ", fill="black", anchor='sw')


delay = 5
def fonction(x1,x2,x3,x4,x5,x6,x7,i,dico):
    if i in L :
        # create a bar chart once the variables x1, x2, x3, etc... are inserted by the user (and the user then clicks on button2 below)
        figure1 = Figure(figsize=(5,4), dpi=100) # create a Figure (matplotlib module)
        subplot1 = figure1.add_subplot(111) # add a subplot
        xAxis = ['plastique', 'dechets organiques ', 'batteries', 'metal', 'papier', 'ampoule','verre'] # intakes the values inserted under x1, x2, x3,etc... to represent the x Axis  
        yAxis = [float(x1),float(x2),float(x3),float(x4),float(x5),float(x6),float(x7)] # intakes the values inserted under x1, x2, x3,etc... to represent the y Axis 
        strit = iter(yAxis)
        subplot1.bar(xAxis,yAxis, color = 'b') # create the bar chart based on the input variables x1, x2, x3, etc...
        bar1 = FigureCanvasTkAgg(figure1, root) # create a canvas figure (matplotlib module)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=0)
        root.after(1)
        yAxis[1] = 0.4
         
        # create a pie chart once the variables x1, x2, x3, etc... are inserted by the user (and the user then clicks on button2 below)
        figure2 = Figure(figsize=(5,4), dpi=100) # create a Figure (matplotlib module)
        subplot2 = figure2.add_subplot(111) # add a subplot
        labels2 ='plastique', 'dechets organiques ', 'batteries', 'metal', 'papier', 'ampoule','verre'# add labels for each slice in the pie chart
        pieSizes = [float(x1),float(x2),float(x3),float(x4),float(x5),float(x6),float(x7)] # intakes the values inserted under x1, x2, x3,etc... to represent the pie slices 
        pieSizes2 = iter(pieSizes)
        explode2 = (0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01)  # explodes all slices
        subplot2.pie(pieSizes, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90) # create the pie chart based on the input variables x1, x2, x3, etc...
        subplot2.axis('equal')  # Use equal to draw the pie chart as a circle 
        pie2 = FigureCanvasTkAgg(figure2, root) # create a canvas figure (matplotlib module)
        pie2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=0)
        root.update()
        time.sleep(delay)
        if i<len(dico)-1:
            pie2.get_tk_widget().destroy()
            bar1.get_tk_widget().destroy()
        
    #button2 = tk.Button (root, text='Draw Chart ',command=insert_number) # button to call the 'insert_number' command above 
    #canvas1.create_window(127, 350, window=button2) # create a canvas window to place button2 on top of the background image


   

"""def refresh():
    try:
        for e in [0.1,0.1,0.1,0.1,0.3,0.1,0.2]:
            e = next(iter([0.1,0.1,0.1,0.1,0.3,0.1,0.2]))
            root.after(1, refresh)
    except StopIteration:
        root.destroy()
   """
dico = [

{'plastique': 0, 'verre': 0, 'papier': 0, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 0}
,
{'plastique': 0, 'verre': 0, 'papier': 0, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 0}
,
{'plastique': 0, 'verre': 0, 'papier': 1, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 0}
,
{'plastique': 0, 'verre': 0, 'papier': 1, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 0}
,
{'plastique': 0, 'verre': 0, 'papier': 1, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 0}
,
{'plastique': 0, 'verre': 0, 'papier': 1, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 0}
,
{'plastique': 1, 'verre': 0, 'papier': 1, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 0}
,
{'plastique': 1, 'verre': 0, 'papier': 1, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 0}
,
{'plastique': 1, 'verre': 0, 'papier': 1, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 1}
,
{'plastique': 1, 'verre': 0, 'papier': 1, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 1}
,
{'plastique': 1, 'verre': 0, 'papier': 1, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 1}
,
{'plastique': 1, 'verre': 0, 'papier': 1, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 1}
,
{'plastique': 1, 'verre': 0, 'papier': 1, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 0, 'papier': 1, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 0, 'papier': 2, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 2, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 2, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 2, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 2, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 2, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 2, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 2, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 2, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 2, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 3, 'metal': 0, 'dechets organiques ': 0, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 3, 'metal': 0, 'dechets organiques ': 1, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 3, 'metal': 0, 'dechets organiques ': 1, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 3, 'metal': 0, 'dechets organiques ': 1, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 3, 'metal': 0, 'dechets organiques ': 1, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 1, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 0, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 2, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 3, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 3, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 3, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 3, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 3, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 3, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 4, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 1, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 4, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 2, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 4, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 2, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 4, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 2, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 4, 'verre': 1, 'papier': 4, 'metal': 0, 'dechets organiques ': 2, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 4, 'verre': 1, 'papier': 5, 'metal': 0, 'dechets organiques ': 2, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 4, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 2, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 4, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 2, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 4, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 2, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 5, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 2, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 6, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 2, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 6, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 2, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 6, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 3, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 6, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 3, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 6, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 3, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 7, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 3, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 7, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 3, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 7, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 3, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 7, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 4, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 7, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 4, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 7, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 5, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 7, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 5, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 7, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 5, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 7, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 5, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 7, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 5, 'batteries': 1, 'ampoule': 2}
,
{'plastique': 7, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 5, 'batteries': 2, 'ampoule': 2}
,
{'plastique': 7, 'verre': 1, 'papier': 6, 'metal': 0, 'dechets organiques ': 5, 'batteries': 2, 'ampoule': 2}
,
{'plastique': 7, 'verre': 1, 'papier': 6, 'metal': 1, 'dechets organiques ': 5, 'batteries': 2, 'ampoule': 2}
,
{'plastique': 8, 'verre': 1, 'papier': 6, 'metal': 1, 'dechets organiques ': 5, 'batteries': 2, 'ampoule': 2}
,
{'plastique': 8, 'verre': 1, 'papier': 6, 'metal': 1, 'dechets organiques ': 5, 'batteries': 2, 'ampoule': 2}
,
{'plastique': 8, 'verre': 1, 'papier': 6, 'metal': 1, 'dechets organiques ': 5, 'batteries': 2, 'ampoule': 2}
,
{'plastique': 8, 'verre': 1, 'papier': 6, 'metal': 1, 'dechets organiques ': 5, 'batteries': 2, 'ampoule': 3}
,
{'plastique': 8, 'verre': 1, 'papier': 6, 'metal': 1, 'dechets organiques ': 5, 'batteries': 2, 'ampoule': 3}
,
{'plastique': 8, 'verre': 1, 'papier': 6, 'metal': 1, 'dechets organiques ': 5, 'batteries': 2, 'ampoule': 3}
,
{'plastique': 8, 'verre': 1, 'papier': 6, 'metal': 1, 'dechets organiques ': 6, 'batteries': 2, 'ampoule': 3}
,
{'plastique': 8, 'verre': 1, 'papier': 6, 'metal': 1, 'dechets organiques ': 6, 'batteries': 2, 'ampoule': 3}
,
{'plastique': 8, 'verre': 2, 'papier': 6, 'metal': 1, 'dechets organiques ': 6, 'batteries': 2, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 1, 'dechets organiques ': 6, 'batteries': 2, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 1, 'dechets organiques ': 6, 'batteries': 2, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 1, 'dechets organiques ': 6, 'batteries': 2, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 1, 'dechets organiques ': 6, 'batteries': 2, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 1, 'dechets organiques ': 6, 'batteries': 2, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 1, 'dechets organiques ': 6, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 1, 'dechets organiques ': 6, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 1, 'dechets organiques ': 6, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 1, 'dechets organiques ': 6, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 2, 'dechets organiques ': 6, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 2, 'dechets organiques ': 6, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 2, 'dechets organiques ': 6, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 2, 'dechets organiques ': 6, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 2, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 3, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 3, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 3, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 7, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 8, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 8, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 8, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 9, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 9, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 9, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 9, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 6, 'metal': 2, 'dechets organiques ': 9, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 7, 'metal': 2, 'dechets organiques ': 9, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 9, 'verre': 4, 'papier': 7, 'metal': 2, 'dechets organiques ': 10, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 10, 'verre': 4, 'papier': 7, 'metal': 2, 'dechets organiques ': 10, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 10, 'verre': 4, 'papier': 7, 'metal': 2, 'dechets organiques ': 10, 'batteries': 4, 'ampoule': 3}
,
{'plastique': 10, 'verre': 4, 'papier': 7, 'metal': 2, 'dechets organiques ': 10, 'batteries': 4, 'ampoule': 4}
,
{'plastique': 10, 'verre': 4, 'papier': 7, 'metal': 2, 'dechets organiques ': 10, 'batteries': 4, 'ampoule': 4}
,
{'plastique': 11, 'verre': 4, 'papier': 7, 'metal': 2, 'dechets organiques ': 10, 'batteries': 4, 'ampoule': 4}
,
{'plastique': 11, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 4, 'ampoule': 4}
,
{'plastique': 11, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 4, 'ampoule': 4}
,
{'plastique': 11, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 4, 'ampoule': 4}
,
{'plastique': 11, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 4, 'ampoule': 4}
,
{'plastique': 11, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 4}
,
{'plastique': 11, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 4}
,
{'plastique': 11, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 4}
,
{'plastique': 11, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 4}
,
{'plastique': 11, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 4}
,
{'plastique': 11, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 4}
,
{'plastique': 12, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 4}
,
{'plastique': 12, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 4}
,
{'plastique': 12, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 12, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 12, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 12, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 4, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 7, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 8, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 8, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 8, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 8, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 9, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 9, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 9, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 9, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 9, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 9, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 9, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 9, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 9, 'metal': 3, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 9, 'metal': 4, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 9, 'metal': 4, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 9, 'metal': 4, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 10, 'metal': 4, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 13, 'verre': 5, 'papier': 10, 'metal': 4, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 14, 'verre': 5, 'papier': 10, 'metal': 4, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 14, 'verre': 5, 'papier': 10, 'metal': 4, 'dechets organiques ': 10, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 14, 'verre': 5, 'papier': 10, 'metal': 4, 'dechets organiques ': 11, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 14, 'verre': 5, 'papier': 10, 'metal': 4, 'dechets organiques ': 11, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 14, 'verre': 5, 'papier': 10, 'metal': 5, 'dechets organiques ': 11, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 14, 'verre': 5, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 14, 'verre': 5, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 14, 'verre': 6, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 14, 'verre': 6, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 14, 'verre': 6, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 5}
,
{'plastique': 14, 'verre': 6, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 14, 'verre': 6, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 14, 'verre': 6, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 10, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 11, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 11, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 11, 'metal': 5, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 11, 'metal': 6, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 11, 'metal': 6, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 11, 'metal': 6, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 11, 'metal': 6, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 11, 'metal': 6, 'dechets organiques ': 12, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 11, 'metal': 6, 'dechets organiques ': 13, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 11, 'metal': 6, 'dechets organiques ': 13, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 15, 'verre': 6, 'papier': 11, 'metal': 6, 'dechets organiques ': 13, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 16, 'verre': 6, 'papier': 11, 'metal': 6, 'dechets organiques ': 13, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 16, 'verre': 6, 'papier': 11, 'metal': 7, 'dechets organiques ': 13, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 11, 'metal': 7, 'dechets organiques ': 13, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 11, 'metal': 7, 'dechets organiques ': 13, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 11, 'metal': 7, 'dechets organiques ': 14, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 11, 'metal': 7, 'dechets organiques ': 14, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 11, 'metal': 7, 'dechets organiques ': 14, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 11, 'metal': 7, 'dechets organiques ': 14, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 11, 'metal': 7, 'dechets organiques ': 14, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 11, 'metal': 7, 'dechets organiques ': 14, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 11, 'metal': 7, 'dechets organiques ': 14, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 12, 'metal': 7, 'dechets organiques ': 14, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 12, 'metal': 7, 'dechets organiques ': 14, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 12, 'metal': 7, 'dechets organiques ': 14, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 12, 'metal': 7, 'dechets organiques ': 14, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 12, 'metal': 7, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 12, 'metal': 7, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 12, 'metal': 7, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 12, 'metal': 7, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 17, 'verre': 6, 'papier': 12, 'metal': 7, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 18, 'verre': 6, 'papier': 12, 'metal': 7, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 18, 'verre': 6, 'papier': 12, 'metal': 7, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 18, 'verre': 6, 'papier': 12, 'metal': 8, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 18, 'verre': 6, 'papier': 12, 'metal': 8, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 18, 'verre': 6, 'papier': 12, 'metal': 8, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 6, 'papier': 12, 'metal': 8, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 6, 'papier': 12, 'metal': 8, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 6, 'papier': 12, 'metal': 8, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 6, 'papier': 12, 'metal': 8, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 6, 'papier': 12, 'metal': 8, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 6, 'papier': 12, 'metal': 8, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 6, 'papier': 12, 'metal': 8, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 12, 'metal': 8, 'dechets organiques ': 15, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 12, 'metal': 8, 'dechets organiques ': 16, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 8, 'dechets organiques ': 16, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 9, 'dechets organiques ': 16, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 9, 'dechets organiques ': 16, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 9, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 9, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 9, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 9, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 9, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 9, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 9, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 9, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 9, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 10, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 10, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 10, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 10, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 10, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 17, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 18, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 18, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 18, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 18, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 18, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 18, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 18, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 18, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 18, 'batteries': 5, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 13, 'metal': 11, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 19, 'verre': 7, 'papier': 14, 'metal': 11, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 19, 'verre': 8, 'papier': 14, 'metal': 11, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 19, 'verre': 8, 'papier': 15, 'metal': 11, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 15, 'metal': 11, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 15, 'metal': 11, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 15, 'metal': 11, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 15, 'metal': 11, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 15, 'metal': 11, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 15, 'metal': 11, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 15, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 15, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 15, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 15, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 15, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 15, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 15, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 20, 'verre': 8, 'papier': 16, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 21, 'verre': 8, 'papier': 16, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 21, 'verre': 8, 'papier': 16, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 21, 'verre': 8, 'papier': 16, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 21, 'verre': 9, 'papier': 16, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 21, 'verre': 9, 'papier': 16, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 21, 'verre': 9, 'papier': 16, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 21, 'verre': 9, 'papier': 16, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 21, 'verre': 9, 'papier': 16, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 21, 'verre': 9, 'papier': 16, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 21, 'verre': 9, 'papier': 16, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 21, 'verre': 9, 'papier': 16, 'metal': 12, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 21, 'verre': 9, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 21, 'verre': 9, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 22, 'verre': 9, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 22, 'verre': 9, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 22, 'verre': 9, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 22, 'verre': 9, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 22, 'verre': 9, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 22, 'verre': 10, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 13, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 14, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 14, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 14, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 14, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 14, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 14, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 14, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 14, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 14, 'dechets organiques ': 18, 'batteries': 6, 'ampoule': 6}
,
{'plastique': 23, 'verre': 10, 'papier': 16, 'metal': 14, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 24, 'verre': 10, 'papier': 16, 'metal': 14, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 24, 'verre': 10, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 24, 'verre': 10, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 25, 'verre': 10, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 25, 'verre': 10, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 25, 'verre': 10, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 25, 'verre': 10, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 25, 'verre': 10, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 25, 'verre': 10, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 25, 'verre': 10, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 26, 'verre': 10, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 26, 'verre': 10, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 26, 'verre': 10, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 26, 'verre': 11, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 26, 'verre': 11, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 26, 'verre': 11, 'papier': 16, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 26, 'verre': 11, 'papier': 17, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 6}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 18, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 19, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 19, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 19, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 18, 'metal': 15, 'dechets organiques ': 19, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 7, 'ampoule': 7}
,
{'plastique': 26, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 7, 'ampoule': 8}
,
{'plastique': 26, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 7, 'ampoule': 8}
,
{'plastique': 26, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 7, 'ampoule': 8}
,
{'plastique': 26, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 7, 'ampoule': 8}
,
{'plastique': 26, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 26, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 26, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 26, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 27, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 27, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 27, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 28, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 28, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 28, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 28, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 28, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 28, 'verre': 11, 'papier': 19, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 28, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 28, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 28, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 28, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 29, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 29, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 29, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 29, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 29, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 8, 'ampoule': 8}
,
{'plastique': 29, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 9, 'ampoule': 8}
,
{'plastique': 29, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 29, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 29, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 30, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 30, 'verre': 11, 'papier': 20, 'metal': 15, 'dechets organiques ': 19, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 30, 'verre': 11, 'papier': 20, 'metal': 16, 'dechets organiques ': 19, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 30, 'verre': 11, 'papier': 20, 'metal': 16, 'dechets organiques ': 19, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 30, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 19, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 30, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 19, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 30, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 30, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 30, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 30, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 30, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 30, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 9}
,
{'plastique': 30, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 30, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 30, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 30, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 30, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 31, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 32, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 32, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 32, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 32, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 32, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 32, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 32, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 32, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 32, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 32, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 33, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 33, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 33, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 9, 'ampoule': 10}
,
{'plastique': 33, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 10, 'ampoule': 10}
,
{'plastique': 34, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 10, 'ampoule': 10}
,
{'plastique': 34, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 10, 'ampoule': 10}
,
{'plastique': 34, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 10, 'ampoule': 10}
,
{'plastique': 34, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 10, 'ampoule': 10}
,
{'plastique': 34, 'verre': 11, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 10, 'ampoule': 10}
,
{'plastique': 34, 'verre': 12, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 10, 'ampoule': 10}
,
{'plastique': 35, 'verre': 12, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 10, 'ampoule': 10}
,
{'plastique': 35, 'verre': 12, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 10, 'ampoule': 10}
,
{'plastique': 35, 'verre': 12, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 11, 'ampoule': 10}
,
{'plastique': 35, 'verre': 12, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 11, 'ampoule': 10}
,
{'plastique': 35, 'verre': 12, 'papier': 21, 'metal': 16, 'dechets organiques ': 20, 'batteries': 11, 'ampoule': 10}
,
{'plastique': 35, 'verre': 12, 'papier': 21, 'metal': 16, 'dechets organiques ': 21, 'batteries': 11, 'ampoule': 10}
,
{'plastique': 35, 'verre': 12, 'papier': 21, 'metal': 16, 'dechets organiques ': 21, 'batteries': 11, 'ampoule': 10}
,
{'plastique': 35, 'verre': 12, 'papier': 21, 'metal': 16, 'dechets organiques ': 21, 'batteries': 11, 'ampoule': 10}
,
{'plastique': 35, 'verre': 12, 'papier': 22, 'metal': 16, 'dechets organiques ': 21, 'batteries': 11, 'ampoule': 10}
,
{'plastique': 36, 'verre': 12, 'papier': 22, 'metal': 16, 'dechets organiques ': 21, 'batteries': 11, 'ampoule': 10}
,
{'plastique': 36, 'verre': 12, 'papier': 22, 'metal': 16, 'dechets organiques ': 21, 'batteries': 11, 'ampoule': 10}
,
{'plastique': 36, 'verre': 12, 'papier': 22, 'metal': 16, 'dechets organiques ': 21, 'batteries': 11, 'ampoule': 10}
,
{'plastique': 36, 'verre': 12, 'papier': 22, 'metal': 16, 'dechets organiques ': 21, 'batteries': 11, 'ampoule': 10}
,
{'plastique': 36, 'verre': 13, 'papier': 22, 'metal': 16, 'dechets organiques ': 21, 'batteries': 11, 'ampoule': 10}
,
{'plastique': 36, 'verre': 13, 'papier': 22, 'metal': 16, 'dechets organiques ': 21, 'batteries': 11, 'ampoule': 10}
,
{'plastique': 36, 'verre': 13, 'papier': 22, 'metal': 16, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 36, 'verre': 13, 'papier': 22, 'metal': 16, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 36, 'verre': 13, 'papier': 22, 'metal': 16, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 36, 'verre': 13, 'papier': 22, 'metal': 16, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 36, 'verre': 13, 'papier': 22, 'metal': 16, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 36, 'verre': 13, 'papier': 22, 'metal': 17, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 37, 'verre': 13, 'papier': 22, 'metal': 17, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 38, 'verre': 13, 'papier': 22, 'metal': 17, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 38, 'verre': 13, 'papier': 22, 'metal': 17, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 38, 'verre': 13, 'papier': 22, 'metal': 17, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 38, 'verre': 13, 'papier': 22, 'metal': 17, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 38, 'verre': 13, 'papier': 23, 'metal': 17, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 38, 'verre': 13, 'papier': 23, 'metal': 17, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 38, 'verre': 13, 'papier': 23, 'metal': 17, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 38, 'verre': 13, 'papier': 23, 'metal': 17, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 38, 'verre': 13, 'papier': 23, 'metal': 17, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 38, 'verre': 13, 'papier': 23, 'metal': 17, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 39, 'verre': 13, 'papier': 23, 'metal': 17, 'dechets organiques ': 21, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 39, 'verre': 13, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 39, 'verre': 14, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 10}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 39, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 40, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 40, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 41, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 41, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 41, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 41, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 41, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 41, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 11}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 12, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 22, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 23, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 23, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 23, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 23, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 23, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 23, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 23, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 23, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 23, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 23, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 23, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 17, 'dechets organiques ': 24, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 23, 'metal': 18, 'dechets organiques ': 24, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 24, 'metal': 18, 'dechets organiques ': 24, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 24, 'metal': 18, 'dechets organiques ': 24, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 24, 'metal': 18, 'dechets organiques ': 24, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 15, 'papier': 24, 'metal': 18, 'dechets organiques ': 24, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 42, 'verre': 16, 'papier': 24, 'metal': 18, 'dechets organiques ': 24, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 24, 'metal': 18, 'dechets organiques ': 24, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 24, 'metal': 19, 'dechets organiques ': 24, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 24, 'metal': 19, 'dechets organiques ': 25, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 24, 'metal': 19, 'dechets organiques ': 26, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 24, 'metal': 19, 'dechets organiques ': 26, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 24, 'metal': 19, 'dechets organiques ': 26, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 24, 'metal': 19, 'dechets organiques ': 26, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 24, 'metal': 19, 'dechets organiques ': 26, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 24, 'metal': 19, 'dechets organiques ': 26, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 24, 'metal': 19, 'dechets organiques ': 26, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 24, 'metal': 19, 'dechets organiques ': 26, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 24, 'metal': 19, 'dechets organiques ': 26, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 26, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 26, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 26, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 26, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 27, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 27, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 27, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 27, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 27, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 27, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 27, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 27, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 27, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 16, 'papier': 25, 'metal': 19, 'dechets organiques ': 27, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 27, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 43, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 27, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 44, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 27, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 44, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 28, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 44, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 28, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 44, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 28, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 44, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 28, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 44, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 28, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 44, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 28, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 44, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 29, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 29, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 29, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 29, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 29, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 25, 'metal': 19, 'dechets organiques ': 29, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 26, 'metal': 19, 'dechets organiques ': 29, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 26, 'metal': 19, 'dechets organiques ': 29, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 26, 'metal': 19, 'dechets organiques ': 29, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 26, 'metal': 19, 'dechets organiques ': 29, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 26, 'metal': 20, 'dechets organiques ': 29, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 26, 'metal': 20, 'dechets organiques ': 29, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 26, 'metal': 20, 'dechets organiques ': 29, 'batteries': 13, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 26, 'metal': 20, 'dechets organiques ': 29, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 26, 'metal': 20, 'dechets organiques ': 29, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 27, 'metal': 20, 'dechets organiques ': 29, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 27, 'metal': 20, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 27, 'metal': 20, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 27, 'metal': 20, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 27, 'metal': 20, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 27, 'metal': 20, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 45, 'verre': 17, 'papier': 27, 'metal': 20, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 46, 'verre': 17, 'papier': 27, 'metal': 20, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 47, 'verre': 17, 'papier': 27, 'metal': 20, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 47, 'verre': 17, 'papier': 27, 'metal': 21, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 48, 'verre': 17, 'papier': 27, 'metal': 21, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 48, 'verre': 17, 'papier': 27, 'metal': 21, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 49, 'verre': 17, 'papier': 27, 'metal': 21, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 49, 'verre': 17, 'papier': 27, 'metal': 21, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 50, 'verre': 17, 'papier': 27, 'metal': 21, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 50, 'verre': 17, 'papier': 27, 'metal': 21, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 51, 'verre': 17, 'papier': 27, 'metal': 21, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 51, 'verre': 17, 'papier': 28, 'metal': 21, 'dechets organiques ': 30, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 51, 'verre': 17, 'papier': 28, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 51, 'verre': 17, 'papier': 28, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 51, 'verre': 17, 'papier': 28, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 51, 'verre': 18, 'papier': 28, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 51, 'verre': 18, 'papier': 28, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 51, 'verre': 18, 'papier': 28, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 51, 'verre': 18, 'papier': 28, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 52, 'verre': 18, 'papier': 28, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 18, 'papier': 28, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 18, 'papier': 29, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 18, 'papier': 29, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 18, 'papier': 29, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 18, 'papier': 29, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 18, 'papier': 29, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 19, 'papier': 29, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 19, 'papier': 29, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 19, 'papier': 29, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 20, 'papier': 29, 'metal': 21, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 20, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 20, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 20, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 21, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 21, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 21, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 21, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 21, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 21, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 21, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 22, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 22, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 23, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 23, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 14, 'ampoule': 12}
,
{'plastique': 53, 'verre': 23, 'papier': 29, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 53, 'verre': 23, 'papier': 30, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 53, 'verre': 23, 'papier': 30, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 53, 'verre': 23, 'papier': 30, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 53, 'verre': 23, 'papier': 30, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 53, 'verre': 23, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 54, 'verre': 23, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 54, 'verre': 23, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 54, 'verre': 23, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 54, 'verre': 23, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 54, 'verre': 23, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 55, 'verre': 23, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 55, 'verre': 24, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 56, 'verre': 24, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 56, 'verre': 24, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 56, 'verre': 24, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 57, 'verre': 24, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 57, 'verre': 24, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 57, 'verre': 24, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 58, 'verre': 24, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 58, 'verre': 24, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 59, 'verre': 24, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 59, 'verre': 24, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 59, 'verre': 24, 'papier': 31, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 59, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 59, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 59, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 59, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 60, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 60, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 61, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 62, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 63, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 63, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 64, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 64, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 65, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 65, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 31, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 65, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 32, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 65, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 32, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 66, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 32, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 66, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 32, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 67, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 32, 'batteries': 15, 'ampoule': 12}
,
{'plastique': 67, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 12}
,
{'plastique': 67, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 12}
,
{'plastique': 67, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 12}
,
{'plastique': 67, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 12}
,
{'plastique': 68, 'verre': 24, 'papier': 32, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 12}
,
{'plastique': 68, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 12}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 12}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 12}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 12}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 12}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 69, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 70, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 70, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 70, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 70, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 71, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 71, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 13}
,
{'plastique': 71, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 72, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 73, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 73, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 73, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 73, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 73, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 73, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 73, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 73, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 74, 'verre': 24, 'papier': 33, 'metal': 22, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 74, 'verre': 24, 'papier': 33, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 74, 'verre': 24, 'papier': 33, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 74, 'verre': 24, 'papier': 33, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 74, 'verre': 24, 'papier': 33, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 74, 'verre': 24, 'papier': 33, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 74, 'verre': 24, 'papier': 33, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 74, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 74, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 74, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 75, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 75, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 75, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 14}
,
{'plastique': 75, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 15}
,
{'plastique': 75, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 15}
,
{'plastique': 75, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 16}
,
{'plastique': 75, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 16}
,
{'plastique': 76, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 16}
,
{'plastique': 77, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 16}
,
{'plastique': 77, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 16}
,
{'plastique': 77, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 16}
,
{'plastique': 77, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 16}
,
{'plastique': 77, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 32, 'batteries': 16, 'ampoule': 16}
,
{'plastique': 77, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 16, 'ampoule': 16}
,
{'plastique': 77, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 16, 'ampoule': 16}
,
{'plastique': 77, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 17, 'ampoule': 16}
,
{'plastique': 77, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 17, 'ampoule': 16}
,
{'plastique': 77, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 17, 'ampoule': 16}
,
{'plastique': 78, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 17, 'ampoule': 16}
,
{'plastique': 78, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 17, 'ampoule': 16}
,
{'plastique': 79, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 17, 'ampoule': 16}
,
{'plastique': 79, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 17, 'ampoule': 16}
,
{'plastique': 79, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 17, 'ampoule': 16}
,
{'plastique': 79, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 17, 'ampoule': 16}
,
{'plastique': 79, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 17, 'ampoule': 16}
,
{'plastique': 79, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 79, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 79, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 79, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 80, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}

,
{'plastique': 81, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 82, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 83, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 83, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 84, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 84, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 84, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 85, 'verre': 24, 'papier': 34, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 85, 'verre': 24, 'papier': 35, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 85, 'verre': 24, 'papier': 36, 'metal': 23, 'dechets organiques ': 33, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 85, 'verre': 24, 'papier': 36, 'metal': 23, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 85, 'verre': 24, 'papier': 36, 'metal': 23, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 85, 'verre': 24, 'papier': 36, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 86, 'verre': 24, 'papier': 36, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 86, 'verre': 24, 'papier': 36, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 86, 'verre': 24, 'papier': 36, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 86, 'verre': 24, 'papier': 36, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 87, 'verre': 24, 'papier': 36, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 88, 'verre': 24, 'papier': 36, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 88, 'verre': 24, 'papier': 37, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 88, 'verre': 24, 'papier': 37, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 88, 'verre': 24, 'papier': 37, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 89, 'verre': 24, 'papier': 37, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 89, 'verre': 24, 'papier': 37, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 90, 'verre': 24, 'papier': 37, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 90, 'verre': 24, 'papier': 38, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 90, 'verre': 24, 'papier': 39, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 91, 'verre': 24, 'papier': 39, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 91, 'verre': 24, 'papier': 39, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 91, 'verre': 25, 'papier': 39, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 91, 'verre': 25, 'papier': 39, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 91, 'verre': 25, 'papier': 39, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 92, 'verre': 25, 'papier': 39, 'metal': 24, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 92, 'verre': 25, 'papier': 39, 'metal': 25, 'dechets organiques ': 34, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 92, 'verre': 25, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 92, 'verre': 26, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 92, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 93, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 93, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 94, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 94, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 94, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 94, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 94, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 94, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 94, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 95, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 95, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 18, 'ampoule': 16}
,
{'plastique': 95, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 95, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 95, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 95, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 35, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 95, 'verre': 27, 'papier': 39, 'metal': 25, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 95, 'verre': 27, 'papier': 39, 'metal': 26, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 96, 'verre': 27, 'papier': 39, 'metal': 26, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 96, 'verre': 27, 'papier': 39, 'metal': 26, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 96, 'verre': 27, 'papier': 39, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 97, 'verre': 27, 'papier': 39, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 97, 'verre': 27, 'papier': 40, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 97, 'verre': 27, 'papier': 41, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 97, 'verre': 27, 'papier': 41, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 97, 'verre': 27, 'papier': 41, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 97, 'verre': 27, 'papier': 42, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 97, 'verre': 27, 'papier': 42, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 97, 'verre': 27, 'papier': 42, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 97, 'verre': 27, 'papier': 42, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 98, 'verre': 27, 'papier': 42, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 99, 'verre': 27, 'papier': 42, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 100, 'verre': 27, 'papier': 42, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 101, 'verre': 27, 'papier': 42, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 102, 'verre': 27, 'papier': 42, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 102, 'verre': 27, 'papier': 43, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 102, 'verre': 27, 'papier': 44, 'metal': 27, 'dechets organiques ': 36, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 102, 'verre': 27, 'papier': 44, 'metal': 27, 'dechets organiques ': 37, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 102, 'verre': 27, 'papier': 44, 'metal': 27, 'dechets organiques ': 37, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 102, 'verre': 27, 'papier': 44, 'metal': 27, 'dechets organiques ': 37, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 102, 'verre': 27, 'papier': 44, 'metal': 27, 'dechets organiques ': 37, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 102, 'verre': 27, 'papier': 44, 'metal': 27, 'dechets organiques ': 38, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 103, 'verre': 27, 'papier': 44, 'metal': 27, 'dechets organiques ': 38, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 103, 'verre': 27, 'papier': 44, 'metal': 27, 'dechets organiques ': 39, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 103, 'verre': 27, 'papier': 44, 'metal': 28, 'dechets organiques ': 39, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 104, 'verre': 27, 'papier': 44, 'metal': 28, 'dechets organiques ': 39, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 104, 'verre': 27, 'papier': 44, 'metal': 28, 'dechets organiques ': 39, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 105, 'verre': 27, 'papier': 44, 'metal': 28, 'dechets organiques ': 39, 'batteries': 19, 'ampoule': 16}
,
{'plastique': 105, 'verre': 27, 'papier': 44, 'metal': 28, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 105, 'verre': 27, 'papier': 44, 'metal': 28, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 105, 'verre': 27, 'papier': 44, 'metal': 28, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 105, 'verre': 27, 'papier': 44, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 105, 'verre': 27, 'papier': 45, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 105, 'verre': 27, 'papier': 45, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 105, 'verre': 27, 'papier': 46, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 106, 'verre': 27, 'papier': 46, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 106, 'verre': 28, 'papier': 46, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 107, 'verre': 28, 'papier': 46, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 107, 'verre': 28, 'papier': 47, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 108, 'verre': 28, 'papier': 47, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 108, 'verre': 29, 'papier': 47, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 109, 'verre': 29, 'papier': 47, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 109, 'verre': 29, 'papier': 48, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 109, 'verre': 29, 'papier': 48, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 109, 'verre': 30, 'papier': 48, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 109, 'verre': 30, 'papier': 49, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 109, 'verre': 30, 'papier': 50, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 30, 'papier': 50, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 31, 'papier': 50, 'metal': 29, 'dechets organiques ': 39, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 31, 'papier': 50, 'metal': 29, 'dechets organiques ': 40, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 31, 'papier': 50, 'metal': 29, 'dechets organiques ': 40, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 31, 'papier': 50, 'metal': 29, 'dechets organiques ': 40, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 31, 'papier': 51, 'metal': 29, 'dechets organiques ': 40, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 31, 'papier': 51, 'metal': 29, 'dechets organiques ': 40, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 31, 'papier': 52, 'metal': 29, 'dechets organiques ': 40, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 32, 'papier': 52, 'metal': 29, 'dechets organiques ': 40, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 32, 'papier': 52, 'metal': 29, 'dechets organiques ': 40, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 32, 'papier': 52, 'metal': 29, 'dechets organiques ': 41, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 32, 'papier': 53, 'metal': 29, 'dechets organiques ': 41, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 32, 'papier': 53, 'metal': 30, 'dechets organiques ': 41, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 32, 'papier': 53, 'metal': 30, 'dechets organiques ': 41, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 110, 'verre': 32, 'papier': 54, 'metal': 30, 'dechets organiques ': 41, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 111, 'verre': 32, 'papier': 54, 'metal': 30, 'dechets organiques ': 41, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 112, 'verre': 32, 'papier': 54, 'metal': 30, 'dechets organiques ': 41, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 112, 'verre': 32, 'papier': 55, 'metal': 30, 'dechets organiques ': 41, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 113, 'verre': 32, 'papier': 55, 'metal': 30, 'dechets organiques ': 41, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 114, 'verre': 32, 'papier': 55, 'metal': 30, 'dechets organiques ': 41, 'batteries': 20, 'ampoule': 16}
,
{'plastique': 114, 'verre': 32, 'papier': 55, 'metal': 30, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 114, 'verre': 32, 'papier': 56, 'metal': 30, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 114, 'verre': 32, 'papier': 57, 'metal': 30, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 114, 'verre': 32, 'papier': 57, 'metal': 30, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 114, 'verre': 32, 'papier': 57, 'metal': 31, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 115, 'verre': 32, 'papier': 57, 'metal': 31, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 115, 'verre': 32, 'papier': 57, 'metal': 31, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 115, 'verre': 32, 'papier': 57, 'metal': 31, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 116, 'verre': 32, 'papier': 57, 'metal': 31, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 116, 'verre': 32, 'papier': 58, 'metal': 31, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 117, 'verre': 32, 'papier': 58, 'metal': 31, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 118, 'verre': 32, 'papier': 58, 'metal': 31, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 118, 'verre': 32, 'papier': 58, 'metal': 31, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 118, 'verre': 32, 'papier': 58, 'metal': 31, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 119, 'verre': 32, 'papier': 58, 'metal': 31, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 120, 'verre': 32, 'papier': 58, 'metal': 31, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 120, 'verre': 32, 'papier': 58, 'metal': 32, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 120, 'verre': 32, 'papier': 58, 'metal': 33, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 120, 'verre': 32, 'papier': 58, 'metal': 33, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 120, 'verre': 33, 'papier': 58, 'metal': 33, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 121, 'verre': 33, 'papier': 58, 'metal': 33, 'dechets organiques ': 41, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 121, 'verre': 33, 'papier': 58, 'metal': 33, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 122, 'verre': 33, 'papier': 58, 'metal': 33, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 122, 'verre': 33, 'papier': 58, 'metal': 33, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 122, 'verre': 33, 'papier': 59, 'metal': 33, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 122, 'verre': 33, 'papier': 60, 'metal': 33, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 122, 'verre': 33, 'papier': 60, 'metal': 33, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 122, 'verre': 33, 'papier': 60, 'metal': 33, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 122, 'verre': 33, 'papier': 60, 'metal': 33, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 122, 'verre': 33, 'papier': 60, 'metal': 33, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 122, 'verre': 34, 'papier': 60, 'metal': 33, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 122, 'verre': 34, 'papier': 60, 'metal': 33, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 122, 'verre': 34, 'papier': 60, 'metal': 34, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 122, 'verre': 34, 'papier': 60, 'metal': 34, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 123, 'verre': 34, 'papier': 60, 'metal': 34, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 123, 'verre': 34, 'papier': 60, 'metal': 34, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 123, 'verre': 34, 'papier': 60, 'metal': 34, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 123, 'verre': 34, 'papier': 61, 'metal': 34, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 123, 'verre': 34, 'papier': 61, 'metal': 34, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 123, 'verre': 35, 'papier': 61, 'metal': 34, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 123, 'verre': 35, 'papier': 62, 'metal': 34, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 124, 'verre': 35, 'papier': 62, 'metal': 34, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 124, 'verre': 35, 'papier': 62, 'metal': 34, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 124, 'verre': 35, 'papier': 63, 'metal': 34, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 124, 'verre': 35, 'papier': 63, 'metal': 35, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 125, 'verre': 35, 'papier': 63, 'metal': 35, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 125, 'verre': 35, 'papier': 63, 'metal': 35, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 125, 'verre': 35, 'papier': 63, 'metal': 35, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 125, 'verre': 35, 'papier': 63, 'metal': 35, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 125, 'verre': 35, 'papier': 64, 'metal': 35, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 125, 'verre': 35, 'papier': 64, 'metal': 35, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 125, 'verre': 35, 'papier': 64, 'metal': 35, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 125, 'verre': 35, 'papier': 64, 'metal': 35, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 125, 'verre': 35, 'papier': 64, 'metal': 36, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 126, 'verre': 35, 'papier': 64, 'metal': 36, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 126, 'verre': 35, 'papier': 64, 'metal': 36, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 126, 'verre': 35, 'papier': 65, 'metal': 36, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 126, 'verre': 35, 'papier': 66, 'metal': 36, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 126, 'verre': 35, 'papier': 67, 'metal': 36, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 126, 'verre': 35, 'papier': 67, 'metal': 37, 'dechets organiques ': 42, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 126, 'verre': 35, 'papier': 67, 'metal': 37, 'dechets organiques ': 43, 'batteries': 21, 'ampoule': 16}
,
{'plastique': 126, 'verre': 35, 'papier': 67, 'metal': 37, 'dechets organiques ': 43, 'batteries': 21, 'ampoule': 17}
,
{'plastique': 126, 'verre': 35, 'papier': 67, 'metal': 37, 'dechets organiques ': 43, 'batteries': 21, 'ampoule': 17}
,
{'plastique': 126, 'verre': 35, 'papier': 67, 'metal': 37, 'dechets organiques ': 43, 'batteries': 21, 'ampoule': 17}
,
{'plastique': 127, 'verre': 35, 'papier': 67, 'metal': 37, 'dechets organiques ': 43, 'batteries': 21, 'ampoule': 17}
,
{'plastique': 127, 'verre': 35, 'papier': 67, 'metal': 37, 'dechets organiques ': 43, 'batteries': 21, 'ampoule': 17}
,
{'plastique': 127, 'verre': 35, 'papier': 68, 'metal': 37, 'dechets organiques ': 43, 'batteries': 21, 'ampoule': 17}
,
{'plastique': 127, 'verre': 35, 'papier': 68, 'metal': 37, 'dechets organiques ': 43, 'batteries': 21, 'ampoule': 17}
,
{'plastique': 128, 'verre': 35, 'papier': 68, 'metal': 37, 'dechets organiques ': 43, 'batteries': 21, 'ampoule': 17}
,
{'plastique': 128, 'verre': 35, 'papier': 68, 'metal': 37, 'dechets organiques ': 44, 'batteries': 21, 'ampoule': 17}
,
{'plastique': 129, 'verre': 35, 'papier': 68, 'metal': 37, 'dechets organiques ': 44, 'batteries': 21, 'ampoule': 17}
,
{'plastique': 129, 'verre': 35, 'papier': 69, 'metal': 37, 'dechets organiques ': 44, 'batteries': 21, 'ampoule': 17}
,
{'plastique': 129, 'verre': 35, 'papier': 69, 'metal': 37, 'dechets organiques ': 44, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 129, 'verre': 35, 'papier': 69, 'metal': 37, 'dechets organiques ': 44, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 129, 'verre': 35, 'papier': 69, 'metal': 37, 'dechets organiques ': 45, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 129, 'verre': 35, 'papier': 69, 'metal': 37, 'dechets organiques ': 45, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 129, 'verre': 35, 'papier': 69, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 129, 'verre': 35, 'papier': 69, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 129, 'verre': 36, 'papier': 69, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 130, 'verre': 36, 'papier': 69, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 130, 'verre': 36, 'papier': 69, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 130, 'verre': 36, 'papier': 69, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 130, 'verre': 36, 'papier': 69, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 130, 'verre': 36, 'papier': 69, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 131, 'verre': 36, 'papier': 69, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 132, 'verre': 36, 'papier': 69, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 133, 'verre': 36, 'papier': 69, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 133, 'verre': 36, 'papier': 69, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 133, 'verre': 36, 'papier': 70, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 133, 'verre': 36, 'papier': 70, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 133, 'verre': 36, 'papier': 70, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 36, 'papier': 70, 'metal': 37, 'dechets organiques ': 46, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 36, 'papier': 70, 'metal': 37, 'dechets organiques ': 47, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 36, 'papier': 71, 'metal': 37, 'dechets organiques ': 47, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 36, 'papier': 72, 'metal': 37, 'dechets organiques ': 47, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 36, 'papier': 72, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 36, 'papier': 72, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 37, 'papier': 72, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 37, 'papier': 72, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 37, 'papier': 72, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 37, 'papier': 72, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 37, 'papier': 72, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 37, 'papier': 73, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 37, 'papier': 74, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 134, 'verre': 37, 'papier': 75, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 135, 'verre': 37, 'papier': 75, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 136, 'verre': 37, 'papier': 75, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 136, 'verre': 37, 'papier': 75, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 136, 'verre': 37, 'papier': 75, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 137, 'verre': 37, 'papier': 75, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 138, 'verre': 37, 'papier': 75, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 139, 'verre': 37, 'papier': 75, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 139, 'verre': 37, 'papier': 76, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 140, 'verre': 37, 'papier': 76, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 140, 'verre': 37, 'papier': 76, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 141, 'verre': 37, 'papier': 76, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 141, 'verre': 37, 'papier': 76, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 141, 'verre': 37, 'papier': 76, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 141, 'verre': 37, 'papier': 76, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 142, 'verre': 37, 'papier': 76, 'metal': 37, 'dechets organiques ': 48, 'batteries': 22, 'ampoule': 17}
,
{'plastique': 142, 'verre': 37, 'papier': 76, 'metal': 37, 'dechets organiques ': 48, 'batteries': 23, 'ampoule': 17}
,
{'plastique': 143, 'verre': 37, 'papier': 76, 'metal': 37, 'dechets organiques ': 48, 'batteries': 23, 'ampoule': 17}
,
{'plastique': 143, 'verre': 37, 'papier': 76, 'metal': 37, 'dechets organiques ': 48, 'batteries': 24, 'ampoule': 17}
,
{'plastique': 143, 'verre': 37, 'papier': 76, 'metal': 37, 'dechets organiques ': 48, 'batteries': 24, 'ampoule': 17}
,
{'plastique': 143, 'verre': 37, 'papier': 77, 'metal': 37, 'dechets organiques ': 48, 'batteries': 24, 'ampoule': 17}
,
{'plastique': 143, 'verre': 37, 'papier': 78, 'metal': 37, 'dechets organiques ': 48, 'batteries': 24, 'ampoule': 17}
,
{'plastique': 143, 'verre': 37, 'papier': 78, 'metal': 37, 'dechets organiques ': 48, 'batteries': 24, 'ampoule': 17}
,
{'plastique': 143, 'verre': 37, 'papier': 78, 'metal': 37, 'dechets organiques ': 48, 'batteries': 24, 'ampoule': 18}
,
{'plastique': 143, 'verre': 37, 'papier': 78, 'metal': 37, 'dechets organiques ': 48, 'batteries': 24, 'ampoule': 18}]



L = [50,len(dico)//10,len(dico)//5,len(dico)//3,len(dico)//2,len(dico)*(1-1//10),len(dico)*(1-1//5),len(dico)*(1-1//3),len(dico)*(1-1//2),len(dico)-1]
def fonction_n(dico,L):
    i = 0
    while i<len(dico):
        fonction(dico[i]['plastique'],dico[i]['dechets organiques '],dico[i]["batteries"],dico[i]["metal"],dico[i]["papier"],dico[i]["ampoule"],dico[i]['verre'],i,dico)
        i = i+1
fonction_n(dico,L)
root.mainloop()


