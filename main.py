from tkinter import *
import random

root = Tk()
root.title('Guitar chords quiz')
root.geometry("800x500")

img1 = PhotoImage(file="guitarChords/A minor 7.png")
img2 = PhotoImage(file="guitarChords/A minor.png")
img3 = PhotoImage(file="guitarChords/A.png")
img4 = PhotoImage(file="guitarChords/C.png")
img5 = PhotoImage(file="guitarChords/D minor.png")
img6 = PhotoImage(file="guitarChords/D.png")
img7 = PhotoImage(file="guitarChords/E.png")
img8 = PhotoImage(file="guitarChords/E minor.png")
img9 = PhotoImage(file="guitarChords/G.png")
error = PhotoImage(file="")
background = PhotoImage(file="guitarChords/background.png")

my_background = Label(root, image=background)
my_background.place(x=0, y=0, relwidth=1, relheight=1)


def restart():
   print("restarted")





def Creation():
    number = random.randint(1, 9)

    chord = ""

    if number == 1:
        image1 = img1
        chord = "Am7"
    elif number == 2:
        image1 = img2
        chord = "Am"
    elif number == 3:
        image1 = img3
        chord = "A"
    elif number == 4:
        image1 = img4
        chord = "C"
    elif number == 5:
        image1 = img5
        chord = "Dm"
    elif number == 6:
        image1 = img6
        chord = "D"
    elif number == 7:
        image1 = img7
        chord = "E"
    elif number == 8:
        image1 = img8
        chord = "Em"
    elif number == 9:
        image1 = img9
        chord = "G"
    
    
    my_label = Label(root, image=image1)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    

    e1 = Entry(root, show=None, font=('Arial', 14))
    e1.place(x=290, y=25)

    def myClick():
        my_label2 = Label(root, text=e1.get())
        my_label3 = Label(root, bg="pink", text="Correct!")
        my_label4 = Label(root, text="incorrect :(")
        if e1.get() == chord:
            my_label3.place(x=320, y=28)
        else:
            my_label4.place(x=200, y=25)
        exit_button = Button(root, width=5, height=1, text="next", command=Creation)
        exit_button.place(x=550, y=25)


    myButton = Button(root, text="Submit", command=myClick)
    myButton.place(x=500, y=25)
myButton2 = Button(root, bg="red", width=20, height=10, text="Start", command=Creation)
myButton2.place(x=320, y=200)


#exit_button = Button(root, text="next", command=Creation)
#exit_button.pack()



root.mainloop()
