from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random

import time

root = Tk()
root.title('Visualisasi Algoritma Selection Sort & Bubble Sort')
root.maxsize(1170,600)

bg = tk.PhotoImage(file='sample4.png')
bl = tk.Label(root, image=bg)
bl.place(relwidth=1, relheight=1)

angkaA = []
angkaB = []
time_start = time.time()

############################################################################
def about():
    messagebox.showinfo("About", "Visualisasi Algoritma Selection Sort & Bubble Sort")

def tampilan_tutorial(event=None):
    messagebox.showinfo("tutorial", "masukan bilangan interger yang anda inginkan,kemudian tekan generate,setelah itu tekan mulai sort untuk memulai penyortiran")

def help_box(event=None):
    messagebox.showinfo(
        "Help", "Fikri Muhammad Fajri & Nabiil Azzumar Labib", icon='question')
    
def exit_editor():
    if messagebox.askokcancel("quit", "apakah anda yakin ingin keluar?"):
         root.destroy()
root.protocol('WM_DELETE_WINDOW', exit_editor)

def donothing():
        print("tidak ada yang bisa dilakukan")

 ########################################################################
        
    # Bubble Sort
    
def bbsort(angka,gambarData,canvas):
     global time_start
     time_start = time.time()
        
     for i in range(len(angka)-1, 0, -1):
         
          for j in range(i):
                if angka[j] > angka[j+1]:
                    tampung = angka[j]
                    angka[j] = angka[j+1]
                    angka[j+1] = tampung
                    
                    gambarData(angka, ['white' if x == j or x == j+1 else 'blue' for x in range(len(angka))], canvas)
                    updateTime(timerA,time_start)
                    j -= 1
                    gambarData(angka, ['green' for x in range(len(angka))], canvas)
                
     # Selection Sort

def sssort(angka,gambarData,canvas):
     global time_start
     time_start = time.time()    
     i = len(angka) // 2
     
     for i in range(len(angka)):
         min_idx = i
         for j in range(i, len(angka)):
              if angka[j] < angka[min_idx]:
                min_idx = j
         tampung = angka[i]
         angka[i] = angka[min_idx]
         angka[min_idx] = tampung
         
         gambarData(angka, ['white' if x == j or x == j+1 else 'blue' for x in range(len(angka))], canvas)
         updateTime(timerB,time_start)
         j -= 1
         angka[j+1] = tampung
         gambarData(angka, ['green' for x in range(len(angka))], canvas)

############################### fungsi lainnya ##############################
def updateTime(timeLabel,startTime):
    timeLabel.config(text=time.time() - time_start)

def gambarData(angka, color, canvas):
    canvas.delete("all")
    c_width = 350
    c_height = 400
    x_width = c_width / (len(angka) + 1)
    offset = 10
    space = 5
    normalizedangka = [ i / max(angka) for i in angka]
    for i, height in enumerate(normalizedangka):
        
        x0 = i * x_width + offset + space
        y0 = c_height - height * 336
       
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i], outline=color[i])

    root.update_idletasks()

def mulai():
    global angkaA
    global angkaB

    bbsort(angkaB, gambarData, canvasB)
    sssort(angkaA, gambarData, canvasA)
    
def generateData():
    global angkaA
    global angkaB
    angkaA = []  
    angkaB = []
    

    size = int(sizeInput.get())
    for _ in range(size):
        angkaA.append(random.randrange(7, 150))
    angkaB[:] = angkaA[:]
    gambarData(angkaA,['white' for x in range(len(angkaA))],canvasA)
    gambarData(angkaB,['white' for x in range(len(angkaB))],canvasB)
    
######################################### MenuBar ###################################
    
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=exit_editor)
filemenu.add_separator()
filemenu.add_command(label="Tutorial", command=tampilan_tutorial)
menubar.add_cascade(label="File", menu=filemenu)

aboutmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=aboutmenu)
aboutmenu.add_command(label="About", command=about)
aboutmenu.add_command(label="Help", command=help_box)

root.config(menu=menubar)

##################################### Canvas ####################################

Label(root,text="Bubble sort",bg='blue').grid(row=1,column=0)
Label(root,text="Selection sort",bg='blue').grid(row=1,column=2)

buttonsFrame = Frame(root, width = 960, height = 100, bg ='blue')
buttonsFrame.grid(row = 4, column=0, padx =10, pady=10)

canvasA = Canvas(root, width=340, height=385, bg = 'black')
canvasA.grid(row=2, column=0, padx=10, pady=10)

canvasB = Canvas(root, width=340, height=385, bg = 'black')
canvasB.grid(row=2, column=2, padx=10, pady=10)

labelFrameB = Frame(root, width = 800, height = 70, bg='green')
labelFrameB.grid(row= 2,column=1, padx=20,pady=20)
Label(labelFrameB,text="waktu sorting/second:",bg='blue').grid(row=1,column=0)
timerB = Label(labelFrameB, text="",bg = "green")
timerB.grid(row=2, column=0,pady=20)

labelFrameA = Frame(root, width = 800, height = 70, bg='green')
labelFrameA.grid(row= 2,column=4, padx=20,pady=20)
Label(labelFrameA,text="waktu sorting/seconds:",bg='blue').grid(row=1,column=1)
timerA = Label(labelFrameA, text="", bg = "green")
timerA.grid(row=2, column=1,pady=20)

######################################## tombol #######################################
Label(buttonsFrame, text=" #####################masukan bilangan integer####################:", bg= 'white').grid(row=0, column=0, padx=5,pady=5)

sizeInput = Entry(buttonsFrame)
sizeInput.grid(row=1, column=0, padx=5,pady=5)

mulaiButton = Button(buttonsFrame, text="mulai Sorting", command=mulai)
mulaiButton.grid(row=2, column=0, padx=5, pady=5)

generateButton =Button(buttonsFrame, text="Generate bilangan", command=generateData)
generateButton.grid(row=4, column=0, padx=5, pady=5)

root.mainloop()

