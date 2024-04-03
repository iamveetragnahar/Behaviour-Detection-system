from tkinter import *
from PIL import Image,ImageTk
import cv2

# GLOBAL VARIABLES 
BGCOLOR = 'white'
FONTCOLOR = '#000000'
BORDERWIDTH = 1
FONTSTYLE = ''
BUTTONBG = 'green'
BUTTONTEXTSIZE = '12'


# root screen code 
root = Tk()
root.state('zoomed')
root.title("Behavior Recognition")
root.configure(bg=BGCOLOR)

'''Header'''

# Heading Frame    
headingFrame = Frame(root,borderwidth=BORDERWIDTH,relief='sunken',bg='#375999')
headingFrame.pack(fill='x')

# Heading Text
headingText = Label(headingFrame,text='Heading comes here...',font=(FONTSTYLE,'18'),bg=BGCOLOR,fg=FONTCOLOR)
headingText.pack(padx=20,pady=5)

'''Section'''

# Section Frame
sectionFrame = Frame(root,borderwidth=BORDERWIDTH,relief='sunken',bg=BGCOLOR) 
sectionFrame.pack(fill='x')

'''Left Section'''

# Section Left Frame
leftFrame = Frame(sectionFrame,border=BORDERWIDTH,relief='sunken',bg=BGCOLOR)
leftFrame.grid(row=1,column=1)

'''   '' Input Frame ''   '''
# Left Section Input Frame 
inputFrame = Frame(leftFrame,borderwidth=BORDERWIDTH,relief='sunken',bg=BGCOLOR)
inputFrame.grid(column=1,row=1)

# Left Section SubHeading
subHeadingLeft = Label(inputFrame,text="Classrooms",font=(FONTSTYLE,14),bg=BGCOLOR)
subHeadingLeft.grid(column=1,row=1)

# Input Section Row 1
inputRowFrame1= Frame(inputFrame,borderwidth=BORDERWIDTH,relief='sunken',bg=BGCOLOR,padx=50)
inputRowFrame1.grid(column=1,row=2)

'''      ' Buttons '      ''' 
# Button 1 
classButon1 = Button(inputRowFrame1,text='Classroom 1',bg=BUTTONBG,font=(FONTSTYLE,BUTTONTEXTSIZE),padx=5)
classButon1.grid(column=1,row=1,padx=20,pady=25)

# Button 2 
classButon2 = Button(inputRowFrame1,text='Classroom 2',bg=BUTTONBG,font=(FONTSTYLE,BUTTONTEXTSIZE),padx=5)
classButon2.grid(column=2,row=1,padx=20,pady=25)

# Button 3 
classButon1 = Button(inputRowFrame1,text='Classroom 3',bg=BUTTONBG,font=(FONTSTYLE,BUTTONTEXTSIZE),padx=5)
classButon1.grid(column=3,row=1,padx=20,pady=25)

# Button 4
classButon1 = Button(inputRowFrame1,text='Classroom 4',bg=BUTTONBG,font=(FONTSTYLE,BUTTONTEXTSIZE),padx=5)
classButon1.grid(column=4,row=1,padx=20,pady=25)

# Left Section Output Frame 
ouputFrame = Frame(leftFrame,borderwidth=BORDERWIDTH,relief='sunken',bg=BGCOLOR)
ouputFrame.grid(column=1,row=2)


'''Right Section'''

# Section Right Frame
rightFrame = Frame(sectionFrame,borderwidth=BORDERWIDTH,relief='sunken',bg=BGCOLOR)
rightFrame.grid(row=1,column=2)

# Right Subheading
subHeadingRight = Label(rightFrame,text='Video Frame',font=(FONTSTYLE,'14'),bg=BGCOLOR)
subHeadingRight.grid(column=1,row=1)

# Right Video Label 
imageLabel = Label(rightFrame,bg=BGCOLOR)
imageLabel.grid(column=1,row=2)



cap = cv2.VideoCapture('Videos\classroom1.mp4')

while True:

    rat,frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame,(512,256))
    frame = ImageTk.PhotoImage(Image.fromarray(frame))
    
    imageLabel['image'] = frame 

    root.update()
