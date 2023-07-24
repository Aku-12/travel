from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.state("zoomed")
root.title("Home Page")
root.resizable(False, False)

topFrame = Frame(root, width = 1920, height = 680, bg = "#FFFACD")
topFrame.place(x = 0, y = 0)

bottomFrame = Frame(root, width = 1920, height = 500, bg = "#FFFACD")
bottomFrame.place(x = 0, y = 600)

backgroundImage = Image.open("C:\\Users\\user\\Downloads\\Travel\\Images\\mainbg.jpg")
resizeBackground = backgroundImage.resize((1920, 1160))
imageBackground = ImageTk.PhotoImage(resizeBackground)

logoImage = Image.open("C:\\Users\\user\\Downloads\\Travel\\Images\\flight.png")
resizeLogo = logoImage.resize((40, 40))
imageLogo = ImageTk.PhotoImage(resizeLogo)

bhaktapurImage = Image.open("C:\\Users\\user\\Downloads\\Travel\\Images\\bkt.jpg")
resizeBhaktapur = bhaktapurImage.resize((350, 200))
imageBhaktapur = ImageTk.PhotoImage(resizeBhaktapur)

patanImage = Image.open("C:\\Users\\user\\Downloads\\Travel\\Images\\patan.jpg")
resizePatan = patanImage.resize((350, 200))
imagePatan = ImageTk.PhotoImage(resizePatan)

pashupatiImage = Image.open("C:\\Users\\user\\Downloads\\Travel\\Images\\pashupati.jpg")
resizePashupati = pashupatiImage.resize((350, 200))
imagePashupati = ImageTk.PhotoImage(resizePashupati)

pokharaImage = Image.open("C:\\Users\\user\\Downloads\\Travel\\Images\\pkr.jpg")
resizePokhara = pokharaImage.resize((350, 200))
imagePokhara = ImageTk.PhotoImage(resizePokhara)

backgroundLabel = Label(topFrame, image = imageBackground, border = 0, bg = "#FFFACD")
backgroundLabel.place(x = 0, y = 0)

frame1 = Frame(bottomFrame, width = 350, height = 350, bg = "#e4e4e4", border = 0)
frame1.place(x = 100, y = 84)

# textBhaktapur = Label(frame1, )

bhaktapurLabel = Label(frame1, image = imageBhaktapur, border = 0, bg = "#e4e4e4")
bhaktapurLabel.place(x = 0, y = 0)

frame2 = Frame(bottomFrame, width = 350, height = 350, bg = "#e4e4e4", border = 0)
frame2.place(x = 560, y = 84)

patanLabel = Label(frame2, image = imagePatan, border = 0, bg = "#e4e4e4")
patanLabel.place(x = 0, y = 0)

frame3 = Frame(bottomFrame, width = 350, height = 350, bg = "#e4e4e4", border = 0)
frame3.place(x = 1020, y = 84)

pashupatiLabel = Label(frame3, image = imagePashupati, border = 0, bg = "#e4e4e4")
pashupatiLabel.place(x = 0, y = 0)

frame4 = Frame(bottomFrame, width = 350, height = 350, bg = "#e4e4e4", border = 0)
frame4.place(x = 1480, y = 84)

pokharaLabel = Label(frame4, image = imagePokhara, border = 0, bg = "#e4e4e4")
pokharaLabel.place(x = 0, y = 0)

buttonFrame = Frame(root, width = 1920, height = 68, border = 0, bg = "#FFFACD")
buttonFrame.place(x = 0, y = 0)

headingTitle = Label(buttonFrame, image = imageLogo, compound = LEFT, text = "  Tours & Travels Booking", bg = "#FFFACD", font = ("Helvetica Neue", 22, "bold"))
headingTitle.place(x = 34, y = 10)

def create_frame():
    pass
def dostg():
    pass
def dontg():
    pass
def dojpt():
    pass
def dodo():
    pass
def hjk():
    pass

def on_enter(e):
    global frame9
        

def on_leave(e):
    global frame9
    frame9.destroy()

def create_button(buttonFrame, text, x , y, cmd):
    global frame9
    button = Button(buttonFrame, text=text, font = ("Tahoma", 14, "bold"), border = 0, bg = "#FFFACD", cursor = "hand2", command = cmd)
    
    # button.bind("<Enter>",on_enter)
    # button.bind("<Leave>", on_leave)
    button.place(x=x, y=y)
    if text=="Home":
        frame9 = Frame(backgroundLabel, width = 1000, height = 300)
        frame9.place(x = x , y = y)
        
    return button
buttons = []

buttons.append(create_button(buttonFrame, "Home", 592, 16, create_frame))
buttons.append(create_button(buttonFrame, "Destination", 762, 16, dostg))
buttons.append(create_button(buttonFrame, "Adventure Type", 988, 16, dontg))
buttons.append(create_button(buttonFrame, "Help and Feedback", 1268, 16, dojpt))
buttons.append(create_button(buttonFrame, "Contacts", 1574, 16, dodo))
buttons.append(create_button(buttonFrame, "Account", 1784, 16, hjk))
   

root.mainloop()